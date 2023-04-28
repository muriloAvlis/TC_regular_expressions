class Family():
    def a(self, input) -> bool:
        """
        Função que verifica se a string de entrada corresponde
        a expressão regular com as regras {(HM or MH)((m{2,} or h{1,}) or (h{2,} and m{1,}))},
        retornando True caso corresponda ou False caso não corresponda.

        Parameters:
            input (str): uma string que representa a estrutura familiar
        Returns:
            bool: Binário que representa a validação ou não da entrada
        """
        # define as regras da expressão regular
        expression = r"^(?=.*m.*m|.*h|.*h.*h.*m)(HM|MH)[hm]+$"
        # chama função de validação da entrada com a expressão
        result = validate(expression, input)
        # retorna o resultado da validação (true ou false)
        return result

    def b(self, input) -> bool:
        """
        Função que verifica se a string de entrada corresponde
        a expressão regular com as regras {(HM or MH)(m(impar)h*)},
        retornando True caso corresponda ou False caso não corresponda.

        Parameters:
            input (str): uma string que representa a estrutura familiar
        Returns:
            bool: Binário que representa a validação ou não da entrada
        """
        # define as regras da expressão regular
        expression = r"^(?:[^m]*m[^m]m)(HM|MH)(?:[hm]m){1,2}[hm]$"
        # chama função de validação da entrada com a expressão
        result = validate(expression, input)
        # retorna o resultado da validação (true ou false)
        return result

    def c(self, input) -> bool:
        """
        Parameters:
            input(str): uma string que representa a estrutura familiar
        Returns:
            bool: Binário que representa a validação ou não da entrada
        """
        # define as regras da expressão regular
        expression = r"^(HM|MH)m[hm]*h$"
        # chama função de validação da entrada com a expressão
        result = validate(expression, input)
        # retorna o resultado da validação (true ou false)
        return result

    def d(self, input) -> bool:
        """
        Parameters:
            input(str): uma string que representa a estrutura familiar
        Returns:
            bool: Binário que representa a validação ou não da entrada
        """
        # define as regras da expressão regular
        expression = r"^(MM|HH)(hm|mh)[hm]{2,}(hm|mh)$"
        # chama função de validação da entrada com a expressão
        result = validate(expression, input)
        # retorna o resultado da validação (true ou false)
        return result

    def e(self, input) -> bool:
        """
        Parameters:
            input(str): uma string que representa a estrutura familiar
        Returns:
            bool: Binário que representa a validação ou não da entrada
        """
        # define as regras da expressão regular
        expression = r"^(?!.*mm)(?!.*hh)(MM|HH)[hm]+$"
        # chama função de validação da entrada com a expressão
        result = validate(expression, input)
        # retorna o resultado da validação (true ou false)
        return result

    def f(self, input) -> bool:
        """
        Parameters:
            input(str): uma string que representa a estrutura familiar
        Returns:
            bool: Binário que representa a validação ou não da entrada
        """
        # define as regras da expressão regular
        expression = r"^(?!.*hh)(MM|HH)[hm]*$"
        # chama função de validação da entrada com a expressão
        result = validate(expression, input)
        # retorna o resultado da validação (true ou false)
        return result

    def g(self, input, x, y) -> bool:
        """
        Parameters:
            input(str): uma string que representa a estrutura familiar
        Returns:
            bool: Binário que representa a validação ou não da entrada
        """
        # define as regras da expressão regular
        expression = f"^(?![MH]*hhh)[HM]{{{x},{y}}}[hm]*$"
        # chama função de validação da entrada com a expressão
        result = validate(expression, input)
        # retorna o resultado da validação (true ou false)
        return result


if __name__ == "__main__":
    from utils.validate import validate
    # a tests
    lines = f"{10*'-'}A-Family Tests{10*'-'}"
    print(lines)
    family_structure = Family()
    inputs = ["MHmm", "HMhmm", "MHhmhm", "MHm", "MHh", "HM", "MH"]
    for v in inputs:
        r = family_structure.a(v)
        print(v, "--", r)
    print(len(lines) * "-")

    # b tests (TODO)
    lines = f"{10*'-'}B-Family Tests{10*'-'}"
    print(lines)
    family_structure = Family()
    inputs = ["MHh", "HMm", "MHmmm", "MHhmhmhm",
              "MHmm", "MHmhmhm", "HM", "MHhhmhhh"]
    for v in inputs:
        r = family_structure.b(v)
        print(v, "--", r)
    print(len(lines) * "-")

    # # c tests
    # lines = f"{10*'-'}C-Family Tests{10*'-'}"
    # print(lines)
    # family_structure = Family()
    # inputs = ["MHh", "HMm", "HMmh", "HMmmmh", "HMmhmhmh", "MHmhhhm", "HM"]
    # for v in inputs:
    #     r = family_structure.c(v)
    #     print(v, "--", r)
    # print(len(lines) * "-")

    # # d tests
    # lines = f"{10*'-'}D-Family Tests{10*'-'}"
    # print(lines)
    # family_structure = Family()
    # inputs = ["MMhmmmmh", "HHmhhhhm", "MMmh",
    #           "HHmhhhm", "MMhmhhhh", "MMhmhmhmhmhmmh"]
    # for v in inputs:
    #     r = family_structure.d(v)
    #     print(v, "--", r)
    # print(len(lines) * "-")

    # # e tests
    # lines = f"{10*'-'}E-Family Tests{10*'-'}"
    # print(lines)
    # family_structure = Family()
    # inputs = ["MMhmhmhm", "HHmhmhm", "MMhmmh",
    #           "HHmmhmh", "MMhm"]
    # for v in inputs:
    #     r = family_structure.e(v)
    #     print(v, "--", r)
    # print(len(lines) * "-")

    # # f tests
    # lines = f"{10*'-'}F-Family Tests{10*'-'}"
    # print(lines)
    # family_structure = Family()
    # inputs = ["MM", "HH", "MMmhmhh",
    #           "HHhmhm", "MMmmhhm", "MMhmmh"]
    # for v in inputs:
    #     r = family_structure.f(v)
    #     print(v, "--", r)
    # print(len(lines) * "-")

    # # g tests
    # lines = f"{10*'-'}G-Family Tests{10*'-'}"
    # print(lines)
    # family_structure = Family()
    # # limites do arranjo
    # x, y = 2, 4
    # inputs = ["M", "HH", "MMMm",
    #           "MHhhhm", "MHHMmhhh", "MMmhhhm"]
    # for v in inputs:
    #     r = family_structure.g(v, x, y)
    #     print(v, "--", r)
    # print(len(lines) * "-")
else:
    from src.utils.validate import validate