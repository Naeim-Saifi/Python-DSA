import creation as tr
from collections import deque

def BFS(root):
    queue=deque()
    res=[]
    queue.append(root)
    while queue:
        node=queue.popleft() #node variable store only address
        res.append(node.data)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return res

    


if __name__ == "__main__":
    root=tr.Node(10)
    root.insert(5)
    root.insert(19)
    root.insert(6)
    root.insert(40 )
    root.insert(2)
    root.insert(12)
    #tr.inorder(root)
    print(BFS(root))