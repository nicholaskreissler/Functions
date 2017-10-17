import time
#Homework assignments
#Loops through an infinite exponential growth visualizer
#Takes a string and returns it backwards
#Takes a
def exponentiallgrowthbyone(product,exponent):
    x = product
    n = exponent
    while(True):

        x=x+1
        n=n+1
        print(str(x**n) + "\n")
def reverse_string(x):
    newlist = list(x)
    newlist.reverse()
    z =''
    for letter in newlist:
        z = z + letter
    print(z)
def pay(wage, hour):
    if hour <= 40:
        print(hour * wage)
    else:
        print(((hour-40)*(wage*1.5))+(40*wage))
def returnGreater(list, integer):
    "list:list,integer:int; return list"
    x = []
    for i in list:
        if i > integer:
            x = x + [i]
    print(x)
def pay(wage, hours):
        "wage:int, hours:int; return:int or float"
        if hours > 60:
            x = ((hours - 60)*(wage * 2)) + ((20)*(wage * 1.5)) + (40 * wage)
        elif hours > 40 and hours < 60:
            x = ((hours - 40)*(wage * 1.5)) + (wage * 40)
        else:
            x = (wage * hours)

        print(x)
def statement(list): #returns sum of positive and negative numbers
    "list:list, x:int, y:int; return:list"
    x = 0
    y = 0
    for i in list:
        if i > 0:
            x = x + i
        else:
            y = y + i
    print([x, y])
def Abbreviation(day): #Abbreviates week days
    "day:string; return:string"
    f = ""
    for i in day[0:2]:
        f = f + i
    print(f)
def LastF(first, last): #Returns last name and first letter of first name
    "first:string, last:string; rerturn:string"
    x = last + ', ' + first[0] + "."
    print(x)
def sum_of_squares(xs):
    'xs:list(float), return:float'
    x = 0
    for element in xs:
        x = x + (element*element)
    return x
def countOdd(xs):
    "l:list(float),return:float"
    x = 0
    for i in xs:
        if i % 2 != 0:
            x = x + 1
    return x
def sumEven(xs):
    "xs:list(int),return:int"
    x = 0
    y = 0
    for i in xs:
        if i % 2 == 0:
            x = x + i
        else:
            y = y + i
    return x
def sumNegative(xs):
    "xs:list(int),return(int)"
    y = 0
    for i in xs:
        if i < 0:
            y = y + i
    return y
def sumUptoEven(xs):
    "xs:list(int), return:int"
    x = 0
    for element in xs:
        if element % 2 == 0:
            break
        else:
            x = x + element
    return x
def countUptoIncl(xs):
    "xs:list(str),return:int"
    x = 0
    for elements in xs:
        x = x +1
        for element in elements:
            if element in "sam":
                break
        else:
            continue
        break
    return x
def countUptoIncl1(xs):
    "xs:list(str),return:int"
    x = 0
    for element in xs:

        if element == "sam":
            x = x+1
            break
        else:
            x = x+1
    return x
def vowel_indices(string):
    'string:string, return:list'
    list = []
    for index in range(len(string)):
       if string[index] in 'aeiouAEIOU':
            list = list + [index]
    return list
def returnNth(list, n):
    'list:list, n:int, return:list'
    list
    l = []
    g = 0
    while(True):
        l = l + [list[g]]
        g = g + n
        if len(list) <= g:
            break
    return l
def findsubstr(substring):
    'substring:list, return:list'
    list =[]
    for index in range(len(substring)):
        if index > 0:
            if substring[index] in substring[index - 1]:
                list = list + [substring[index]]
    return list
def n_letter(list,n):
    'list:list, n:int, return:list'
    res =[]
    for item in list:
        if len(item) == n:
            res = res +[item]
    return res
def finddigits(string):
    'string:string, return:list'
    list = []
    for character in string:
       if character in '1234567890':
            z = int(character)
            list = list + [z]
    return list
def countevens(list):
    'list:list(int), return:int'
    x = 0
    for lists in list:
        for items in lists:
            if items % 2 == 0:
                x = x + 1
    return x
def findminrow(list):
    'list:list(lists), var:integer, variable1:integer, variable2:integer, return:integer'
    if list == []:
        return -1
    list2 = []
    for index in range(len(list)):
        x = 0
        for items in list[index]:
            x = x + items
        list2 = list2 + [x]
    var = list2[0]
    variable1 = -1
    variable2 = -1
    for index in range(len(list2)):
        variable2 = variable2 + 1
        if list2[index] < var:
            var = list2[index]
            variable1 = variable2
    return variable1
def findmaxdif(list):
    'list:list(list), variable1:integer, variable1:integer, variable3:integer, return:integer,integer'
    listofdifferences = []
    for index in range(len(list)):
        listofdifferences = listofdifferences + [((max(list[index]))- (min(list[index])))]
    variable1 = -1
    variable2 = -1
    variable3 = listofdifferences[0]
    for index1 in range(len(listofdifferences)):
        variable1 = variable1 + 1
        if listofdifferences[index1] > variable3:
            variable3 = listofdifferences[index1]
            variable2 = variable1

    return (variable3,variable2)
def replace(string, old, new):
    'string:string, old:string, new:string, return:string'
    newstring = ""
    for letters in string:

        if letters == old:
            newstring = newstring + new
        else:
            newstring = newstring + letters

    return newstring
def subsetsum(list, int):
    'list:list, int:integer, return:boolean'
    res = False
    for index in range(len(list)-2):
        for item in range(index+1, len(list)):
            for char in range(item+1, len(list)):
                if list[index]+list[item]+list[char] == int:
                    res = True
                    break
        if res == True:
            break
    #if res == True:
       # break
    return res

#notes
def contains3(l,x):
    found = False
    i = 0
    while(not found) and (i < len(l)):
        if l[i] == x: # Index error if i < len(l) index ou of range error
            found == True
        i = i + 1
    return found
    #use a while loop when you don't know how many times you have to run something
def merge(l1,l2):
    'l1:list(str), l2:list(str), return:list(str)'
    i = 0
    j = 0
    list = []
    while(True):
        if l1[i] < l2[j]:
            list = list + [l1[i]]
            i = i + 1
        else:
            list = list + [l2[j]]
            j = j+ 1
        if (j)+ (i) == len(l1) + len(l2):
            break
    print(list)
merge([1,4,7,9],[2,5,8])

