from django.core.exceptions import ValidationError


def SoloLetras(palabra, name_camp):
    for x in palabra:
        if not x.isspace():
            cadena = x
    if not cadena.isalpha():
        raise ValidationError('El campo ' + name_camp +
                              ' solo tiene que contener letras.')
    return palabra


def SoloNumeros(value):
    if not value.isdigit():
        raise ValidationError('El campo solo tiene que contener numeros.')
    return value


def Min_lenght(value):
    if len(value) < 10:
        raise ValidationError(
            'Asegúrese de que este valor tenga 10 caracteres')


def vcedula(value):
    # sin ceros a la izquierda
    SoloNumeros(value)
    try:
        nocero = value.strip("0")
        cedula = int(nocero, 0)
        verificador = cedula % 10
        numero = cedula//10

    # mientras tenga números
        suma = 0
        while (numero > 0):

            # posición impar
            posimpar = numero % 10
            numero = numero//10
            posimpar = 2*posimpar
        if (posimpar > 9):
            posimpar = posimpar-9

        # posición par
        pospar = numero % 10
        numero = numero//10

        suma = suma + posimpar + pospar

        decenasup = suma//10 + 1
        calculado = decenasup*10 - suma
        if (calculado >= 10):
            calculado = calculado - 10

        if (calculado == verificador):
            validado = 1
        else:
            raise ValidationError('Numero de cedula incorrecta')
        return (validado)

    except ValueError:
        raise ValidationError('Algo fallo')
