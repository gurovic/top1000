import re

def inputer(filename): 
    text = list(set(open(str(filename) + ".txt").read().lower().split())) 
    return text 


def librarian(filename): 
    libriary = set(open(str(filename) + ".txt").read().split()) 
    return libriary 


def finder(templ, text): 
    allwords = [] 
    for key in text: 
        if re.fullmatch(templ, key) != None: 
            allwords += re.findall(templ, key) 
    return allwords 


def sorter(words):
    a = []
    b = []
    for i in words:
        a += [[int(open("text" + ".txt").read().lower().split().count(i)), str(i)]]
    a = sorted(a)
    for i in a:
        b += [i[1]]
        
    return reversed(b)

              
def printer(text, lib): 
    print("\n".join(sorter(list(set(finder(re.compile('[a-zA-Z]+'), inputer(text))) - librarian(lib))))) 

printer("text", "lib")