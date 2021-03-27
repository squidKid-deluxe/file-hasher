import hashlib
import os
from os import system
from time import sleep
from multiprocessing import Process
from sys import argv


def start(file_path, command):
    prev_data = ""
    while True:
        data = hash_directory(file_path)
        if data != prev_data:
            print()
            print("-" * 100)
            print(f"{command}ing {file_path}...")
            system(f"{command} {file_path}")
            prev_data = data
        sleep(0.5)


def hash_directory(path):
    digest = hashlib.sha256()
    if os.path.isfile(path):
        with open(path, "rb") as f_obj:
            while True:
                buf = f_obj.read(1024 * 1024)
                if not buf:
                    break
                digest.update(buf)
        return digest.hexdigest()
    for root, dirs, files in os.walk(path):
        for names in files:
            file_path = os.path.join(root, names)
            # Hash the path and add to the digest to account for empty files/directories
            digest.update(hashlib.sha256(file_path[len(path) :].encode()).digest())
            # Per @pt12lol - if the goal is uniqueness over repeatability, this is an alternative method using 'hash'
            # digest.update(str(hash(file_path[len(path):])).encode())
            if os.path.isfile(file_path):
                with open(file_path, "rb") as f_obj:
                    while True:
                        buf = f_obj.read(1024 * 1024)
                        if not buf:
                            break
                        digest.update(buf)
    return digest.hexdigest()


if __name__ == "__main__":
    children = {}
    directory = input(
        f"What directory (off of the current) do you want to monitor for changes?\n\t{os.path.abspath(os.getcwd())}/"
    )
    command = argv[1]
    extension = argv[2]
    print("\033c")
    directory = os.path.abspath(os.getcwd()) + "/" + directory
    child_number = 0
    for root, _, files in os.walk(directory):
        for names in files:
            file_path = os.path.join(root, names)
            file_path += " "
            if file_path[-4:-1:1] == "." + str(extension):
                children[child_number] = Process(
                    target=start, args=(file_path.rstrip(" "), command)
                )
                children[child_number].start()
    while True:
        sleep(60)
