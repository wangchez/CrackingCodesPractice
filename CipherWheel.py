import string


class CipherWheel:
    def __init__(self, key):
        self.letters = list(string.ascii_uppercase)
        self.key = key

    def encrypt(self, message):
        ciphers = ''
        for m in message:
            try:
                index = self.letters.index(m)
                slot_number = index + self.key
                if slot_number >= len(self.letters):
                    slot_number = slot_number - len(self.letters)
                ciphers = ciphers + self.letters[slot_number]
            except ValueError:
                ciphers = ciphers + m
        return ciphers

    def decrypt(self, ciphers):
        plaintext = ''
        for c in ciphers:
            try:
                index = self.letters.index(c)
                slot_number = index - self.key
                if slot_number < 0:
                    slot_number = slot_number + len(self.letters)
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
