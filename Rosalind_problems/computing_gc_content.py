def read_file(path):
    '''Reading a file and return lines as a list'''
    with open(path, "r") as file:
        return [l.strip() for l in file.readlines()]

