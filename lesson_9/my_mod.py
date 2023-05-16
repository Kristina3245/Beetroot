import os
my_path=os.path.dirname(os.path.abspath('file')).replace("module_2", "module_1")
def func():
    for root, dirs, files in os.walk(my_path):
        if "file.txt" in files:
            result= os.path.join(root , "".join(files[files.index('file.txt')]))
            return result

def count_lines(name):
    with open(name, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        return len(lines)

def count_chars(name):
    with open(name, 'r', encoding='utf-8') as file:
        content = file.read()
        return len(content)

def test(name):
    lines = count_lines(name)
    chars = count_chars(name)
    print(f"Number of lines: {lines}")
    print(f"Number of characters: {chars}")

if __name__ == '__main__':
     filename = input("Enter the filename: ")
     test(filename)