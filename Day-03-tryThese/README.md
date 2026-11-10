# AI Model Tracker

## What this project does
This small Python program helps you track how often different AI model names appear in a list.

For example, if you have a list like this:

```python
requests = ["GPT", "Claude", "GPT", "Gemini", "gpt"]
```

The program will:
- count how many times each model appears
- add all the counts together
- find which model appears the most
- ask for a token count
- print everything out nicely

It is a simple example of how Python can help us organize and analyze data.

## Why this is useful
This type of code is helpful when you want to:
- track repeated words or names
- analyze patterns in data
- learn how to use loops and dictionaries
- understand how real programs process information

## A kid-friendly explanation of the code

### 1) Importing helper functions
```python
from prctiSmodel_utils import (
    calculate_total_requests,
    count_requests,
    most_used_model,
)
```
This line imports functions from another file called `prctiSmodel_utils.py`.

Think of it like this: instead of writing all the logic in one place, we split it into small helper tools. That makes the code easier to read and reuse.

### 2) Creating a list of model names
```python
requests = ["GPT", "Claude", "GPT", "Gemini", "gpt"]
```
This is a list. A list is just a group of values stored together.

The program wants to count how often each model name appears in that list.

### 3) Asking for a token count
```python
while True:
    try:
        token_count = int(input("Enter token count: "))
        if token_count < 0:
            raise ValueError
        break
    except ValueError:
        print("Invalid token count. Enter a non-negative integer.")
```
This part keeps asking until the user enters a valid number.

- `input()` gets text from the user
- `int()` turns that text into a whole number
- if the number is negative, it raises an error
- the program shows a message and asks again

This is called input validation. It means: "Only accept good data."

### 4) Counting requests
```python
counts = count_requests(requests)
```
This calls a function that counts the number of times each model appears.

It turns this:
```python
["GPT", "Claude", "GPT", "Gemini", "gpt"]
```
into something like this:
```python
{'gpt': 2, 'claude': 1, 'gemini': 1}
```
This is a dictionary, which stores data as a key-value pair.

### 5) Adding everything up
```python
total_requests = calculate_total_requests(counts)
```
This adds all the counts together.

If the counts are:
```python
{'gpt': 2, 'claude': 1, 'gemini': 1}
```
then the total is:
```python
4
```

### 6) Finding the most used model
```python
most_used = most_used_model(counts)
```
This checks which model appears the most.

The `max()` function is used with the dictionary values to find the biggest count.

### 7) Printing results
```python
print("Counts:", counts)
print("Total requests:", total_requests)
print("Most used:", most_used)
print("Token count:", token_count)
```
This shows the results to the user in a readable way.

## What the helper file does
The helper file is `prctiSmodel_utils.py`.

It contains three functions:

### `count_requests(model_requests)`
This counts how many times each item appears in a list.

```python
def count_requests(model_requests):
    counts = {}

    for model in model_requests:
        model = model.lower()

        if model in counts:
            counts[model] += 1
        else:
            counts[model] = 1

    return counts
```

This works by:
- going through each item in the list
- changing it to lowercase so `GPT` and `gpt` are treated the same
- adding 1 each time it sees the same name

### `calculate_total_requests(counts)`
```python
def calculate_total_requests(counts):
    return sum(counts.values())
```
This adds all the numbers in the dictionary together.

### `most_used_model(counts)`
```python
def most_used_model(counts):
    if not counts:
        return None

    return max(counts, key=counts.get)
```
This finds the key with the highest value. In simple words: it picks the model that was used the most.

## Simple example
If the user enters:
```python
requests = ["GPT", "Claude", "GPT", "Gemini", "gpt"]
```
And enters:
```python
2500
```
The program may print something like:
```python
Counts: {'gpt': 2, 'claude': 1, 'gemini': 1}
Total requests: 4
Most used: gpt
Token count: 2500
```

## Learning goals
This project teaches:
- lists in Python
- dictionaries
- loops
- user input
- error handling
- functions and modular code

## Summary
This project is a beginner-friendly example of how code can count, compare, and report information. It is simple, but it shows real programming ideas used in data analysis, apps, and AI tools.

If you are learning Python, this is a great mini-project because it uses many important ideas in a small and understandable way.
