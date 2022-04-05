#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# BFS, DFS 
from collections import deque

# BFS 함수 정의
def bfs(graph, start, visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

# 정의된 BFS 함수 호출
bfs(graph, 1, visited)



#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# DFS 함수 정의
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)





#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Merge Sort
def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Insertion Sort
def insertion_sort(arr):
    for end in range(1, len(arr)):
        for i in range(end, 0, -1):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]

 
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Recursion
# Python program to display the Fibonacci sequence

def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Graph  https://www.bogotobogo.com/python/python_graph_data_structures.php

class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()  

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost = 0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.keys()

if __name__ == '__main__':

    g = Graph()

    g.add_vertex('a')
    g.add_vertex('b')
    g.add_vertex('c')
    g.add_vertex('d')
    g.add_vertex('e')
    g.add_vertex('f')

    g.add_edge('a', 'b', 7)  
    g.add_edge('a', 'c', 9)
    g.add_edge('a', 'f', 14)
    g.add_edge('b', 'c', 10)
    g.add_edge('b', 'd', 15)
    g.add_edge('c', 'd', 11)
    g.add_edge('c', 'f', 2)
    g.add_edge('d', 'e', 6)
    g.add_edge('e', 'f', 9)

    for v in g:
        for w in v.get_connections():
            vid = v.get_id()
            wid = w.get_id()
            print '( %s , %s, %3d)'  % ( vid, wid, v.get_weight(w))

    for v in g:
        print 'g.vert_dict[%s]=%s' %(v.get_id(), g.vert_dict[v.get_id()])


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------



# Trie https://butter-shower.tistory.com/217

class Trie:
 
    def __init__(self):
        self.trie = {}  # root 
 
    def insert(self, word):
        t = self.trie
        for c in word:
            if c not in t:
                t[c] = {}
            t = t[c]
        t['*'] = True # 끝이라는걸 알림
 
    def search(self, str):
        t = self.trie
        for c in str:
            if c not in t:
                return False
            t = t[c]
        return '*' in t
 
    def startsWith(self, prefix):
        t = self.trie
        for c in prefix:
            if c not in t:
                return False
            t = t[c]
        return True

trie = Trie()
trie.insert("apple")
trie.search("apple")    #return True
trie.search("app")      #return False
trie.startsWith("app")  #return True
trie.insert("app")
trie.search("app");     #return True


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Binary Heap
from heapq import heappush, heappop, heapify 

# A class for Min Heap
class MinHeap:
      
    # Constructor to initialize a heap
    def __init__(self):
        self.heap = [] 
  
    def parent(self, i):
        return (i-1)/2
      
    # Inserts a new key 'k'
    def insertKey(self, k):
        heappush(self.heap, k)           
  
    # Decrease value of key at index 'i' to new_val
    # It is assumed that new_val is smaller than heap[i]
    def decreaseKey(self, i, new_val):
        self.heap[i]  = new_val 
        while(i != 0 and self.heap[self.parent(i)] > self.heap[i]):
            # Swap heap[i] with heap[parent(i)]
            self.heap[i] , self.heap[self.parent(i)] = (
            self.heap[self.parent(i)], self.heap[i])
              
    # Method to remove minium element from min heap
    def extractMin(self):
        return heappop(self.heap)
  
    # This functon deletes key at index i. It first reduces
    # value to minus infinite and then calls extractMin()
    def deleteKey(self, i):
        self.decreaseKey(i, float("-inf"))
        self.extractMin()
  
    # Get the minimum element from the heap
    def getMin(self):
        return self.heap[0]

# Driver pgoratm to test above function
heapObj = MinHeap()
heapObj.insertKey(3)
heapObj.insertKey(2)
heapObj.deleteKey(1)
heapObj.insertKey(15)
heapObj.insertKey(5)
heapObj.insertKey(4)
heapObj.insertKey(45)
  
print(heapObj.extractMin()),
print(heapObj.getMin()),
heapObj.decreaseKey(2, 1)
print(heapObj.getMin()),
  


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Red Black Tree https://www.youtube.com/watch?v=v6eDztNiJwo
"""
Rules:
root is always black
new node is always red
every path from root has same num of black nodes
no path can 2 consecutive red nodes
null is black

Rebalance:
black aunt rotate => after rotate, parent => black, children => red
red aunt color filp
rotating is based on child node, rotates parent and grandparent
"""

class Node():
    def __init__(self, data):
        self.data = data
        self.parent = self.left = self.right = None
        self.color = 'Red' # 신규 삽입되는 노드는 항상 빨강
          
