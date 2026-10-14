
sales = {
    "Monday": 2000,
    "Tuesday": 3000,
    "Wednesday": 7000,
    "Thursday": 4000,
    "Friday": 3000,
    "Saturday": 5000
}

total = sum(sales.values())
average = total / len(sales)
maximum = max(sales.values())
minimum = min(sales.values())

print("Total sales:", total)
print("Average sales:", average)
print("Maximum sales:", maximum)
print("Minimum sales:", minimum)

