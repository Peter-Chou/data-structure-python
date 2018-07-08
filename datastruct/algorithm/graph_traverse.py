# -*- coding: utf-8 -*-

from ..queue import Deque
from ..stack import Stack


def bfs(graph, start):
    search_queue = Deque()
    search_queue.append(start)
    searched = set()
    while search_queue:
        cur_node = search_queue.popleft()
        if cur_node not in searched:
            print(cur_node)
            searched.add(cur_node)
            for node in graph[cur_node]:
                search_queue.append(node)


def dfs(graph, start):
    stack = Stack()
    stack.push(start)
    searched = set()
    while stack:
        cur_node = stack.pop()
        if cur_node not in searched:
            print(cur_node)
            searched.add(cur_node)
            for node in reversed(graph[cur_node]):
                stack.push(node)
