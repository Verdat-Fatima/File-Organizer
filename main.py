from tkinter import filedialog
import os
import shutil

folder_path=filedialog.askdirectory(title="Select Folder to Organize")

files=os.listdir(folder_path)

categories={
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
    'Videos': ['.mp4', '.mov', '.avi', '.mkv'],
    'Music': ['.mp3', '.wav'],
    'Archives': ['.zip', '.rar', '.7z'],
    'Programs': ['.exe', '.msi', '.bat']
}

for file in files:
    file_path=os.path.join(folder_path,file)

    if not os.path.isfile(file_path):
        continue

    name,extension=os.path.splitext(file)

    if not extension:
        continue

    for category,extensions in categories.items():
        if extension.lower() in extensions:
            category_folder=os.path.join(folder_path,category)

            if not os.path.exists(category_folder):
                os.makedirs(category_folder)

            shutil.move(file_path, os.path.join(category_folder,file))
            print(f'Move {file} -> {category_folder}')
            break



print('File organize successfully')