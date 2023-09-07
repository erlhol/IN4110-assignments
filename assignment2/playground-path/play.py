from pathlib import Path
# Iterate over all directories and files

def get_type(p: str | Path) -> str:
    """Returns the type of the file, based on the fileending (suffix)"""
    match p.suffix:
        case '.csv':
            return '.csv files'
        case '.txt':
            return '.txt files'
        case '.npy':
            return '.npy files'
        case '.md':
            return '.md files'
        case default:
            return 'other files'

def DFS(p: str | Path, res):
    """A simple DFS traversal to traverse all subdirectories"""
    stack = [p]
    visited = set()
    while stack:
        v = stack.pop()

        if v.is_dir():
            res["subdirectories"] += 1
            for u in v.iterdir():
                if u not in visited:
                    stack.append(u)
                    visited.add(u)
        else:
            res["files"] += 1 # Assuming that directory is not a file
            res[get_type(v)] += 1
    
    return res

p = Path('..')
res = {
        "files": 0,
        "subdirectories": 0,
        ".csv files": 0,
        ".txt files": 0,
        ".npy files": 0,
        ".md files": 0,
        "other files": 0,
    }
print(DFS(p,res))




    