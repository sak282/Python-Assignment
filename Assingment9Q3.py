def Squarenum(no):

    return no*no

def main():
    print("enter number:")
    value=int(input())

    ret=Squarenum(value)
    print("Square of the no is :",ret)


if __name__=="__main__":
    main()