class RedBlackTree:
    
    # 조부모 노드 찾기
    def find_grandparent_node(self,node):
        if (node != None and node.parent != None):
            return node.parent.parent
        else:
            return None
    
    # 삼촌 노드 찾기
    def find_uncle_node(self,node):
        grandparent_node = self.find_grandparent_node(node)
        if grandparent_node == None:
            return None
    
        if node.parent == grandparent_node.left:
            return grandparent_node.right
        else:
            return grandparent_node.left
        
    # case1. 루트 노드는 항상 블랙  
    def insert_case1(self,node):
        if node.parent == None:
            node.color = 'Black'
        else:
            self.insert_case2(node)
        
    # case2. 부모 노드가 블랙이면 회전, 색변환등 수행 필요 x, 하지만 빨강색이라면 case3 수행
    def insert_case2(self,node):
        if node.parent.color == 'Black':
            return
        else:
            self.insert_case3(node)
    
    # case3. 부모노드, 삼촌노드 모두 빨강이라면 색변환 수행, 아닐경우 case4로 이동
    def insert_case3(self,node):
        uncle = self.find_uncle_node(node)
    
        if (uncle != None and uncle.color == 'Red'):
            node.parent.color = 'Black'
            uncle.color = 'Black'
            grandparent = self.find_grandparent_node(node)
            grandparent.color = 'Red'
            self.insert_case1(grandparent)
        else:
            self.insert_case4(node)
    
    
    # case4,5 회전 수행
    def insert_case4(self,node):
        
        grandparent = self.find_grandparent_node(node)
    
        if(node == node.parent.right and node.parent == grandparent.left):
            self.rotate_left(node.parent)
            node = node.left
        elif (node == node.parent.left and node.parent == grandparent.right):
            self.rotate_right(node.parent)
            node = node.right
    
        self.insert_case5(node)
    
    def rotate_left(self,node):
        c = node.right
        p = node.parent
    
        if (c.left != None):
            c.left.parent = node
    
        node.right = c.left
        node.parent = c
        c.left = node
        c.parent = p
        
        if c.parent == None:
            self.root = c
    
        if (p != None):
            if (p.left == node):
                p.left = c
            else:
                p.right = c

    def rotate_right(self,node):
        c = node.left
        p = node.parent
    
        if (c.right != None):
            c.right.parent = node
    
        node.left = c.right
        node.parent = c
        c.right = node
        c.parent = p
        
        if c.parent == None:
            self.root = c
            
        if (p != None):
            if (p.right == node):
                p.right = c
            else:
                p.left = c
     
    def insert_case5(self,node):
        grandparent = self.find_grandparent_node(node)
    
        node.parent.color = 'Black'
        grandparent.color = 'Red'

        if (node == node.parent.left):
            self.rotate_right(grandparent)
        else:
            self.rotate_left(grandparent)

            
    def __init__(self):
        self.root = None
        self.inserted_node = None
	
    # 삽입
    def insert(self, data, parent_node):
        self.root = self.insert_value(self.root, data, parent_node)
        self.insert_case1(self.inserted_node)
        return 
    
    def insert_value(self, node, data, parent_node):
        if node is None:
            node = Node(data)
            node.parent = parent_node
            self.inserted_node = node
        else:
            if data <= node.data:
                node.left = self.insert_value(node.left,data,node)
            else:
                node.right = self.insert_value(node.right,data,node)
        return node
    
    # 탐색
    def find(self,search_key):
        return self.find_value(self.root, search_key)
    
    def find_value(self, root, search_key):
        if root is None or root.data == search_key:
            return root 
        elif search_key > root.data:
            return self.find_value(root.right, search_key)
        else:
            return self.find_value(root.left, search_key)      




rbt = RedBlackTree()

a = [2, 1, 8, 9, 7, 3, 6, 4, 5]
    
for x in a:
    rbt.insert(x,None)
    

# 레드블랙트리 key, 부모, 색상 출력
def check(node):
    if not node.left  == None : check(node.left)
    if node.parent != None:
        print('key: ', node.data, 'parents: ', node.parent.data, 'color: ', node.color, end = '\n')
    else:
        print('key: ', node.data, 'parents: ', node.parent, 'color: ', node.color, end = '\n')
    if not node.right == None : check(node.right)

check(rbt.root)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# AVL Tree https://favtutor.com/blogs/avl-tree-python
class treeNode(object):
	def __init__(self, value):
		self.value = value
		self.l = None
		self.r = None
		self.h = 1

class AVLTree(object):

	def insert(self, root, key):
	
		if not root:
			return treeNode(key)
		elif key < root.value:
			root.l = self.insert(root.l, key)
		else:
			root.r = self.insert(root.r, key)

		root.h = 1 + max(self.getHeight(root.l),
						self.getHeight(root.r))

		b = self.getBal(root)

		if b > 1 and key < root.l.value:
			return self.rRotate(root)

		if b < -1 and key > root.r.value:
			return self.lRotate(root)

		if b > 1 and key > root.l.value:
			root.l = self.lRotate(root.l) 
			return self.rRotate(root)

		if b < -1 and key < root.r.value:
			root.r = self.rRotate(root.r)
			return self.lRotate(root)

		return root

	def lRotate(self, z):

		y = z.r
		T2 = y.l

		y.l = z
		z.r = T2

		z.h = 1 + max(self.getHeight(z.l),
						self.getHeight(z.r))
		y.h = 1 + max(self.getHeight(y.l),
						self.getHeight(y.r))

		return y

	def rRotate(self, z):

		y = z.l
		T3 = y.r

		y.r = z
		z.l = T3

		z.h = 1 + max(self.getHeight(z.l),
						self.getHeight(z.r))
		y.h = 1 + max(self.getHeight(y.l),
						self.getHeight(y.r))

		return y

	def getHeight(self, root):
		if not root:
			return 0

		return root.h

	def getBal(self, root):
		if not root:
			return 0

		return self.getHeight(root.l) - self.getHeight(root.r)

	def preOrder(self, root):

		if not root:
			return

		print("{0} ".format(root.value), end="")
		self.preOrder(root.l)
		self.preOrder(root.r)

