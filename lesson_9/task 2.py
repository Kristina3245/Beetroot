import sys

print(sys.path)
sys.path.append('C:\\Users\konys\\PycharmProjects\pythonProject\\beetroot\\lesson_10 (exceptions)')
print(sys.path)
from Task_1 import catch_error
catch_error ()

sys.path.remove('C:\\Users\konys\\PycharmProjects\pythonProject\\beetroot\\lesson_10 (exceptions)')
print(sys.path)