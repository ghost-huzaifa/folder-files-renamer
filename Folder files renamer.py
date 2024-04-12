import os
import re

def remove_text_from_filenames(folderPath, textToRemove):
    
    # Itterate through all files in given folder Path
    files = os.listdir(folderPath)

    for file_name in files:
        file_path = os.path.join(folderPath, file_name)

        # Check if the file_name belongs to a file
        if os.path.isfile(file_path):

            # Make new filename for each file
            new_file_name = re.sub(re.escape(textToRemove), '', file_name)
            new_file_path = os.path.join(folderPath, new_file_name)

            # Rename filename
            os.rename(file_path, new_file_path)

            # Print each renamed file's info
            print(f"Renamed '{file_name}' to '{new_file_name}'")


folderPath = r'C:\Users\PMLS\Downloads\Hamd-o-Naat'
textToRemove = r'[SPOTIFY-DOWNLOADER.COM] '

remove_text_from_filenames(folderPath, textToRemove)