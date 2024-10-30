# --*-- conding:utf-8 --*--
# @Time : 10/30/24 1:53 PM
# @Author : Yuqi Zhang
# @Email : yzhan135@kent.edu
# @File : read_pdb_chain.py

from Bio import PDB


def read_pdb_file(file_path):
    # 创建 PDB 解析器
    parser = PDB.PDBParser(QUIET=True)
    structure = parser.get_structure("structure_id", file_path)

    # 遍历每个模型
    for model in structure:
        print(f"模型编号: {model.id}")

        # 遍历模型中的每个链
        for chain in model:
            print(f"\n链 ID: {chain.id}")

            # 用于记录氨基酸序列和计数氨基酸数量
            amino_acid_sequence = []
            amino_acid_count = 0

            # 遍历链中的每个残基
            for residue in chain:
                # 检查残基是否为标准氨基酸
                if residue.id[0] == " ":
                    # 提取氨基酸的三字母代码
                    res_name = residue.resname
                    amino_acid_sequence.append(res_name)
                    amino_acid_count += 1

            # 打印氨基酸序列和总数量
            print(f"  氨基酸链序列: {'-'.join(amino_acid_sequence)}")
            print(f"  氨基酸数量: {amino_acid_count}")

if __name__ == '__main__':

    # 指定 .pdb 文件路径
    file_path = "./PDBbind/1a30/1a30_pocket.pdb"  # 将此路径替换为实际的 .pdb 文件路径
    read_pdb_file(file_path)
