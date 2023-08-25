text = 'yeah, but no, but yeah, but no, but yeah awdoij'

# if letter == 'y'

def replace(text, find, replace):
    front_text = ''
    last_text = ''
    new_text = ''
    current_char_count = 0
    text_char_count = len(find)
    find_index_start_at = 0

    end_of_sentence_not_find = 0
    start_of_sentence_not_find = 0

    run = True

    for i in range(len(text)):
    

        if text[i] == find[0]: 
            find_index_start_at = i
        if text[i] == find[current_char_count]:
            current_char_count += 1
            print(text[i])
        else: 
            current_char_count = 0 
            end_of_sentence_not_find = i+1

        if current_char_count == 4: # reset current char count to 0 as word has been found. 
            current_char_count = 0
            print('start_of_sentence_not_find', start_of_sentence_not_find, 'end_of_sentence_not_find', end_of_sentence_not_find)
            
            new_text = new_text + text[start_of_sentence_not_find:end_of_sentence_not_find] + 'yep'  
            print('new text:', new_text)
            start_of_sentence_not_find = i+1

    new_text = new_text + text[start_of_sentence_not_find:]
    print(new_text)

        


            


replace(text, 'yeah', 'yep') 