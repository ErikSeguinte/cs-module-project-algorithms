#!/usr/bin/python

import sys
from collections import namedtuple
from collections import deque
from functools import lru_cache

Item = namedtuple("Item", ["index", "size", "value"])

# def knapsack_solver(items, capacity):
#     items.sort(key=lambda x: (x.value / x.size) * -1)
#
#     total_value = 0
#     total_cost = 0
#     contents = []
#     items = deque(items)
#
#     while items and total_cost < capacity:
#         item = items.popleft()
#         if (item.size + total_cost) < capacity:
#             total_cost += item.size
#             total_value += item.value
#             contents.append(item.index)
#
#     contents.sort()
#
#     return {'Chosen': contents, 'Value': total_value}

def memoize(f):
    memo = {}
    def helper(x, y, z):
        if x not in memo:
            memo[(x, y, z)] = f(x, y, z)
        return memo[x]
    return helper

@memoize
def knapsack(capacity, items, n):
    if n == 0 or capacity == 0:
        return [], 0

    item:Item = items[n-1]

    if item.size > capacity:
        return knapsack(capacity, items, n-1)

    else:
        new_capacity = capacity - item.size
        new_n = n-1
        with_item = knapsack(new_capacity, items, n-1)
        with_item = list(with_item)
        # with_item[0] = list(with_item[0])
        with_item[0].append(item.index)
        with_item[0].sort()
        # with_item[0] = tuple(with_item)
        with_item[1] += item.value

        without_item = knapsack(capacity, items, n-1)

        if with_item[1] > without_item[1]:
            return with_item
        else:
            return without_item



def knapsack_solver(items, capacity):
    sack = knapsack(capacity, tuple(items), len(items))

    contents = sack[0]

    total_value = sack[1]
    return {'Chosen': contents, 'Value': total_value}


if __name__ == "__main__":
    if len(sys.argv) > 1:
        capacity = int(sys.argv[2])
        file_location = sys.argv[1].strip()
        file_contents = open(file_location, "r")
        items = []

        for line in file_contents.readlines():
            data = line.rstrip().split()
            items.append(Item(int(data[0]), int(data[1]), int(data[2])))

        file_contents.close()
        print(knapsack_solver(items, capacity))
    else:
        print("Usage: knapsack.py [filename] [capacity]")
