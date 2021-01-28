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

    for word in string.split('_'):
        camelCase.append(f'{word[0].upper()}{word[1:]} ')


        

    return print(camelCase)

snake_to_camel('snake_camels')


def longest_word_length(words):
    pass  # TODO: replace this line with your code


def truncate(string):
    pass  # TODO: replace this line with your code


def has_balanced_parens(string):
    pass  # TODO: replace this line with your code


def compress(string):
    pass  # TODO: replace this line with your code
