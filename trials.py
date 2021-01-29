"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    for item in items:
        print(item)  



def get_all_evens(nums):
    evennums= []

    for num in nums:
        if num / 2 == 0:
            evennums.append(num)
    
    return evennums


def get_odd_indices(items):
    odd_indices = []

    for idx in items:
        if idx % 2 != 0:
            odd_indices.append(idx)
    
    return odd_indices


def print_as_numbered_list(items):

    i = 1

    for item in items:
        print(f'{i}, {item}')
        i += 1



def get_range(start, stop):
    nums = [] 

    for num in range( start, stop):
        nums.append(num)
        #print(nums)
#get_range(2,8)

def censor_vowels(word):
    chars = [] 
    vowels = list("aeiou")
    for letter in word:
        chars.append(letter)
        for vowel in vowels:
            if letter == vowel:
                chars.pop()
                chars.append("*")
        
     
    return print(chars)

censor_vowels("hello")


def snake_to_camel(string):
    camelCase = []
    new_string = ("")
    for word in string.split('_'):
        if camelCase == []:
            camelCase.append(word)
        else:
            camelCase.append(f'{word[0].upper()}{word[1:]} ')


    return print(new_string.join(camelCase))

        

    

snake_to_camel('snake_camels')


def longest_word_length(words):
    longest = len(words[0])

    for word in words:
        if longest < len(word):
            longest = len(word)

    return print(longest)

longest_word_length(['jellyfish', 'zebra'])

def truncate(string):
    
    result = []
    result1 = ""
    for char in string:
        if len(result) == 0 or char != result[len(result)-1]:
            result.append(char)

    return print(result1.join(result))

truncate('aaaabbbbcccca')    

def has_balanced_parens(string):
    
    parens = 0

    for char in string:
        if char == '(':
            parens += 1
        elif char == ')':
            parens -= 1
        elif parens < 0:
            return false
    return print(parens == 0)

has_balanced_parens('(Oh no!)(')


def compress(string):
    compressed = []
    compressed1 = ""

    curr_char = ""
    char_count = 0

    for char in string:
        if char != curr_char:
            compressed.append(curr_char)

            if char_count > 1:
                compressed.append(str(char_count))

            curr_char = char
            char_count = 0
        
        char_count += 1   

    compressed.append(curr_char)
    if char_count > 1:
        compressed.append(str(char_count))   

    return print(compressed1.join(compressed))  

compress('Hello, world! Cows go moooo...')