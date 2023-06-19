#!/usr/bin/python3
# -*- coding: utf-8 -*-

import argparse
import json

from pathlib import Path

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pkg.obj_storage import S3Client
from moo.setting import *
from moo.trace import *

VERSION_AUTO_GENERATE = "auto_generate"


class ZooOption:

    def __init__(self, config_file, access_key, secret_key, endpoint, bucket, model_meta):
        """
        parse config yml file
        :param config_file:
        """
        if not config_file and not model_meta:
            print('missing model conf args')
            return

        if config_file and not os.path.exists(config_file):
            print('local model config file path invalid', config_file)
            return

        if not config_file:
            self.mm = model_meta
        else:
            with open(config_file) as f:
                d = f.read()
                self.mm = json.loads(d)

                # if 'Remote' in conf:
                #     r = conf['Remote']
                #     self.app_id = r.get('AccessKey')
                #     self.secret = r.get('SecretKey')
                #     self.url = r.get('Endpoint')
                #     self.bucket_name = r.get('Bucket')
                # else:
                #     raise Exception("missing remote config")

        self.model_name = self.mm.get('model_name')
        self.model_version = self.mm.get('revision')

        if not access_key or not secret_key or not endpoint or not bucket:
            raise Exception('missing remote config: access_key, secret_key, endpoint or bucket')

        self.app_id = access_key
        self.secret = secret_key
        self.endpoint_url = endpoint
        self.bucket_name = bucket


def _start_with(key, prefix):
    prefix_len = len(prefix)
    return key[:prefix_len] == prefix


def _end_with(key, tail):
    tail_len = len(tail)
    return key[-tail_len:] == tail


def _key_index_str(key, model_name):
    """
    :param key: object key
    :return: object index int
    """
    try:
        items = key.split('/')
        if len(items) < 2:
            return None
        if items[1].startswith(model_name + "_"):
            s = items[1].rindex('_')
            return items[1][s + 1:]
    except Exception as e:
        return None
    return None


def _key_index(key, model_name):
    """
    :param key: object key
    :return: object index int
    """
    idx = _key_index_str(key, model_name)
    if idx is None:
        return 0
    try:
        idx = int(idx)
        return idx
    except Exception as e:
        return 0


def _max_index(key_list, model_name):
    max_idx = 0
    for key in key_list:
        idx = _key_index(key, model_name)
        if idx > max_idx:
            max_idx = idx
    return max_idx


def _history_fmt(data_array, widths):
    data = ''
    for i, d in enumerate(data_array):
        data = data + '{0:{width}}'.format(d, width=widths[i], end='')
    return data


def _print_versions(version_list, cur):
    print("{0:<12s}".format('STATUS'), "VERSION")

    for v in version_list:
        if v == cur:
            print("{0:<12s}".format('current ->'), v)
            continue
        print("{0:12s}".format(' '), v)


