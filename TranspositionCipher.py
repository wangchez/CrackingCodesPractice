import string
from random import randint

import math


class TranspositionCipher:
    def __init__(self):
        self.letters = list(string.ascii_letters)
        self.key = 0

    def create_encrypted_boxes_version1(self, message):
        max_no = len(message)
        self.key = randint(2, int(max_no / 2))
        boxes = []
        for i in range(0, max_no, self.key):
            boxes.append(message[i:(i + self.key)])
        cipher_boxes = []
        for i in range(self.key):
            cipher_text = ''
            for j in range(len(boxes)):
                text = boxes[j]
                if len(text) > i:
                    cipher_text = cipher_text + text[i]
            cipher_boxes.append(cipher_text)
        return ''.join(cipher_boxes)

    def create_encrypted_boxes_version2(self, key, message):
        self.key = key
        boxes = [''] * key
        for column in range(key):
            current_index = column
            while current_index < len(message):
                boxes[column] += message[current_index]
                current_index += key
        return ''.join(boxes)

    def decrypt_boxes_version1(self, cipher_text, key_guessing=None):
        key = key_guessing or self.key
        divide_no = int(round(len(cipher_text) / key))
        boxes = [''] * divide_no
        for i in range(0, divide_no):
            no = (i + 1) * key
            if no < len(cipher_text):
                boxes[i] = [''] * key
            else:
                boxes[i] = [''] * (key - (no - len(cipher_text)))

        shadow_count = 0
        for i in range(0, key):
            for j in range(0, divide_no):
                if i < len(boxes[j]):
                    index = j + (i * divide_no) - shadow_count
                    boxes[j][i] = cipher_text[index]
                else:
                    shadow_count += 1
        return ''.join([''.join(translated) for translated in boxes])

    def decrypt_boxes_version2(self, cipher_text, key_guessing=None):
        key = key_guessing or self.key
        number_of_columns = int(math.ceil(len(cipher_text) / key))
        number_of_rows = key
        number_of_shaded_boxes = (number_of_columns * number_of_rows) - len(cipher_text)

        translated = [''] * number_of_columns
        column = 0
        row = 0
        for symbol in cipher_text:
            translated[column] += symbol
            column += 1

            if (column == number_of_columns) or (column == number_of_columns - 1 and
                                                 row >= number_of_rows - number_of_shaded_boxes):
                column = 0
                row += 1
        return ''.join(translated)


def main():
    transposition_cipher = TranspositionCipher()
    # print(transposition_cipher.create_encrypted_boxes_random_key(input("input message:")))
    ciphers = transposition_cipher.create_encrypted_boxes_version2(8, 'Common sense is not so common.')
    print(ciphers)
    print(transposition_cipher.decrypt_boxes_version2(ciphers, 8))


if __name__ == '__main__':
    main()
