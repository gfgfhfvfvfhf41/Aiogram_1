# #from vlc import dll
# #import clr
# from ctypes import *
# lib = cdll.LoadLibrary(r"D:\Sharaga_bot\Build\Debug\STLib.dll")
# #from Build.Debug import STLib.dll
# #clr.AddReference("")
# #from ST
# lib.Main.Init("D:\Sharaga_bot\CMPHandler\model.json")
# #STLib.Main.Init("D:\Sharaga_bot\CMPHandler\model.json")
# print(lib.Main.GetAnswer("Сколько стоит обучение?"))
# #print(STLib.Main.GetAnswer("Сколько стоит обучение?"))
import os


# import clr
# clr.AddReference("D:\Build\Debug\STLib.dll")
# from STLib import Main


# pathDLL = os.getcwd() + "D:\Build\Debug\STLib.dll"
# clr.AddReference(pathDLL)
# import STLib.dll\


# from CMPHandler import STLib
#
# STLib.Init("D:\Build\Debug\identifier.sqlite")
# #
import string
a = "цена учиться?"
a = a.translate(str.maketrans({char: " " for char in string.punctuation})).lower().split()
print(a)
import clr
clr.AddReference("D:\Build\Debug\STLib.dll")
from STLib import Main
Main.Init("D:\Sharaga_bot\CMPHandler\model.json")
answer = Main.GetAnswer(a)
if answer is not None:
    print(answer)
else:
    print("хуй там плавал")