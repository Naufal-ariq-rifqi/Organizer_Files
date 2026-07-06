import os

from Service.File_Type import FILE_TYPES

class ScannerService:

    def scan(self, folder):

        if not os.path.isdir(folder):
            raise ValueError("Folder not found.")

        result = {
            "total_files": 0,
            "documents": 0,
            "images": 0,
            "videos": 0,
            "audio": 0,
            "archives": 0,
            "others": 0
        }

        for item in os.listdir(folder):

            item_path = os.path.join(folder, item)

            if not os.path.isfile(item_path):
                continue

            result["total_files"] += 1

            _, extension = os.path.splitext(item)
            extension = extension.lower()

            found = False

            for category, extensions in FILE_TYPES.items():

                if extension in extensions:
                    result[category] += 1
                    found = True
                    break

            if not found:
                result["others"] += 1

        return result