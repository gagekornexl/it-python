from banner import banner
banner("Pythagorean Calculator","Gage")

print("We will help you find the missing side of a right triangle. The lengths of the two legs are 'a' and 'b', and the length of the hypotensue is 'c'.")
print("")


while True:
    print("Please enter the length of each side, or leave it blank if you don't know.")
    a = input("a = ")
    b = input("b = ")
    c = input("c = ")

    if a == "":
        b = float(b)
        c = float(c)
        a = ((c*c) - (b*b))**.5
        print(f"Your missing side length is {a}")


    if b == "":
        a = float(a)
        c = float(c)
        b = ((c*c) - (b*b))**.5
        print(f"Your missing side length is {b}")


    if c == "":
        b = float(b)
        a = float(a)
        c = ((c*c) - (b*b))**.5
        print(f"Your missing side length is {c}")

