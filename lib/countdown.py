def countdown(n): 
    
    while n > 0:
        print(f"{n} SECOND(S)!")
        n -= 1
    print("HAPPY NEW YEAR!")

def countdown_with_sleep(n): 
    import time

    while n > 0:
        print(f"{n} SECOND(S)!")
        n -= 1
        time.sleep(1)
    print("HAPPY NEW YEAR!")


print(countdown_with_sleep(15))