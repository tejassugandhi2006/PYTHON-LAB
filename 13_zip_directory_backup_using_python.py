import os
import sys
import pathlib
import zipfile

dirName = r"C:\CODES\COLLEGE\1 St SEM\C ALL"

if not os.path.isdir(dirName):
    print("Directory", dirName, "doesn't exist")
    sys.exit(0)

curDir = pathlib.Path(dirName)

with zipfile.ZipFile("myZip.zip", "w") as archive:
    for file_path in curDir.rglob("*"):
        if file_path.is_file():
            print(file_path)
            archive.write(file_path, arcname=file_path.relative_to(curDir))

if os.path.isfile("myZip.zip"):
    print("Archive myZip.zip created successfully")
else:
    print("Error in creating zip archive")

input("Press Enter to exit...")