# --*-- conding:utf-8 --*--
# @Time : 10/29/24 PM4:06
# @Author : Yuqi Zhang
# @Email : yzhan135@kent.edu
# @File : Print_Info.py

import os
from Bio import PDB
from rdkit import Chem


def extract_protein_info(protein_pdb_path):
    parser = PDB.PDBParser()
    structure = parser.get_structure('protein', protein_pdb_path)
    protein_name = os.path.basename(protein_pdb_path).split('_')[0]  # 使用文件名中的PDB ID作为蛋白质名称

    chain_ids = set()
    amino_acid_count = 0

    for model in structure:
        for chain in model:
            chain_ids.add(chain.id)  # 记录链ID
            for residue in chain:
                if PDB.is_aa(residue):
                    amino_acid_count += 1  # 统计氨基酸残基数量

    return protein_name, chain_ids, amino_acid_count


def extract_ligand_info(ligand_file_path):
    ligand_mol = None
    if ligand_file_path.endswith('.mol2'):
        ligand_mol = Chem.MolFromMol2File(ligand_file_path)
    elif ligand_file_path.endswith('.sdf'):
        ligand_mol = Chem.SDMolSupplier(ligand_file_path)[0]

    if ligand_mol is not None:
        ligand_name = ligand_mol.GetProp('_Name') if ligand_mol.HasProp('_Name') else "Unknown"
        ligand_type = ligand_mol.GetProp('TYPE') if ligand_mol.HasProp('TYPE') else "Unknown"
    else:
        ligand_name = "Unknown"
        ligand_type = "Unknown"

    return ligand_type, ligand_name


def extract_pocket_info(pocket_pdb_path):
    parser = PDB.PDBParser()
    structure = parser.get_structure('pocket', pocket_pdb_path)

    chain_ids = set()
    amino_acid_count = 0

    for model in structure:
        for chain in model:
            chain_ids.add(chain.id)  # 记录口袋中的链ID
            for residue in chain:
                if PDB.is_aa(residue):
                    amino_acid_count += 1  # 统计口袋中的氨基酸残基数量

    return chain_ids, amino_acid_count


def main():
    pdbbind_dir = './PDBbind'  # 修改为实际的PDBbind文件夹路径
    results = []

    for folder in os.listdir(pdbbind_dir):
        folder_path = os.path.join(pdbbind_dir, folder)
        if os.path.isdir(folder_path):
            protein_pdb_path = os.path.join(folder_path, f"{folder}_protein.pdb")
            ligand_file_path = os.path.join(folder_path, f"{folder}_ligand.mol2")
            pocket_pdb_path = os.path.join(folder_path, f"{folder}_pocket.pdb")

            if not os.path.exists(ligand_file_path):  # 检查是否存在SDF格式的配体文件
                ligand_file_path = os.path.join(folder_path, f"{folder}_ligand.sdf")

            if os.path.exists(protein_pdb_path) and os.path.exists(ligand_file_path) and os.path.exists(
                    pocket_pdb_path):
                # 提取蛋白质信息
                protein_name, chain_ids, amino_acid_count = extract_protein_info(protein_pdb_path)

                # 提取配体信息
                ligand_type, ligand_name = extract_ligand_info(ligand_file_path)

                # 提取口袋信息
                pocket_chain_ids, pocket_amino_acid_count = extract_pocket_info(pocket_pdb_path)

                result = {
                    'Protein Name': protein_name,
                    'Protein Chains': ', '.join(chain_ids),
                    'Protein Amino Acid Count': amino_acid_count,
                    'Ligand Type': ligand_type,
                    'Ligand Name': ligand_name,
                    'Pocket Chains': ', '.join(pocket_chain_ids),
                    'Pocket Amino Acid Count': pocket_amino_acid_count
                }
                results.append(result)

                # 输出结果
                print(f"Protein Name: {protein_name}")
                print(f"Protein Chains: {', '.join(chain_ids)}")
                print(f"Protein Amino Acid Count: {amino_acid_count}")
                print(f"Ligand Type: {ligand_type}")
                print(f"Ligand Name: {ligand_name}")
                print(f"Pocket Chains: {', '.join(pocket_chain_ids)}")
                print(f"Pocket Amino Acid Count: {pocket_amino_acid_count}")
                print("-" * 50)


if __name__ == '__main__':
    main()
