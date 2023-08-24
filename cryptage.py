from itertools import cycle

#cette fonction de cryptage prend en parametre le mot a crypter et une clé de cryptage 

def xor_crypt_string(data, cle):
    return ''.join(chr(ord(x) ^ ord(y)) for (x,y) in zip(data, cycle(cle)))

"""La variable cle est la clé du cryptage 
#le cryptage change lorsque cette variable change """

cle = 'my secret key'

message = input(" Entrer le mot a crypter")

message_crypte = xor_crypt_string(message, cle)
print(f'Encrypted message: {message_crypte} \n')

message_decrypte = xor_crypt_string(message_crypte, cle)
print(f'Decrypted message: {message_decrypte} \n' )