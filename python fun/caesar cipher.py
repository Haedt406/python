import string

def caesar_cipher(plain_text, key):
    result = ""
    for ch in plain_text:
        if ch in string.ascii_lowercase:
            result += "X"
        else:
            result += ch
    return result


answer = caesar_cipher(' the longest word in the english language is antidisestablistism.', 6)
print(answer)
