text = list(map(str, open("input").read().split()))
def sort_text(text):
    for i in text:
        if i in open("lib"):
            text[i] = "None"
leng = len(text)