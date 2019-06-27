try_timer = 3
while True:    
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
    finally:
        try_timer -=1
        if(try_timer < 0):
            print("try 3 times")
            try_timer= 3
    print("Run after try ... exception clause")    #



    