from abc import ABC, abstractmethod


class Ticket:
    def __init__(self, ticket_id, price, place, datetime, is_valid):
        self.ticket_id = ticket_id
        self.price = price
        self.place = place
        self.datetime = datetime
        self.is_valid = is_valid


class TicketRepo(ABC):
    @abstractmethod
    def add_ticket(self, ticket):
        pass

    @abstractmethod
    def remove_ticket(self, ticket_id):
        pass

    @abstractmethod
    def get_ticket(self, ticket_id):
        pass


class TicketRepository(TicketRepo):
    def __init__(self):
        self.tickets = {}

    def add_ticket(self, ticket):
        self.tickets[ticket.ticket_id] = ticket

    def remove_ticket(self, ticket_id):
        if ticket_id in self.tickets:
            del self.tickets[ticket_id]

    def get_ticket(self, ticket_id):
        return self.tickets.get(ticket_id, None)
