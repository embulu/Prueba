#NO ELIMINAR LAS SIGUIENTES IMPORTACIONES, sirven para probar tu código en consola, y el funcionamiento del módulo csv respectivamente
from os import read
from pruebas import pruebas_codigo_estudiante
import csv
"""NOTAS: 
    -PARA ESTE RETO PUEDES PROBAR TU PROGRAMA, DANDO CLICK EN LA NAVE ESPACIAL
    -LA CONSOLA TE DARÁ INSTRUCCIONES SI PUEDES EVALUAR O NO TU CÓDIGO
"""

"""Inicio espacio para programar funciones propias"""
#En este espacio podrás programar las funciones que deseas usar en la función solución (ES OPCIONAL)

"""Fin espacio para programar funciones propias"""

def solucion():
    #ESTA ES LA FUNCIÓN A LA QUE LE DEBES GARANTIZAR LOS RETORNOS REQUERIDOS EN EL ENUNCIADO.
    with open('TSLA.csv') as tesla:
        with open ('analisis_archivo.csv', 'w', newline= '' ) as solut:
            reader_tesla = csv.reader(tesla)
            writer_solucion= csv.writer(solut, delimiter = '\t')
            data_solucion = [['Fecha', 'Concepto']]
            
            for i, renglon_tesla in enumerate(reader_tesla):
                if i == 0:
                    continue
                elif i == 1:
                    date_lowest = renglon_tesla[0]
                    lowest_value = float(renglon_tesla[3])
                    
                    date_highest = renglon_tesla[0]
                    highest_value = float(renglon_tesla[2])
                    
                if lowest_value > float(renglon_tesla[3]):
                    date_lowest = renglon_tesla[0]
                    lowest_value = float(renglon_tesla[3])
                    
                if highest_value < float(renglon_tesla[2]):
                    date_highest = renglon_tesla[0]
                    highest_value = float(renglon_tesla[2])
                    
                lista_aux = [renglon_tesla[0]]
                
                if float(renglon_tesla[4]) < 200:
                    lista_aux.append('MUY BAJO')
                    
                elif 200 <=  float(renglon_tesla[4]) < 300: 
                    lista_aux.append('BAJO') 
                    
                elif 300 <= float(renglon_tesla[4]) < 500:
                    lista_aux.append('MEDIO') 
                
                elif 500 <= float(renglon_tesla[4]) < 600:
                    lista_aux.append('ALTO') 
                    
                elif 600 <= float(renglon_tesla[4]):
                    lista_aux.append('MUY ALTO') 
                    
                data_solucion.append(lista_aux)
                
            writer_solucion.writerows(data_solucion)
                
    
    
    return date_lowest, lowest_value, date_highest, highest_value

"""
NO COLOCAR CÓDIGO FUERA DE LAS FUNCIONES QUE USTED CREE
Esta línea de código que sigue permite saber si su solución al ejercicio es correcto
Por favor NO ELIMINARLA, NO MODIFICARLA
"""
pruebas_codigo_estudiante(solucion)