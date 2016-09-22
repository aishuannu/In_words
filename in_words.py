a = {"1":"one", "2":"two" , "3":"three", "4":"four", "5":"five", "6":"six", "7":"seven", "8":"eight", "9":"nine", "0":""}
b = {"11":"eleven", "12":"twelve" , "13":"thirteen", "14":"fourteen", "15":"fifteen", "16":"sixteen", "17":"seventeen", "18":"eighteen", "19":"nineteen"}
c = {"00":"", "10":"ten", "20":"twenty" , "30":"thirty", "40":"forty", "50":"fifty", "60":"sixty", "70":"seventy", "80":"eighty", "90":"ninety"}


def first_nonzero_entry(a):
    i = 0
    while i < len(a):
        if a[i] != "0":
            return i
            break
        i += 1    


def f(x):
    d = first_nonzero_entry(x)
    if d == 2 or d == None:
        y = a[x[2]]
    elif d == 1:
        if x[1: ] in b:
            y = b[x[1: ]]
        else:
            y = c[x[1] + "0"] + " " + a[x[2]]
    else:
        if x[1: ] in b:
            y = a[x[0]] + " " + "hundred" + " " + b[x[1: ]]
        else:
            y = a[x[0]] + " " + "hundred" + " " + c[x[1] + "0"] + " " + a[x[2]]
    return y  



def in_words(x):
    i = 0
    j = 0
    e = ""
    y = ""
    while i <= 8 - len(x):
        e = e + "0"
        i += 1
    x = e + x
    p = [" million ", "", "", " thousand ", "", "", ""]
    while j <= 6 :
        if f(x[j:j+3]) != "":
            y = y + f(x[j:j+3]) + p[j] 
        j += 3
    if y == "":
        y = "zero"
    return y

x = raw_input("Enter a number : ")
print in_words(x)

    