class Zoo(object):
    """
    Zoo is used to register the deep learning models for online server
    """

    def __init__(self, option):
        self.url = option.endpoint_url
        self.app_id = option.app_id
        self.secret = option.secret
        self.bucket_name = option.bucket_name
        self.model_name = option.model_name
        self.model_version = option.model_version
        self.model_meta = option.mm
        self.auto_version = False
        if option.model_version == VERSION_AUTO_GENERATE:
            self.auto_version = True

    def publish(self, publish, force):
        if not self.model_name:
            print("model name is required, using --model_name")
            return

        with S3Client(self.app_id, self.secret, self.url) as s3:
            key_list = self._obj_key_list(s3)

            if not key_list:
                # no history and donefile
                print('No earlier versions')
                return

            model_keys = filter(lambda x: _start_with(x, self.model_name), key_list)
            version_list = [_key_index_str(mk, self.model_name) for mk in model_keys]

            if publish not in version_list:
                print("version is not exists")
                return

            last_done = self._done_data(s3, key_list)

            hk = history_key(self.model_name)

            new_hk = history_key(self.model_name)
            new_done = done_file_key(self.model_name)

            last_idx = ''
            if last_done:
                last_idx = last_done.split()[0]

            if self.auto_version:

                if last_done:
                    hk = history_key(self.model_name, last_idx)

                idx = index()
                new_hk = history_key(self.model_name, idx)
                new_done = done_file_key(self.model_name, idx)

            try:
                if last_done:
                    resp = s3.get_object(Bucket=self.bucket_name, Key=hk)

                history_data = ''
                if last_done and 'Body' in resp:
                    resp_body = resp['Body']
                    b = resp_body.read().decode('ascii')
                    history_data = str(b)

                print('last index  ', last_idx)
                if last_done and not force and last_idx == publish:
                    print('every already update, --force will update donefile')
                    return

                ts = timestamp()
                done_file_data = [publish, '0', publish, ts]
                done_log_data = JOIN_STR.join(done_file_data) + '\n'

                history_data = history_data + done_log_data
                s3.put_object(Bucket=self.bucket_name, Key=new_hk, Body=history_data, ContentType="txt")

                s3.put_object(Bucket=self.bucket_name, Key=new_done, Body=done_log_data, ContentType="txt")

                print('# publish to - ', done_log_data)
            except Exception as e:
                raise e

    def _file_list(self, s3):
        bs = s3.list_buckets()['Buckets']

        b = map(lambda x: x['Name'], bs)
        if self.bucket_name in b:
            # Create a reusable Paginator
            paginator = s3.get_paginator('list_objects')
            # Create a PageIterator from the Paginator
            page_iterator = paginator.paginate(
                Bucket=self.bucket_name,
                PaginationConfig={'PageSize': 100}
            )
            for page in page_iterator:
                if 'Contents' in page:
                    fs = page['Contents']
                    data = map(lambda x: x['Key'], fs)

                    if self.model_name:
                        data = filter(lambda x: _start_with(x, self.model_name), data)

                    print("{0:^15s}".format('TYPE'), "PATH")
                    for d in data:
                        if _end_with(d, "donefile"):
                            print("{0:^15s}".format('donefile'), d)
                            continue
                        if _end_with(d, "history"):
                            print("{0:^15s}".format('history'), d)
                            continue
                        if _key_index_str(d, self.model_name) == self.model_version:
                            print("{0:^15s}".format('new'), d)
                            continue
                        print("{0:^15s}".format(' '), d)
                else:
                    print('Bucket Empty.')

        else:
            raise Exception('bucket not found')

    def file_list(self):

        with S3Client(self.app_id, self.secret, self.url) as s3:
            self._file_list(s3)

    def _done_data(self, s3, obj_list=None):

        done_key = done_file_key(self.model_name)

        if self.auto_version:

            if not obj_list:
                return None

            done_list = filter(
                lambda obj_key: _end_with(obj_key, 'donefile') and _start_with(obj_key, self.model_name), obj_list)

            max_idx = _max_index(done_list, self.model_name)
            if max_idx == 0:
                return None

            done_key = done_file_key(self.model_name, str(max_idx))

        try:
            resp = s3.get_object(Bucket=self.bucket_name, Key=done_key)
            if 'Body' in resp:
                resp_body = resp['Body'].read()
                done_data = str(resp_body.decode('ascii'))
                return done_data
        except Exception as e:
            print('#  Query donefile and history   ->', e)

    def revision(self):
        if not self.model_name:
            print("model name is required, using --model_name")
            return

        with S3Client(self.app_id, self.secret, self.url) as s3:
            key_list = self._obj_key_list(s3)
            last_done = self._done_data(s3, key_list)

            cur = ''
            if last_done:
                cur = last_done.split()[0]

            model_keys = filter(lambda x: _start_with(x, self.model_name) and _end_with(x, 'model.onnx'), key_list)

            version_list = [_key_index_str(mk, self.model_name) for mk in model_keys]

            _print_versions(version_list, cur)

    def review_model_conf(self):
        with S3Client(self.app_id, self.secret, self.url) as s3:

            conf = conf_key(self.model_name, self.model_version)

            try:
                resp = s3.get_object(Bucket=self.bucket_name, Key=conf)
                if 'Body' in resp:
                    resp_body = resp['Body'].read()
                    conf_data = str(resp_body.decode('ascii'))
                    print(conf_data)
            except Exception as e:
                print('#  Query model.conf   ->', e)

    def review_donefile(self):
        if not self.model_name:
            print("model name is required, using --model_name")
            return
        with S3Client(self.app_id, self.secret, self.url) as s3:
            done_file = self._done_data(s3)
            print(_history_fmt(DONE_FILE, DONE_DATA_WIDTH))
            if done_file:
                print(_history_fmt(done_file.split(), DONE_DATA_WIDTH))

    def history_list(self):
        if not self.model_name:
            print("model name is required, using --model_name")
            return
        # filter version message from history file
        with S3Client(self.app_id, self.secret, self.url) as s3:

            key_list = self._obj_key_list(s3)
            last_done = self._done_data(s3, key_list)

            if not last_done:
                # no history and donefile
                print('No earlier versions')
                return

            hk = history_key(self.model_name)

            last_done_data = last_done.split()
            last_idx = last_done_data[0]
            if self.auto_version:
                hk = history_key(self.model_name, last_idx)
            try:
                resp = s3.get_object(Bucket=self.bucket_name, Key=hk)

                if 'Body' in resp:
                    resp_body = resp['Body']

                    print(_history_fmt(DONE_FILE, DONE_DATA_WIDTH))

                    while True:
                        li = resp_body.readline()
                        if li == b'':
                            break
                        line = li.decode('ascii')
                        line_str = str(line)

                        line_data = line_str.split()
                        # history_idx = line_data[0]

                        # if history_idx == last_idx:
                        #     print(_history_fmt(last_done_data, DONE_DATA_WIDTH))
                        #     continue

                        print(_history_fmt(line_data, DONE_DATA_WIDTH))

            except Exception as e:
                raise e
                # print('# get history failed - ', e)

    def _upload_big_file(self, s3_client, model_file, key):
        mpu = s3_client.create_multipart_upload(Bucket=self.bucket_name, Key=key)
        part_info = {
            'Parts': []
        }
        i = 1  # part No.
        seen_so_far = 0
        model_size = float(os.path.getsize(model_file))
        with open(model_file, 'rb') as file:
            while True:
                data = file.read(BLOCK_SIZE)  # 每个分块5MiB大小
                seen_so_far += BLOCK_SIZE
                if seen_so_far > model_size:
                    seen_so_far = model_size
                if not data:
                    break
                # step2.上传分片，可改用多线/进程
                response = s3_client.upload_part(Bucket=self.bucket_name, Key=key, PartNumber=i,
                                                 UploadId=mpu["UploadId"],
                                                 Body=data)
                part_info['Parts'].append({'PartNumber': i, 'ETag': response['ETag']})

                percentage = (seen_so_far / model_size) * 100
                sys.stdout.write(
                    "\r%s  %s / %s  (%.2f%%)" % (
                        self.model_name, seen_so_far, model_size,
                        percentage))
                sys.stdout.flush()

                i += 1

            # step3.完成上传
            s3_client.complete_multipart_upload(Bucket=self.bucket_name, Key=key, UploadId=mpu["UploadId"],
                                                MultipartUpload=part_info)

    def upload_model(self, model_file, done):
        """
        donefile key = model_name_{index}/donefile
        history key = model_name_{index}/history
        remote model file key = model_name_{version}_{index}/model.onnx
        remote model.conf key = model_name_{version}_{index}/model.conf

        :param done: decide to update donefile and history
        :param model_file:file path or file current dir path
        :return:
        """

        if not os.path.exists(model_file):
            print("check {} exists, model_file is required,you can got help use moo upload -h".format(model_file))
            return
        # Get file info
        source_size = os.stat(model_file).st_size

        with S3Client(self.app_id, self.secret, self.url) as s3:
            b = map(lambda x: x['Name'], s3.list_buckets()['Buckets'])

            if self.bucket_name not in b:
                try:
                    s3.create_bucket(Bucket=self.bucket_name)
                except Exception as e:
                    raise e

            key_list = self._obj_key_list(s3)
            last_done_str = self._done_data(s3, key_list)

            idx = self.model_version  # new idx
            donefile = done_file_key(self.model_name)
            history = history_key(self.model_name)

            ts = timestamp()

            if self.auto_version:
                idx = ts  # new idx
                self.model_version = ts
                donefile = done_file_key(self.model_name, ts)
                history = history_key(self.model_name, ts)

            try:
                self._upload_model_config(s3)

                onnx = onnx_key(self.model_name, self.model_version)
                # if self._file_exists(s3, onnx):
                #     s3.delete_object(Bucket=self.bucket_name, Key=onnx)
                # s3.upload_file(model_file, self.bucket_name, onnx, Callback=ProgressPercentage(model_file))
                if source_size > BLOCK_SIZE:
                    self._upload_big_file(s3, model_file, onnx)
                else:
                    s3.upload_file(model_file, self.bucket_name, onnx, Callback=ProgressPercentage(model_file))
                # resp = s3.put_object(Bucket=self.bucket_name, Key=onnx,
                #                      Body=open(model_file, 'rb').read(),
                #                      ContentType="txt")
                # print('upload onnx', resp)
            except Exception as e:
                print("# Upload  ->", e)

            print()
            if done:
                # done data: index md5 version timestamp
                md5_code = '0'
                # if source_size < BLOCK_SIZE:
                #     md5_code = get_md5(model_file)
                done_data = (idx, md5_code, self.model_version, ts)
                done_log = JOIN_STR.join(done_data)

                if last_done_str:
                    last_done = last_done_str.split()
                    l_idx = None
                    if self.auto_version:
                        l_idx = last_done[0]  # last index
                    resp = s3.get_object(Bucket=self.bucket_name, Key=history_key(self.model_name, l_idx))

                    resp_body = resp['Body'].read()
                    de = resp_body.decode('ascii')

                    history_data = str(de) + done_log + '\n'
                else:
                    history_data = done_log + '\n'

                s3.put_object(Bucket=self.bucket_name, Key=history, Body=history_data, ContentType="txt")

                s3.put_object(Bucket=self.bucket_name, Key=donefile, Body=done_log, ContentType="txt")

            self._file_list(s3)

    def _upload_model_config(self, s3):
        conf = conf_key(self.model_name, self.model_version)
        mm = self.model_meta

        if not mm.get('model_name') or not mm.get('revision'):
            raise Exception('WARNING: missing model meta info')

        mm['revision'] = int(self.model_version)

        conf_data = json.dumps(mm)
        s3.put_object(Bucket=self.bucket_name, Key=conf, Body=conf_data, ContentType="txt")

    def _obj_key_list(self, s3):
        try:
            resp = s3.list_objects(Bucket=self.bucket_name)
            if 'Contents' in resp:
                obj_list = map(lambda obj: obj['Key'], resp['Contents'])
                return obj_list
        except Exception as e:
            print("key list empty ->", e)

        return None


