import os
import hashlib as hl


def compare_files(main_file_path, another_file_path):
    return file_hash(main_file_path) == file_hash(another_file_path)


def file_hash(file_path):
    sha256 = hl.sha256()

    with open(file_path, "rb") as f:
        while True:
            data = f.read(65536)
            if not data:
                break
            sha256.update(data)

    return sha256.hexdigest()


if __name__ == "__main__":
    directories = []
    print("Searching directories...")
    print("Enter paths to directories (enter blank line to stopping this process): ")
    while True:
        directory = input("Directory path: ")
        if directory == "":
            break
        if os.path.exists(directory):
            directories.append(directory)
        else:
            print("Directory not found!")
    files = []
    for directory in directories:
        files.extend([os.path.join(directory, f) for f in os.listdir(directory) if
                     os.path.isfile(os.path.join(directory, f))])

    print(len(files))

    hash_dict = {}


    for file in files:
        file_hash_value = file_hash(file)
        if file_hash_value in hash_dict:
            print(f"Found duplicates:\nFirst file: {hash_dict[file_hash_value]}\nSecond file: {file}")
        else:
            hash_dict[file_hash_value] = file
