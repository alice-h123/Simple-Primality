"""
Filename: simple_primality.py
Author: <NAME>
Created: <DATE>
Instructor: Holtslander
"""

def prime():
    # Write your code here


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