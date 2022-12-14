def cipher(text, shift, encrypt=True):
    """	
       Encrypts a string of text (1st argument) by shifting each letter
       by the integer "shift" (2nd argument) towards the end of the alphabet.
       If "encrypt" (3rd argument) is set to False, the function will decrypt 
       the string of text by shifting the letters towards the start of the
       alphabet. The alphabet string used is duplicated for capitals as follows:
       'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'. 

       Parameters
       ----------
       text : string
       shift : integer
       encrypt : boolean

       Returns
       -------
       Encrypted or decrypted string.

       Examples
       --------
       >>> import cipher_fb2493
       >>> cipher_fb2493.cipher("hello world",3,True)
       'khoor zruog'
       """ 
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text
