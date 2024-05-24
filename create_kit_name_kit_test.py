

import configuration
import pytest
import requests
import sender_stand_request
import data

# FUNCIÓN PARA PRUEBA POSITIVA
def positive_assert(name):
    kit_response = sender_stand_request.post_new_client_kit(name)
    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == name

# FUNCIÓN PARA PRUEBA NEGATIVA
def negative_assert_code_400(name):
    kit_response = sender_stand_request.post_new_client_kit(name)
    assert kit_response.status_code == 400

# PRUEBA 1 Kit creado con éxito. El parámetro name contiene 1 caracter
def test_one_character_field():
    positive_assert(data.one_character)

# PRUEBA 2 Kit creado con éxito. El parámetro name contiene 511 caracteres.
def test_maximum_character_length():
    positive_assert(data.maximum_character_length)

# PRUEBA 3 Error. El parámetro name contiene 0 carácteres
def test_empty_name_field():
    negative_assert_code_400(data.empty_name)

# PRUEBA 4 El parámetro name contiene 512 carácteres
def test_exceed_max_length_name_field():
    negative_assert_code_400(data.exceed_max_character_length)

# PRUEBA 5 Kit creado con éxito. El parámetro name contiene caracteres especiales
def test_special_characters_name_field ():
    positive_assert(data.special_characters)

# PRUEBA 6 Kit creado con éxito. El parámetro name contiene espacios
def test_spaces_in_name_field ():
    positive_assert(data.space_in_name_field)

# PRUEBA 7 Kit creado con éxito. El parámetro name contiene numeros como string
def test_numbers_in_name_field():
    positive_assert(data.numbers_in_name_field)
# PRUEBA 8 Error. Falta el parámetro name en la solicitud
def test_missing_parameter():
    negative_assert_code_400(data.no_parameter)

# PRUEBA 9 Error. El tipo del parámetro name es Integer
def test_parameter_type_mismatch():
    negative_assert_code_400(data.different_parameter)