def build_with_config(args):
    model_conf = MODEL_LOCAL_CONFIG

    if args.model_config_path:
        model_conf = args.model_config_path

    if not args.max_batch:
        args.max_batch = '100'
    if not args.opset_version:
        args.opset_version = '10'
    if not args.use_gpu:
        args.use_gpu = '0'
    output_names = []
    if args.output_names:
        output_names = args.output_names.split(',')

    # model meta
    mm = {
        "ai_framework_info": args.ml_framework if args.ml_framework is not None else '',
        "train_pipeline_info": args.train_pipeline if args.train_pipeline is not None else '',
        "ps_framework_info": args.ps_framework if args.ps_framework is not None else '',
        "model_name": args.model_name,
        "revision": args.model_version,
        "max_batch_size": int(args.max_batch),
        "use_gpu": int(args.use_gpu),
        "opset_version": int(args.opset_version),
        "output_num": 1,
        "output_names": output_names
    }

    if args.gen_model_conf == 'true':
        model_conf = None

        if not args.model_name or not args.model_version:
            print("missing model.conf param")
            return

    op = ZooOption(model_conf, args.app_id, args.secret_key, args.endpoint, args.bucket, mm)
    z = Zoo(op)
    return z


def build_zoo(args):
    # model meta
    mm = {
        "model_name": args.model_name,
        "revision": args.model_version
    }

    op = ZooOption(None, args.app_id, args.secret_key, args.endpoint, args.bucket, mm)
    z = Zoo(op)
    return z


