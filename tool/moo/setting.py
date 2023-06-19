JOIN_STR = ' '

BLOCK_SIZE = 64 << 20

DONE_FILE = ['INDEX', 'MD5', 'VERSION', 'TIMESTAMP']
DONE_DATA_WIDTH = [20, 35, 20, 15]


def done_file_key(model_name, idx=None):
    return model_name + '/' + 'donefile'


def history_key(model_name, idx=None):
    return model_name + '/' + 'history'


def onnx_key(model_name, idx):
    return model_name + '/' + model_name + '_' + str(idx) + '/' + 'model.onnx'


def conf_key(model_name, idx):
    return model_name + '/' + model_name + '_' + str(idx) + '/' + 'model_conf.json'


MODEL_LOCAL_CONFIG = 'model_conf.json'


def create_moo_config():
    content = '''
# moo config
---
# model.conf
ModelMeta:
  ML: "pytorch-1.9.0+cu11"    # required, ml framework info
  TrainPipeline: ""           # optional
  PS: ""                      # optional, ps framework info
  ModelName: "AlexCNN"        # required
  Revision: "20220630195007"  # required, model version %Y%m%d%H%M%S
  MaxBatchSize: 100           # max training batch, default 100
  UseGPU: 0                   # 1=True, 0=False
  OpsetVersion: 10            # required, default 10

# Remote base, object storage or hdfs
Remote:
  AccessKey: ""
  SecretKey: ""
  Endpoint: ""
  Bucket: ""
    '''
    try:
        with open("moo_config.yml", 'x') as f:
            f.write(content)
    except not FileExistsError as e:
        raise e
