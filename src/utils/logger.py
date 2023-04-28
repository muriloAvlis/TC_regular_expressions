import logging


class Logger:
    """
    Classe utilizada para imprimir os logs da aplicação via CLI
    """

    def __init__(self) -> None:
        # Cria o formato do log
        logging.basicConfig(level=logging.NOTSET, format='[%(asctime)s - %(levelname)s] - %(message)s',
                            datefmt='%d/%m/%Y %I:%M:%S %p')
        self.ENDC = '\033[0m'  # fechamento de cor

    def success(self, msg: str) -> None:
        OKGREEN = '\033[92m'  # abertura da cor verde
        logging.info(f"{OKGREEN}{msg}{self.ENDC}")

    def warning(self, msg: str) -> None:
        WARNING = '\033[93m'  # abertura da cor amarela
        logging.warning(f"{WARNING}{msg}{self.ENDC}")

    def fail(self, msg: str) -> None:
        FAIL = '\033[91m'  # abertura da cor vermelha
        logging.error(f"{FAIL}{msg}{self.ENDC}")


if __name__ == "__main__":
    # testes
    log = Logger()
    log.success("Deu tudo certo!")
    log.warning("Deu + ou -")
    log.fail("Deu tudo errado!")
