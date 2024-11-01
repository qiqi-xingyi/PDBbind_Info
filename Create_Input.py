# --*-- conding:utf-8 --*--
# @Time : 10/30/24 3:16 PM
# @Author : Yuqi Zhang
# @Email : yzhan135@kent.edu
# @File : Create_Input.py

from Bio import PDB

# 三字母代码到单字母代码的映射字典
three_to_one = {
    "ALA": "A", "ARG": "R", "ASN": "N", "ASP": "D", "CYS": "C",
    "GLN": "Q", "GLU": "E", "GLY": "G", "HIS": "H", "ILE": "I",
    "LEU": "L", "LYS": "K", "MET": "M", "PHE": "F", "PRO": "P",
    "SER": "S", "THR": "T", "TRP": "W", "TYR": "Y", "VAL": "V"
}


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

            # 用于记录主链和侧链序列
            main_chain_residue_seq = []  # 主链氨基酸序列
            side_chain_residue_sequences = []  # 侧链序列

            # 遍历链中的每个残基
            for residue in chain:
                # 检查残基是否为标准氨基酸
                if residue.id[0] == " ":
                    # 获取氨基酸三字母代码并转换为单字母代码
                    res_name = residue.resname
                    main_chain_residue_seq.append(three_to_one.get(res_name, ""))

                    # 检查是否有侧链原子，排除主链原子N, CA, C, O
                    # side_chain_atoms = [atom for atom in residue if atom.name not in ["N", "CA", "C", "O"]]
                    # if side_chain_atoms:
                    #     # 如果有侧链原子，则记录侧链氨基酸单字母代码
                    #     side_chain_residue_sequences.append(three_to_one.get(res_name, ""))
                    # else:
                    #     # 否则记录空字符串
                    side_chain_residue_sequences.append("")

            # 输出主链和侧链序列
            print("main_chain_residue_seq =", "".join(main_chain_residue_seq))  # 主链
            print("side_chain_residue_sequences =", side_chain_residue_sequences)  # 侧链


if __name__ == '__main__':
    # 指定 .pdb 文件路径
    file_path = "./PDBbind/3jvs/3jvs_pocket.pdb"  # 将此路径替换为实际的 .pdb 文件路径
    read_pdb_file(file_path)

