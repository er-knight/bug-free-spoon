import random
import string
import os

def create_text_files(count=10):
    random_text = "".join([string.ascii_letters for _ in range(10)])

    for _ in range(count):
        file_name = "".join(random.sample(random_text, k=10))
        file_text = "".join(random.sample(random_text, k=100))
        with open(f"files/{file_name}.txt", "w") as random_file:
            random_file.write(file_text)

def rename_text_files(path="files/"):
    os.chdir(path=path)
    for i, file_name in enumerate(os.listdir()):
        _, extension = os.path.splitext(file_name)
        os.rename(file_name, f"file-{i}{extension}")

if __name__ == "__main__":
    create_text_files()
    # rename_text_files()