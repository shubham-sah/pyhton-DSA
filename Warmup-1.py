def sleep_in(weekday, vacation):
    if (weekday == True and vacation==False):
        return False
    else:
        return True
    

def diff21(n):
    diff = abs(n-21)
    if(n > 21):
        return 2*diff
    else:
        return diff
    

def near_hundred(n):
    if abs(100 - n) <= 10:
        return True
    elif abs(200 -n) <= 10:
        return True
    else:
        return False
    

def missing_char(str, n):
    str1 = str[0:n]
    str2 = str[n+1:len(str)]
    return str1+str2



def monkey_trouble(a_smile, b_smile):
    if (a_smile == True and b_smile == True) or (a_smile == False and b_smile == False):
        return True
    else:
        return False
    

def parrot_trouble(talking, hour):
    if(talking) and (hour < 7 or hour > 20):
        return True
    else:
        return False



def pos_neg(a, b, negative):
    if(negative):
        if(a<0 and b<0):
            return True
        else:
            return False
    elif((a < 0 and b< 0) or (a>0 and b > 0)):
        return False
    else:
        return True 


def front_back(str):
    if len(str) < 2:
        return str
    return str[-1] + str + str[0]





def sum_double(a, b):
    if(a==b):
        return 2*(a+b)
    else:
        return a+b
    


def makes10(a, b):
  if(a + b == 10):
    return True
  elif(a == 10 or b == 10):
    return True
  else:
    return False


def not_string(str):
  if(str[0:3] == "not"):
    return str
  else:
    return "not "+ str



def front3(str):
    if(len(str) < 3):
        return str+str+str
    else:
        str = str[0:3]
        return str+str+str  



print("shubham")



#learn about string and substring in python
#learn about in built math operations in python
#learn about conditionals in python

