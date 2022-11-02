from cipher_fb2493 import cipher_fb2493

def test_cipher_with_word():
    assert cipher_fb2493.cipher("Hello",3,True) == 'Khoor', "Should be 'Khoor'"

def test_cipher_with_negative_shift():
    assert cipher_fb2493.cipher("Hello",-3,True) == 'Ebiil', "Should be 'Ebiil'"
   
