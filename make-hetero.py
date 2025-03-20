#%% Template for making hetero-structure
from ase.io import read, write
from ase.build import make_supercell, cut, stack, add_vacuum, find_optimal_cell_shape

fe_bcc = read("Fe.cif", format='cif')
main_cell = read("POSCAR", format='vasp')

# Convert to cubic unit cell [Only if non-cubic]
main_cell = make_supercell(main_cell, P=find_optimal_cell_shape(main_cell.cell, 2, 'sc'), order='atom-major')

# Make supercells of nearly equal base
fe_sc = make_supercell(fe_bcc, P=[[3,0,0],[0,3,0],[0,0,2]], order='atom-major')
fe_sc = cut(fe_sc, a=(1,0,0),b=(0,1,0),c=(0,0,3/4)) # Optionally cutting top layer
main_sc = make_supercell(main_cell, P=[[2,0,0],[0,1,0],[0,0,5]], order='atom-major')

# Stack two supercells (straining Fe to match size) ; then adding vacuum
hetero = stack(fe_sc, main_sc, axis=2, fix=1, maxstrain=10, distance=2.5)
add_vacuum(hetero, vacuum=20)

write("hetero.vasp", hetero, format='vasp')
#%%