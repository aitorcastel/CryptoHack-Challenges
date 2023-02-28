def gdc(x:int, y: int) -> int:
    # euclid's algorithm
    return gdc(int(y%x) , x) if x else y

def main():

    #a = 66528, b = 52920

    print("[>] Result: "+str(gdc(66528,52920)))
    return 0

if __name__ == "__main__":
    main()