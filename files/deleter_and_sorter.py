text = set(open("text.txt").read().split())
libriary = set(open("lib.txt").read().split())
print(" ".join(text - libriary))