import os
import shutil

def organize_files(folder_path):
    # Dictionary of file extensions and their categories
    file_types = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
        "Videos": [".mp4", ".mkv", ".mov", ".avi"],
        "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx"],
        "Audio": [".mp3", ".wav", ".m4a"],
        "Code": [".py", ".cpp", ".c", ".java", ".html", ".css", ".js"],
        "Compressed": [".zip", ".rar", ".tar", ".gz"],
        "Executables": [".exe", ".msi", ".apk"]
    }

    # Change directory to the folder
    os.chdir(folder_path)
    files = os.listdir()

    print(f"🔍 Found {len(files)} files in {folder_path}")
    
    for file in files:
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):
            _, ext = os.path.splitext(file)
            moved = False
            
            for category, extensions in file_types.items():
                if ext.lower() in extensions:
                    category_folder = os.path.join(folder_path, category)
                    if not os.path.exists(category_folder):
                        os.makedirs(category_folder)
                    shutil.move(file_path, os.path.join(category_folder, file))
                    print(f"📁 Moved {file} → {category}/")
                    moved = True
                    break
            
            if not moved:
                others_folder = os.path.join(folder_path, "Others")
                if not os.path.exists(others_folder):
                    os.makedirs(others_folder)
                shutil.move(file_path, os.path.join(others_folder, file))
                print(f"📦 Moved {file} → Others/")

    print("\n✅ All files organized successfully!")

# Example usage:
if __name__ == "__main__":
    folder = input("Enter the folder path to organize: ")
    if os.path.exists(folder):
        organize_files(folder)
    else:
        print("❌ Folder not found!")
