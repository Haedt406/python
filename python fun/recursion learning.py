word = "computer"
print (len(word))

def length_recursive(sentence):
    if sentence == "": #base case
        return 0
    else:               #general case
        return 1 + length_recursive(sentence[1:])

def length_iterative(sentence):
    answer = 0
    for char in sentence:
        answer += 1
    return answer

def palindrome(sentence):
    if sentence == "":
        return ""
    else:
        return sentence [0] + palindrome(sentence[1:]) + sentence[0]
    
my_sentence = "Today is January 30, 2019."
result = length_iterative(my_sentence)
print (result)

sentence = 'today is wednesday'
result_recursive = length_recursive(sentence)
print (result_recursive)

word + word[::-1]
##def example(n):
##    if n >= 0:
##        print (n)
##        example(n-1)
##
##example(10)
