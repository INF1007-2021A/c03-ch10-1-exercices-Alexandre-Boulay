#!/usr/bin/env python
# -*- coding: utf-8 -*-


# TODO: Importez vos modules ici
import numpy as np


# TODO: Définissez vos fonctions ici (il en manque quelques unes)
def linear_values() -> np.ndarray:
    return np.array([np.random.uniform(-1.3, 2.5, 64)])


def coordinate_conversion(cartesian_coordinates: np.ndarray) -> np.ndarray:
    polaire = []

    for i in cartesian_coordinates:
        norme = np.sqrt(i[0]**2 + i[1]**2)
        orientation = np.arctan(i[1] / i[0])
        polaire.append((norme, orientation))

    return np.array(polaire)


def find_closest_index(values: np.ndarray, number: float) -> int:
    return 0


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    print(linear_values())
    print(coordinate_conversion([(3,4), (1,2), (5,1)]))
