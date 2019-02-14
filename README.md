# NamedAssignments
NamedAssignments is a library that I developed for myself to use named assignments in my Python <= 3.7 projects.

## What is named assignments?
Actual thing I don't even know how should I call them but this is the best name I found for them. If you've read [PEP 572](https://www.python.org/dev/peps/pep-0572/) there is a new operator coming in Python 3.8 called as ***Named Expressions*** (this is how it is going to look like in your code `:=`) which helps you to write more clean and shorter code.

## But how?
For original examples you can check [PEP 572 examples](https://www.python.org/dev/peps/pep-0572/#examples) directly but if you are looking this library you are probably not using Python 3.8 so just stay in here and continue reading.


* Caching computationally expensive computations (This is definitely a bad example of expensive computation but lets just act like it is)
  ###### Old way:

  ```python
  # Makes two addition every time
  strange_list = [[x + 1, x/(x + 1)] for x in range(5)]
  ```
  ###### Improved:

  ```python
  # Makes only one addition every time
  strange_list = [[N('y', lambda: x + 1), x/N.y] for x in range(5)]
  ```

* Usage in while loops
  ###### Old way:

  ```python
  # conn is a accepted socket connection
  while True:
      data = conn.recv(1024)
      if not data:
          break
      conn.sendall(data)
  ```
  ###### Improved:

  ```python
  # conn is a accepted socket connection
  while N('data', conn.recv, 1024):
      conn.sendall(N.data)
  ```

## Usage
Usage is not clean as original due to limitations but it is the cleanest way I found.
```python
from namedassignments import NamedAssignments as N

N(variable_name, function, *args, **kwargs)
```

## Installation
Library is avaible on PyPi so just run
```
pip install namedassignments
```

## API
Since the whole code is only 5 lines there is nothing too much. Library uses Python's magic method `__new__` to return what function returns this is all library does on the background.
* `__new__` Arguments:
  * `variable_name`: Variable name you want to use while retrieving data. (String) (Required)
  * `function`: Function you want to execute. (Function) (Required)
  * `*args`: Arguments you want to pass function. (List) (Optional)
  * `**kwargs`: Keyword arguments you want to pass function. (Dict) (Optional)
