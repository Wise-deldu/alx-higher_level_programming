# 0x00. Python - Hello, World projects

## Concepts
* This project explores the concept of Python programming

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General
Why Python programming is awesome
Who created Python
Who is Guido van Rossum
Where does the name ‘Python’ come from
What is the Zen of Python
How to use the Python interpreter
How to print text and variables using `print`
How to use strings
What are indexing and slicing in Python
What is the official Python coding style and how to check your code with `pycodestyle`

### Requirements
#### Python Scripts
* Allowed editors: `vi`, `vim`, `emacs`
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All your files should end with a new line
* The first line of all your files should be exactly #!/usr/bin/python3
* A `README.md` file at the root of the repo, containing a description of the repository
* A `README.md` file, at the root of the folder of this project, is mandatory
* Your code should use the pycodestyle (version `2.8.*`)
* All your files must be executable
* The length of your files will be tested using `wc`

#### Shell Scripts
* Allowed editors: vi, vim, emacs
* All your scripts will be tested on Ubuntu 20.04 LTS
* All your scripts should be exactly two lines long (`wc -l file` should print 2)
* All your files should end with a new line
* The first line of all your files should be exactly `#!/bin/bash`
* All your files must be executable

#### C Scripts
* Allowed editors: `vi`, `vim`, `emacs`
* All your files will be compiled on Ubuntu 20.04 LTS using gcc, using the options -Wall -Werror -Wextra -pedantic -std=gnu89
* All your files should end with a new line
* Your code should use the `Betty` style. It will be checked using betty-style.pl and betty-doc.pl
* You are not allowed to use global variables
* No more than 5 functions per file
* In the following examples, the `main.c` files are shown as examples. You can use them to test your functions, but you don’t have to push them to your repo (if you do we won’t take them into account). We will use our own `main.c` files at compilation. Our `main.c` files might be different from the one shown in the examples
* The prototypes of all your functions should be included in your header file called lists.h
* Don’t forget to push your header file
* All your header files should be include guarded.

## Tasks
### 0-run
* The task is to write a Shell script that runs a Python script.
* The Python file name will be saved in the environment variable `$PYFILE`
* Using the command `export PYFILE=main.py`
* And the expected output is `Best School` after the command `./0-run` is executed.

**Explanation:** 
* The `export` keyword instructs the shell to create a new environmental variable
* The `PYFILE=main.py` assigns the value `main.py` to the variable `PYFILE`
* The `$` sign in front of `$PYFILE` is used to substitute the value of the environment variable `PYFILE` into the command
* So, the command `python $PYFILE` effectively becomes `python3 main.py`
* The [main.py](./main.py) is exported into the [0-run](./0-run) to get the desired output by following the commands below:
* 1. `export PYFILE=main.py` and
* 2. `/.0-run`


### 1-run_inline
* The task here is to write a *Shell script* that runs a *Python code*. 
* The *Python code* will be saved in the environment variable `$PYCODE`.

**Explanation:**
* The `python3 -c "$PYCODE"` is used to execute a string of Python code directly from the command line without the need to create a separate `.py` file.
* The `-c`: flag tells the Python interpreter to execute the following string as Python code.
* The `"PYCODE"`: is a shell variable that contains the Python code to be executed. 
* `export PYCODE='print(f"Best School: {88+10")'` is entered on the terminal
* Then the executed file [1-run_inline](./1-run_inline) `./1-run_inline` is executed to produce the output `Best school: 98`

### 2-print.py
* The task here is to write a *Python script* that prints exactly `"Programming is like building a multilingual puzzle` followed by a new line.
* The requirement is to use the `print` function.

**Explanation:**
* This task is simple and straightforward. 
* To achieve `"` in front of the strings without errors due to double quotations, a `\` is used in front `"` to maintain it in the strings.
* Here is the [solution](./2-print.py)

