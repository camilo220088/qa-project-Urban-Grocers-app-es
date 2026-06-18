import data
import sender_stand_request

def positive_assert(kit_body):
    token = sender_stand_request.get_new_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, token)
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]

def negative_assert_code_400(kit_body):
    token = sender_stand_request.get_new_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, token)
    assert response.status_code == 400

def test_1_un_caracter():
    positive_assert(data.get_kit_body("a"))

def test_2_quinientos_once_caracteres():
    positive_assert(data.get_kit_body("a" * 511))

def test_3_cero_caracteres():
    negative_assert_code_400(data.get_kit_body(""))

def test_4_quinientos_doce_caracteres():
    negative_assert_code_400(data.get_kit_body("a" * 512))

def test_5_caracteres_especiales():
    positive_assert(data.get_kit_body('"№%@","'))

def test_6_espacios_permitidos():
    positive_assert(data.get_kit_body(" A Aaa "))

def test_7_numeros_permitidos():
    positive_assert(data.get_kit_body("123"))

def test_8_parametro_no_pasado():
    negative_assert_code_400({})

def test_9_tipo_dato_incorrecto():
    negative_assert_code_400(data.get_kit_body(123))