# --*-- conding:utf-8 --*--
# @Time : 10/27/24 PM2:51
# @Author : Yuqi Zhang
# @Email : yzhan135@kent.edu
# @File : Read.py

from rdkit import Chem

if __name__ == '__main__':

    # 读取mol2文件
    mol2_file = "./PDBbind/1a30/1a30_ligand.mol2"
    mol2_molecule = Chem.MolFromMol2File(mol2_file)
    print("MOL2 molecule:", mol2_molecule)

    # 读取sdf文件
    sdf_file = "./PDBbind/1a30/1a30_ligand.sdf"
    sdf_molecules = Chem.SDMolSupplier(sdf_file)
    for mol in sdf_molecules:
        if mol is not None:
            print("SDF molecule:", mol)
