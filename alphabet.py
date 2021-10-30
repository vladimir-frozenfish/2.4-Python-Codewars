# In this kata you are required to, given a string, replace every letter with its position in the alphabet.
# # If anything in the text isn't a letter, ignore it and don't return it.
def alphabet_position(text):
    alphabet = ['a','b','c','d','e','f','g','h',
                'i','j','k','l','m','n','o','p',
                'q','r','s','t','u','v','w','x','y','z']
    text_val = ''
    text = text.lower()

    for i in text:
        if i in alphabet:
            text_val += str(alphabet.index(i)+1) + ' '

    text_val = text_val.strip(' ')

    return text_val

print(alphabet_position("The sunset sets at twelve o' clock."))
