
def task1():
    MIN_SAFE_TEMP = 36.0
    MAX_SAFE_TEMP = 37.5
    temperature = float(input("Please enter the baby's temperature: "))
    if temperature < MIN_SAFE_TEMP:
        print("Warning: Baby temperature is too low")
    elif temperature > MAX_SAFE_TEMP:
        print("Warning: Baby temperature is too high")

def task2():
    MIN_SAFE_TEMP = 36.0
    MAX_SAFE_TEMP = 37.5
    temperatures = []
    while len(temperatures) < 18:    # 10 minute intervals in 3 hours = 18 measurements
        temperature = float(input("Please enter the baby's temperature: "))
        if temperature < MIN_SAFE_TEMP:
            print("Warning: Baby temperature is too low")
        elif temperature > MAX_SAFE_TEMP:
            print("Warning: Baby temperature is too high")
        temperatures.append(temperature)
    highest = max(temperatures)
    lowest = min(temperatures)
    difference = highest - lowest
    print(f"The highest temperature was {highest}")
    print(f"The lowest temperature was {lowest}")
    print(f"The difference in temperatures was {difference}")

def task3():
    MIN_SAFE_TEMP = 36.0
    MAX_SAFE_TEMP = 37.5
    temperatures = []
    range_violations = 0
    while len(temperatures) < 18:
        temperature = float(input("Please enter the baby's temperature: "))
        if temperature < MIN_SAFE_TEMP:
            print("Warning: Baby temperature is too low")
            range_violations += 1
        elif temperature > MAX_SAFE_TEMP:
            print("Warning: Baby temperature is too high")
            range_violations += 1
        temperatures.append(temperature)
        highest = max(temperatures)
        lowest = min(temperatures)
        difference = highest - lowest
        if difference > 1.0:
            print("Warning: Baby temperature difference over 1 degree in 3 hours")
        if range_violations > 2:
            print("Warning: Baby temperature outside acceptable range more than twice")
    print(f"The highest temperature was {highest}")
    print(f"The lowest temperature was {lowest}")
    print(f"The difference in temperatures was {difference}")

print()
print()
task1()


