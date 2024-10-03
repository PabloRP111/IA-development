def is_pal(string):
    half =int(len(string) / 2)
    for i in range(half):
        if(string[i] != string[- (i + 1)]):
            return (False)
    return (True)

string = input("Dime un palindromo \n")
print("Es un palindromo? ", is_pal(string))