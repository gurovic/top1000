import re
import collections

def inputer(inputed):
    text = list(set(inputed.lower().split()))
    return text

def finder(templ, text):
    allwords = []
    for key in text:
        if re.match(templ, key) != None: 
            allwords += re.findall(templ, key) 
    return allwords

def sorter(allwords):
    collector = collections.Counter()
    for word in allwords:
        collector[word] += 1
    for i in range(len(collector)):
        collector[i] = collector[i][0]
    return collector

def outputer(text, lib):
    return "\n".join(sorter(list(set(finder(re.compile('[a-zA-Z]+'), text)) - lib)))

print(outputer(inputer(input()), set(open("lib.txt").read().lower().split())))