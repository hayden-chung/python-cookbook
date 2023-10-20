class Stack():

    def __init__(self, list):
        self.list = list
    
    def push(self, value):
        self.list.append(value)
    def pop(self):
        self.list.pop()
    def print(self):
        print(self.list)

    def get_first_num(self):
        return self.list[0]
    def get_last_num(self):
        return self.list[-1]
    
    def get_total(self):
        product = 0
        for i in range(len(self.list)):
            product += self.list[i]
        return product

    def get_mean(self):
        average = self.get_total() / len(self.list)
        return average

    def get_median(self):
        median_index = len(self.list)
        median = 0
        if median_index % 2 == 0:
            median = (self.list[median] + self.list[median])/2
            print('median1', median)
        else: 
            median = self.list[round(median_index/2)]
            print('median', median)
        return median

my_list = Stack([1, 5, 7, 10, 2, 4, 9, 8, 2])
print(my_list.get_median())
my_list.print()