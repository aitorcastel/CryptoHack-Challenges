encoded_flag = '0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104'
initial_flag = 'crypto{'
final_flag = '}'

def xor(keyA: bytes, keyB: bytes) -> bytes:
    return bytes(bytes([(i ^ j) for (i,j) in zip(keyA,keyB)]))

def main():

    secret_key_part1 = str(xor(bytes.fromhex(encoded_flag)[:7],bytes(initial_flag, 'ascii')), 'utf-8')
    secret_key_part2 = str(xor(bytes.fromhex(encoded_flag)[-1:],bytes(final_flag, 'ascii')),'utf-8')
    secret_key = secret_key_part1 + secret_key_part2
    
    flag = []

    for i in range(len(bytes.fromhex(encoded_flag))):
        flag.append(secret_key.encode()[i % len(secret_key.encode())] ^ bytes.fromhex(encoded_flag)[i])

    print("[i] Secret key: "+secret_key
        +"\n[>] Flag: "+bytes(flag).decode('utf-8'))

if __name__ == "__main__":
    main()