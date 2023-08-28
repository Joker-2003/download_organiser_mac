import os
import shutil

def organize_downloads(downloads_folder):
    file_types = {
        'dmg': ['dmg'],
        'videos': ['mp4', 'mov', 'avi', 'mkv'],
        'pictures': ['jpg', 'jpeg', 'png', 'gif', 'webp'],
        'pdfs': ['pdf'],
        'docs': ['doc', 'docx', 'txt'],
        'ppts': ['ppt', 'pptx'],
        'zips': ['zip', 'tar', 'gz', 'rar'],
        'audio': ['mp3', 'wav', 'ogg', 'm4a'],
    }

    ignored_folders = ['misc', 'folders', '.DS_Store']

    misc_folder = os.path.join(downloads_folder, 'misc')
    if not os.path.exists(misc_folder):
        os.makedirs(misc_folder)

    folders_folder = os.path.join(downloads_folder, 'folders')
    if not os.path.exists(folders_folder):
        os.makedirs(folders_folder)

    for folder_name, extensions in file_types.items():
        folder_path = os.path.join(downloads_folder, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    for filename in os.listdir(downloads_folder):
        full_path = os.path.join(downloads_folder, filename)
        if os.path.isfile(full_path) and filename not in ignored_folders:
            # Consider only the last extension if a file has multiple extensions
            file_extension = filename.split('.')[-1].lower()
            moved = False

            for folder_name, extensions in file_types.items():
                if file_extension in extensions:
                    destination_folder = os.path.join(downloads_folder, folder_name)
                    shutil.move(full_path, os.path.join(destination_folder, filename))
                    moved = True
                    break
            
            if not moved:
                shutil.move(full_path, os.path.join(misc_folder, filename))

if __name__ == "__main__":
    downloads_folder = '/Users/<USER>/Downloads'  //change the USER NAME
    organize_downloads(downloads_folder)
    print("Downloads organized!")
