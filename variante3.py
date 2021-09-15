#NO ELIMINAR LAS SIGUIENTES IMPORTACIONES, sirven para probar tu código en consola, y el funcionamiento de la clase cliente
from pruebas import pruebas_codigo_estudiante
from cliente import cliente
"""NOTAS: 
    -PARA ESTE RETO PUEDES PROBAR TU PROGRAMA, DANDO CLICK EN LA NAVE ESPACIAL
    -LA CONSOLA TE DARÁ INSTRUCCIONES SI PUEDES EVALUAR O NO TU CÓDIGO
"""

"""Inicio espacio para programar funciones propias"""
#En este espacio podrás programar las funciones que deseas usar en la función solución (ES OPCIONAL

"""Fin espacio para programar funciones propias"""

def sede_bancaria(cola_general):
    #ESTA ES LA FUNCIÓN A LA QUE LE DEBES GARANTIZAR LOS RETORNOS REQUERIDOS EN EL ENUNCIADO.
    cola_caja= []
    cola_info=[]
    suma_retiros=0  
    suma_consignaciones=0 
    edad_minima_retiro=-1
    edad_minima_info=-1
    edad_minima_consignacion = -1
    
    for i in cola_general:
        custoumer = i
        
        if custoumer.fila_interes =="caja":
            cola_caja.append(custoumer.nombre)
            
            if custoumer.transaccion == 'retirar':
                suma_retiros = suma_retiros+ custoumer.cantidad_retirar
                if edad_minima_retiro==-1:
                    edad_minima_retiro = custoumer.edad
                else:
                    if custoumer.edad < edad_minima_retiro:
                        edad_minima_retiro = custoumer.edad
            else:
                if custoumer.transaccion == 'consignar':
                    suma_consignaciones += custoumer.cantidad_consignar
                    if edad_minima_consignacion == -1:
                        edad_minima_consignacion = custoumer.edad  
                    else:
                        if custoumer.edad < edad_minima_consignacion:
                            edad_minima_consignacion = custoumer.edad
            
        else:
            cola_info.append(custoumer.nombre)
            
            if  edad_minima_info == -1:
                edad_minima_info = custoumer.edad
            elif custoumer.edad <  edad_minima_info:
                 edad_minima_info = custoumer.edad
                              
    
    return cola_caja, cola_info, suma_retiros, suma_consignaciones, edad_minima_retiro, edad_minima_info, edad_minima_consignacion

"""
NO PEDIR DATOS CON LA FUNCIÓN input(), NO COLOCAR CÓDIGO FUERA DE LAS FUNCIONES QUE USTED CREE
Esta línea de código que sigue, permite probar si su ejercicio es correcto
Por favor NO ELIMINARLA, NO MODIFICARLA
"""
pruebas_codigo_estudiante(sede_bancaria)