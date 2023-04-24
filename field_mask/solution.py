import re

class Validate():
    def __init__(self) -> None:
        pass

    def first_mid_last_name(self, input:str) -> bool:
        """
        Função que verifica se a string de entrada corresponde a
        regra da expressão regular {Nome Nome_do_meio Sobrenome},
        retornando True caso corresponda ou False caso não corresponda.

        Parameters:
            input (str): uma string que representa o nome de entrada
        Returns:
            bool: Binário que representa a validação ou não da string de entrada
        """
        # define a regra da expressão regular
        expression = r"^[A-Z][a-z]+(\s[A-Z][a-z]+)?\s[A-Z][a-z]+$"
        # compila a regra e atribui a uma variável
        pattern = re.compile(expression)
        # Verifica se a entrada não corresponde a regra da expressão
        if pattern.match(input) == None:
            return False
        return True        

    def email(self, input:str) -> bool:
        pass

if __name__ == "__main__":
    # Name tests
    mask = Validate()
    name_inputs = ["Yoshi Sauro", "Yoshi silva Sauro", "Ada Lovel@ce", "Alan Turing", "A1an # Turing", "Alan Mathison Turing"]
    for v in name_inputs:
        r = mask.first_mid_last_name(v)
        print(r)

    # Email tests
    