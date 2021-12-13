from collections import defaultdict, deque

#     start
#     /   \
# c--A-----b--d
#     \   /
#      end

global_count_1 = 0
global_count_2 = 0


def dfs(start, end, visited, graph):
    if start.islower():
        visited.append(start)
    if start == end:
        visited.remove(end)
        global global_count_1
        global_count_1 += 1
        return
    for v in graph[start]:
        if v not in visited:
            dfs(v, end, visited, graph)
    if start.islower():
        visited.remove(start)


def puzzle_one(graph):
    visited = []
    dfs('start', 'end', visited, graph)
    print(global_count_1)


def can_add(current_path, v):
    small = list(filter(lambda a: a.islower(), current_path))
    return len(small) == len(set(small)) or v not in current_path


def puzzle_two(graph):
    count = 0
    queue = deque()
    queue.append(['start'])
    while queue:
        current_path = queue.popleft()
        if current_path[-1] == 'end':
            count += 1
        else:
            for v in graph[current_path[-1]]:
                if v.isupper() or (v != 'start' and can_add(current_path, v)):
                    next_path = current_path[:]
                    next_path.append(v)
                    queue.append(next_path)
    print(count)


if __name__ == '__main__':
    graph = defaultdict(list)
    with open('input') as f:
        for line in f:
            p = line.strip().split('-')
            graph[p[0]].append(p[1])
            graph[p[1]].append(p[0])
    puzzle_one(graph)
    puzzle_two(graph)
    


