import string

def print_common_word(dictionary, threshold):
    for word, count in dictionary.items():
        if count >= threshold:
            print(word, count)

def most_frequent_word(dictionary):
    highest_count = 0
    most_frequent_word = "UNKNOWN"
    for word, count in dictionary.items():
        if count > highest_count:
            highest_count = count
            most_frequent_word = word
    print("the most frequently occurnig word is:", most_frequent_word)
    print("occurences:", highest_count)
    

def process_text(raven_text):
    letter_count = {}
    for ch in string.ascii_lowercase:
        letter_count[ch] = 0
    for ch in raven_text:
        letter_count[ch] += 1
    return letter_count

def print_dictionary(raven_dictionary):
    for word, count in raven_dictionary.items():
        print(word,count)
##    for ch in string.ascii_lowercase:
##        print(ch, raven_dicionary[ch])

def create_dictionary(words):
    dictionary = {}
    for word in words:
        dictionary[word] = dictionary.get(word, 0) + 1
    return dictionary

def process(word):
    result = ""
    for ch in word:
        if ch in string.ascii_lowercase:
            result += ch
    return result

def keep_words(filename):
    file = open(filename, "r")
    words = []
    final_words = []
    for line in file:
        line = line.lower()
        words = line.split()
        for word in words:
            candidate = process(word)
            if candidate != "":
                final_words += [candidate]
    file.close()
    return final_words

##def keep_letters(filename):
##    file = open(filename, "r")
##    modified_text = []
##    for line in file:
##        words = line.split()
##        print(words)
##    file.close()
##    return modified_text
##    
# ---------------------------

def keep_letters(filename):
    file = open(filename, "r")
    modified_text = ""
    line = file.readline()
    for line in file:
        line = line.lower()
        for letter in line:
            if letter == 'a':
                modified_text += letter
    print(modified_text.count('a'))           
    file.close()
    return modified_text

# ---------------------------

text = keep_letters("raven.txt")
print(text)

words = keep_words("raven.txt")
dictionary = create_dictionary(words)
print_dictionary(dictionary)
most_frequent_word(dictionary)
        
