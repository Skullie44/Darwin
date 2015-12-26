__author__ = 'ADM_Skullie'

import Create

print "specimen creation . . . "
reproduction = "provide method of reproduction:"
locomotion = "provide method of movement:"
energy = "provide method of attaining energy:"

specimen = Create.specimen(reproduction, locomotion, energy)

print len(specimen.specimens)