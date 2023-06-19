#!/usr/bin/python3
# -*- coding: utf-8 -*-

from boto3.session import Session


class S3Client(object):

    def __init__(self, access_key, secret_key, url):
        session = Session(access_key, secret_key)
        self.s3 = session.client('s3', endpoint_url=url)

    def __enter__(self):
        return self.s3

    def __exit__(self, ctx_type, ctx_value, ctx_traceback):
        pass
        # self.s3.close()
