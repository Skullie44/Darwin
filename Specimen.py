__author__ = 'ADM_Skullie'

import Reproduction
import Energy
import Locomotion

class Specimen(object):
    def _init_(self, reproduction, energy, locomotion):
        self.rep = reproduction
        self.eng = energy
        self.loc = locomotion

    def reproduction(self):
        return self

    def energy(self):
        return self

    def locomotion(self):
        return self

