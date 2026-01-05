import numpy as np

def pdb_file(filepath, ligand_name):
    """
    Parse a PDB file and extract protein and ligand atoms.

    :param filepath: str
        Path to the PDB file.
    :param ligand_name: str
        Residue name of the ligand (e.g. 'HEM', 'ATP', 'AXI).
    :return:
    dictionary with keys:
        'protein_atoms': np.ndarray of shape (N, 3)
        'ligand_atoms' : np.ndarray of shape (M, 3)
    """
    protein_coord = []
    ligand_coord = []
    with open(filepath, 'r') as f:
        for line in f:
            if line.startswith('ATOM'):
                resname = line[17:20].strip()  # ALA, GLU....
                x = float(line[30:38])
                y = float(line[38:46])
                z = float(line[46:54])
                protein_coord.append([x, y, z])

            elif line.startswith('HETATM'):
                resname = line[17:20].strip()
                if resname == ligand_name:
                    x = float(line[30:38])
                    y = float(line[38:46])
                    z = float(line[46:54])
                    ligand_coord.append([x, y, z])

    return {
        "protein_atoms": np.array(protein_coord),
        "ligand_atoms": np.array(ligand_coord)
    }

print(pdb_file("../data/4AG8.pdb", "AXI"))
