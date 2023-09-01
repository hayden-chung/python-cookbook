# find 
def find_point_from_back(num1, num2):
    num1_dec = num1.find('.')
    num2_dec = num2.find('.')
    num1_dec_from_back = len(num1)-1 - num1_dec # 10.5: 4-1-2
    num2_dec_from_back = len(num2)-1 - num2_dec
    multiplier = 0

    if num1_dec_from_back > num2_dec_from_back:
        multiplier = num1_dec_from_back
    elif num2_dec_from_back > num1_dec_from_back:
        multiplier = num2_dec_from_back
    
    return multiplier



class MyDecimal:
    def __init__(self, num_string):
        self.num_string = num_string

    def plus(self, decimal_number):
        multiplier = find_point_from_back(self.num_string, decimal_number.num_string)
        print(multiplier)
        int1 = float(self.num_string) * (10**multiplier)
        int2 = float(decimal_number.num_string) * (10**multiplier)
        sum = int1+int2
        
        return sum/ (10**multiplier) 
        

    def print(self):
        pass

a = MyDecimal('10.1293817319832')
b = MyDecimal('5.23')
c= a.plus(b)
print('final', c)


