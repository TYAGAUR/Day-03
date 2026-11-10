# Day-03: Learning Python with AI Model Examples

## What is this folder for?

This folder contains beginner Python exercises. They use AI model names such as
GPT, Claude, and Gemini as sample data, but they do **not** connect to AI
services or send requests to the internet.

The examples help you practise:

- getting information from the keyboard
- handling mistakes without crashing
- using Python modules from the standard library
- splitting your own code into separate files
- counting items with a dictionary
- finding which item appears most often

Think of a Python program like a recipe: it gives the computer steps to follow.
These exercises show how to organize those steps and handle different inputs.

## Folder map

```text
Day-03/
├── tryExcept/
│   └── tryExcept.py
├── ownModleErrHndling/
│   ├── Import.py
│   └── functionImport.py
├── myModule/
│   ├── main.py
│   └── model_utils.py
└── Day-03-tryThese/
    ├── prctiSmain.py
    ├── prctiSmodel_utils.py
    └── README.md
```

The folder names are kept as they are in the project, including
`ownModleErrHndling`.

## The examples

### 1. Catching invalid input

File: [`tryExcept/tryExcept.py`](./tryExcept/tryExcept.py)

This program asks you to enter a token count, then tries to turn your answer
into a whole number using `int()`.

- `try` means “try these steps.”
- `except ValueError` handles the problem if the answer is not a whole number.
- Instead of showing a long error and stopping, the program prints a helpful
  message.

For example, entering `250` works, while entering `hello` displays an error
message written for the user.

### 2. Importing Python's `random` module

Files:

- [`ownModleErrHndling/Import.py`](./ownModleErrHndling/Import.py)
- [`ownModleErrHndling/functionImport.py`](./ownModleErrHndling/functionImport.py)

Both files choose one name at random from a list of model names.

`Import.py` imports the `random` module and calls `random.choice(...)`.
`functionImport.py` imports just the `choice` function and calls `choice(...)`.
These are two ways to use code that Python already provides.

### 3. Making your own Python module

Files:

- [`myModule/main.py`](./myModule/main.py)
- [`myModule/model_utils.py`](./myModule/model_utils.py)

`model_utils.py` holds helper functions for counting model names and finding
the most common one. `main.py` imports those functions, gives them a list, and
prints the results.

Keeping helpers in a separate file is useful when a program grows: each file
can focus on one job, and the same helper can be reused by other programs.

### 4. Putting the ideas together

Files:

- [`Day-03-tryThese/prctiSmain.py`](./Day-03-tryThese/prctiSmain.py)
- [`Day-03-tryThese/prctiSmodel_utils.py`](./Day-03-tryThese/prctiSmodel_utils.py)
- [`Day-03-tryThese/README.md`](./Day-03-tryThese/README.md)

This example combines helper functions with input checking. It counts the
sample model names, calculates the total number of names, finds the most common
one, and asks the user for a non-negative token count.

The token count is separate from the model-name list: this is a practice
program, not a real usage tracker.

The folder's own README explains this example in more detail.

## How to run an example

You need Python installed. Open a terminal in the `Day-03` folder and run one
of these commands:

```text
python .\tryExcept\tryExcept.py
python .\ownModleErrHndling\Import.py
python .\ownModleErrHndling\functionImport.py
python .\myModule\main.py
python .\Day-03-tryThese\prctiSmain.py
```

On some computers, the Python command is named `python3` instead of `python`.
When prompted, type an answer and press Enter. For the token-count programs,
enter a whole number; the final practice example also rejects negative numbers.

## A few Python words

- **List:** An ordered group of values, written with square brackets, such as
  `["GPT", "Claude", "GPT"]`.
- **Function:** A named set of steps that can be used when needed.
- **Module:** A Python file that can provide functions to another Python file.
- **Dictionary:** A collection of key/value pairs. Here, a model name is the key
  and its count is the value.
- **Exception:** An error that happens while a program is running. `try` and
  `except` let the program respond to some errors.
- **Input validation:** Checking that a user's answer is in an acceptable form.

## What to try next

1. Add another name to one of the model lists.
2. Run the program again and see how the counts change.
3. Try typing letters instead of a number in a token-count exercise.
4. Read the helper module, then find where the main program imports it.

These are small examples, but the same ideas are used in much larger programs:
break work into functions, put related code in modules, and check user input
before relying on it.
