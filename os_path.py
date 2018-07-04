import os

# 获得当前路径
cwd = os.getcwd()
print(cwd)

# 得到当前文件夹下的所有文件和文件夹
print(os.listdir())  # listdir(../)

# 检查是否是文件／文件夹
print(os.path.isfile('E:/sanfordpython/self_study/exercise/tests/path.py'))
print(os.path.isdir('E:/sanfordpython/self_study/exercise/tests'))

# 检查文件路径是否存在
print(os.path.exists('E:/sanfordpython/self_study/exercise/test'))

# 分离文件名
[dirname, filename] = os.path.split('E:/sanfordpython/self_study/exercise/tests/path.py')
print(dirname, "\n", filename)

# 获得文件路径（不包括文件名）
print("get pathname:", os.path.dirname('E:/sanfordpython/self_study/exercise/tests/path.py'))
# 获得文件名
print("get pathname:", os.path.basename('E:/sanfordpython/self_study/exercise/tests/path.py'))
