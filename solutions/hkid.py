
def hkid_check(hkid):
    """
    Check if a HKID number has a valid check digit
    """
    if len(hkid) == 10:
        # HKID with one letter at the start in this style: X0000000(0)
        if hkid[0].isalpha() and hkid[-3] == "(" and hkid[-1] == ")" and hkid[1:-3].isnumeric():
            # Convert the letter into a number from 1 to 26
            letters = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            letter_val = letters.index(hkid[0])
            # Perform calculation on each digit and total them together
            calculated = letter_val*8 + int(id[1])*7 + int(id[2])*6 + int(id[3])*5 + int(id[4])*4 + int(id[5])*3 + int(id[6])*2
            # Get the remainder when divided by 11
            remainder = calculated % 11
            check = 11 - remainder
            # Determine what the check digit should be
            if check == 11:
                check = "0"
            elif check == 10:
                check = "A"
            else:
                check = str(check)
            # Does our check digit match the one provided?
            if check == hkid[-2].upper():
                return True
            else:
                return False
        else:
            print("Incorrect format for a HKID. Expecting A000000(0)")
            return False
    elif len(hkid) == 11:
        # HKID with two letters at the start in this style: XX0000000(0)
        if hkid[0].isalpha() and hkid[1].isalpha() and hkid[-3] == "(" and hkid[-1] == ")" and hkid[2:-3].isnumeric():
            # Convert the letters into numbers from 1 to 26
            letters = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            letter1_val = letters.index(hkid[0])
            letter2_val = letters.index(hkid[1])
            # Perform calculation on each digit and total them together
            calculated = 8 + letter2_val*8 + int(id[1])*7 + int(id[2])*6 + int(id[3])*5 + int(id[4])*4 + int(id[5])*3 + int(id[6])*2
            # Get the remainder when divided by 11
            remainder = calculated % 11
            check = 11 - remainder
            # Determine what the check digit should be
            if check == 11:
                check = "0"
            elif check == 10:
                check = "A"
            else:
                check = str(check)
            # Does our check digit match the one provided?
            if check == hkid[-2].upper():
                return True
            else:
                return False
        else:
            print("Incorrect format for a HKID. Expecting AA000000(0)")
            return False
    else:
        print("Incorrect length for a HKID")
        return False

if __name__ == "__main__":
    id = input("Enter a HKID: ")
    valid = hkid_check(id)
    print(valid)
