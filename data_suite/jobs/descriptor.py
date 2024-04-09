from typing import List


class Descriptor:
    def __init__(self, keys=None, names=None, text="", expression="", used_or=False):
        self.keys = keys if keys is not None else []
        self.names = names if names is not None else []
        self.text = text
        self.expression = expression
        self.used_or = used_or


def filter_description(d_lis: List[Descriptor]) -> (str, dict):
    used = dict()
    expr_set = set()

    for des in d_lis:

        t = removeBlank(des.text, [' and ', ' or '])
        if t != '':
            expr_set.add(t)

        for i, k in enumerate(des.keys):
            used[k] = des.names[i]

    return ','.join(list(expr_set)), used


def removeBlank(text: str, delimit: List[str]) -> str:
    for lim in delimit:

        ts = text.split(lim)
        ts = [x for x in ts if x != '()']
        if len(ts) > 0:
            text = lim.join(ts)
        else:
            return ''

    return text.strip()


def condition_description(rule_g) -> list:
    if not isinstance(rule_g, list):
        return []

    d = []
    for g in rule_g:
        logics = g.get('logics')
        used_or = has_or(logics)
        text = ""
        expr = ""
        ks = []
        ns = []
        rules = g.get('rules')
        for i, ru in enumerate(rules):
            des, exp, keys, names = rule_description(ru)
            if i < len(logics):
                text += des + " " + logical_opt_map[logics[i]] + " "
                expr += exp + " " + logical_opt_map[logics[i]] + " "
            else:
                text += des
                expr += exp
            ks.extend(keys)
            ns.extend(names)
        d.append(Descriptor(text=text, keys=ks, names=ns, expression=expr, used_or=used_or))
    return d


def has_or(ops):
    return 2 in ops


def is_in_int_slice(ss, s):
    return s in ss


def string_list_to_int_list(in_list):
    return [int(op) for op in in_list]


def rule_description(rule) -> (str, str, list, list):
    rule_ops = rule.get('operators')
    if not rule_ops:
        return "", "", [], []
    ops = string_list_to_int_list(rule_ops)
    cpt = ops[-1]
    use_key = not is_in_int_slice([10, 11, 12, 13, 14, 15, 20, 21], cpt)
    keys, names = [], []
    desc = ""
    expr = ""

    rule_vs = rule.get('variables')
    if not rule_vs:
        return "", "", [], []

    vs = [v for v in rule_vs if v.get('source_type', 0) in [1, 2, 3, 4, 6, 9]]
    for i, v in enumerate(vs):
        key = v.get('value', '')
        name = v.get('render', '')
        if use_key:
            keys.append(key)
            names.append(name)
            continue
        if i < len(ops):
            op = ops[i]
            if op not in comparator_map:
                continue
            desc += name + " " + comparator_map[op] + " "
            expr += key + " " + comparator_map[op] + " "
        else:
            desc += name
            expr += key

    if desc == "":
        desc = "()"
    return desc, expr, keys, names


comparator_map = {
    10: "=",
    11: "!=",
    12: ">",
    13: ">=",
    14: "<",
    15: "<=",
    16: "isNull",
    17: "notNull",
    18: "in",
    19: "notIn",
    20: "contain",
    21: "not contain",
    22: "isEmpty",
    23: "notEmpty",
}

logical_opt_map = {
    1: "and",
    2: "or",
}

# from data_suite.jobs.data_examples import condition_json_str
# from data_suite.jobs.common import get_value_by_path
# import json
#
# if __name__ == '__main__':
#     branches = json.loads(condition_json_str)
#
#     for branch in branches:
#         groups = get_value_by_path(branch, "$.branch_rule.value.groups")
#         if isinstance(groups, list):
#             ds = condition_description(list(groups))
#             tx, vs = filter_description(ds)
#             print(tx)
