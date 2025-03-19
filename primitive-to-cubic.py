#%% Convert non-cubic primitive cell to cubic cell
from ase.io import read, write
from ase.build import make_supercell, find_optimal_cell_shape

prim_cell = read("POSCAR", format='vasp')
max_size = 10

cubic_cell = 0
for i in range(max_size):
    P = find_optimal_cell_shape(prim_cell.cell, i+1, 'sc')
    new_cell = make_supercell(prim_cell, P)
    angles = new_cell.cell.angles()
    if 89<=angles[0]<=91 and 89<=angles[1]<=91 and 89<=angles[2]<=91:
        cubic_cell = new_cell
        print("Supercell size:", i+1)
        print("Cubic cell lengths:", cubic_cell.cell.lengths())
        break

if cubic_cell==0:
    print("Could not transform to cubic cell ! \nYou can try increasing 'max_size'.")
else:
    write("cubic_cell.vasp", cubic_cell, format='vasp')

#%%