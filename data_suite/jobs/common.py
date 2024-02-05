import json
from enum import Enum


class JsonPath(Enum):
    LB = '['  # left bracket
    RB = ']'  # right bracket
    INTERACTION = 'interaction'
    CARD_TYPE = "card_type"
    ORDER_CARD_STYLE = "order_card_style"
    VALUE = 'value'
    DELIMITER = '.'
    ROOT = '$'


class Error(Enum):
    UNKNOWN = 'Unknown'


def find_json_obj(obj: object, key: str, pwd: str) -> []:
    """
    :param pwd:
    :param obj:
    :param key:
    :return: all path of object in json
    """
    path_list = []
    if isinstance(obj, list):
        lis = list(obj)
        for i, o in enumerate(lis):
            p_lis = find_json_obj(o, key, pwd + "[{0}]".format(i))

            for p in p_lis:
                path_list.append(p)

        return path_list

    if not isinstance(obj, dict):
        return path_list

    for k, v in obj.items():
        c = pwd + "." + k
        if k.count(key) > 0:
            path_list.append(c)
            continue

        p_lis = find_json_obj(v, key, c)

        for p in p_lis:
            path_list.append(p)

    return path_list


def is_json(j: str) -> bool:
    try:
        _ = json.loads(j)
    except ValueError:
        return False
    return True


def get_json_obj(x: str, path: str) -> object:
    """
    get value in json
    :param x: json str
    :param path: object path
    :return: the object in json
    """
    k_list = path.split(JsonPath.DELIMITER.value)
    content = json.loads(x)
    if not content:
        return None
    for k in k_list:
        if k == JsonPath.ROOT.value:
            continue

        i_ = -1
        if k.find(JsonPath.LB.value) > 0:
            l = k.index(JsonPath.LB.value)
            r = k.index(JsonPath.RB.value)
            i = k[l + 1:r]
            k = k[:l]
            i_ = int(i)

        if k not in content:
            return None

        content = content[k]
        if isinstance(content, list) and i_ >= 0:
            content = content[i_]

    return content


def get_value_by_path(x: object, path: str) -> object:
    k_list = path.split(JsonPath.DELIMITER.value)

    for k in k_list:
        if k == JsonPath.ROOT.value:
            continue

        i_ = -1
        if k.find(JsonPath.LB.value) > 0:
            l = k.index(JsonPath.LB.value)
            r = k.index(JsonPath.RB.value)
            i = k[l + 1:r]
            k = k[:l]
            i_ = int(i)

        if k not in x:
            return None
        x = x[k]
        if isinstance(x, list) and i_ >= 0:
            x = x[i_]

    return x
