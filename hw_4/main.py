import hashlib
from user import User, UserRepository
from ticket import Ticket, TicketRepository
from datetime import datetime
from carrier import Carrier, CarrierRepository
from bankaccount import BankAccount, BankAccountRepository

if __name__ == "__main__":
    user_repo = UserRepository()
    user1 = User(1, "john_doe", "mysecretpassword", "1234 5678 9012 3456")
    user2 = User(2, "jane_doe", "anotherpassword", "9876 5432 1098 7654")
    user_repo.add_user(user1)
    user_repo.add_user(user2)
    print(user_repo.get_user(1).username)
    user_repo.remove_user(2)
    print(user_repo.get_user(2))

    ticket_repo = TicketRepository()
    ticket1 = Ticket(1, 10, "A1", datetime(2023, 10, 15, 12, 30), True)
    ticket2 = Ticket(2, 20, "B2", datetime(2023, 10, 16, 15, 45), True)
    ticket_repo.add_ticket(ticket1)
    ticket_repo.add_ticket(ticket2)
    print(ticket_repo.get_ticket(1).place)
    ticket_repo.remove_ticket(2)
    print(ticket_repo.get_ticket(2))

    carrier_repo = CarrierRepository()
    carrier1 = Carrier(1, 100, "1234 5678 9012 3456")
    carrier2 = Carrier(2, 50, "9876 5432 1098 7654")
    carrier_repo.add_carrier(carrier1)
    carrier_repo.add_carrier(carrier2)
    print(carrier_repo.get_carrier(1).card_number)
    carrier_repo.remove_carrier(2)
    print(carrier_repo.get_carrier(2))

    bank_account_repo = BankAccountRepository()
    account1 = BankAccount("1234 5678 9012 3456", 1000)
    account2 = BankAccount("9876 5432 1098 7654", 500)
    bank_account_repo.add_account(account1)
    bank_account_repo.add_account(account2)
    print(bank_account_repo.get_account("1234 5678 9012 3456").balance)  # Output: 1000
    bank_account_repo.remove_account("9876 5432 1098 7654")
