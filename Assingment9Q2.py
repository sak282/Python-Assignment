def ChkGreater(no1,no2):
    
    if no1>no2:
        return no1
    else:
        return no2
    

def main():
    print("Enter first number:")
    value1=int(input())

    print("Enter second number:")
    value2=int(input())
    
    ret=ChkGreater(value1,value2)

    print("Greater number is :",ret)

if __name__=="__main__":
    main()