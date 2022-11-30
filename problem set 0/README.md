## 1. indoor.py

### Task:
In a file called indoor.py, implement a program in Python that prompts the user for input and then outputs that same input in lowercase. Punctuation and whitespace should be outputted unchanged. You’re welcome, but not required, to prompt the user explicitly, as by passing a str of your own as an argument to input.

### Test:

- Run your program with python indoor.py.
* Type HELLO and press Enter. 
- Your program should output:
```
hello.
```

```
Run your program with python indoor.py. 
Type THIS IS CS50 and press Enter. 
Your program should output:
this is cs50.
```

Run your program with python indoor.py. 
Type 50 and press Enter. 
Your program should output:
50.

2. playback.py

Task:

In a file called playback.py, implement a program in Python that prompts the user for input and then outputs that same input, replacing each space with ... (i.e., three periods)

Test:

Here’s how to test your code manually:

Run your program with python playback.py. 
Type This is CS50 and press Enter. 
Your program should output:
This...is...CS50
    
Run your program with python playback.py. 
Type This is our week on functions and press Enter. 
Your program should output:
This...is...our...week...on...functions

Run your program with python playback.py. 
Type Let's implement a function called hello and press Enter. 
Your program should output
Let's...implement...a...function...called...hello

3. faces.py

Task:

In a file called faces.py, implement a function called convert that accepts a str as input and returns that same input with any :) converted to 🙂 (otherwise known as a slightly smiling face) and any :( converted to 🙁 (otherwise known as a slightly frowning face). All other text should be returned unchanged.

Then, in that same file, implement a function called main that prompts the user for input, calls convert on that input, and prints the result. You’re welcome, but not required, to prompt the user explicitly, as by passing a str of your own as an argument to input. Be sure to call main at the bottom of your file.

Test:

Run your program with python faces.py. 
Type Hello :) and press Enter. 
Your program should output:
Hello 🙂

Run your program with python faces.py. 
Type Goodbye :( and press Enter. 
Your program should output:
Goodbye 🙁

Run your program with python faces.py. 
Type Hello :) Goodbye :( and press Enter. 
Your program should output:
Hello 🙂 Goodbye 🙁


4. einstein.py

Task:

In a file called einstein.py, implement a program in Python that prompts the user for mass as an integer (in kilograms) and then outputs the equivalent number of Joules as an integer. Assume that the user will input an integer.

Task:

Run your program with python einstein.py. 
Type 1 and press Enter. 
Your program should output:
90000000000000000

Run your program with python einstein.py. 
Type 14 and press Enter. 
Your program should output:
1260000000000000000

Run your program with python einstein.py. 
Type 50 and press Enter. 
Your program should output:
4500000000000000000

5. tip.py

Task:

Well, we’ve written most of a tip calculator for you. Unfortunately, we didn’t have time to implement two functions:

dollars_to_float, which should accept a str as input (formatted as $##.##, wherein each # is a decimal digit), remove the leading $, and return the amount as a float. For instance, given $50.00 as input, it should return 50.0.
percent_to_float, which should accept a str as input (formatted as ##%, wherein each # is a decimal digit), remove the trailing %, and return the percentage as a float. For instance, given 15% as input, it should return 0.15.
Assume that the user will input values in the expected formats.

Test:

Run your program with python tip.py. 
Type $50.00 and press Enter. 
Then, type 15% and press Enter. 
Your program should output:
Leave $7.50
    
Run your program with python tip.py. 
Type $100.00 and press Enter. 
Then, type 18% and press Enter. 
Your program should output:
Leave $18.00

Run your program with python tip.py. 
Type $15.00 and press Enter. 
Then, type 25% and press Enter. 
Your program should output:
Leave $3.75
