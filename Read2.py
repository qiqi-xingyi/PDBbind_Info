# --*-- conding:utf-8 --*--
# @Time : 10/27/24 PM2:54
# @Author : Yuqi Zhang
# @Email : yzhan135@kent.edu
# @File : Read2.py

from Bio.PDB import PDBParser

if __name__ == '__main__':

    # 读取pocket.pdb和protein.pdb文件
    pdb_parser = PDBParser()

    # 解析pocket
    pocket_file = "./PDBbind/1a30/1a30_pocket.pdb"
    pocket_structure = pdb_parser.get_structure("pocket", pocket_file)
    print("Pocket structure:", pocket_structure)

    # 解析protein
    protein_file = "./PDBbind/1a30/1a30_protein.pdb"
    protein_structure = pdb_parser.get_structure("protein", protein_file)
    print("Protein structure:", protein_structure)
