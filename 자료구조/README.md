## 자료구조/알고리즘 총 복습
최종 복습한 내용으로 대표적인 자료구조/알고리즘 유형들을 정리하였습니다
자료구조: Array, Hash Tables, Hash Tables, Linked List, Stack, Queues, Trees, Graphs
알고리즘: Recursion, Sorting, BFS, DFS, Dynamic Programming

### Big O
![big0] (./bigo.png)
-O(1) : loop 없음
-O(log N) : 탐색 알고리즘이 대표적
-O(n) : 전체 반복
-O(n log(n)) : sorting 알고리즘이 대표적
-O(n^2) : 2개의 n이 중첩된 것으로 개별적 원소가 모든 원소와 비교해야할 때
-O(2^n) : 재귀적 함수를 n번 반복시
-O(n!) : 모든 원소별로 반복시
*2개의 다른 집합은 O(a * b)로 표현한다
*space complexity는 변수 추가, 자료구조, 함수 호출, 값 설정 등에서 나온다


### Array
-lookup : o(1)
-push : o(1)
-insert : o(n)
-delete : o(n)

장점 : 개별값 찾기, push/pop에는 최적화
단점 : insert/delete에서는 항상 o(n)이 걸린다


### Hash Tables
-insert : o(1)
-lookup : o(1) => 중첩에 따라 O(n)이 걸릴 수 있다
-delete : o(1)
-search : o(1)

장점 : 시간효율성이 빠른다
단점 : hash collision이 발생시 overflow가 발생한다. 하나의 메모리 주소에 여러 
값이 설정되어 있다면 O(n)이 발생할 수 있다


### Linked List
-prepend/append : o(1)
-lookup : o(n)
-insert : o(n)
-delete : o(n)

장점 : insert/delete에 빠르며 순서가 있고 확장성을 가진다
단점 : lookup이 느리고 메모리를 많이 차지한다



### Stack
-lookup : o(n)
-pop : o(1)
-push : o(1)
-peek : o(1)

장점 : 빠른 실행, peek이 빠르다, 순서가 있다
단점 : lookup이 느리다

### Queue
-lookup : o(n)
-enqueue : o(1)
-dequeue : o(1)
-peek : o(1)

장점 : 빠른 실행, peek이 빠르다, 순서가 있다
단점 : lookup이 느리다

### Tree
-lookup : o(logN)
-insert : o(logN)
-delete : o(logN)

장점 : O(n)보다 빠르다, 순서가 있다, 확장성이 있다
단점 : O(1)인 것이 없다
*unbalanced인 경우 최악의 경우 O(n)일수도 있지만 balance를 하고 search를 해도 O(N)보다 빠르다


### AVL Tree

특징 : Tree가 unbalance된 경우, O(n)이 될 수도 있지만, avl 알고리즘으로 balance를 맞춘다
-높이가 2이상이 안되게한다
-ll, rr, lr, rl rotation으로 각 노드를 전환시킨다

장점 : 빠른 search와 strictly balanced
단점 : 각 노드에 좌우 및 height 정보를 요구

### Red Black Tree

특징: AVL과 마찬가지로 트리의 균형을 위해 사용된다.
위 avl과의 차이점은 strictly하게 균현을 잡지 않는 점이다. 즉 모든 height이 
2 미만이지 않는다. 즉 모든 avl tree가 red black tree과 같지 않다.

장점 : 빠른 insertion과 deleteion
단점 : searching에는 효율적이지 않는다.

### Binary Heap (min/max)
-Time Complexity : log(n)

특징: 최소/최댓값을 빠르게 찾기 위해 구현된 알고리즘으로 root에 최소/최댓값이 있다. 또한 배열 상태로 저장이 가능하여 정렬이 필요없다. 


### 
-lookup : o()
-push : o()
-insert : o()
-delete : o()

장점 : 
단점 : 

### 
-lookup : o()
-push : o()
-insert : o()
-delete : o()

장점 : 
단점 : 
