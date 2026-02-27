"""
Filename: simple_primality.py
Author: Alice Hertz
Created: 2/27/2026
Instructor: Holtslander
"""

def prime():
    num=int(input("pick a non-negative whole number\n"))
    
    for i in range (num-1,1,-1):
        if num%i == 0:
            print("this isnt a prime number")
            break
    else:
        print("this is a prime number")



    


# You should not need to change any code below this point
def main():
    print("This program will determine the primality of a number.")
    running = "y"
    while running == "y":
        prime()
        running = input("Check another number? (y/N)\n").lower()
    print("Thank you for using this primality program!")

if __name__ == "__main__":
    main()