import time

def exV2(word):
    b = 0
    for i in word:
        if i == " ":
            pass
        else:
            a = ord(i)
            b += a
    return b
word = "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"
start = time.time()
print('answerV2: ', exV2(word))
print('timeV3: ', (time.time()-start)*1000)

