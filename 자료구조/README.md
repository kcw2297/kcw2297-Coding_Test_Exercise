## 자료구조/알고리즘 총 복습


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

장점 : 
단점 : hash collision이 발생시 overflow가 발생한다. 하나의 메모리 주소에 여러 
값이 설정되어 있다면 O(n)이 발생할 수 있다


### Linked List
-prepend/append : o(1)
-lookup : o(n)
-insert : o(n)
-delete : o(n)

장점 : insert/delete에 빠르며 순서가 있고 확장성을 가진다
단점 : lookup이 느리고 메모리를 많이 차지한다



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