__author__ = 'skullie'

import Creature.py
import Validate.py

class Create:

    terrain = Validate.ver_terrain(input('where will this creature live?'))
    locomotion = Validate.ver_locomotion(input('how will this creature move?'))
    blood = Validate.ver_blood(input('is it warm blooded? Y/N'))
    respiratory = Validate.ver_respiratory(input('how does this creature breath?'))
    birth = Validate.ver_birth(input('does this creature lay eggs? Y/N'))
    offspring = Validate.ver_offspring(input('how many offspring does it typically have?'))
    care = Validate.ver_care(input('do they care for their young? Y/N'))
    skin = Validate.ver_skin(input('what type of skin does it have?'))
    nest = input('does this animal have a nest? Y/N')




    animal = dict()
    animal['blood'] = blood
    animal['respiratory'] = respiratory
    animal['birth']= birth
    animal['offspring'] = offspring
    animal['care'] = care
    animal['locomotion'] = locomotion
    animal['terrain'] = terrain



    creature = Creature(animal)

    print "you've created a " + creature.name()
