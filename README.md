# Ciphers

This project features two ciphers, both of which take in any input and disguise the message using the unique features of the cipher
  1. Caesar Cipher
  2. Poly Alphabetic Cipher

### Caesar Cipher :
Known for being a very simple and popular cipher

This cipher notes the index position in the English alphabet of every letter in the inputted message.
Based on the numerical shift value the user enters, the cipher will replace each letter in the message with the letter in the English alphabet that is
however many shifts to the right as the shift specifies.

For example, the word "ACE" with a shift of 2 will be ciphered into "CEG" because those respective letters are two positions to the right
in the English alphabet

### Poly Alphabetic Cipher:
Was created to be a more safer cipher than the Caesar cipher since the shift values are not consistent

User inputs a single word from the English alphabet as the shift for this cipher. The index positions of every letter in this shift word
is noted, and then those numerical shift values are applied to the inputted message.

For example, if the word "ABZ" is entered as a shift, then the first letter of the message will have a shift of 1, the second letter will have 
a shift of 2, and the third letter will have a shift of 26 because these are their respective positions in the alphabet.

Note:
For both of these ciphers, after reaching the rightmost letter in the alphabet Z, the shift continues from the beginning letter A

## Built With:
Python

## Author:
Shruthi Kondin

