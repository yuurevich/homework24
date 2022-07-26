import re
from typing import List, Any, Iterator


def build_query(cmd: str, val: str, file_list: Iterator) -> List[Any]:
    if cmd == 'filter':
        result = list(filter(lambda x: val in x, file_list))
        return result
    if cmd == 'map':
        val = int(val)
        result = list([x.split()[int(val)] for x in file_list])
        return result
    if cmd == 'unique':
        result = list(set(file_list))
        return result
    if cmd == 'sort':
        reverse = val == "desc"
        result = list(sorted(file_list, reverse=reverse))
        return result
    if cmd == 'limit':
        result = list(file_list)[:int(val)]
        return result
    if cmd == "regex":
        regex = re.compile(val)
        print(val)
        result = list(filter(lambda x: regex.search(x), file_list))
        print(result)
        return result
    return []