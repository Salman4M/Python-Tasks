"""
Folderler >> Oxuma
"""

import os 


'''
The os.listdir() method in Python is used to get the list of all files and directories in the specified directory
If we don’t specify any directory, then a list of files and directories in the current working directory will be returned.

Syntax: os.listdir(path)

Parameters: path (optional) : path of the directory

'''
# 1-ci Yol ->
# print(os.listdir())

'''
os.getcwd() method tells us the location of current working directory (CWD).

'''
# Hangi folder oxunacaq onun yerini teyin edirem:
folder_yolu = os.getcwd()
#to see the current directory print(folder_yolu)

content = os.listdir(folder_yolu)
# print(content)
# for ic in content:
#     print(ic)
    
'''
The os.scandir() method in Python is used to get an iterator of os.DirEntry
objects corresponding to the entries in the directory given by the specified path. 
Syntax: os.scandir(path = '.')

'''
# 2-ci Yol -> os.scandir()
# content = os.scandir(folder_yolu)
# for ic in content:
#     print(ic)


# 3-cu Yol -> 
# pathlib.Path.iterdir()
# Path - yol, url
from pathlib import Path

# content = Path(folder_yolu).iterdir()
# for ic in content:
#     print(ic)


# Folder icerisinde olan fayllari ekrana cixartmaq:
import os 
# Hangi folder oxunacaq onun yerini teyin edirem:
folder_yolu = os.getcwd()

content = os.listdir(folder_yolu)
'''
os.path.isfile() method in Python is used to check whether the specified path is an existing regular file or not.
Syntax: os.path.isfile(path)
Return Type: This method returns a Boolean value of class bool. 
This method returns True if specified path is an existing regular file, otherwise returns False.
'''
# for ic in content:
#     if os.path.isfile(ic): 
#         print(ic)
        
# Sirf folderleri gormek ucun:
# folder_yolu = os.getcwd()

# content = os.listdir(folder_yolu)

'''
os.path.isdir() method in Python checks whether the specified path is a directory or not. This method follows the symbolic link,
which means if the specified path is a symbolic link pointing to an existing directory then the method will return True.
isdir() stands for “is directory”.
'''
for ic in content:
    if os.path.isdir(ic): 
        print(ic)



# =========================================================================
"""
Folder - Yaratma

1. os.mkdir():
    * mkdir() - tek folder yatamaq ucundur
    * makedirs() - Birden cox folder yaratmaq ucun
    
2. path.Path.mkdir() -> hem tek hemde birden cox folder yatamaq ucundur
"""

# Tek folder yatamaq:
import os
from pathlib import Path

# ana_folder_yolu = os.getcwd()

# Numune 1:
# try:
#     os.mkdir("Folder 3")
    
# except FileExistsError:
#     print("Bu adda fayl movcuddur, ona gore uygun ad qoyub yenisini yaratdiq")
#     os.mkdir("Folder 3 (1)")
    
#  Eger file movcuddursa FileExistsError xetasini verir


# 2-ci Yol -> pathlib.Path.mkdir()

# p = Path("Path 1").mkdir()

# Bir nece folder eyni anda yaratmaq ucun -> os.makedirs():
# os.makedirs("Level 1/Level 2/Level 3", exist_ok=True)



"""
Folder - Axtarma

Iki yol:
    * String methodlari -> find, startswith, endswith
    * fnmatch kitabxanasi
    
"""

import os
from pathlib import Path
import fnmatch

# Axtarma funksiyasi:
axtarilan_yol = "c:\Windows"

# Ilk once bu folderin icini gorek:
# for ic in os.listdir(axtarilan_yol):
#     print(ic)
    
# Indi ise .exe ile biten fayllari mene qaytar:
# with Path(axtarilan_yol) as folder:
#     for file in folder.iterdir():
# #         # Fayldimi deyilmi, ikinci ise .exe ile bitirmi?
#         if file.is_file() and file.name.endswith(".exe"):
#             print(file)


# Fnmatch ile (Daha cox istifade olunur):
# sonluq = "*.exe"

# with Path(axtarilan_yol) as folder:
#     for file in folder.iterdir():
#         if file.is_file() and fnmatch.fnmatch(file, sonluq):
#             print(file)



"""
File - Silme - Ad deyisme - Kocurme, kopyalama
"""

import shutil
import os
import pathlib

# 1 Folder silme:
"""
os.rmdir() -> tek folder silir (Eger ici bosdursa)
path.Path.rmdir() -> tek folder silir (Eger ici bosdursa)
shutil.rmtree() -> Isaret olunan folderi silir (Ici dolu olsada)
"""

# os.mkdir("NewFolder")
# os.rmdir("NewFolder")

# shutil.rmtree("NewFolder")


# 2 -> Folder ve File kopyalama
# shutil.copy()
photo="porsche.jpg"
file1 = "Folder1/app.py"
# file2 = "Folder2/copy.py"
# shutil.copy("nə?, "hara?")
shutil.copy(photo, "Folder2")
# shutil.copy("Folder1/app.py", "Folder3")

# File ve Folder kocurme:
# shutil.move(kocurelecek olan, hara kocurulecek)

## only one to cut  and one to  move . There will be one change in the third one (Folder3)
shutil.move("Folder1", "Folder2", "Folder3")


# Folder adini deyismek ucun:
# os.rename("Folder1", "NewFolder1")