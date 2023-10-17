# module main
'''
Computes the chemical properties of equilibrium air. The partition functions for each species and
subreaction are calculated and fed into a linear solution matrix to calculate the number of moles of
each species.
'''

import initialize as init

def main():
    '''
    Runs the program.
    '''

    species_list = init.create_species_list()

    print(species_list)

if __name__ == '__main__':
    main()
