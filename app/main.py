from typing import Any, Optional


class Node:
    def __init__(self, key: Any, hash_val: int, value: Any) -> None:
        self.key = key
        self.hash = hash_val
        self.value = value


class Dictionary:
    def __init__(self, capacity: int = 8) -> None:
        self.capacity = capacity
        self.size = 0
        self.table: list[Optional[Node]] = [None] * self.capacity

    def __len__(self) -> int:
        return self.size

    def _resize(self) -> None:
        old_table = self.table
        self.capacity *= 2
        self.table: list[Optional[Node]] = [None] * self.capacity
        self.size = 0

        for node in old_table:
            if node is not None:
                self.__setitem__(node.key, node.value)

    def __setitem__(self, key: Any, value: Any) -> None:
        if self.size / self.capacity >= 0.66:
            self._resize()

        hash_val = hash(key)
        index = hash_val % self.capacity

        while self.table[index] is not None:
            if self.table[index].key == key:
                self.table[index].value = value
                return
            index = (index + 1) % self.capacity

        self.table[index] = Node(key, hash_val, value)
        self.size += 1

    def __getitem__(self, key: Any) -> Any:
        hash_val = hash(key)
        index = hash_val % self.capacity

        while self.table[index] is not None:
            if self.table[index].key == key:
                return self.table[index].value
            index = (index + 1) % self.capacity
        raise KeyError(key)
