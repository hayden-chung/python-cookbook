text = 'yeah, but no, but yeah, but no, but yeah'

# if letter == 'y'

def replace(text, find, replace):
    front_text = ''
    last_text = ''
    new_text = ''
    index_start = 0
    current_char_count = 0
    text_char_count = len(find)
    for char_index in range(len(text)):
        if current_char_count >= text_char_count:
            print(f'current count {current_char_count}')
            for i in range(current_char_count):
                print(text[index_start+i])
            current_char_count = 0
            front_text = new_text
            print('index_start cont: ', index_start)
            last_text = text[index_start+text_char_count:]
            new_text = front_text + 'yep'
            print('last', last_text, 'NEW:', new_text)
            
            print(front_text)
            print(last_text)
        if text[char_index] == find[0]:
            index_start = char_index
            print(index_start, 'deaw')
        if text[char_index] == find[current_char_count]:
            current_char_count += 1

    print('finished', new_text)


replace(text, 'yeah', 'yep') 