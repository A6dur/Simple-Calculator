while(True):
    try: 

        a = int(input("Enter the 1st number :"))
        b = int(input("Enter the 2nd number :"))


        print("Enter the operation you want to perform on these number :\n + for addition \n - for subtraction \n * for multiplication \n / for division \n q for quit ")

        o = input("Enter operation : ")

        match o:
            case "+":
                print(f"The sum is : {a+b}")
            case "-":
                print(f"The differnce is : {a-b}")
            case "*":
                print(f"The product is : {a*b}")
            case "/":
                print(f"The division is : {a/b}")
            case "q":
                break
            case default : 
                print("There was an error")

    except Exception as e : 
        print("Enter a valid value of a and b")

