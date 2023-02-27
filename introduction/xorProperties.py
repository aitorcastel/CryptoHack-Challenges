
KEY1        = 'a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313'
KEY2_KEY1   = '37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e'
KEY2_KEY3   = 'c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1'
FLAG_KEY1_KEY3_KEY2 = '04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf'

def xor(keyA, keyB):

    bytes_keyA = bytes.fromhex(keyA)
    bytes_keyB = bytes.fromhex(keyB)

    return bytes.hex(bytes([(i ^ j) for (i,j) in zip(bytes_keyA,bytes_keyB)]))

def main():

    KEY2 = xor(KEY2_KEY1,KEY1)
    KEY3 = xor(KEY2_KEY3, KEY2)

    KEYFLAG = xor(KEY1, xor(FLAG_KEY1_KEY3_KEY2,KEY2_KEY3))

    print('[i] KEYS:\nKEY1: \t'+str(bytes.fromhex(KEY1)) +'\nKEY2: \t'+ str(bytes.fromhex(KEY2))+'\nKEY3: \t'+ str(bytes.fromhex(KEY3))+'\nKEYFLAG: \t'+ str(bytes.fromhex(KEYFLAG),'utf-8'))

if __name__ == "__main__":
    main()