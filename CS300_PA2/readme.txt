CS300 PA2 20120281김영은

python version: 2.7.10사용.
PA_2.py에 main()이 위치.
디렉토리에서 $python ./PA_2.py input_#.txt 를 입력하면 실행됩니다.




dynamic programming으로 O(n^2)에 구현

A: 힌트에서 준 대로 A[j]가 l_1, l_2, …, l_j까지의 텍스트들을 사용했을 때의  optimal cost라고 한다.
	with length n+1, and A[0] = 0
elem: input 파일에서 주어진 text들의 길이의 list with length n
sum[j] = l_1 + 1 + l_2 + 1 + … + 1 + l_j with length n+1
	thus, sum[i]-sum[j]-1 = l_(j+1) + 1 + l_(j+2) + … + 1 + l_i for j<i


j+1부터 i번째 텍스트까지를 한 줄에 넣을 수 있다고 하면
이 때의 cost = A[j] + (p - (sum[i] - sum[j] - 1))이다
따라서 A[j] = min(A[j] + (p - (sum[i] - sum[j] - 1)) for j<i and sum[i]-sum[j]-1 <= p
A[j]를 계산하는 데 O(i-j)의 시간이 걸린다. -> O(n)

i = 1부터 n까지 A[i]값을 위의 방법으로 차례대로 구하면 전체 time complexity = O(n^2)


PA2.py는 처음에 무조건  dynamic programming으로 해야하는지 모르고 greedy algorithm으로 짠건데 그냥 같이 제출합니다.
