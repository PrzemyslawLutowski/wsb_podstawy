import string


class CezarCipher:
    def __init__(self, text, rot):
        self.alphabet = ""
        self.text = text.lower()
        self.rot = rot

    def alphabet_generating(self):
        self.alphabet = string.ascii_lowercase
        return self.alphabet

    def nuber_list(self):
        self.alphabet_generating()
        self.code = []
        for i in self.text:
            for ii in range(0, len(self.alphabet), +1):
                if self.alphabet[ii] == i:
                    if ii >= len(self.alphabet) - self.rot:
                        ii = self.rot - (len(self.alphabet) - ii)
                        self.code.append(ii)
                    else:
                        self.code.append(ii + self.rot)
                elif " " == i:
                    self.code.append(" ")
                    break
        return self.code

    def encrypt(self):
        self.nuber_list()
        text_encrypted = ""
        for i in self.code:
            if i == " ":
                text_encrypted += " "
            else:
                text_encrypted += self.alphabet[i]
        self.text = text_encrypted
        return self.text

    def decrypt(self):
        self.rot = self.rot - self.rot * 2
        self.encrypt()
        return self.text


rot = 10
text_encrypt = CezarCipher(text='Welcome to cezar world of cipher', rot=rot).encrypt()
print(text_encrypt)

text_decrypt = CezarCipher(text=text_encrypt, rot=rot).decrypt()
print(text_decrypt)
