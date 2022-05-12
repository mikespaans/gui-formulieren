special_chars = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+",]

def count_special(x):
    Teller = 0
    for i in special_chars:
        for f in x:
            print (f)
            if i == x:
                Teller += 1
    return Teller


print(count_special("asdqwe!@#431d12@!dsg$"))