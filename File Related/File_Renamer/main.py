import os

files = os.listdir(os.getcwd())

for file in sorted(files):
    if file.startswith("Ava"):
        os.rename(file, f"{file[:3]} {file[3:]}")
    elif file.startswith("Lacey"):
        os.rename(file, f"{file[:5]} {file[5:]}")
    elif file.startswith("MILF"):
        os.rename(file, f"{file[:4]} {file[4:]}")
    elif file.startswith("Sara"):
        os.rename(file, f"{file[:4]} {file[4:]}")
    else:
        print(f"****** {file} ******")