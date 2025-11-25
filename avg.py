# avg.py
# Ben Underwood

numbers = []

for i in range(10):
    s = input(f"Enter decimal #{i+1}: ").strip()
    numbers.append(float(s))   # convert and store

avg = sum(numbers) / len(numbers)

print(f"The average is: {avg}")