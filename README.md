# Laboratorio A

Programa encargado de implementar la conversión de una expresión Regex a AFN pasando por postfix de primero. La ejecución se realiza con el comando

- python labA.py

## Clases

- Regex a Postfix
- Postfix a AFN

## Gramaticas Soportadas

- r = (a)
- r = ab
- r = a|b
- r = a\*
- r = a+
- r = a?
- r = ϵ

## Observaciones

Es necesario tener graphviz instalado en la computadora y agregado al PATH en las variables de entorno. Para obviar la implementación gráfica remover la linea 235 del archivo Postfix_AFN.py

- self.graficar() # imagen del AFN