Tree = AVLTree()
root = None

root = Tree.insert(root, 1)
root = Tree.insert(root, 2)
root = Tree.insert(root, 3)
root = Tree.insert(root, 4)
root = Tree.insert(root, 5)
root = Tree.insert(root, 6)

# Preorder Traversal
print("Preorder traversal of the",
	"constructed AVL tree is")
Tree.preOrder(root)
print()


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# BST(binary search tree)

class Node:
 
    # Constructor to create a new node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
 
 
# A utility function to do inorder traversal of BST
def inorder(root):
    if root is not None:
        inorder(root.left)
        print (root.key,end=" ")
        inorder(root.right)
 
 
# A utility function to insert a
# new node with given key in BST
def insert(node, key):
 
    # If the tree is empty, return a new node
    if node is None:
        return Node(key)
 
    # Otherwise recur down the tree
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
 
    # return the (unchanged) node pointer
    return node
 
# Given a non-empty binary
# search tree, return the node
# with minimum key value
# found in that tree. Note that the
# entire tree does not need to be searched
 
 
def minValueNode(node):
    current = node
 
    # loop down to find the leftmost leaf
    while(current.left is not None):
        current = current.left
 
    return current
 
# Given a binary search tree and a key, this function
# delete the key and returns the new root
 
 
def deleteNode(root, key):
 
    # Base Case
    if root is None:
        return root
 
    # If the key to be deleted
    # is smaller than the root's
    # key then it lies in left subtree
    if key < root.key:
        root.left = deleteNode(root.left, key)
 
    # If the kye to be delete
    # is greater than the root's key
    # then it lies in right subtree
    elif(key > root.key):
        root.right = deleteNode(root.right, key)
 
    # If key is same as root's key, then this is the node
    # to be deleted
    else:
 
        # Node with only one child or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp
 
        elif root.right is None:
            temp = root.left
            root = None
            return temp
 
        # Node with two children:
        # Get the inorder successor
        # (smallest in the right subtree)
        temp = minValueNode(root.right)
 
        # Copy the inorder successor's
        # content to this node
        root.key = temp.key
 
        # Delete the inorder successor
        root.right = deleteNode(root.right, temp.key)
 
    return root
 


root = None
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)
 
print("Inorder traversal of the given tree")
inorder(root)
 
print("\nDelete 20")
root = deleteNode(root, 20)
print("Inorder traversal of the modified tree")
inorder(root)
 
print("\nDelete 30")
root = deleteNode(root, 30)
print("Inorder traversal of the modified tree")
inorder(root)
 
print("\nDelete 50")
root = deleteNode(root, 50)
print("Inorder traversal of the modified tree")
inorder(root)
 


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Queue
queue = [4,5,6]
queue.insert(0, 3) #=> [3,4,5,6]
#이는 O(n)으로 전체 요소들을 한간씩 밀려난다

#deque를 활용하여 insert와 pop을 쉽게한다, deque는 내부적으로 linkedlist형식을 사용하기 때문에, lookup은 O(n)이다

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# LinkedList in python
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def push(self,value):
        new_node = Node(value)

        new_node.next = self.head
        
        if self.head != None:    
            self.head.prev = new_node
        
        self.head = new_node
        

    def insertAfter(self, prev_node, new_data):

        if prev_node is None:
            print("the given previous node cannot be NULL")
            return
        
        new_node = Node(new_data)

        new_node.next = prev_node.next
        prev_node.next.prev = new_node
        new_node.prev = prev_node
        prev_node.next = new_node

    def append(self, new_data):
        new_node = Node(new_data)

        last = self.head
        while last.next:
            last = last.next
        
        last.next = new_node
        new_node.prev = last





if __name__=='__main__':
 
    llist = DoublyLinkedList()
 
    # Insert 6. So the list becomes 6->None
    llist.append(6)
    
    # # Insert 7 at the beginning.
    # # So linked list becomes 7->6->None
    # llist.push(7)
    
    # # Insert 1 at the beginning.
    # # So linked list becomes 1->7->6->None
    # llist.push(1)
    
    # # Insert 4 at the end.
    # # So linked list becomes 1->7->6->4->None
    # llist.append(4)
    
    # # Insert 8, after 7.
    # # So linked list becomes 1->7->8->6->4->None
    # llist.insertAfter(llist.head.next, 8)