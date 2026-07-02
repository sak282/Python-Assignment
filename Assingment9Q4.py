def Cubenum(no):

    return no*no*no

def main():
    print("enter number:")
    value=int(input())

    ret=Cubenum(value)
    print("Cube of the no is :",ret)


if __name__=="__main__":
    main()


