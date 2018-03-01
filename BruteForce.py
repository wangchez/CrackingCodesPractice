from CipherWheel import CipherWheel

if __name__ == '__main__':
    cipher_wheel = CipherWheel()

    plain_text = 'Guess the encrypt key'
    cipher_text = cipher_wheel.encrypt(plain_text)

    symbol = cipher_wheel.letters

    for key in range(0, len(symbol)):
        translated = ''
        for cipher_bit in cipher_text:
            if cipher_bit in symbol:
                index = symbol.index(cipher_bit)
                slot_number = index - key
                if slot_number < 0:
                    slot_number = slot_number + len(symbol)
                translated = translated + symbol[slot_number]
            else:
                translated = translated + cipher_bit
        if translated == plain_text:
            print("key:{}-translated:{}-Perfect decrypt".format(key, translated))
        else:
            print("key:{}-translated:{}-Wrong decrypt".format(key, translated))