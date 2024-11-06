# --*-- conding:utf-8 --*--
# @Time : 11/4/24 1:49 PM
# @Author : Yuqi Zhang
# @Email : yzhan135@kent.edu
# @File : Choose_data.py

import os
from Bio import PDB


def read_pdb_file(file_path):
    parser = PDB.PDBParser(QUIET=True)
    structure = parser.get_structure("structure_id", file_path)

    chain_lengths = {}

    for model in structure:
        for chain in model:
            amino_acid_count = sum(1 for residue in chain if residue.id[0] == " ")

            if amino_acid_count > 0: # delete which length=0

                chain_lengths[chain.id] = amino_acid_count

                print(f'{chain}:{chain_lengths[chain.id]}')

    return chain_lengths


def process_pdb_folder(folder_path, length_threshold=18):
    selected_files = []


    for root, dirs, files in os.walk(folder_path):
        for file in files:

            if file.endswith("_pocket.pdb"):
                file_path = os.path.join(root, file)

                print("************************")
                print(root)
                print(file_path)

                chain_lengths = read_pdb_file(file_path)

                # for AA_chain in chain_lengths.values():
                for chain_id, length in chain_lengths.items():
                    # print(f"Chain ID: {chain_id}, Length: {length}")

                    if length < length_threshold:
                        selected_files.append(file)

    unique_files = list(set(selected_files))

    return unique_files


if __name__ == '__main__':
    folder_path = "./PDBbind"
    selected_files = process_pdb_folder(folder_path)
    print(selected_files)


