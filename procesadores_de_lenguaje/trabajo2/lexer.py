import ply.lex as lex

# Lista de nombres de tokens
tokens = [
    'KEYWORD',
    'IDENTIFIER',
    'NUMBER',
    'STRING',
    'ARITHMETIC_OPERATOR',
    'LOGICAL_OPERATOR',
    'COMPARISON_OPERATOR',
    'PARENTHESIS',
    'SEMICOLON',
    'COMMENT_LINE',
    'COMMENT_BLOCK'
]

# Definir palabras clave
keywords = {
    'if': 'KEYWORD',
    'else': 'KEYWORD',
    'while': 'KEYWORD',
    'for': 'KEYWORD',
    'int': 'KEYWORD',
    'float': 'KEYWORD',
    'string': 'KEYWORD'
}

# Definir expresiones regulares para los tokens simples
t_ARITHMETIC_OPERATOR = r'\+|\-|\*|\/|%'
t_LOGICAL_OPERATOR = r'&&|\|\||!'
t_COMPARISON_OPERATOR = r'==|!=|<=|>=|<|>'
t_PARENTHESIS = r'[\(\)\{\}\[\]]'
t_SEMICOLON = r';'
t_ignore = ' \t\n'  # Ignorar espacios en blanco y tabulaciones

# Definir comentarios
def t_COMMENT_BLOCK(t):
    r'/\*.*?\*/'
    pass  # Ignorar comentarios de bloque

def t_COMMENT_LINE(t):
    r'//.*'
    pass  # Ignorar comentarios de una línea

# Definir números (enteros y flotantes)
def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t

# Definir cadenas de texto
def t_STRING(t):
    r'\"([^\\"]|\\.)*\"'
    return t

# Definir identificadores y palabras clave
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = keywords.get(t.value, 'IDENTIFIER')  # Verificar si es una palabra clave
    return t

# Manejo de errores
def t_error(t):
    print(f"Caracter ilegal '{t.value[0]}'")
    t.lexer.skip(1)

# Construir el lexer
lexer = lex.lex()

# Interacción con el usuario
def main():
    print("Bienvenido al analizador léxico interactivo.")
    print("Introduce el código que deseas analizar (o 'salir' para terminar):")

    while True:
        # Solicitar entrada del usuario
        user_input = input(">> ")

        # Si el usuario escribe 'salir', termina el programa
        if user_input.lower() == 'salir':
            print("Saliendo del analizador léxico. ¡Hasta luego!")
            break

        # Alimentar el código ingresado al lexer
        lexer.input(user_input)

        # Tokenizar la entrada y mostrar resultados
        while True:
            tok = lexer.token()
            if not tok:
                break
            print(f"Token encontrado: {tok.type}, Valor: {tok.value}")

# Ejecutar el programa principal
if __name__ == "__main__":
    main()
