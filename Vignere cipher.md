# Vigenère cipher

## TASK ONE

Another early cipher, Vigenère used the letters of a key-word to determine how many positions an each letter shifted. 

The premise behind the cipher is that it can be encoded or decoded using a key word or phrase. For example, let's say you wanted to encode the message "HELLO" using the keyword "ONE". In this case, the keyword is shorter than the plain text, so you start repeating the keyword again until you have enough characters. Eg:

```
Plaintext: HELLO 
Keyword:   ONEON
```

The first character in the phrase is H and the first character in the keyword is O. To find the first character in your encoded phrase simply shift the plain text character by the  place value of the relevant key word letter value (a=0, b=1, c=2, d=3 etc). The step would be repeated for every subsequent character in the plaintext.

```
Plaintext:  HELLO 
Keyword:    ONEON 
Ciphertext: VRPZB
```


| Example input clear text  | Key word | Example output                        |
| ------------------------- | -------- | ------------------------------------- |
| defend the east wall of the castle  | help | kiqtuh ewl ilha alas sq ioi npzxwt |
| My name is Bond. James Bond. | secret | Ec prqx aw Dfrw. Beovw Ugrf.  |
|                           |          |                                       |

## TASK TWO

## TASK THREE

## MORE INFORMATION

* [https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher)


