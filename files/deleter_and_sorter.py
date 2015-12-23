import re

def inputer(filename): 
    text = list(set(filename.lower().split())) 
    return text 


def librarian(filename, level): 
    libriary = set(open(str(filename) + ".rtf").read().split()[:level-1]) 
    return libriary 


def finder(templ, text): 
    allwords = [] 
    for key in text: 
        if re.fullmatch(templ, key) != None: 
            allwords += re.findall(templ, key) 
    return allwords 


def sorter(words):
    adjacent = []
    output = []
    temporary = []
    
    for i in words:
        adjacent += [[int(open("text" + ".txt").read().lower().split().count(i)), str(i)]]
        
    adjacent = sorted(adjacent)
    
    for i in adjacent:
        output += [i[1]]
        
    for i in range(len(output)):
        if re.search('es$', output[i]) or re.search('ed$', output[i]) or re.search("'s$", output[i]) or re.search("'m$", output[i]):
            tmp = str(output[i])[:-2]
            if tmp in librarian("lib") or tmp in output:
                temporary += [output[i]]
        elif  re.search('ing$', output[i]):
            tmp = str(output[i])[:-3]
            if tmp in librarian("lib") or tmp in output:
                temporary += [output[i]]
        
                
    for i in range(len(temporary)):
        try:
            output.remove(str(temporary[i]))
        except builtins.ValueError:
            pass
        
    return reversed(output)

              
def distinguish(text, lib, level): 
    print("\n".join(sorter(list(set(finder(re.compile('[a-zA-Z]+'), inputer(text))) - librarian(lib, level)))))

distinguish(input(), "lib", int(input()))