# --*-- conding:utf-8 --*--
# @Time : 10/30/24 1:44 PM
# @Author : Yuqi Zhang
# @Email : yzhan135@kent.edu
# @File : read_pdb.py

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
            print(f"  链 ID: {chain.id}")

            # 遍历链中的每个残基
            for residue in chain:
                # 检查残基是否为标准氨基酸或核苷酸
                if residue.id[0] != " ":
                    continue

                # 输出残基信息
                res_name = residue.resname
                res_id = residue.id[1]
                print(f"    残基: {res_name}, 序号: {res_id}")

                # # 遍历残基中的每个原子
                # for atom in residue:
                #     atom_name = atom.name
                #     atom_coord = atom.coord
                #     print(
                #         f"      原子: {atom_name}, 坐标: ({atom_coord[0]:.3f}, {atom_coord[1]:.3f}, {atom_coord[2]:.3f})")

if __name__ == '__main__':
    # 指定 .pdb 文件路径
    file_path = "./PDBbind/1a30/1a30_pocket.pdb"  # 将此路径替换为实际的 .pdb 文件路径
    read_pdb_file(file_path)

