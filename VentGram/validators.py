from django.core.exceptions import ValidationError
from django import forms

def NumerosYLetras(usuario):
    if usuario.isalnum():
        if usuario.isdigit():
            raise forms.ValidationError('En el campo Nombre de Usuario debe ingresar solo numeros y letras sin ningun espacio.')
    else:
         raise forms.ValidationError('En el campo Nombre de Usuario debe ingresar solo numeros y letras sin ningun espacio.')
    return usuario


def SoloLetras(palabra, name_camp):
    if palabra:
        for x in palabra:
            if not x.isspace():
                cadena = x
        if not cadena.isalpha():
            raise ValidationError('El campo ' + name_camp +' solo tiene que contener letras.')
    return palabra

def SoloNumeros(value):
    if not value.isdigit():
        raise ValidationError('El campo solo tiene que contener numeros.')
    return value


def Min_lenght(value):
    if len(value) < 10:
        raise ValidationError(
            'Asegúrese de que este valor tenga 10 caracteres')

def dividirCadena(cadena, separador, numeroCaracteres):
    cifra = ""
    contador = 0
    for numero in cadena[::-1]:
        if contador == numeroCaracteres:
            cifra += separador
            contador = 0
            
        contador += 1
        cifra += numero

    return (cifra)

def vcedula(value):
    # sin ceros a la izquierda
    SoloNumeros(value)
    cont=0
    cedula=""
    suma=0
    validador=0
    try:
        for digit in value:
            cedula+=digit
            cont=cont+1
            if cont==2:
                pro=int(cedula)
                if not(pro > 0 and pro <= 24):
                    raise ValidationError('Error provincia')

            if cont==3:
                indi=int(digit)
                if not indi<6:
                    raise ValidationError('Error digito 3 ')
            if cont<10: 
                if cont%2==0 :
                    mult=int(digit)*1
                else:
                    mult=int(digit)*2      
                
                if mult>=10:
                    mult=mult-9
                suma+=mult
                
            if cont==10:
                while suma%10 != 0:
                    suma+=1
                    validador+=1
                    
                if validador!=int(digit):
                    raise ValidationError('Cedula Incorrecta')
    except ValueError:
        raise ValidationError('Algo fallo')
