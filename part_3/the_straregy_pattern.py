import string
import random
from abc import ABC, abstractmethod
from typing import List


class SupportTicket:
    id: str
    customer: str
    issue: str

    def __init__(self, customer, issue):
        self.id = generate_id()
        self.customer = customer
        self.issue = issue


def generate_id(lenght=8):
    # helper function for generating and id
    return ''.join(random.choices(string.ascii_uppercase, k=lenght))


class TicketOrderingStrategy(ABC):
    @abstractmethod
    def create_ordering(self, list_in: List[SupportTicket]) -> List[SupportTicket]:
        pass


class FIFOOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, list_in: List[SupportTicket]) -> List[SupportTicket]:
        return list_in.copy()


class FILOOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, list_in: List[SupportTicket]) -> List[SupportTicket]:
        list_copy = list_in.copy()
        list_copy.reverse()
        return list_copy


class BlackHoleOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, list_in: List[SupportTicket]) -> List[SupportTicket]:
        return []


class RandomOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, list_in: List[SupportTicket]) -> List[SupportTicket]:
        list_copy = list_in.copy()
        random.shuffle(list_copy)
        return list_copy


class CustomerSupport:

    tickets: List[SupportTicket] = []

    def create_ticket(self, customer, issue):
        self.tickets.append(SupportTicket(customer, issue))

    def process_tickets(self, processing_strategy: TicketOrderingStrategy):

        # create the ordered list
        ticket_list = processing_strategy.create_ordering(self.tickets)

        # if it's empty, don't do anything
        if len(ticket_list) == 0:
            print('There are no tickets to process. Well done!')
            return

        for ticket in ticket_list:
            self.process_ticket(ticket)

    def process_ticket(self, ticket: SupportTicket):
        print('===================================')
        print(f'Processing ticket id: {ticket.id}')
        print(f'Customer: {ticket.customer}')
        print(f'Issue: {ticket.issue}')
        print('====================================')


if __name__ == '__main__':
    # create the application
    app = CustomerSupport()

    # register a few tickets
    app.create_ticket('Jot Smith', 'My computer makes strange sounds!')
    app.create_ticket('Linus Sebastian', 'I can`t upload any videos, please help.')
    app.create_ticket('Arjan Egges', 'VSCode doesn`t automatically solve my bug')

    # process the tickets
    app.process_tickets(BlackHoleOrderingStrategy())
