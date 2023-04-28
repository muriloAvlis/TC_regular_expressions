import logging


class Logger:
    def __init__(self) -> None:
        # Cria o formato do log
        logging.basicConfig(level=logging.NOTSET, format='[%(asctime)s - %(levelname)s] - %(message)s',
                            datefmt='%d/%m/%Y %I:%M:%S %p')
        self.ENDC = '\033[0m'

    def success(self, msg: str) -> None:
        OKGREEN = '\033[92m'
        logging.info(f"{OKGREEN}{msg}{self.ENDC}")

    def warning(self, msg: str) -> None:
        WARNING = '\033[93m'
        logging.warning(f"{WARNING}{msg}{self.ENDC}")

    def fail(self, msg: str) -> None:
        FAIL = '\033[91m'
        logging.error(f"{FAIL}{msg}{self.ENDC}")


if __name__ == "__main__":
    log = Logger()
    log.success("Deu tudo certo!")
    log.warning("Deu + ou -")
    log.fail("Deu tudo errado!")
