Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = [6,'ICT',2.5,True,('AL',2018),[-1.2,'python']]
>>> s[::-1]
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    s[::-1]
NameError: name 's' is not defined
>>> a[::-1]
[[-1.2, 'python'], ('AL', 2018), True, 2.5, 'ICT', 6]
>>> a[:5:2]
[6, 2.5, ('AL', 2018)]
>>> a[1:5:2]
['ICT', True]
>>> a[5:1:-2]
[[-1.2, 'python'], True]
>>> a[1::-1]
['ICT', 6]
>>> a[1:-4:-1]
[]
>>> a[1:0:-1]
['ICT']
>>> a[-2::-2]
[('AL', 2018), 2.5, 6]
>>> a[-2:-4:-2]
[('AL', 2018)]
>>> a[1:7:2]
['ICT', True, [-1.2, 'python']]
>>> a[0:1:2]
[6]
>>> word = 'Shehan Ravindra'
>>> word[0]
'S'
>>> word[6]
' '
>>> word[-1]
'a'
>>> word[0:2]
'Sh'
>>> word[2:5]
'eha'
>>> word[:2]
'Sh'
>>> word[:2] + word[2:]
'Shehan Ravindra'
>>> word[:2] + word[5:]
'Shn Ravindra'
>>> word[:4] + word[4:]
'Shehan Ravindra'
>>> word[::-1]
'ardnivaR nahehS'
>>> a = "python"
>>> [x for x in a]
['p', 'y', 't', 'h', 'o', 'n']
>>> S = {'Index':'0001','Name':'Shehan'}
>>> [x for x in S]
['Index', 'Name']
>>> a = ['ICT','AL','Exam']
>>> A = [et '!!' for e in a]
SyntaxError: invalid syntax
>>> a = ['ICT','AL','Exam']A = [et '!!' for e in a]
SyntaxError: invalid syntax
>>> a = ['ICT','AL','Exam']A = [et '!!' for e in a]a = ['ICT','AL','Exam']
SyntaxError: invalid syntax
>>> 
>>> 
>>> 
>>> 
>>> 
>>> a = ['ICT','AL','Exam']
>>> A = [e+ '!!' for e in a]
>>> B = [len(x) for x in a]
>>> print(B)
[3, 2, 4]
>>> print(A)
['ICT!!', 'AL!!', 'Exam!!']
>>> 
