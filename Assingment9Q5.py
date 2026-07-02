def Chkdivi(no):
    if no%3==0 and no%5==0:
        return no
    
    
def main():
    print("enter number:")
    value=int(input())

    ret=Chkdivi(value)
    print("The number  is divisile by 3 and 5 :")


if __name__=="__main__":
    main()


