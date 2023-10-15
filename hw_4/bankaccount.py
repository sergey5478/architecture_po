from abc import ABC, abstractmethod


class BankAccount:
    def __init__(self, card, balance):
        self.card = card
        self.balance = balance


class BankAccountRepo(ABC):
    @abstractmethod
    def add_account(self, account):
        pass

    @abstractmethod
    def remove_account(self, card):
        pass

    @abstractmethod
    def get_account(self, card):
        pass


class BankAccountRepository(BankAccountRepo):
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.card] = account

    def remove_account(self, card):
        if card in self.accounts:
            del self.accounts[card]

    def get_account(self, card):
        return self.accounts.get(card, None)
