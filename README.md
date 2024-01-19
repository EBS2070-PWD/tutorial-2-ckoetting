# EBS2070 - Python and Web Design - Tutorial 2

# General Python Programming Exercises

## General information

This set of exercises is to solved individually or in a group, before
the tutorial. The subjects of the exercises are meant to help you gain
proficiency in programming with Python.

You are strongly encouraged to [prepare the material]{.underline}
individually or in study groups, in the form of slides or other forms
that can be used to discuss your results with your colleagues.

Research subjects (e.g. list comprehension) but try to not search for
the solution of the exercises. If you use any code from the internet,
please acknowledge it correctly and pay attention to the license.

The tutorial will start with a pre-discussion of which material and
exercises are discussed. If you have any questions about exercises that
were not discussed in the tutorial, please use the discussion board.

The goal of this tutorial is to discuss problems and solutions
encountered while solving the preparation material and the exercises,
but also any tips and tricks or additional resources on Python
programming. You are encouraged to first discuss the issues with your
colleagues (via discussion board) and then with the tutor.

### Suggested material

-   [TDD with
    Python](https://rubikscode.net/2021/05/24/test-driven-development-tdd-with-python/)

-   [Chapter 1-5 of Sweigart, Al. Automate the boring stuff with
    Python](https://automatetheboringstuff.com/)

### Tools

-   Python 3.6+ [Download and install Python
    vanilla](https://www.python.org/downloads/)

-   PyCharm [Download and install
    PyCharm](https://www.jetbrains.com/pycharm/)

-   [pytest](https://docs.pytest.org/en/latest/)

### Concepts in exercises

-   Test-Driven-Development

-   Unit-tests

-   Separation of concerns

-   Exceptions

-   Pythonic programming

## Exercises

### Concepts in programming


1.  Research how Python handles and catches exceptions, and exception
    propagation.

2.  Research the difference between "Easier to ask for forgiveness than
    permission" and "Look before you leap" and when in idiomatic python
    you should use `try` and `if` for flow control.

3.  Research examples of pythonic code.

### Development and programming in Python


#### Example

-   Write a program that asks the user for the names of two football
    teams, and the score of one team followed by the score of the other
    team. Your program should output how many points each team gets (3
    for a win,1 for a draw, 0 if they lose). Write down unit tests, make
    use of functions and use the concept of separation of concerns.

Solutions: files [tests/test_football_exercise.py](./tests/test_football_exercise.py) and [football_exercise.py](football_exercise.py).

#### Exercises

For all exercises, use unit tests (using `pytest`) make use of
functions, and separation of concerns. You are encouraged to use GitHub,
but it's not mandatory for this session. If you do, make one commit per
test, and another for the code that passes that test. Make a push every
time you stop working. Use the pythonic way of coding and follow the
[PEP8 naming conventions](https://www.python.org/dev/peps/pep-0008/).

1.  Research the differences and applications of lists, tuples, set and
    dictionaries

2.  Write a program that asks the users how old they are and returns an
    answer indicating if the users are old enough to vote and how many
    years are there until they can retire (assume at age 65).

3.  Write a program for an extension of the program from the previous
    question to include the possibility to indicate also the amount of
    years to the age of pre-retirement (assumed at 60), and if already
    illegible to display the percentage of full retirement (assumed at
    60% at 60 and growing linearly with each year).

4.  Write a program for an extension of the program from the previous
    question to include the possibility to indicate also if they are
    legal drinking age.

5.  Sorting is an algorithm that you can use to sort items in a list of
    strings or list of numbers. It can be expressed in pseudo-code as:

    ``` {frame="single" fontsize="\\small"}
    Set n to number of records to be sorted
    REPEAT
    flag = False;
    FOR counter = 1 to n-1 DO
        IF key[counter] > key[counter+1] THEN
            swap the records;
            set flag = True;
        END IF
    END FOR
    n = n-1;
    until flag = False or n=1
    ```

    Write a program to implement this pseudo code. Unit tests are provided in file [tests/test_exercise5.py](./tests/test_exercise5.py)

6.  Write a program which will find all numbers which are divisible by 7
    but are not a multiple of 5, between 2000 and 3200 (both included).

7.  Using a list comprehension, create a new list called "newlist" out
    of the list "numbers", which contains only the positive numbers from
    the list, as integers.

8.  With a given integer number $n$, write a program to generate a
    dictionary that contains ($i$, $i*i$) such that is an integral
    number between 1 and $n$ (both included) and then the program should
    print the dictionary. An example of a unit test is: If 8 is
    provided, the output should be:
    ` {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64} `

9.  Write a program that given a list, will print out each value and the
    position they are in (starting in 1). Example,
    `first_letters = [’a’, ’b’, ’c’, ’d’]` should output
    `a, 1 \n b, 2 \n c, 3 \n d, 4`. Note that \\n is just an indication
    of new line to save space in this question, your solution should
    output each pair in different lines.

10. Write a program that given 3 lists with the same number of elements,
    it returns a new list of tuples with the elements of the original
    list aligned. Example:
    `numbers = [1, 2, 3, 4], first_letters = [’a’, ’b’, ’c’, ’d’], end_letters = [’z’, ’y’, ’x’, ’w’]`
    returns
    `[(1, ’a’, ’z’), (2, ’b’, ’y’), (3, ’c’, ’x’), (4, ’d’, ’w’)]`.
    *Hint:* use `zip`

11. Write a Python program to count the number of strings where the
    string length is 2 or more and the first and last character are same
    from a given list of strings. Example: for a sample List:
    `[‘abc’, ‘xyz’, ‘aba’, ‘1221’]` the result should be 2.
