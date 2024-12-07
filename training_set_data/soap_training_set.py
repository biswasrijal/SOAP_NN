import descriptor as ds
import os
import numpy as np

os.chdir('poscars')

poscar_files = os.listdir('poscars/.')

for poscar in poscar_files:
    avg=ds.average_descriptor('poscar1707.vasp')
    
