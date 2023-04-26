import re


def validate(expression: str, input: str) -> bool:
    # compila a regra e atribui a uma variável
    pattern = re.compile(expression)
    # Verifica se a entrada não corresponde a regra da expressão
    if not pattern.match(input):
        return False
    return True
