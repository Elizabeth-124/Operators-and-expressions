a=float(input("Enter a number"))
b=float(input("Enter a another number"))
sum=a+b
difference=a-b
product=a*b
quotient=a/b
print(f"The sum of {a} and {b} is {sum}")
print(f"The differece between {a} and {b} is {difference}")
print(f"The product of {a} and {b} is {product}")
print(f"The quotient of {a} and {b} is {quotient}")
if a>b:
    print(f"{a} is greater than {b}")
else:
    print(f"{a} is less than {b}")
if a>=b:
    print(f"{a}is greater than or equal to {b}")
else:
    print(f"{a}is less than or equal to {b}")
if a==b:
    print(f"{a}and {b} are equal")
else:
    print(f"{a} and {b} are not equal")