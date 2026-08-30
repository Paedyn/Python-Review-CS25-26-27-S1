# Python Programming Review

This activity is pass-fail. For each section you will be asked to create a Python file and perform a small review task. By completing each task, you will pass that task.

The tasks you should complete are as follows:

1. [ ] [Primitive Data Types](#1-primitive-data-types)
2. [ ] [Output](#2-output)
3. [ ] [Input](#3-input)
4. [ ] [If Statements](#4-if-statements)
5. [ ] [Combining Conditions](#5-combining-conditions)
6. [ ] [For Loops](#6-for-loops)
7. [ ] [For Loops and Strings](#7-for-loops-and-strings)
8. [ ] [While loops](#8-while-loops)
9. [ ] [Input Validation with a While Loop](#9-input-validation-with-a-while-loop)
10. [ ] [Putting It Together](#10-putting-it-together)
11. [ ] [Final Review Challenge](#11-final-review-challenge)

By the end, you should have 11 distinct Python files that have been appropriately modified, and this assignment will be out of 11 marks.

If you need any help with the review material there are some [guidelines at the bottom of this document for an effective way to use AI to help you review](#ai-practice-prompt).

---

This activity reviews the Python skills you will need before moving into Computer Science 25. Work through each section in order. For each topic, you will:

1. Review the basic idea.
2. Run an example program.
3. Modify the example.
4. Write a small program of your own.

---

## 1. Primitive Data Types

Programs store information in **variables**. Every value stored in a variable has a **data type**.

The four primitive data types we will use most often are:

| Data Type | Description              | Examples               |
| --------- | ------------------------ | ---------------------- |
| `int`     | Whole numbers            | `5`, `-12`, `100`      |
| `float`   | Numbers with decimals    | `3.14`, `-0.5`, `10.0` |
| `str`     | Text                     | `"Hello"`, `"Python"`  |
| `bool`    | `True` or `False` values | `True`, `False`        |

Variables are created using the `=` assignment operator.

```python
name = "Alex"
age = 16
height = 1.72
likes_programming = True

print(name)
print(age)
print(height)
print(likes_programming)
```

### Try It

Create a new Python file named `data_types.py`.

Copy and run the program above.

Then change each variable so that it contains different information.

### Check the Data Type

Python's `type()` function tells you the data type of a value.

```python
name = "Alex"
age = 16
height = 1.72
likes_programming = True

print(type(name))
print(type(age))
print(type(height))
print(type(likes_programming))
```

Add the code above to `data_types.py` and run it.

### Create Your Own

In `data_types.py`, create four new variables:

* One `str`
* One `int`
* One `float`
* One `bool`

Print each variable.

---

## 2. Output

The `print()` function displays information to the console.

```python
name = "Sam"
score = 92

print("Welcome to Python!")
print(name)
print(score)
```

You can print several pieces of information together.

```python
name = "Sam"
score = 92

print("Student:", name)
print("Score:", score)
```

You can also use an **f-string** to insert variables into text.

```python
name = "Sam"
score = 92

print(f"{name} earned a score of {score}.")
```

### Try It

Create a new Python file named `output.py`.

Copy and run the f-string example above.

Change the values of `name` and `score`.

### Create Your Own

In `output.py`, create variables containing:

* Your name
* Your favourite number
* Your favourite school subject

Use one `print()` statement and an f-string to display all three pieces of information in a sentence.

---

## 3. Input

The `input()` function allows the user to enter information while the program is running.

```python
name = input("What is your name? ")

print(f"Hello, {name}!")
```

Anything returned by `input()` is automatically stored as a `str`.

If you want the user to enter a number, you need to convert the input.

```python
age = int(input("How old are you? "))

next_age = age + 1

print(f"Next year you will be {next_age}.")
```

For decimal numbers, use `float()`.

```python
temperature = float(input("Enter the temperature: "))

print(f"The temperature is {temperature} degrees.")
```

### Try It

Create a new Python file named `input.py`.

Copy and run this program:

```python
name = input("What is your name? ")
age = int(input("How old are you? "))

print(f"{name} is {age} years old.")
```

Modify the program so that it also asks the user for their favourite food.

### Create Your Own

In `input.py`, write a program that:

1. Asks the user for their name.
2. Asks the user for two numbers.
3. Adds the two numbers together.
4. Prints the result.

Example:

```text
What is your name? Alex
Enter a number: 10
Enter another number: 5

Alex, the total is 15.
```

---

# 4. If Statements

Programs often need to make decisions.

An `if` statement runs code only when a condition is `True`.

```python
temperature = 30

if temperature > 25:
    print("It is hot outside.")
```

Notice the colon `:` and indentation.

Python uses indentation to determine which code belongs inside the `if` statement.

Common comparison operators include:

| Operator | Meaning                  |
| -------- | ------------------------ |
| `==`     | Equal to                 |
| `!=`     | Not equal to             |
| `<`      | Less than                |
| `>`      | Greater than             |
| `<=`     | Less than or equal to    |
| `>=`     | Greater than or equal to |

---

## If / Else

An `else` statement runs when the `if` condition is `False`.

```python
age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult.")
else:
    print("You are under 18.")
```

### Try It

Create a new Python file named `if_else.py`.

Copy and run the program above.

Change the program so that it checks whether someone is old enough to drive based on an age of `16`.

---

## If / Elif / Else

Sometimes a program needs to choose between several possibilities.

```python
score = int(input("Enter your score: "))

if score >= 80:
    print("Excellent")
elif score >= 70:
    print("Good")
elif score >= 60:
    print("Satisfactory")
else:
    print("Keep practicing")
```

Python checks the conditions from top to bottom.

Once it finds a condition that is `True`, it runs that block and skips the remaining options.

### Try It

Add the example above to `if_else.py`.

Run the program several times using different scores.

Try:

```text
95
75
65
40
```

### Create Your Own

Create a new Python file named `temperature_checker.py`.

Write a program that asks the user for the current temperature.

The program should print:

* `"Very hot"` if the temperature is `30` or higher.
* `"Warm"` if the temperature is `20` or higher.
* `"Cool"` if the temperature is `10` or higher.
* `"Cold"` otherwise.

---

# 5. Combining Conditions

Conditions can be combined using:

* `and`
* `or`
* `not`

## `and`

Both conditions must be `True`.

```python
age = int(input("Enter your age: "))
has_permission = input("Do you have permission? ")

if age >= 16 and has_permission == "yes":
    print("You may participate.")
else:
    print("You may not participate.")
```

## `or`

At least one condition must be `True`.

```python
day = input("Enter the day of the week: ")

if day == "Saturday" or day == "Sunday":
    print("It is the weekend.")
else:
    print("It is a weekday.")
```

### Create Your Own

Create a new Python file named `event_entry.py`.

Write a program that asks the user for:

* Their age
* Whether they have a ticket

Allow them to enter an event only if they are at least `14` **and** have a ticket.

---

# 6. For Loops

A loop repeats a block of code.

A `for` loop is useful when you know how many times something should repeat.

```python
for number in range(5):
    print(number)
```

This produces:

```text
0
1
2
3
4
```

`range(5)` generates the numbers from `0` up to, but not including, `5`.

---

## Starting and Stopping

You can give `range()` a starting and stopping value.

```python
for number in range(1, 6):
    print(number)
```

Output:

```text
1
2
3
4
5
```

---

## Changing the Step

A third number controls how much the loop increases each time.

```python
for number in range(0, 11, 2):
    print(number)
```

Output:

```text
0
2
4
6
8
10
```

### Try It

Create a new Python file named `for_loops.py`.

Write a loop that prints:

```text
1
2
3
4
5
6
7
8
9
10
```

### Modify It

In the same file, change your loop so that it prints:

```text
10
20
30
40
50
60
70
80
90
100
```

### Create Your Own

Create a new Python file named `multiplication_table.py`.

Ask the user for a number.

Use a `for` loop to print that number's multiplication table from `1` to `10`.

Example:

```text
Enter a number: 5

5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
```

---

# 7. For Loops and Strings

A `for` loop can also move through the characters in a string.

```python
word = "Python"

for letter in word:
    print(letter)
```

Output:

```text
P
y
t
h
o
n
```

### Try It

Create a new Python file named `string_loop.py`.

Copy and run this program:

```python
word = input("Enter a word: ")

for letter in word:
    print(letter)
```

### Create Your Own

In `string_loop.py`, modify your program so that it asks the user for a word and counts how many times the letter `"a"` appears.

For example:

```text
Enter a word: banana
The letter a appears 3 times.
```

---

# 8. While Loops

A `while` loop repeats **while a condition remains `True`**.

```python
number = 1

while number <= 5:
    print(number)
    number = number + 1
```

Output:

```text
1
2
3
4
5
```

Be careful with `while` loops.

If the condition never becomes `False`, the program creates an **infinite loop**.

For example:

```python
number = 1

while number <= 5:
    print(number)
```

`number` never changes, so `number <= 5` will always be `True`.

---

## While Loops with Input

A `while` loop can repeat until the user gives a particular answer.

```python
password = ""

while password != "python":
    password = input("Enter the password: ")

print("Access granted.")
```

### Try It

Create a new Python file named `while_loops.py`.

Copy and run the password program.

Change the correct password to something different.

### Create Your Own

Create a new Python file named `number_entry.py`.

Write a program that repeatedly asks the user to enter a number.

The program should stop when the user enters `0`.

---

# 9. Input Validation with a While Loop

Loops are useful when you need to make sure the user enters a valid value.

```python
number = int(input("Enter a number from 1 to 10: "))

while number < 1 or number > 10:
    print("Invalid number.")
    number = int(input("Enter a number from 1 to 10: "))

print(f"You entered {number}.")
```

### Create Your Own

Create a new Python file named `percentage_validator.py`.

Ask the user to enter a percentage from `0` to `100`.

If they enter an invalid number, continue asking until they enter a valid percentage.

---

# 10. Putting It Together

Create a new Python file named `number_guessing_game.py`.

Create a small number guessing game.

Your program should:

1. Store a secret number between `1` and `10`.
2. Ask the player to guess the number.
3. Use a `while` loop to continue until they guess correctly.
4. Tell the player whether each incorrect guess is too high or too low.
5. Print a congratulatory message when they find the correct answer.

Example:

```text
Guess the secret number: 4
Too low!

Guess the secret number: 8
Too high!

Guess the secret number: 6
Correct!
```

Start with a fixed secret number rather than generating a random number.

---

# 11. Final Review Challenge

Create a new Python file named `number_analyzer.py`.

Create a program called **Number Analyzer**.

The program should first ask the user how many numbers they would like to enter.

```text
How many numbers would you like to enter? 5
```

Use a `for` loop to ask for that many numbers.

For each number, print whether it is:

* Positive
* Negative
* Zero

Also print whether a non-zero number is:

* Even
* Odd

Example:

```text
How many numbers would you like to enter? 3

Enter number 1: 8
8 is positive.
8 is even.

Enter number 2: -5
-5 is negative.
-5 is odd.

Enter number 3: 0
0 is zero.
```

Your program should include:

* Variables
* `int`
* `input()`
* `print()`
* An f-string
* `if`
* `elif`
* `else`
* A `for` loop

---

# Review Checklist

Before moving on, make sure you can do each of the following without copying an example.

* [ ] Create and assign variables.
* [ ] Identify `int`, `float`, `str`, and `bool` values.
* [ ] Display information using `print()`.
* [ ] Insert variables into output using f-strings.
* [ ] Get information from the user using `input()`.
* [ ] Convert user input using `int()` and `float()`.
* [ ] Write an `if` statement.
* [ ] Write an `if` / `else` statement.
* [ ] Write an `if` / `elif` / `else` statement.
* [ ] Compare values using comparison operators.
* [ ] Combine conditions using `and` and `or`.
* [ ] Create a `for` loop using `range()`.
* [ ] Use a `for` loop to process a sequence.
* [ ] Create a `while` loop.
* [ ] Update a variable inside a loop.
* [ ] Use a loop to repeatedly request input.
* [ ] Combine variables, input, output, conditions, and loops in one program.

---

# Using AI for Extra Review

If there is a topic from this review that you do not remember well, you can use an AI assistant to give you additional practice.

The goal is **not** to have the AI write programs for you. Instead, use it like a tutor that gives you small programming challenges, checks your attempts, and helps you understand mistakes.

Replace `[TOPIC]` in the prompt below with the topic you want to practice.

Possible topics include:

* Primitive data types
* Variables
* Input
* Output and f-strings
* If statements
* If / elif / else
* Comparison operators
* `and`, `or`, and `not`
* For loops
* `range()`
* While loops
* Input validation

## AI Practice Prompt

For additional practice with a topic, copy and paste this prompt into an LLM of your choice, replacing `[TOPIC]` with the topic you would like more practice with.

```text
I am reviewing Python programming and need more practice with [TOPIC].

Act as a programming tutor. Give me one small Python programming challenge at a time that focuses specifically on [TOPIC].

Do not give me the solution before I attempt the problem.

For each challenge:

1. Briefly explain any important concept I need to remember.
2. Give me a small programming task to complete.
3. Wait for me to write my code.
4. Check my code and tell me whether it works.
5. If I make a mistake, explain what is wrong without immediately giving me the completed solution.
6. Give me a hint and allow me to try again.
7. Once I solve the problem, briefly explain why my solution works.
8. Give me another challenge that is slightly more difficult.

Keep the programs short and appropriate for someone reviewing introductory Python.

Continue until I tell you to stop.
```

## If You Are Completely Stuck

If you cannot remember how a topic works at all, use this version first:

```text
I am reviewing Python and do not remember how [TOPIC] works.

Teach me the basics of [TOPIC] using short Python examples.

After explaining it, give me one very simple programming challenge to try myself. Do not provide the solution until I have attempted it.

If my code is incorrect, explain the specific problem, give me a hint, and let me try again before showing any solution.

Once I understand the basic challenge, gradually give me more difficult challenges involving [TOPIC].
```

## If You Want a Challenge

If you already understand the basics but want additional practice:

```text
Give me a series of short Python programming challenges focused on [TOPIC].

Start at an introductory level and gradually increase the difficulty.

Give me only one challenge at a time and wait for my code before continuing.

Do not write the solution for me. If my solution has a problem, identify what part of my code I should investigate and give me a hint.

After I successfully complete each challenge, give me the next one.
```

