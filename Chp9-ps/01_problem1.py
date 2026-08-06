f = open("poem.txt")
content = f.read()
if("twinkle" in content):
    print("The word twinkal is present in the content")
else:
    print("The word twinkal is not present in the content")

f.close()