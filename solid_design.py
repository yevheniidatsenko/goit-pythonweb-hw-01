from abc import ABC, abstractmethod
from typing import List
from colorama import Fore, init

# Initialisation of  colorama
init(autoreset=True)


# SRP principle: Book class for storing information about a book
class Book:
    def __init__(self, title: str, author: str, year: str):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self) -> str:
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"


# The ISP principle: Interface for working with the library
class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book: Book) -> None:
        pass

    @abstractmethod
    def remove_book(self, title: str) -> None:
        pass

    @abstractmethod
    def get_books(self) -> List[Book]:
        pass


# LSP principle: the Library class implements the LibraryInterface interface
class Library(LibraryInterface):
    def __init__(self):
        self._books = []

    def add_book(self, book: Book) -> None:
        self._books.append(book)

    def remove_book(self, title: str) -> None:
        self._books = [book for book in self._books if book.title != title]

    def get_books(self) -> List[Book]:
        return self._books


# The DIP principle: LibraryManager depends on the LibraryInterface interface
class LibraryManager:
    def __init__(self, library: LibraryInterface):
        self.library = library

    def add_book(self, title: str, author: str, year: str) -> None:
        book = Book(title, author, year)
        self.library.add_book(book)
        print(f'{Fore.GREEN}Book "{title}" added successfully.{Fore.RESET}')

    def remove_book(self, title: str) -> None:
        self.library.remove_book(title)
        print(f'{Fore.RED}Book "{title}" removed successfully.{Fore.RESET}')

    def show_books(self) -> None:
        books = self.library.get_books()
        if books:
            print(f"{Fore.YELLOW}Books in the library:{Fore.RESET}")
            for book in books:
                print(f"{Fore.CYAN}{book}{Fore.RESET}")
        else:
            print(f"{Fore.MAGENTA}The library is empty.{Fore.RESET}")


# OCP principle: Library code is extended through composition
class ExtendedLibrary(Library):
    def find_books_by_author(self, author: str) -> List[Book]:
        return [book for book in self._books if book.author == author]


# Main function
def main():
    library = Library()
    manager = LibraryManager(library)

    while True:
        command = (
            input(f"{Fore.BLUE}Enter command (add, remove, show, exit): {Fore.RESET}")
            .strip()
            .lower()
        )

        if command == "add":
            title = input(f"{Fore.CYAN}Enter book title: {Fore.RESET}").strip()
            author = input(f"{Fore.CYAN}Enter book author: {Fore.RESET}").strip()
            year = input(f"{Fore.CYAN}Enter book year: {Fore.RESET}").strip()
            manager.add_book(title, author, year)
        elif command == "remove":
            title = input(
                f"{Fore.CYAN}Enter book title to remove: {Fore.RESET}"
            ).strip()
            manager.remove_book(title)
        elif command == "show":
            manager.show_books()
        elif command == "exit":
            print(f"{Fore.RED}Exiting program...{Fore.RESET}")
            break
        else:
            print(f"{Fore.YELLOW}Invalid command. Please try again.{Fore.RESET}")


if __name__ == "__main__":
    main()