### 3-print_number.py
* The requirement for this task is to complete this [source code](https://github.com/alx-tools/0x00.py/blob/master/3-print_number.py) in order to print the integer stored in the variable `number`, followed by `Battery street`, followed by a new line. 
* The output of the script should be:
  * the number, followed by `Battery street`,
  * followed by a new line.
* It is not allowed to cast the variable `number` into a string.
* It is required to use f-strings. 
* Output must be: `98 Battery street`.

**Explanation:**
* Here, the [solution](./3-print_number.py) is straightforward with f-strings.
* The `d` attached to `number` in the curly braces indicates **decimal integer** which is a format specifier that that tells Python to format `number` as decimal integer.
* After executing the `./3-print_number.py`, the output is `98 Battery street`.

### 4-print_float.py
* The requirement for this task is to complete the [source code](https://github.com/alx-tools/0x00.py/blob/master/4-print_float.py) in order to print the float stored in the variable `number` with a precision of 2 digits.
* The output of the program should be:
  * `Float:`, followed by the float with only 2 digits.
  * followed by a new line.
* It is not allowed to cast `number` to string.
* It is must to use f-strings.
* Output must be: `Float: 3.14`.

**Explanation:**
* This [solution](./4-print_float.py) contains `{number:.2f}` with the following meaning:
  * `number` is the variable holding the floating value.
  * `:` indicates what follows is a formatting specification.
  * `.2f` formats the number as a floating-point number with 2 decimal places.
* When [./4-print_float.py](./4-print_float.py) is executed, the desired output `Float: 3.14` was yielded.

### 5-print_string.py
* The requirement for this task is to complete the [source code](https://github.com/alx-tools/0x00.py/blob/master/5-print_string.py) in order to print 3 times a string stored in the variable `str`, followed by its 9 characters.
* The output of the program should be:
  * 3 times the value of `str`
  * followed by a new line
  * followed by the 9 first characters of `str`
  * followed by a new line
* It is not allowed to use any loop or conditional statement.
* The program should be maximum 5 lines long.
* The output of the program should be:
  * `Holberton SchoolHolberton SchoolHolberton School`
  * `Holberton`

**Explanation:**
* The [solution](./5-print_string.py) contains 2 main parts.
  * The multiplication of `str` variable by 3.
  * And printing the substring of `str` by using slicing method where the 9 characters were produced by using `str[0:9]`. This means take substring of `str` starting from index '0' up to '8' but not including '9'.
* This [./5-print_string.py](./5-print_string.py) yielded the desired output.

### 6-concat.py
* The requirement of this task is to complete this [source code](https://github.com/alx-tools/0x00.py/blob/master/6-concat.py) to print `Welcome to Holberton School!`
* It is not allowed to use any loop or conditional statement.
* It is required to use the variables `str1` and `str2` in the new line of code.
* The program should be exactly 5 lines long.
* The desired outputs:
  * When  `./6-concat.py` is executed, the desired output should be:
    * `Welcome to Holberton School!`
  * When `wc -l 6-concat.py` is executed, the desired output should be:
    * `5 6-concat.py`

**Explanation:**
* The [solution](./6-concat.py) is straightforward by using concatenation and assignment.
* Breaking down the meaning of `wc -l 6-concat.py`.
  * The `wc` means `word count` which is a command used to count lines, words, and characters in files.
  * The `-l` flag specifies to count the number of lines.
* When these commands were executed, the desired output required were gotten.

### 7-edges.py
* The requirement of this task is to complete this [source code](https://github.com/alx-tools/0x00.py/blob/master/7-edges.py)
* It is not allowed to use any loops or conditional statements.
* The program should be exactly 8 lines long.
* `word_first_3` should contain the first 3 letters of the variable `word`
* `word_last_2` should contain the last 2 letters of the variable `word`
* `middle_word` should contain the value of the variable `word` without the first and last letters.
* Desired output when `./7-edges.py` is executed.
  * `First 3 letters: Hol`
  * `Last 2 letters: on`
  * `Middle word: olberto`
* When `wc -l 7-edges.py` is executed, the desired output should be:
  * `8 7-edges.py`

**Explanation:**
* This task is straight forward using the slicing method.
* Here is the [solution](./7-edges.py).
* By executing [7-edges.py](./7-edges.py), the desired output was produced.

### 8-concat_edges.py
* The requirement of this task is to complete the [source code](https://github.com/alx-tools/0x00.py/blob/master/8-concat_edges.py) to print `object-oriented programming with Python`, followed by a new line.
* It is not allowed to use any loops or conditional statements
* The program should be exactly 5 lines long.
* It is not allowed to create new variables.
* It is not allowed to use string literals.
* Desired output when `./8-concat_edges.py` is executed:
  * `object-oriented programming with Python`
* When `wc -l 8-concat_edges.py` is executed, the desired output should be:
  * `5 8-concat_edges.py`

**Explanation:**
* This project is simple and straight forward with slicing.
* By executing the [solution](./8-concat_edges.py), desired outputs were obtained.

### 9-easter_egg.py
* The requirement of this task is to write a Python script that prints "The Zen of Python", by TimPeters, followed by a new line.
* The script should be maximum 98 characters long and checked with `wc -m 9-easter_egg.py`.

**Explanation:**
* This task is simple and straightforward.
* The `this` module is a standard module in Python.
* `The Zen of Python` is a collection of aphorisms which provides a set of philosophical guidelines for writing computer programs in Python.
* By executing this [solution](./9-easter_egg.py), `The Zen of Python` is printed.

### 10-check_cycle.c
Below are the requirements of this project.

**Technical interview preparation:**

* It is not allowed to google anything
* Whiteboard first
* This task checks the efficiency of the solution, i.e. is the solution’s runtime fast enough, does it require extra memory usage / mallocs, etc.
Write a function in C that checks if a singly linked list has a cycle in it.

* Prototype: `int check_cycle(listint_t *list);`
* Return: `0` if there is no cycle, `1` if there is a cycle
Requirements:

* Only these functions are allowed: `write`, `printf`, `putchar`, `puts`, `malloc`, `free`

**Explanation:**
* This code implements `Floyd's Cycle-Finding Algorithm` popularly known as `Tortoise and Hare algorithm`. 
* The code uses two pointers moving at different speeds to detect if a cycle exists in a singly linked list.
* If a cycle is present, the hare will meet the turtle, otherwise the hare will reach the end of the list. 
* This is how the code works:
    * This function `int check_cycle(listint_t *list)` checks whether the linked list `list` has a cycle. 
    * The `list` parameter is a pointer to the head of a singly linked list type of type `listint_t`.
    * The `listint_t *turtle, *hare;`
        * The `turtle` moves through the list one node at a time.
        * The `hare` moves through the list two nodes at a time.

    ``` 
     if (list == NULL || list->next == NULL)
            return (0);
    ```

    * The above line checks if the list is `NULL(empty)` or if it contains one node (`list->next == NULL`).
    * If this condition is true, there cannot be any cycle, so return 0.

    ```
    turtle = list->next;
    hare = list->next->next;

    ```
    * This snippet initializes the pointers. 
    * `turtle` starts at the second node of the list (`list->next`).
    * `hare` starts at the third node of the list (`list->next->next`).

    ```
    while (turtle && hare && hare->next)
    {
        if (turtle == hare)
            return (1);

        turtle = turtle->next;
        hare = hare->next->next;
    }
    ```
    * **Condition:** The loop continues as long as `turtle`, `hare`, and `hare->next` are not NULL.
    * **Cycle Detection:** Inside the loop, the function checks whether turtle and hare are pointing to the same node. 
        * If they are, it indicates a cycle, and the function returns 1.
* Here is the full [solution](./10-check_cycle.c).


### 100-write.py
* This task requires that a Python script is written and print exactly `and that piece of art is useful - Dora Korpar, 2015-10-19`, followed by a new line.
* It is required to use the function `write` from the `sys` module.
* It is not allowed to use `print`.
* The script should print `stderr`.
* The script should exit with the status code `1`.

**Explanation:**
* The `sys` module was imported and the code written using the `write` function as [solution](./100-write.py)
* The status code was also demonstrated in the code. 


### 101-compile
* This task requires a script that compiles a Python script file.
* The Python file name is required to be stored in the environment variable $PYFILE
* The output filename is required to be `$PYFILEc` (ex: `export PYFILE=my_main.py` => output filename:`my_main.pyc`)
* The following commands were expected to be run the terminal:
  * `export PYFILE=main.py`
  * `./101-compile`
  * `cat main.pyc | zgrep -c "Best School"`
  * `od -t x1 main.pyc # SYSTEM DEPENDANT => CAN BE DIFFERENT`

**Explanation:**
* The `import` module was used to import `py_compile` which is a standard Python library used to compile Python source files into a bytecode. 
* Here is the [solution.](./101-compile)


### 102-magic_calculation.py
* In this task, it is required to write the Python function `def magic_calculation(a, b):` that does exactly the same as represented by a bytecode in the task. 

```
  3           0 LOAD_CONST               1 (98)
              3 LOAD_FAST                0 (a)
              6 LOAD_FAST                1 (b)
              9 BINARY_POWER
             10 BINARY_ADD
             11 RETURN_VALUE
```
* Tip: [Python bytecode](https://docs.python.org/3.4/library/dis.html)

