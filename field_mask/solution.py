import re
from utils.validate import validate


class Mask():
    def __init__(self) -> None:
        pass

    def first_mid_last_name(self, input: str) -> bool:
        """
        Função que verifica se a string de entrada corresponde
        a expressão regular com as regras {Nome Nome_do_meio Sobrenome},
        retornando True caso corresponda ou False caso não corresponda.

        Parameters:
            input (str): uma string que representa o nome de entrada
        Returns:
            bool: Binário que representa a validação ou não do nome de entrada
        """
        # define as regras da expressão regular
        expression = r"^([A-Z][a-z]+)(\s[A-Z][a-z]+)?\s([A-Z][a-z]+)$"
        # compila a regra e atribui a uma variável
        pattern = re.compile(expression)
        # Verifica se a entrada não corresponde a regra da expressão
        if not pattern.match(input):
            return False
        return True

    def email(self, input: str) -> bool:
        """
        Função que verifica se a string de entrada corresponde a expressão
        regular com as regras {somename@somedomain(.com.br or .br)}, retornando
        True caso corresponda ou False caso não corresponda.

        Parameters:
            input (str): uma string que representa o email de entrada
        Returns:
            bool: Binário que representa a validação ou não do email de entrada
        """
        # define as regras da expressão regular
        expression = r"^([a-z]+)@([a-z]+)\.(com\.br|br)$"
        # compila a regra e atribui a uma variável
        pattern = re.compile(expression)
        # Verifica se a entrada não corresponde a regra da expressão
        if not pattern.match(input):
            return False
        return True

    def passwd(self, input: str) -> bool:
        """
        Função que verifica se a string de entrada corresponde a expressão
        regular com as regras {a-z or (A-Z and 0-9)} | len(8), retornando
        True caso corresponda ou False caso não corresponda.

        Parameters:
            input (str): uma string que representa a senha de entrada
        Returns:
            bool: Binário que representa a validação ou não da senha de entrada
        """
        # define as regras da expressão regular
        expression = r"^(?=.*[A-Z])(?=.*[0-9])[a-zA-Z0-9]{8}$"
        # compila a regra e atribui a uma variável
        pattern = re.compile(expression)
        # Verifica se a entrada não corresponde a regra da expressão
        if not pattern.match(input):
            return False
        return True

    def cpf(self, input: str) -> bool:
        """
        Parameters:
            input (str): uma string que representa o CPF
        Returns:
            bool: Binário que representa a validação ou não da senha
        """
        # define as regras da expressão regular
        expression = r"^[0-9]{3}\.[0-9]{3}\.[0-9]{3}\-[0-9]{2}$"
        # compila a regra e atribui a uma variável
        pattern = re.compile(expression)
        # Verifica se a entrada não corresponde a regra da expressão
        if not pattern.match(input):
            return False
        return True

    def telephone(self, input: str) -> bool:
        """
        Parameters:
            input (str): uma string que representa o telefone
        Returns:
            bool: Binário que representa a validação ou não da senha
        """
        # define as regras da expressão regular
        expression = r"^(\([0-9]{2}\)\s9[0-9]{4}\-?[0-9]{4}|[0-9]{2}\s9[0-9]{8})$"
        # compila a regra e atribui a uma variável
        pattern = re.compile(expression)
        # Verifica se a entrada não corresponde a regra da expressão
        if not pattern.match(input):
            return False
        return True

    def date_time(self, input: str) -> bool:
        """
        Parameters:
            input (str): uma string que representa a data e hora
        Returns:
            bool: Binário que representa a validação ou não do número
        """
        # define as regras da expressão regular
        expression = r"^[0-9]{2}\/[0-9]{2}\/[0-9]{4}\s[0-9]{2}\:[0-9]{2}\:[0-9]{2}$"
        result = validate(expression, input)
        return result

    def real_number(self, input: str) -> bool:
        """
        Parameters:
            input (str): uma string que representa o número real com ou sem sinal
        Returns:
            bool: Binário que representa a validação ou não do número
        """
        # define a expressão regular
        expression = r"^[+-]?[0-9]+(\.[0-9]+)?$"
        result = validate(expression, input)
        return result


if __name__ == "__main__":
    # Name tests
    print(f"{10*'-'}Name Tests{10*'-'}")
    mask = Mask()
    name_inputs = ["Ada Lovelace", "1Alan", "Alan Turing", "Alan",
                   "Stephen Cole Kleene", "A1an", "A1an Turing", "Alan turing", "Yoshi Sauro"]
    for v in name_inputs:
        r = mask.first_mid_last_name(v)
        print(v, "--", r)
    print(f"{30*'-'}\n")

    # Email tests
    print(f"{10*'-'}Email Tests{10*'-'}")
    email_inputs = ["a@a.br", "divulga@ufpa.br", "a@a.com.br", "@",
                    "a@.br", "@a.br", "T@teste.br", "a@A.com.br", "sauros@com.br"]
    for v in email_inputs:
        r = mask.email(v)
        print(v, "--", r)
    print(f"{31*'-'}\n")

    # passwords tests
    print(f"{10*'-'}Password Tests{10*'-'}")
    passwd_inputs = ["518R2r5e", "F123456A", "1234567T", "ropsSoq0",
                     "F1234567A", "abcdefgH", "1234567HI"]
    for v in passwd_inputs:
        r = mask.passwd(v)
        print(v, "--", r)
    print(f"{34*'-'}\n")

    # CPF tests
    print(f"{10*'-'}CPF Tests{10*'-'}")
    cpf_inputs = ["04199988844", "041.999.244-32", "123.456.789-09", "000.000.000-00",
                  "123.456.789-0", "111.111.11-11"]
    for v in cpf_inputs:
        r = mask.cpf(v)
        print(v, "--", r)
    print(f"{33*'-'}\n")

    # Telephone tests
    print(f"{10*'-'}Telephone Tests{10*'-'}")
    telephone_inputs = ["(91) 99999-9999", "(91) 999999999",
                        "91 999999999", "(91) 59999-9999", "99 99999-9999", "(94)95555-5555"]
    for v in telephone_inputs:
        r = mask.telephone(v)
        print(v, "--", r)
    print(f"{35*'-'}\n")

    # Datetime tests
    print(f"{10*'-'}Datetime Tests{10*'-'}")
    inputs = ["31/08/2019 20:14:55", "99/99/9999 23:59:59",
              "99/99/9999 3:9:9", "9/9/99 99:99:99", "99/99/999903:09:09"]
    for v in inputs:
        r = mask.date_time(v)
        print(v, "--", r)
    print(f"{34*'-'}\n")

    # Real numbers tests
    print(f"{10*'-'}Real Numbers Tests{10*'-'}")
    inputs = ["-25.467", "1", "-1", "+1", "64.2", "1.", "2.", "+64,2"]
    for v in inputs:
        r = mask.real_number(v)
        print(v, "--", r)
    print(f"{38*'-'}")
