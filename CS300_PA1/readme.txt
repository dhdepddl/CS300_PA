CS300 PA1 20120281김영은

python version: 2.7.11사용.
PA_1.py에 main()이 위치.
디렉토리에서 $python ./PA_1.py input_#.txt 를 입력하면 실행됩니다.


list로 young tableau를 구현하기 위해 list를 상속받은 YoungTableau라는 class 생성.

0. utility를 위한 함수들

__init__(m, n)
	처음의 column수와 row의 수를 입력받아 YoungTableau를 생성.

__len__
	self.col * self.row를 리턴.
	column의 수와 row의 수를 곱한 만큼의 길이를 가진 list.

insert(i, j, value)
	list의 insert함수를 상속받아 YoungTableau상에서 i번째 column, j번째 row의 위치에 value값 insert.
	YoungTableau의 (i, j)위치는 list에서 i*self.col+j번째 element.

last
	YoungTableau에서 가장 아래 row부터 탐색해서 #이 아닌 가장 오른쪽에 integer값이 있는 위치를 리턴.

no_right(index)
	index를 input값으로 받아 row의 가장 오른쪽에 있거나 오른쪽 값이 #이면 True를 리턴

no_under(index)
	index를 input값으로 받아 column의 가장 아래에 있거나 아래의 값이 #이면 True를 리턴



1. extract_min()
heap의 경우와 마찬가지로 우선 index (0, 0)의 최소값을 min에 저장하고 (0)에서 구현한 self.last에 있는 값을 (0, 0)의 위치에 넣는다.
self.last의 위치에 #를 넣은 후의 last row가 모두 #을 가지면 마지막 row를 지우고 self.row의 값은 1만큼 감소.
max_heapify와 같은 기능을 하는 minTableau를 실행 한 후 min에 저장한 최솟값을 리턴한다.
minTableau의 time complexity가 extract_min의 time complexity를 결정.

minTableau(index)
	index의 right, under를 제외하고 YoungTableau의 나머지 위치는 YoungTableau의 조건을 만족한다고 가정.
	1) utility의 no_right, no_under가 true인 경우 종료.
	2) no_right인 경우 under에 있는 값과 비교해서 index의 값이 더 큰 경우 swap value하고 recursive하게 minTableau 실행.
	3) no_under인 경우 right에 있는 값과 비교해서 index의 값이 더 큰 경우 swap value하고 recursive하게 minTableau 실행.
	4) under, right값이 모두 존재할 경우 세 값을 모두 비교해서 index의 값이 가장 작은 경우는 종료.
	   그렇지 않은 경우는 값을 swap하고 recursive하게 minTableau 실행.

minTableau의 time complexity:
	right, under의 값과 비교해서 더 작은 값과 swap하고 right or under의 위치에서 recursive하게 실행.
	처음 인덱스를 (i, j)에서 시작했을 때, 한 번의 실행에서 (i+1, j) 또는 (i, j+1)로 이동.
`	전체 실행횟수는 T(m, n) <= (m-i)+(n-j)이므로 time complexity는 O(m+n)


2. insert_key(value)
YoungTableau가 비어있는 경우 그냥 value를 (0, 0)에 넣고 value를 리턴하면서 종료.
YoungTableau의 마지막 row가 꽉 차있는 경우 self.col을 1만큼 증가하고 새로운 row를 추가해서 value값을 넣는다.
그렇지 않은 경우 마지막 row의 last바로 옆에 value값을 넣는다.
heap_increase_key와 같은 기능을 하는 align_key를 실행하고 만약 마지막 결과에서 value가 있는 위치의 윗칸에 있는 값과 value가 같다면
align_key이전의 상태에서 column을 추가하고 새로 만든 column의 가장 윗칸에 value를 넣고 align_key를 실행한다.
그렇지 않은 경우는 그냥 value를 리턴하고 종료한다.
align_key의 time complexity가 insert_key의 time complexity를 결정.

align_key(index, value)
	index의 left, above를 제외하고 YoungTableau의 나머지 위치는 YoungTableau의 조건을 만족한다고 가정.
	1) index가 0이면 종료
	2) index의 위치가 첫번째 column이면 index의 윗칸에 있는 값과 비교해서 value가 크거나 같으면 종료, 작으면 swap하고 swap한 인덱스에서 계속 실행.
	3) index의 위치가 첫번째 row이면 index의 왼쪽에 있는 값과 비교해서 value가 크거나 같으면 종료, 작으면 swap하고 swap한 인덱스에서 계속 실행.
	4) left, above값을 비교해서 value의 값이 가장 큰 경우는 종료.
	   그렇지 않은 경우는 값을 swap하고 value의 값이 있는 위치에서 계속 실행.
	while문을 빠져나오고 난 후에 value가 있는 최종 index의 값을 리턴하면서 종료.

align_key의 time complexity:
	left, above의 값과 비교해서 더 큰 값과 swap하고 바뀐 위치에서 계속 실행.
	처음 인덱스를 (i, j)에서 시작했을 때, 한 번의 실행에서 (i-1, j) 또는 (i, j-1)로 이동.
	T(m, n) <= i+j이므로 time complexity는 O(m+n)