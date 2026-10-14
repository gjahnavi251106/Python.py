marks=int(input("Enter marks:"))

if marks>=35 and marks<55:
    prnt("Grade c")
elif marks>=55 and marks<75:
    print("Grade b")
elif marks>=75 and marks<100:
    print("Grade a")
else:
    print("Invalid marks")