# Caesars cipher

## TASK

Julius Caesar created one of the first own encryption algorithms. It used a substitution method where each letter was replaced by another a fixed number of letters across from the original. 

The amount each letter shifts is known as the cipher key value. A cipher key with a value of 1 would be the letter "a" would shift to become the letter "b" and so forth. Note in this instance the letter "z" would wrap back to the start to become the letter "a".

Program an implementation of the Caesar cipher that inputs (a) the plain text and (b) a cipher key value, and then outputs the correct cipher text. You should maintain upper/lower casing and ignore punctuation or digits.

| Example input                         | Cipher key | Example output                        |
| ------------------------------------- | ---------- | ------------------------------------- |
| attack                             | 3             |  dwwdfm                             |
| defend the east wall of the castle |      1        |  efgfoe uif fbtu xbmm pg uif dbtumf |
| captain my captain                 | 5             | hfuyfns rd hfuyfns                  |

## REMEMBER

* Your program must include appropriate prompts for the entry of data.
* Error messages and other output need to be set out clearly.
* All variables, constants and other identifiers must have meaningful names.

## NEXT

Look at the Vigenère cipher as an extension of the Caesar cipher.

