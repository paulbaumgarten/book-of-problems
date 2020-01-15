# Credit card number validation

## The task

![](assets/luhn.jpg)

The Luhn algorithm or Luhn formula, also known as the “modulus 10” or “mod 10” algorithm, is a simple checksum formula used to validate a variety of identification numbers, such as credit card numbers, IMEI numbers, National Provider Identifier numbers (wikipedia).

The Luhn test is used by some credit card companies to distinguish valid credit card numbers from what could be a random selection of digits.

Those companies using credit card numbers that can be validated by the Luhn test have numbers that pass the following test:

* Double every second digit starting from the first, ie: the 1st, 3rd, 5th, 7th ... 
* If any value is now greater than 9, sum their individual digits together. (*For example if you had originally doubled 7, this would give a new value of 14, so you would sum 1+4 to result 5.*) **except the last value**
* Sum all the new values together.
* If the modulus ten of your sum total is zero, you have passed the Luhn algorithm test.

---

Worked example...

| Step                                  | Calculations |
| ------------------------------------- | ------------ | 
| Card number                           | `4  9  1  6  8  3  2  4  7  1  4  0  6  2  0  8` |
| Double the odd placed digits          | `8  9  2  6 16  3  4  4 14  1  8  0 12  2  0  8` |
| Sum the digits if >9 except the last  | `8  9  2  6  7  3  4  4  5  1  8  0  3  2  0  8` |
| Sum the digits together               | `8 +9 +2 +6 +7 +3 +4 +4 +5 +1 +8 +0 +3 +2 +0 +8 = 70` |
| Find the modulus with 10              | `70 % 10 = 0`                                    |
| If == 0, it is a valid card           | This card passed the test!                       |

Some fake credit card numbers you can use for testing purposes...

| VISA | MasterCard | American Express (AMEX) |
| ---- | ---------- | ----------------------- |
| 4916832471406208    |  5408608073972181 | 349916382888946 |
| 4539515831865208      |  5448131672611698 | 379279126081887 |
| 4556019822708469278   |  5345203118153280 | 372209733301573 |

## Remember

* Your program must include appropriate prompts for the entry of data.
* Error messages and other output need to be set out clearly.
* All variables, constants and other identifiers must have meaningful names.



