words = [
 'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
 'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
 'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
 'my', 'eyes', "you're", 'under'
]

store = {}

# Store values
for key in words:
    if key in store:
        store[key] += 1
    else:
        store[key] = 1




# for word in store:
#     if store[word] > highest_value:
#         highest_key = word
#         highest_value = store[word]
        
zip_list = zip(store.values(), store.keys())
highest_word_count = max(zip_list)
print(zip_list)
lowest_word_count = min(zip_list)

print(highest_word_count) 

