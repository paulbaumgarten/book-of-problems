
def luhn_check(creditcard):
    # Remove any spaces in the number provided
    creditcard = creditcard.replace(" ","")
    # If we have anything non numeric, abort
    if not creditcard.isnumeric():
        return False
    # Convert credit card string to a list of numbers
    values = []
    for char in creditcard:
        values.append(int(char))
    # Double every second digit
    for i in range(len(values)):
        if i % 2 == 0:
            values[i] = 2 * values[i]
            # If the doubled number > 10, add the digits together
            # except the last value
            if values[i] > 9 and i<len(values)-1:
                values[i] = (values[i] // 10) + (values[i] % 10)
    # Sum the values together
    total = sum(values)
    print(f"The total is {total}")
    # Check the result
    if total % 10 == 0:
        return True
    else:
        return False

cc = input("Enter a credit card number: ")
while cc != "":
    result = luhn(cc)
    if result:
        print("The credit card number is valid")
    else:
        print("The credit card number is fake news")
    cc = input("Enter a credit card number: ")
