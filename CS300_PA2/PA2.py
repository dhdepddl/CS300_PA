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
    A = []

    for i in range(0, n):
        elem[i] = int(elem[i])
        A.append(0)

    rest = p - elem[0]
    A[0] = p - elem[0]

    for i in range(1, n) :
        if rest < elem[i] + 1 :
            rest = p - elem[i]
            A[i] = A[i-1] + p -elem[i]

        else :
            rest = rest - 1 - elem[i]
            A[i] = A[i-1] -1 -elem[i]

    outputFile = open(outputFileName,'w')
    outputFile.write(str(A[n-1]))
    outputFile.close()

if __name__ == "__main__":
    main()