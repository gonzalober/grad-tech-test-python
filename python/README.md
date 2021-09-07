# Grad Tech Test - Python

## Medals Challenge ![Image](assets/image.png)

In the file [medals.py](medals.py), there's a function for creating a medal table. Update this function to be able to process the sample input.

## Available Scripts

### Setup

Install `python3` and matching `pip` on your system, use pip to install `pytest`.

### Scripts

Run all unit tests run `pytest`
Run the test within the medals.py file using `pytest medals.py`

## Clone this repository

Use `git clone` to clone the repository locally, then change the remote, please do not fork this repository. To change the remote, use

```bash
git remote set-url origin <path-to-your-blank-repository>
git push -u origin <branch-name>
```

## Problem solving process

```
- Understand and identify input/output of `create_medal_table` function.
- Implementation:
    - Iterate over the array.
    - Get the podium "key".
    - For each of the elements that are in the podium split them between position and country.
    - Asign points depending on the position of the country.
- Design the tests which checks create_medal_table() returns a {"country": points} object.
- Refactoring the code.
```

Note: I would also like to add that I changed some variables and functions naming to snake_case due to python conventions ([HERE](https://www.python.org/dev/peps/pep-0008/#function-and-variable-names)).
