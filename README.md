# SOG-PLUS
Improved version of .SOGCL, my first ever programming language, my hope is that this language is turing-complete, we're getting there!

# Documentation
There's alot to go over, let us commence.
## Variables
In SOG+, there are no variable types, everything is a string, int's are to be added in version soon to come, as for booleans, they will be ignored, as they are not necessary, just use 1 as true and 0 as false.

To create a variable, you can use the ```var()``` function, inbetween the brackets ```()``` goes the variable's name and value, eg:
```
var(i=1)
```
You can change a variable at any time by changing the value the same as seen inbetween the brackets ```()```

````
i=2
````
## Functions
In SOG+, functions are defined with the ```func[] () {}``` command, inbetween the brackets ```[]``` goes the function name, inbetween the paranthesis ```()``` goes any parameters (v1.0.0 has not implemented this, you can use vars for that) and inbetween the curly brackets ```{}``` goes the code that the function will execute, when put together, this is the result:
```
func[hello_world] () {print("Hello, World!")}
``` 

You can call the function by using its name.

```
func(hello_world) () {print("Hello, World!")}
hello_world
Hello, World!
```
## Running
You can run your code from the terminal if you want, if not, you can create a txt file (preferably .SOGP) and use the ```sog+()``` command to run it, heres an example:

__Content of "HELLO_WORLD.SOGP":__
```
var(i=Hello, World!)
print(i)
```
__Inside Terminal:__
```
sog+(HELLO_WORLD.SOGP)
Hello, World!
```
## Logical Statements
In SOG+, if statements are supported, however, elif and else statements aren't, this will change with more updates.
To execute an if statement, you use the following command: ```if() {}```, inside the brackets ```()``` goes the question, for example: ```i==1```, this is limited to only ==, this will change with more updates.
inside the curly brackets ```{}``` goes the code that will be executed if the question is true, eg:
```
var(i=1)
if(i==1) {print("i is equal to 1")}
i is equal to 1
```

## Imports
For now, you can only import the easter egg "THIS"

All future imports will also case sensitive, with them being in all caps.

```
import(THIS)
```
Do it yourself to see the result ;)

## Notable built in functions:
```
print("Hello, World!")
pause(2)
```

## Final Notes:
I'm really proud how this project is going, and happy coding.
