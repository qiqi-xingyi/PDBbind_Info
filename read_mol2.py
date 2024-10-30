# --*-- conding:utf-8 --*--
# @Time : 10/30/24 12:52 PM
# @Author : Yuqi Zhang
# @Email : yzhan135@kent.edu
# @File : read_mol2.py

from rdkit import Chem


def read_mol2_file(file_path):
    # 使用 RDKit 从 mol2 文件读取分子
    mol = Chem.MolFromMol2File(file_path)

    if mol is None:
        print("无法读取该 .mol2 文件，请检查文件路径或文件内容格式是否正确。")
        return

    # 从 mol2 文件中提取分子名称
    molecule_name = None
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            if line.startswith("@<TRIPOS>MOLECULE"):
                # 获取`@<TRIPOS>MOLECULE`标签下的下一行，通常为分子名称
                molecule_name = lines[i + 1].strip()
                break

    if molecule_name:
        print("分子名称:", molecule_name)
    else:
        print("未找到分子名称，文件格式可能不正确。")

    # 输出原子数量
    atom_count = mol.GetNumAtoms()
    print("原子数量:", atom_count)

    # 输出键的数量
    bond_count = mol.GetNumBonds()
    print("键数量:", bond_count)

    # 遍历原子信息
    print("\n原子信息:")
    for atom in mol.GetAtoms():
        atom_idx = atom.GetIdx()
        atom_symbol = atom.GetSymbol()
        atom_position = mol.GetConformer().GetAtomPosition(atom_idx)
        print(
            f"  原子索引: {atom_idx}, 元素符号: {atom_symbol}, 坐标: ({atom_position.x:.3f}, {atom_position.y:.3f}, {atom_position.z:.3f})")

    # 遍历键信息
    print("\n键信息:")
    for bond in mol.GetBonds():
        bond_type = bond.GetBondType()
        atom1_idx = bond.GetBeginAtomIdx()
        atom2_idx = bond.GetEndAtomIdx()
        print(f"  键: 原子{atom1_idx} - 原子{atom2_idx}, 类型: {bond_type}")


if __name__ == '__main__':

    # 读取 mol2 文件路径
    file_path = "./PDBbind/1a30/1a30_ligand.mol2"
    read_mol2_file(file_path)

