def encode_str(text: str, encoding = 'utf-8', errors = 'surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]

    return hex(int(bits))



def decode_str(code: str, encoding = 'utf-8', errors='surrogatepass'):
    n = int(int(code, 16), 2)

    return n.to_bytes(byteorder='big').decode(encoding, errors) or '\0'

if __name__ == '__main__':
    print(encode_str('hello world'))
    print(decode_str(encode_str('hello world')))