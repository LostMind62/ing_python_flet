from sumar import fun_sumar, fun_restar

a = "1" #string
b = 2 #int
c = ["a","b","c","d","a","b","c","d","a","b","c","d","a","b","c","d","a","b","c","d","a","b","c","d","a","b","c","d","a","b","c","d","a","b","c","d","a","b","c","d"] # listas
d = {1 :"a",2:"b",3:"c"} #dict
e = () #tuple
g = c #permutacion

h = len(c)

print()
print("*" * 10 )

#for f in c:
#    print(dict({f: i}))

#print("*" * 10 )

#if a == "2":
#    print(a)
#elif b > 4:
#    print(b)
#else:
#    print(e)

#print("*" * 10 )


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    a = fun_sumar(2,5)
    b = fun_restar(3,5)
    print(a)
    print(b)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
