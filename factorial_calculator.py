"""
Filename: factorial_calculator.py
Author: <alice hertz>
Created: <3/3/26>
Instructor: Holtslander
"""

def factorial():
    fact= int(input("pick a non-negative whole number\n"))
    num=fact
    count=0
    for i in range(fact,1,-1):
        fact *= i-1
        print(f"{i}", end="*")
    print(f"1={fact}")
    


# You should not need to change any code below this point
def main():
    print("This program computes factorials and displays their intermediate calculations.")
    running = "y"
    while running == "y":
        factorial()
        running = input("Do another calculation? (y/N)\n").lower()
    print("Thank you for using this factorial calculator!")

if __name__ == "__main__":
    main()