text = list(map(str, open("text.txt").read().split()))

for i in range(len(text)):
            if text[i] in list(map(str, open("lib.txt").read().split())):
                        text[i] = None
print(text)