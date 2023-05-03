import math
import os
import random
import re
import sys
from collections import deque

def bfs(adj, start, graph_nodes):
    visited = [False] * (graph_nodes + 1)
    distance = [-1] * (graph_nodes + 1)

    q = deque()
    q.append(start)
    visited[start] = True
    distance[start] = 0

    while q:
        node = q.popleft()
        for neighbor in adj[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                distance[neighbor] = distance[node] + 1
                q.append(neighbor)

    return distance

def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    adj = [[] for _ in range(graph_nodes + 1)]
    for i in range(len(graph_from)):
        u, v = graph_from[i], graph_to[i]
        adj[u].append(v)
        adj[v].append(u)

    target_nodes = [i for i in range(1, graph_nodes + 1) if ids[i - 1] == val]
    if len(target_nodes) < 2:
        return -1  

    shortest_distances = []
    for start in target_nodes:
        shortest_distance = bfs(adj, start, graph_nodes)
        shortest_distances.append(shortest_distance)

    min_distance = float('inf')
    for i in range(len(target_nodes)):
        for j in range(i + 1, len(target_nodes)):
            u, v = target_nodes[i], target_nodes[j]
            distance = shortest_distances[i][v]
            min_distance = min(min_distance, distance)

    return min_distance if min_distance != float('inf') else -1



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    graph_nodes, graph_edges = map(int, input().split())

    graph_from = [0] * graph_edges
    graph_to = [0] * graph_edges

    for i in range(graph_edges):
        graph_from[i], graph_to[i] = map(int, input().split())

    ids = list(map(int, input().rstrip().split()))

    val = int(input())

    ans = findShortest(graph_nodes, graph_from, graph_to, ids, val)

    fptr.write(str(ans) + '\n')

    fptr.close()
