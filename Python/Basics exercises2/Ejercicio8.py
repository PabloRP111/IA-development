def is_pal(string):
    new_str = ""
    for i in range(len(string)):
        if string[i] != ' ':
            new_str = new_str + string[i]
    half =int(len(new_str) / 2)
    for i in range(half):
        if(new_str[i] != new_str[- (i + 1)]):
            return (False)
    return (True)

string = input("Dime una frase palindroma \n")
print("Es un palindromo? ", is_pal(string))