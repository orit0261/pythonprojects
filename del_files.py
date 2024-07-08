import os


def delete_log_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".log"):
                file_path = os.path.join(root, file)
                os.remove(file_path)
                print(f"Deleted: {file_path}")


if __name__ == "__main__":
    target_directory = r"C:\orit"

    if os.path.exists(target_directory):
        delete_log_files(target_directory)
        print("Log files deleted.")
    else:
        print("Target directory does not exist.")