def upload_action(args):
    z = build_with_config(args)

    if args.model_file:
        p = args.model_file
        print("model file - ", p)
        print('publish    - ', args.update_donefile)
        z.upload_model(str(p), args.update_donefile)
    else:
        raise Exception('model file is required, --model_file')


def lookup_action(args):
    if args.model_version == VERSION_AUTO_GENERATE:
        print("model version should not be {} while in lookup action".format(VERSION_AUTO_GENERATE))
        return -1

    z = build_zoo(args)
    if args.all_versions:
        z.revision()

    if args.list:
        z.file_list()

    if args.history:
        z.history_list()

    if args.donefile:
        z.review_donefile()

    if args.model_conf:
        if not args.model_version:
            print("model version is required, using --model_version")
            return
        z.review_model_conf()


def publish_action(args):
    z = build_zoo(args)
    if args.index:
        z.publish(args.index, args.force)
    else:
        raise Exception("index is required, --index")


def gen_model_config(args):
    use_gpu = '0'
    max_batch = '100'
    ov = '10'

    if args.use_gpu:
        use_gpu = args.use_gpu
    if args.max_batch:
        max_batch = args.max_batch
    if args.opset_version:
        ov = args.opset_version
    output_names = []
    if args.output_names:
        output_names = args.output_names.split(',')

    if not use_gpu.isdigit() or not max_batch.isdigit() or not ov.isdigit():
        print('use_gpu max_batch opset version should be digit')
        return

    content = {
        "ai_framework_info": args.ml_framework if args.ml_framework is not None else '',
        "train_pipeline_info": args.train_pipeline if args.train_pipeline is not None else '',
        "ps_framework_info": args.ps_framework if args.ps_framework is not None else '',
        "model_name": args.model_name,
        "revision": int(args.model_version),
        "max_batch_size": int(max_batch),
        "use_gpu": int(use_gpu),
        "opset_version": int(ov),
        "output_num": 1,
        "output_names": output_names
    }

    path = MODEL_LOCAL_CONFIG
    if args.output_path:
        path = str(args.output_path)
    try:
        with open(path, 'w') as f:
            f.write(json.dumps(content))
    except not FileExistsError as e:
        raise e


