# module initialize
'''
Assigns each species a class and creates a list to hold them.
'''

from dataclasses import dataclass

import pandas as pd

import constants as cn
import input as inp

species_dataframe = pd.read_csv(inp.DATAFRAME_PATH)

@dataclass
class Species:
    '''
    Holds various parameters for each molecular or atomic species.
    '''

    name:                     str
    molar_mass:               float # molecular mass,                   [kg / kmol]
    enthalpy_of_formation:    float # heat of formation at 0K,          [kJ / (kg * K)]
    ground_state_elec_energy: float # ground state electronic energy,   [1 / cm]
    ground_state_degeneracy:  float # ground state degeneracy level,    [-]
    rotational_temp_const:    float # rotational temperature constant,  [K]
    vibrational_temp_const:   float # vibrational temperature constant, [K]

    def specific_gas_constant(self) -> float:
        '''
        Calculates the specific gas constant of the species.

        Returns:
            float: specific gas constant
        '''

        return cn.MLGAS / self.molar_mass

def create_species_list() -> list[Species]:
    '''
    Creates each species based on the user's selection and places them in a list.

    Returns:
        list[Species]: list of species objects
    '''

    species_list = []

    for species in inp.SPECIES_SELECTION:
        try:
            row = species_dataframe.loc[species_dataframe['name'] == species].iloc[0]

            species = Species(
                name                     = row['name'],
                molar_mass               = row['molar_mass'],
                enthalpy_of_formation    = row['enthalpy_of_formation'],
                ground_state_elec_energy = row['ground_state_elec_energy'],
                ground_state_degeneracy  = row['ground_state_degeneracy'],
                rotational_temp_const    = row['rotational_temp_const'],
                vibrational_temp_const   = row['vibrational_temp_const']
            )

            species_list.append(species)

        except IndexError:
            print(f'Improper species selected: {species}')

    return species_list
