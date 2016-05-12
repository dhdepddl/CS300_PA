
import sys
import copy


# declare class YoungTableau
class YoungTableau(list):
    def __init__(self, m, n):
        self.row = m
        self.col = n

    def __len__(self):
        return self.row * self.col

    def insert(self, i, j, value):
        list.insert(self, i*self.col + j, value)

    def last(self):
        index = self.row * self.col - 1
        # pick last row's last element, not a maximum element
        while self[index] == '#':
            index -= 1
        return index

    def no_right(self, index):
        if (index + 1)%self.col == 0:
            return True
        elif self.__len__() < index + 2:
            return True
        elif self[index+1] == '#':
            return True
        return False

    def no_under(self, index):
        if index/self.col == self.row - 1:
            return True
        elif self.__len__() < index + self.col + 1:
            return True
        elif self[index + self.col] == '#':
            return True
        return False

    def minTableau(self, index):
        if self.no_right(index) and self.no_under(index):
            return
        elif self.no_right(index):
            under = index + self.col
            if self[index] > self[under]:
                val = self[index]
                self[index] = self[under]
                self[under] = val
                self.minTableau(under)
            elif self[index] == self[under]:
                val = self[index]
                self[index] = self[under-1]
                self[under-1] = val
                self.minTableau(under)
        elif self.no_under(index):
            right = index + 1
            if self[index] > self[right]:
                val = self[index]
                self[index] = self[right]
                self[right] = val
                self.minTableau(right)
        else:
            right = index + 1
            under = index + self.col
            small = index
            if self[index] > self[right]:
                small = right
            if self[under] <= self[small]:
                small = under
            if small != index:
                val = self[small]
                self[small] = self[index]
                self[index] = val
                self.minTableau(small)

    def extract_min(self):
        if self.__len__() < 1 or self[0] == '#':
            return '(error) extract_min: tableau is empty'
        min = self[0]
        self[0] = self[self.last()]
        # remove last row if last row is empty
        if self.last()%self.col == 0:
            self.row -= 1
            for i in range(0, self.col):
                del self[-1]
        else:
            self[self.last()] = '#'
        self.minTableau(0)
        return min

    def align_key(self, index, value):
        while True:
            if index == 0:
                break
            elif index < self.col:
                if self[index-1] > value:
                    self[index] = self[index-1]
                    self[index-1] = value
                    index -= 1
                else:
                    break
            elif index%self.col == 0:
                if self[index - self.col] <= value:
                    break
                else:
                    self[index] = self[index-self.col]
                    self[index-self.col] = value
                    index -= self.col
            else:
                large = index
                if self[index-self.col] > self[large]:
                    large = index-self.col
                if self[index-1] > self[large]:
                    large = index-1
                if large == index:
                    break
                self[index] = self[large]
                self[large] = value
                index = large
        return index

    def insert_key(self, value):
        # if tableay is empty
        if self.__len__() < 1:
            list.append(self, value)
            for i in range(1, self.col):
                list.append(self, '#')
            self.row += 1
            return value

        # not empty
        index = self.col - 1
        while self[index] != '#':
            index += self.col
            if self.__len__() < index+1:
                index = -1
                break

        if index < 0:
            list.append(self, value)
            for i in range(1, self.col):
                list.append(self, '#')
            index = self.row * self.col
            self.row += 1
        else:
            while self[index] == '#':
                index -= 1
            index += 1
            self[index] = value
        a = copy.copy(self)
        ind = a.align_key(index, value)
        if ind - a.col >= 0:
            if a[ind] == a[ind-a.col]:
                self[index] = '#'
                self.col += 1
                for j in range(0, self.row):
                    self.insert(j, self.col-1, '#')
                self[self.col-1] = value
                self.align_key(self.col-1, value)
            else:
                self.align_key(index, value)
        else:
            self.align_key(index, value)
        return value


# get filename, open and read given test file
argument = str(sys.argv)
filename = str(sys.argv[1])

inputFile = open(filename, 'r')
line = inputFile.readline()
l = str(line).split(' ')
m = int(l[1])
n = int(l[0])
k = int(l[2])

listtodo = []

yt = YoungTableau(m, n)
for i in range(0, k):
    line = str(inputFile.readline()).split(' ')
    if line[0] == 'I':
        listtodo.append(int(line[1]))
    else:
        listtodo.append('E')

for i in range(0, m):
    line = str(inputFile.readline()).split(' ')
    for j in range(0, n):
        # if j == n-1:
        #     line[j] = line[j]
        if line[j][0] != '#':
            yt.insert(i, j, int(line[j]))
        else:
            yt.insert(i, j, line[j][0])

inputFile.close()


# do extract_min and insert_key
for i in range(0, k):
    if listtodo[0] == 'E':
        listtodo.pop(0)
        yt.extract_min()
    else:
        new = listtodo.pop(0)
        yt.insert_key(new)
    # print(yt)


# make output file
outputFilename = filename.replace('input_', 'output_')
outputFile = open(outputFilename, 'w')
for i in range(0, yt.row):
    for j in range(0, yt.col):
        if str(yt[i * yt.col + j]) == '#':
            break
        outputFile.write(str(yt[i * yt.col + j]) + ' ')
    outputFile.write('\n')
outputFile.close()