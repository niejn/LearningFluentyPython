"""
@Version: 1.0
@Project: FluentyPython
@Author: Raymond
@Data: 2018/4/10 下午6:09
@File: __iter__and__next.py.py
@License: MIT
"""


class TestIter:
    def __init__(self, num):
        self.data = list(range(1, num))
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if len(self.data) == 0:
            raise StopIteration
        return self.data.pop()


class Data:
    def __init__(self, data_nums=0):
        if not data_nums:
            self.data = []
        else:
            self.data = list(range(data_nums))

    def __iter__(self):
        for item in self.data:
            if not item:
                continue
            yield item


if __name__ == '__main__':
    data = Data(5)
    for item in data:
        print(item)
