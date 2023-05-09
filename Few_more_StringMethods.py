"""
Syntex: startswith(sep) and endswith(sep)
Return True if string starts/ends with the prefix/suffix, otherwise return False
"""

s = 'Patrick'.startswith('Pat')  # case sensitive!
s = 'Patrick'.endswith('k')  # case sensitive!
print()


"""
Syntes: partition(sep) and rpartion(sep)
Returns a tuple where the string is parted into three parts
Split the string at the first occurrence of sep, and return a 3-tuple containing the part before the separator, the separator itself, and the part after the separator. 
If the separator is not found, return a 3-tuple containing the string itself, followed by two empty strings """

str = "Hello-Python"
print(str.partition("-"))
print(str.partition("."))
print()
s = 'Python is awesome!'
parts = s.partition('is') # ('Python ', 'is', ' awesome!')
print(parts)
parts = s.partition('was') # ('Python is awesome!', '', '')
print(parts)
print(str.rpartition("-"))
print(str.rpartition("."))
mystr = "Hello Python"
print(mystr.rpartition("."))



"""
Sytenx: split()or split(sep=None, maxsplit=-1)
Return a list of the words in the string, using sep as the delimiter string. If maxsplit is given, at most maxsplit splits are done.
"""
print()
s = 'string methods in python'.split() #['string', 'methods', 'in', 'python']
print(s)
s = 'string methods in python'.split(' ', maxsplit=1)  # ['string', 'methods in python']
print(s)
mystr2="Hello,,Python"
print(mystr2.split(","))
print()

"""
rsplit()
Return a list of the words in the string, using sep as the delimiter string. If maxsplit is given, at most maxsplit splits are done, the rightmost ones.
"""
s = 'string methods in python'.rsplit() # ['string', 'methods', 'in', 'python']
s = 'string methods in python'.rsplit(' ', maxsplit=1) # ['string methods in', 'python']
print()


"""
replace(old, new[,count]) : Return a copy of the string with all occurrences of substring old replaced by new.
##Returns a string where a specified value is replaced with a specified value """

mystr = "Hello Python.Hello Java. Hello C++."
print(mystr.replace("Hello","Bye")) #Bye Python. Bye Java. Bye C++.
print(mystr.replace("Hello","Hell", 2)) #Hell Python. Hell Java.Hello C++.

s = ' \n \t hello\n'.replace('\n', '')
print(s) # '  \t hello'

#######title() : Converts the first character of each word to upper case

mystr = "Hello PYthon"
print(mystr.title())
mystr1 = "HELLO KUSA!, how are you doing, @#$%&"
print(mystr1.title())
