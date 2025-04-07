def check_vowels():
    # Código a implementar utilizando input.
    name = input('Ingrese un nombre:')

    print('Contiene a: ' + ('True' if 'a' in name or 'A' in name else 'False'))
    print('Contiene e: ' + ('True' if 'e' in name or 'E' in name else 'False'))
    print('Contiene i: ' + ('True' if 'i' in name or 'I' in name else 'False'))
    print('Contiene o: ' + ('True' if 'o' in name or 'O' in name else 'False'))
    print('Contiene u: ' + ('True' if 'u' in name or 'U' in name else 'False'))


# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_in_string_test.py` o `python tp3_in_string_test.py`
