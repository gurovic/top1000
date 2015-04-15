text = open("text.txt").read().split()
i = 0
while text[i] != text[-1]:
            if text[i] in open("lib.txt").read().split():
                        del(text[i])
            else:
                        i += 1
print(" ".join(text))