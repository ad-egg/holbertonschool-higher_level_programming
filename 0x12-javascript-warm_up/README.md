# holbertonschool-higher_level_programming
## 0x12-javascript-warm_up
### 0-javascript_is_amazing.js
This Javascript script prints "Javascript is amazing!"
### 1-multi_languages.js
This script prints 3 lines.
### 2-arguments.js
This script prints a message depending on how many arguments are passed to it.
### 3-value_argument.js
This script prints the first argument passed to it.
### 4-concat.js
This script prints two arguments passed to it.
### 5-to_integer.js
This script prints a specific string if the argument passed to it can be converted to an integer.
### 6-multi_languages_loop.js
This script prints 3 lines using an array of strings and a loop.
### 7-multi_c.js
This script prints x times a string.
### 8-square.js
This script prints a square.
### 9-add.js
This script prints the addition of 2 integers.
### 10-factorial.js
This script computes and prints a factorial.
### 11-second_biggest.js
This script prints the second biggest integer in a list of arguments.
### 12-object.js
This script replaces a value.
### 13-add.js
This script returns the addition of 2 integers.
### 100-let_me_const.js
This script modifies the value of `myVar` to `333`.
```
$ cat 100-main.js
#!/usr/bin/node
myVar = 89;
require('./100-let_me_const')
console.log(myVar);
$ ./100-let_me_const.js
333
```
### 101-call_me_moby.js
This function executes x times a function.
### 102-add_me_maybe.js
This function increments and calls a function.
### 103-object_fct.js
This file is updated by adding a new function `incr` that increments the integer `value`.
```
$ cat 103-object_fct.js
#!/usr/bin/node
let myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
/*
YOUR CODE HERE
*/
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
```
