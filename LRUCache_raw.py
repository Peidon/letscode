# Design a data structure that follows the constraints of the Least Recently Used (LRU) cache.

class _link_node(object):
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class _link(object):
    def __init__(self):
        self.head = _link_node(0, 0)
        self.tail = _link_node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_node(self, item: _link_node) -> None:
        prev = self.tail.prev
        prev.next = item
        self.tail.prev = item
        item.next = self.tail
        item.prev = prev
        return

    def move_to_end(self, item: _link_node) -> None:
        prev = item.prev
        _nex = item.next
        prev.next = _nex
        _nex.prev = prev
        self.add_node(item)
        return

    def pop(self) -> int:
        if self.head.next == self.tail:
            return -1

        item = self.head.next
        _nex = item.next
        _nex.prev = self.head
        self.head.next = _nex
        return item.key


class LRUCache:
    def __init__(self, capacity: int):
        self._cap = capacity
        self._map = dict()
        self.list = _link()
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self._map:
            return -1

        item = self._map[key]
        self.list.move_to_end(item)
        return item.val

    def put(self, key: int, value: int) -> None:
        if key in self._map:
            node = self._map[key]
            node.val = value
            self.list.move_to_end(node)
            return

        item = _link_node(key, value)
        self._map[key] = item
        self.list.add_node(item)

        if self.size + 1 > self._cap:
            k = self.list.pop()
            del self._map[k]
        else:
            self.size += 1

        return


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    test_data = [[2],[2,1],[1,1],[2,3],[4,1],[1],[2]]
    method = ["LRUCache","put","put","put","put","get","get"]
    obj = LRUCache(test_data[0][0])

    for i in range(1, len(test_data)):
        d = test_data[i]
        m = method[i]


        out = []

        if m == "put":
            obj.put(d[0], d[1])
            out.append("null")

        if m == "get":
            param = obj.get(d[0])
            out.append(param)

        print(out)
