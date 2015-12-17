__author__ = 'ADM_Skullie'

import Reproduction
import Energy
import Locomotion

class Specimen(object):
    def _init_(self, reproduction, energy, locomotion):
        self.rep = reproduction
        self.eng = energy
        self.loc = locomotion

