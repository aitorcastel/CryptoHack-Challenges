def xorencript(label):

    string = ''
    for character in label:
        string += chr(ord(character)^13)
    return string

def main():
    flag = "label"
    print('crypto{'+xorencript(flag)+'}')

if __name__ == "__main__":
    main()

