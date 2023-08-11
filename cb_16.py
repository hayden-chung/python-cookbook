from collections import defaultdict


d = defaultdict(list)


d['a'].append(1)
d['a'].append(2)
d['b'].append(4)


prices = {
 'ACME': 45.23,
 'AAPL': 612.78,
 'IBM': 205.55,
 'HPQ': 37.20,
 'FB': 10.75
}

# name = None
# minimum = 10000
# for key in prices:
#     if prices[key] < minimum:
#         print('t4rue', prices[key])
#         minimum = prices[key]
#         name = key
# print(name)

a = {
 'x' : 1,
 'y' : 2,
 'z' : 3
}

b = {
 'w' : 10,
 'x' : 11,
 'y' : 2
}

overlapping_values = {}

for a_key in a:
    for b_key in b:
        if b[b_key] == a[a_key]:
            overlapping_values.append(a[a_key])


print(overlapping_values)