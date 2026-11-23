import pytest
from primo import es_primo

def test_menores_a_dos_no_son_primos():
    assert es_primo(-7) is False
    assert es_primo(0) is False
    assert es_primo(1) is False

def test_primos_conocidos():
    for n in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 97]:
        assert es_primo(n) is True

def test_compuestos_conocidos():
    for n in [4, 6, 8, 9, 10, 12, 15, 21, 25, 49, 100]:
        assert es_primo(n) is False

def test_tipos_invalidos_lanzan_type_error():
    for invalido in [5.5, "7", True, False]:
        with pytest.raises(TypeError):
            es_primo(invalido)
