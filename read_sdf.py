# --*-- conding:utf-8 --*--
# @Time : 10/30/24 1:17 PM
# @Author : Yuqi Zhang
# @Email : yzhan135@kent.edu
# @File : read_sdf.py

from rdkit import Chem

def read_sdf_file(file_path):
    # 使用 RDKit 读取 .sdf 文件
    supplier = Chem.SDMolSupplier(file_path)

    # 检查文件是否正确加载
    if not supplier:
        print("无法读取该 .sdf 文件，请检查文件路径或文件内容格式是否正确。")
        return

    # 遍历每个分子
    for i, mol in enumerate(supplier):
        if mol is None:
            print(f"分子 {i + 1} 加载失败，可能存在问题。")
            continue

        # 提取分子名称
        mol_name = mol.GetProp('_Name') if mol.HasProp('_Name') else f"分子 {i + 1}"
        print(f"分子 {i + 1} 名称:", mol_name)

        # 输出原子数量和键的数量
        atom_count = mol.GetNumAtoms()
        bond_count = mol.GetNumBonds()
        print(f"  原子数量: {atom_count}, 键数量: {bond_count}")

        # 输出分子属性
        print("  分子属性:")
        for prop in mol.GetPropNames():
            print(f"    {prop}: {mol.GetProp(prop)}")

        # 遍历原子信息
        print("  原子信息:")
        for atom in mol.GetAtoms():
            atom_idx = atom.GetIdx()
            atom_symbol = atom.GetSymbol()
            atom_position = mol.GetConformer().GetAtomPosition(atom_idx)
            print(
                f"    原子索引: {atom_idx}, 元素符号: {atom_symbol}, 坐标: ({atom_position.x:.3f}, {atom_position.y:.3f}, {atom_position.z:.3f})")

        # 遍历键信息
        print("  键信息:")
        for bond in mol.GetBonds():
            bond_type = bond.GetBondType()
            atom1_idx = bond.GetBeginAtomIdx()
            atom2_idx = bond.GetEndAtomIdx()
            print(f"    键: 原子 {atom1_idx} - 原子 {atom2_idx}, 类型: {bond_type}")

        print("-" * 50)  # 分隔每个分子的输出

if __name__ == '__main__':

    # 读取 .sdf 文件路径
    file_path = "./PDBbind/1a30/1a30_ligand.sdf"  # 替换为你的 .sdf 文件路径
    read_sdf_file(file_path)
