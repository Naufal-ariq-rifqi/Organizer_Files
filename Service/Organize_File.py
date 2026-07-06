import os
import shutil

from Service.File_Type import FILE_TYPES


class OrganizerService:

    def organize(self, folder):

        if not os.path.isdir(folder):
            raise ValueError("Folder not found.")

        moved_files = 0

        for item in os.listdir(folder):

            item_path = os.path.join(folder, item)

            if not os.path.isfile(item_path):
                continue

            _, extension = os.path.splitext(item)
            extension = extension.lower()

            category = "Others"

            for folder_name, extensions in FILE_TYPES.items():

                if extension in extensions:
                    category = folder_name
                    break

            destination_folder = os.path.join(folder, category)

            os.makedirs(destination_folder, exist_ok=True)

            destination_path = os.path.join(destination_folder, item)

            shutil.move(item_path, destination_path)

            moved_files += 1

        return moved_files