def check_arrays(arr1, arr2):
    new_arr1 = arr1
    new_arr2 = arr2
    if len(arr1) > len(arr2):
        new_arr1 = arr1[:len(arr2)]
    elif len(arr1) < len(arr2):
        new_arr2 = arr2[:len(arr1)]
    print(new_arr1, new_arr2)
    return new_arr1, new_arr2

class MyNumList():
    def __init__(self, array):
        self.array = array

    def add(self, num_list):
        arr1, arr2 = check_arrays(self.array, num_list.array)
        output = []

        for i in range(len(arr1)):
            
            output.append(arr1[i] + arr2[i])

        return output



        
        
    def mul(self, num_list):
        arr1, arr2 = check_arrays(self.array, num_list.array)
        output = []

        for i in range(len(arr1)):
            
            output.append(arr1[i] * arr2[i])

        return output

x = MyNumList([0.5, 4])
y = MyNumList([3/4, 6, 1.2, 3.5])

print(x.add(y))