def main():
    parser = argparse.ArgumentParser(prog='moo')

    parser.add_argument('--app_id', help='remote config app id')

    parser.add_argument('--secret_key', help='remote config secret key')

    parser.add_argument('--endpoint', help='remote endpoint url')

    parser.add_argument('--bucket', help='object storage bucket name')

    parser.add_argument('--model_version', help='model version, e.g 20220705190059')

    parser.add_argument('--model_name', help='model name')

    parser.add_argument('--ml_framework', help='machine learning framework info')

    parser.add_argument('--ps_framework', help='parameter service framework info')

    parser.add_argument('--train_pipeline', help='training pipeline name')

    parser.add_argument('--max_batch', help='training max batch size, default 100')

    parser.add_argument('--use_gpu', help='use gpu, default 0')

    parser.add_argument('--opset_version', help='opset version, default 10')

    parser.add_argument('--output_names', default='',
                        help='Specify which results of outputs needed to get in inference, comon to split. If not '
                             'specified, results of all outputs will get')

    actions = parser.add_subparsers(title='ACTIONS', description='moo actions')

    # upload model
    upload_parser = actions.add_parser('upload', help='upload model file', usage='moo upload [model_file] [--args]')

    upload_parser.add_argument('model_file', type=Path, help='local model file path, is required')

    upload_parser.add_argument('--model_config_path', type=Path, help='local model config file path')

    upload_parser.add_argument('--update_donefile',
                               action='store_true', default=False, help='update model for predict server')

    upload_parser.add_argument('--gen_model_conf', help='upload model.conf by input args')

    # parser.add_argument('--model_version', help='model version')
    #
    # parser.add_argument('--model_name', help='model name')

    upload_parser.set_defaults(func=upload_action)

    # lookup
    lookup_parser = actions.add_parser('lookup', help='lookup model version, file list, history and donefile')

    lookup_parser.add_argument('--all_versions', action='store_true', default=False, help='view the model versions')

    lookup_parser.add_argument('--list', action='store_true',
                               default=False, help='preview file list in bucket, filter by model name')

    lookup_parser.add_argument('--history', action='store_true', default=False, help='view model publishing history')

    lookup_parser.add_argument('--model_conf', action='store_true', default=False, help='view model.conf content')

    lookup_parser.add_argument('--donefile', action='store_true', default=False, help='view model donefile content')

    lookup_parser.set_defaults(func=lookup_action)

    # publish
    publish = actions.add_parser('publish', usage='publish --index', help='publish model for predict server')

    publish.add_argument('--index', help='the version model will publish to predict server')

    publish.add_argument('--force', action='store_true',
                         default=False, help='force update donefile for current version')

    publish.set_defaults(func=publish_action)

    # generate model config
    gen = actions.add_parser('gen_model_conf', help='generate model.conf file which would upload with model file')

    gen.add_argument('--output_path', type=Path, help='the local path you gonna generate on')

    gen.set_defaults(func=gen_model_config)

    # parse args
    args = parser.parse_args()

    args.func(args)


if __name__ == '__main__':
    main()
