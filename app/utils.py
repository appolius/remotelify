import os

def delete_uploaded_file(upload_folder, filename):
    file_path = os.path.join(upload_folder, filename)
    if os.path.exists(file_path):
        os.remove(file_path)
        return True
    return False
