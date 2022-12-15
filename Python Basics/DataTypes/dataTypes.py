Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

num = 10
>>> 
>>> type(num)
<class 'int'>
>>> 
>>> string = num + " Digits"
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    string = num + " Digits"
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 
>>> num + 20
30
>>> 
>>> string = "Hello " + "World"
>>> 
>>> string
'Hello World'
>>> 
>>> type(string)
<class 'str'>
>>> 
>>> string.lower()
'hello world'
>>> 
>>> float_num = 2.5
>>> 
>>> type(float_num)
<class 'float'>
>>> 
>>> int(float_num)
2
>>> 
>>> boolean = True
>>> 
>>> if(boolean):
...     print(boolean)
... 
...     
True
