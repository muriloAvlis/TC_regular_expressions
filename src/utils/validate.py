import re


def validate(expression: str, input) -> bool:
    # Caso a entrada não for uma string, realiza a conversão
    if not isinstance(input, str):
        input = str(input)
    # compila a regra e atribui a uma variável
    pattern = re.compile(expression)
    # Verifica se a entrada não corresponde a regra da expressão
    if not pattern.match(input):
        return False
    return True
