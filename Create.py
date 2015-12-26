__author__ = 'Skullie'

import Specimen

##some means of calling a stored array of specimens already created
##should this become a dictionary? easier cataloging of specimens created
specimens = []



class Create(replication, locomotion, energy):
    ##single cell organisms reproduce by splitting
    specimen = Specimen()
    specimen.energy(energy)
    specimen.reproduction(replication)
    specimen.locomotion(locomotion)



class Breed:
    ## breeding requires 2 specimen to perform, not doing at this time
