from utils.validate import validate


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


if __name__ == "__main__":
    # a tests
    lines = f"{10*'-'}A-Family Tests{10*'-'}"
    print(lines)
    mask = Family()
    name_inputs = ["MHmm", "HMhmm", "MHhmhm", "MHm", ""]
    for v in name_inputs:
        r = mask.a(v)
        print(v, "--", r)
    print(len(lines) * "-")
