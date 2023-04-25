import re

class Validate():
    def __init__(self) -> None:
        pass

    def first_mid_last_name(self, input:str) -> bool:
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

    def email(self, input:str) -> bool:
        """
        Função que verifica se a string de entrada corresponde a expressão
        regular com as regras {somename@somedomain(.com.br|.br)}, retornando
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
    
    def passwd(self, input:str) -> bool:
        # define as regras da expressão regular
        expression = r"^(([a-z]*)([A-Z]+)([0-9]+)){8}$"
        # compila a regra e atribui a uma variável
        pattern = re.compile(expression)
        # Verifica se a entrada não corresponde a regra da expressão
        if not pattern.match(input):
            return False
        return True 

if __name__ == "__main__":
    # Name tests
    print(f"{10*'-'}Name Tests{10*'-'}")
    mask = Validate()
    name_inputs = ["Ada Lovelace", "1Alan", "Alan Turing", "Alan", "Stephen Cole Kleene", "A1an", "A1an Turing", "Alan turing", "Yoshi Sauro"]
    for v in name_inputs:
        r = mask.first_mid_last_name(v)
        print(v, "--", r)
    print(f"{30*'-'}\n")
    
    # Email tests
    print(f"{10*'-'}Email Tests{10*'-'}")
    email_inputs = ["a@a.br", "divulga@ufpa.br", "a@a.com.br", "@", "a@.br", "@a.br", "T@teste.br", "a@A.com.br", "sauros@com.br"]
    for v in email_inputs:
      r = mask.email(v)
      print(v, "--", r)
    print(f"{30*'-'}")

    # passwords tests
    print(f"{10*'-'}Password Tests{10*'-'}")
    passwd_inputs = ["a@a.br", "divulga@ufpa.br", "a@a.com.br", "@", "a@.br", "@a.br", "T@teste.br", "a@A.com.br", "sauros@com.br"]
    for v in passwd_inputs:
      r = mask.email(v)
      print(v, "--", r)
    print(f"{30*'-'}")