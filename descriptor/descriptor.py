from dscribe.descriptors import SOAP
from ase.io import read
from pymatgen.core.structure import Structure

def descriptors(poscar_filename):
    strc = Structure.from_file(poscar_filename) 
    atoms = read(poscar_filename)
    species = [strc.symbol_set[0],strc.symbol_set[1]]
    r_cut = 6.0
    n_max = 8
    l_max = 6

    soap = SOAP(species=species,r_cut=r_cut,n_max=n_max,l_max=l_max,periodic=True,sparse=False)

    descrip = soap.create(atoms)

    return descrip

def species(POSCAR):
    strc = Structure.from_file(POSCAR)
    species = [strc.symbol_set[0],strc.symbol_set[1]]
    return species
    
