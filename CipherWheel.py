import string


class CipherWheel:
    def __init__(self, key):
        self.letters = list(string.ascii_uppercase)
        self.wheel = []
        alphabet_len = len(self.letters)
        for _ in range(alphabet_len):
            if key < alphabet_len:
                self.wheel.append(key)
                key = key + 1
            else:
                self.wheel.append(0)
                key = 1

    def encrypt(self, message):
        ciphers = ''
        for m in message:
            try:
                index = self.letters.index(m)
                slot_number = self.wheel[index]
                ciphers = ciphers + self.letters[slot_number]
            except ValueError:
                ciphers = ciphers + m
        return ciphers

    def decrypt(self, ciphers):
        plaintext = ''
        for c in ciphers:
            try:
                index = self.letters.index(c)
                slot_number = self.wheel.index(index)
                plaintext = plaintext + self.letters[slot_number]
            except ValueError:
                plaintext = plaintext + c
        return plaintext


if __name__ == '__main__':
    cipher_Wheel = CipherWheel(int(input("input encryption key:")))

    input_message = input("input plaintext:").upper()

    encrypt_or_decrypt = input("Encrypt(e) or decrypt(d):").lower()

    if encrypt_or_decrypt == 'e':
        plaint_txt = cipher_Wheel.encrypt(input_message)
        print(plaint_txt)
    elif encrypt_or_decrypt == 'd':
        cipher_text = cipher_Wheel.decrypt(input_message)
        print(cipher_text)

    print(cipher_Wheel.wheel)
