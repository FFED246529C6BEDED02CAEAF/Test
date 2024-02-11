import os

folder_structure = {
    "root": "/",
    "static": ["css", "img", "js"],
    "templates": ["base.html", "index.html", "games", "auth"],
    "games": ["game1", "quiz2"],
    "auth": ["models.py", "views.py", "forms.py"],
    "utils": ["helpers.py", "database.py"],
}

def create_folders(path, subfolders):
  for subfolder in subfolders:
    subfolder_path = os.path.join(path, subfolder)
    if not os.path.exists(subfolder_path):
      os.makedirs(subfolder_path)

def create_files(path, filenames):
  for filename in filenames:
    file_path = os.path.join(path, filename)
    if not os.path.exists(file_path):
      with open(file_path, "w") as f:
        f.write("")

# Create root folder
root_path = folder_structure["root"]
if not os.path.exists(root_path):
  os.makedirs(root_path)

# Create subfolders
for main_folder, subfolders in folder_structure.items():
  if main_folder != "root":
    create_folders(root_path, subfolders)

# Create base files
create_files(root_path, ["requirements.txt", "app.py", "README.md"])

# Create template files
create_files(os.path.join(root_path, "templates"), ["base.html", "index.html"])

print("Folder structure and basic files created successfully!")
