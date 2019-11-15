
def isbn_check( val ):
    # Remove any hyphens or spaces in the isbn provided
    val = val.replace("-","")
    val = val.replace(" ","")
    # If we have anything non numeric, abort
    if not val.isnumeric():
        return False
    # If we don't have exactly 13 digits, abort
    if len(val) != 13:
        return False
    # Iterate over all the digits. 
    # The 2nd, 4th, 6th etc digit all need multiplying by 3
    total = 0
    for n in range(12):
        if n % 2 == 0:
            total = total + int(val[n])
        else:
            total = total + 3*int(val[n])
    # Calculate the check digit value
    check = (total % 10)
    if check != 0:
        check = 10 - check
    # See if our check digit matches the one provided
    if check == int(val[-1]):
        return True
    else:
        return False

a = "978-186-197-272-2"
result = isbn_check(a)
print(f"{a} = {result}")


