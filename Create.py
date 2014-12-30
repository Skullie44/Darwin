__author__ = 'ADM_Skullie'

import Animal.py
import Validate.py

class Create:

    locomotion = Validate.ver_locomotion(input('How does this creature move?'))
    blood = Validate.ver_blood(input('Does this creature have warm blood? Y/N'))
    respiratory = Validate.ver_respiratory(input('How does this creature breath?'))
    birth = Validate.ver_birth(input('How does this creature lay eggs? Y/N'))



    animal = dict()
    animal['blood'] = blood
    animal['respiratory'] = respiratory
    animal['birth']= birth
    animal['locomotion'] = locomotion


    creature = Animal(animal)

    print "you've created a " + creature.name()
