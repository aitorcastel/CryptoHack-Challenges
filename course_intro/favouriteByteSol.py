
encoded_flag = '73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'

def main():
    '''
    for iterator in range(256): 
        results = [chr(character^iterator) for character in bytes.fromhex(encoded_flag)]
        temp_flag = "".join(results)
        if(temp_flag.startswith('crypto')):
            print("[i] Secret byte: "+str(iterator)+"\n[>] Flag: "+temp_flag)
            break
    '''
    secret_byte = bytes.fromhex(encoded_flag)[0] ^ ord('c')
    print("[i] Secret Byte: "+str(secret_byte)+"\n[>] Flag: "+''.join(chr(character^secret_byte) for character in bytes.fromhex(encoded_flag)))

if __name__ == "__main__":
    main()