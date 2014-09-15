__author__ = 'skullie'


class Validate:

    def __init__(self):
        pass

    def ver_terrain(ter):
        if ter == 'land':
            return 'land'
        elif ter == 'water':
            return 'water'
        else:
            return 'land'

    def ver_blood(bl):
        if bl == 'Y':
            return 'warm'
        elif bl == 'N':
            return 'cold'
        else:
            return 'warm'

    def ver_locomotion(lo):
       if lo == 'fly':
           return 'wings'
       else:
           return 'legs'

    def ver_respiratory(rs):
        if rs == 'lungs':
            return 'lungs'
        elif rs == 'skin':
            return 'lungs'
        else:
            return 'lungs'

    def ver_birth(br):
        if br == 'N':
            return 'live'
        else:
            return 'eggs'

    def ver_offspring(of):
        if of <= 10:
            return 'few'
        elif of >= 10:
            return 'many'

    def ver_care(ca):
        if ca == 'Y':
            return 'care'
        else:
            return 'leave'

    def ver_skin(sk):
        if sk == 'skin':
            return 'skin'
        elif sk == 'scales':
            return 'scales'
        elif sk == 'feathers':
            return 'feathers'

    def ver_nest(ne):
        if ne == 'Y':
            return 'nest'
        else:
            return 'none'