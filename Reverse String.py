def stringReverse(string):
    reverse=''
    for i in string:
        reverse=i+reverse
    return reverse
print(stringReverse(input()))