from abc import ABC, abstractmethod

# Умеют печатать
class Printable(ABC):
    @abstractmethod
    def print(self, text: str) -> None:
        pass

# Умеют сканировать
class Scannable(ABC):
    @abstractmethod
    def scan(self) -> str:
        pass

# Умеют отправлять факс
class Faxable(ABC):
    @abstractmethod
    def fax(self, number: str) -> None:
        pass

# Умеют копировать
class Copiable(ABC):
    @abstractmethod
    def copy(self) -> None:
        pass

# Только печатает
class SimplePrinter(Printable):
    def print(self, text: str) -> None:
        print(text)

# Умеет все
class MultiFunctionPrinter(Printable, Scannable, Faxable, Copiable):
    def print(self, text: str) -> None:
        print(f"Printing: {text}")

    def scan(self) -> str:
        return "Scanned document content"

    def fax(self, number: str) -> None:
        print(f"Sending fax to {number}")

    def copy(self) -> None:
        print("Making a copy")

# Зависит только от Printable
def print_document(printer: Printable, text: str) -> None:
    printer.print(text)