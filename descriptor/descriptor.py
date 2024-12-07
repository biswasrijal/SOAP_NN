from dscribe.descriptors import SOAP
from ase.io import read
from pymatgen.core.structure import Structure,Composition
import ase
import os


__author__ = "Biswas Rijal"
__copyright__ = "Copyright 2024"
__maintainer__ = "Biswas Rijal"
__email__ = "biswas.rijal@gmail.com"
__status__ = "Production"
__date__ = "November 3, 2024"


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

def atoms(poscar_file_list):
    atoms = []
    for poscar in poscar_file_list:
        atoms.append(ase.io.read(poscar,format='vasp'))
    return atoms

def poscar_file_list():
    poscars = []
    sorted_poscar_list=[]
    files = os.listdir('.')
    for poscar in files:
        if poscar.endswith('vasp'):
            poscars.append(poscar)
    for i in range(len(poscars)):
        sorted_poscar_list.append('poscar{}.vasp'.format(i))
    return sorted_poscar_list

def average_descriptor(atoms,compound):
    composition = Composition(compound)
    species = [composition.elements[0].name,composition.elements[1].name]
    r_cut = 6.0
    n_max = 8
    l_max = 6
    avg_soap = SOAP(species=species,r_cut=r_cut,n_max=n_max,l_max=l_max,periodic=True,average='inner',sparse=False)
    descrip = avg_soap.create(atoms)

    return descrip

def species(POSCAR):
    strc = Structure.from_file(POSCAR)
    species = [strc.symbol_set[0],strc.symbol_set[1]]
    return species
    
def add_element(filename,compound):
    comp=Composition(compound)
    length=len(comp.elements)
    f=open(filename,'r')
    lines=f.readlines()
    w=open('{}.vasp'.format(filename),'a')
    if length>1:
        element0=comp.elements[0]
        element1=comp.elements[1]
        for i in range(len(lines)):
            w.write(lines[i])
            if i==4:
                w.write(str(element0)+' '+str(element1)+'\n')
        w.close()
    if length==1:
        element0=comp.elements[0]

        for i in range(len(lines)):
            w.write(lines[i])
            if i==4:
                w.write(str(element0)+'\n')
        w.close()
    f.close()
    os.system('rm {}'.format(filename))
