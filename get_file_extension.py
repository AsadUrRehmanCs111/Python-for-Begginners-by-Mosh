def get_file_extension(file):
    return file[file.index(".") + 1:]


file = get_file_extension("file.py")
print(file)
