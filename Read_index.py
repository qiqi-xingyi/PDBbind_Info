# --*-- conding:utf-8 --*--
# @Time : 11/4/24 1:20 PM
# @Author : Yuqi Zhang
# @Email : yzhan135@kent.edu
# @File : Read_index.py


file_path = "2020_index.lst"

if __name__ == '__main__':

    with open(file_path, "r") as file:
        content = file.readlines()

    content = [line.strip() for line in content]

    print(content)
