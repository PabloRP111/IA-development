def isPal(string):
    new_str = ""
    string = string.lower()
    for i in range(len(string)):
        if string[i] != ' ':
            new_str = new_str + string[i]
    half =int(len(new_str) / 2)
    for i in range(half):
        if(new_str[i] != new_str[- (i + 1)]):
            return (False)
    return (True)

#Otra manera
def isPal2(string):
    string = string.replace(" ", "").lower()
    return (string == string[::-1])

string = input("Dime una frase palindroma \n")
print("Es un palindromo? ", isPal(string))
print("Es un palindromo? ", isPal2(string))