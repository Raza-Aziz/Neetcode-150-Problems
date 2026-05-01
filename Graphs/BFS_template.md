Here’s a **reusable BFS template for grid problems**—structured so you can quickly adapt it for islands, shortest path, multi-source BFS, etc.

---

## 🔹 Generic Grid BFS Template

```python
from collections import deque

def bfs_grid(grid):
    if not grid:
        return
    
    rows, cols = len(grid), len(grid[0])
    
    # Standard 4-direction movement (change if diagonals allowed)
    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    def bfs(start_r, start_c):
        queue = deque([(start_r, start_c)])
        
        # Mark visited (choose ONE strategy)
        grid[start_r][start_c] = "0"   # OR use visited set
        
        while queue:
            r, c = queue.popleft()
            
            # 🔹 Do processing here (depends on problem)
            # e.g., count nodes, track distance, etc.
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # 🔹 Validity check (customize per problem)
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                    
                    queue.append((nr, nc))
                    
                    # Mark visited immediately
                    grid[nr][nc] = "0"

    # 🔹 Main traversal (for problems like islands)
    for r in range(rows):
        for c in range(cols):
            
            # 🔹 Start condition (customize)
            if grid[r][c] == "1":
                
                # 🔹 Do something (e.g., count += 1)
                
                bfs(r, c)
```

---

## 🔹 How to Adapt This Template

### 1. **Number of Islands**

* Start condition → `"1"`
* Action → `count += 1`
* Mark visited → `"0"`

---

### 2. **Shortest Path in Grid**

Modify BFS:

```python
queue = deque([(start_r, start_c, 0)])  # include distance

while queue:
    r, c, dist = queue.popleft()
    
    if (r, c) == target:
        return dist
```

---

### 3. **Multi-Source BFS (VERY IMPORTANT)**

Instead of one start:

```python
queue = deque()

# push ALL starting points first
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == SOME_VALUE:
            queue.append((r, c))
```

👉 Used in:

* Rotting Oranges
* Walls and Gates

---

### 4. **Using Visited Set Instead of Modifying Grid**

```python
visited = set()
visited.add((r, c))

if (nr, nc) not in visited:
    visited.add((nr, nc))
```

---

## 🔹 Key Patterns to Remember

### ✔ Always have:

* `queue`
* `directions`
* bounds check

### ✔ Always decide:

* What is a **valid neighbor**
* When to **mark visited**
* What to **do per node**

---

## 🔹 Mental Framework (Important)

Every grid BFS reduces to:

```
1. Find starting points
2. Push into queue
3. Expand neighbors
4. Mark visited
5. Repeat
```

---

## 🔹 Pro Tip (Interview Insight)

> If problem says:

* “minimum steps” → BFS
* “spread over time” → multi-source BFS
* “connected components” → BFS/DFS both work

---

If you want next level: I can give you a **decision tree (DFS vs BFS vs Union-Find)** so you instantly recognize which approach to use.
