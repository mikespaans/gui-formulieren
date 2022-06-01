# def test(maf):
#     if maf.isdigit():
#         print ("test")
#         return True
    
#     print ("geen nummer toegevoegd")
#     return False

# print (test(str(4)))


# def TestFunctie(niks = False):
#     if niks == True:
#         return True
#     else:
#         return False

# maf = TestFunctie("n")

# if maf == False:
#     print ("weerkt")

# def test():
#     return 

# # maf = test()
# # maffer = str(maf)
# # print (type(maffer))
# # print (test())



# import tkinter
# from tkinter.font import Font

# root = tkinter.Tk()

# font_1 = Font(family='Arial', 
#               size=24, 
#               weight='normal', 
#               slant='italic', 
#               underline=1, 
#               overstrike=1)

# font_2 = Font(family='Helvetica',
#               size=12,
#               weight='bold',
#               slant='italic',
#               underline=0,
#               overstrike=0)

# font_3 = Font(family='Courier', size=14, weight='normal', slant='roman', underline=0, overstrike=0)
# font_4 = Font(family='Times', size=22, weight='bold', slant='roman', underline=0, overstrike=0)

# my_label = tkinter.Label(master=root, text='Text', font=font_1)
# my_label.pack()

# tkinter.mainloop()


import random
maf = " "


for i in range(10):
    RandomCijfer = random.randint(0,9)
    
    maf += str(RandomCijfer)


# maf 
print (maf)