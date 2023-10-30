```python
def DFS(graph, start):
    stack=[]
    seen=set()
    res=[]
    stack.append(start)
    seen.add(start)


    while stack:
        current_v=stack.pop()
        possible_v_T=sorted(graph[current_v], reverse=True)
        print("sorted",possible_v_T)
        possible_v=graph[current_v]
        print("origin",possible_v)
        res.append(current_v)

        for v in possible_v:
            if v not in seen:
                seen.add(v)
                stack.append(v)
        print("stack",stack)
        print("====")

    if len(graph)-1==len(seen):
        return res
    else:
        return False

```

```python
[[], [2, 3, 4], [1, 4], [1, 4], [1, 2, 3]]
anser
sorted [4, 3, 2]
origin [2, 3, 4]
stack [2, 3, 4]
====
sorted [3, 2, 1]
origin [1, 2, 3]
stack [2, 3]
====
sorted [4, 1]
origin [1, 4]
stack [2]
====
sorted [4, 1]
origin [1, 4]
stack []
====
[1, 4, 3, 2]

```
