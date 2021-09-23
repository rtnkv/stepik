import os
print('1')
print(os.path.abspath(__file__))


current_dir = os.path.abspath(os.path.dirname(__file__))

file_path = os.path.join(current_dir, 'test.txt')
print('and the file_path is:', file_path)
print('dirname we get is:', os.path.abspath(os.path.dirname(__file__)))
print('this what we get with "os.getcwd()"', os.getcwd())