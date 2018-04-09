import os
import string
def rename_files():
    file_names=os.listdir(r"C:\Users\Deepti Gupta\Documents\Coursers\Python udacity\prank\prank")
    os.chdir(r"C:\Users\Deepti Gupta\Documents\Coursers\Python udacity\prank\prank")
    os.getcwd()
    print(file_names)
    for name in file_names:
        #intab=name
        #outtab=name
        #trantab=string.maketrans(intab,outtab)
        #ew_name=os.rename(name,string.translate(name,None,"0123456789"))
        str = name.translate("0123456789")
        #os.rename(name,name.translate(None,"0123456789")
        print(str)
rename_files()
