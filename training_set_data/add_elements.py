from pymatgen.core.composition import Composition
import os
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
