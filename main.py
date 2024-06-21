import os
import hashlib as hl

def compare_files(main_file_path, another_file_path):
    hash_main_file = file_hash(main_file_path)
    hash_another_file = file_hash(another_file_path)


def file_hash(file_path):

    sha256 = hl.sha256()

    with open(file_path, "rb") as f:
        while True:
            data = f.read(65536) # arbitrary number to reduce RAM usage
            if not data:
                break
            sha256.update(data)

    return sha256.hexdigest()


if __name__ == "__main__":
    print(file_hash('5 Flower Types Classification Dataset/Lotus/0ae8156e1f.jpg'))
    print(file_hash('5 Flower Types Classification Dataset/Lotus/0ae8156e1f.jpg'))
    directory = "5 Flower Types Classification Dataset/Lotus"
    files = []
    files += os.listdir(directory)
    print(files)
