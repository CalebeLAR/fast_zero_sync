from fastapi.testclient import TestClient

from exercicios.a02_ex01 import app

client = TestClient(app)


def test_root_deve_retornar_ok_e_um_html_com_ola_mundo():
    # arrange
    client = TestClient(app)

    # act
    response = client.get('/')
    # assert
    assert '<h1>Ola Mundo</h1>' in response.text
