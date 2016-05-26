import sys


def main():
    inputFileName = sys.argv[1]
    outputFileName = inputFileName.replace('input', 'output')

    inputFile = open(inputFileName, 'r')
    line = inputFile.readline()
    l = str(line).split(' ')
    n = int(l[0])
    p = int(l[1])

    elem = str(inputFile.readline()).split(' ')
    A = [0]
    sum = [-1]

    for i in range(0, n):
        elem[i] = int(elem[i])
        A.append(0)
        if i == 0:
            sum.append(elem[0])
        else:
            sum.append(sum[i]+elem[i]+1)

    A[1] = p - sum[1]

    for i in range(2, n+1) :
        j = i-1
        minv = A[j] + p - (sum[i] - sum[j]) + 1
        while sum[i]-sum[j]-1 <= p:
            if minv > A[j] + p - (sum[i] - sum[j]) + 1:
                minv = A[j] + p - (sum[i] - sum[j]) + 1
            j = j-1
            if j < 0:
                break
        A[i] = minv

    outputFile = open(outputFileName,'w')
    outputFile.write(str(A[n]))
    outputFile.close()

if __name__ == "__main__":
    main()