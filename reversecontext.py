#Program to reverse the content of a string
a="Javascript"
a=a[::-1]
print(a)

#program to reverse order of words in a string
a="Javascript is fun"
a=a.split()
a=a[::-1]
a=" ".join(a)
print(a)