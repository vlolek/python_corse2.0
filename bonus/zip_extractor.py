import zipfile

def extract_zip(archive_path, dest_dir):
    with zipfile.ZipFile(archive_path, 'r') as zip_ref:
        zip_ref.extractall(dest_dir)

if __name__ == "__main__":
    extract_zip("/home/vlad/Desktop/python_corse2.0/bonus/compressed.zip", 
                "/home/vlad/Desktop/python_corse2.0/bonus")