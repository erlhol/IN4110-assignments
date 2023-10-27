"""
Bonus task
"""
from __future__ import annotations
import requesting_urls
import filter_urls
from collections import deque


def find_path(start: str, finish: str) -> list[str]:
    """Find the shortest path from `start` to `finish`

    Arguments:
      start (str): wikipedia article URL to start from
      finish (str): wikipedia article URL to stop at

    Returns:
      urls (list[str]):
        List of URLs representing the path from `start` to `finish`.
        The first item should be `start`.
        The last item should be `finish`.
        All items of the list should be URLs for wikipedia articles.
        Each article should have a direct link to the next article in the list.
    """

    path = shortest_path(start,finish)
    assert path[0] == start
    assert path[-1] == finish
    print(f"Got from {start} to {finish} in {len(path)-1} links")
    return path


def BFS(start,finish):
    queue = deque()
    queue.appendleft(start)
    visited = set()
    visited.add(start)
    parents = {start: None}
    while queue:
        
        # visit the current node
        v = queue.popleft()
        # if we have reaced finish, we are guaranteed to have found the shortes path here
        if v == finish:
            break

        # then visit the edges
        edges = filter_urls.find_english_articles(requesting_urls.get_html(v))
        for u in edges:
            if u not in visited:
                parents[u] = v
                queue.append(u)
                visited.add(u)
         
    return parents

# backtracking to find shorets path
def shortest_path(start,finish):
    if start == finish:
        return []
    parents = BFS(start,finish)
    if finish not in parents:
        return None 
    path = [finish]
    p = parents[finish]
    while p:
        path.append(p)
        p = parents[p]
    return list(reversed(path))


if __name__ == "__main__":
    start = "https://en.wikipedia.org/wiki/Python_(programming_language)"
    finish = "https://en.wikipedia.org/wiki/Peace"
    find_path(start, finish)
