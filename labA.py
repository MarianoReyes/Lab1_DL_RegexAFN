"""
Generador de Automatas AFN y AFD a partir de una REGEX
José Mariano Reyes 20074
Andrea Lam 20102
Kenneth Gálvez 20079
"""

from Regex_Postfix import convertExpression
from Postfix_AFN import PostifixToAFN

# main del programa
if __name__ == '__main__':
    # Expresion de prueba: (b|b)*abb(a|b)*
    # Simbolo epsilon  ε
    exp = input("\nIngrese una expresion a convertir: ")

    #exp = "(b|b)*abb(a|b)*"
    print("\nRegex: ", exp)

    conversion = convertExpression(len(exp))

    # llamada de funcion para convertir a postfix
    conversion.RegexToPostfix(exp)

    postfix = conversion.res
    print("\nPostfix: ", postfix)

    # instancia de clase para convertir a AFN
    conversionAFN = PostifixToAFN(postfix)

    # llamada a metodo para convertir afn
    conversionAFN.conversion()
