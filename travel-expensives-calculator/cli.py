from enum import Enum

from InquirerPy import inquirer
from InquirerPy.base.control import Choice

from rich import print
from rich.panel import Panel
from rich.table import Table
from rich.columns import Columns

from models import Account, Transaction
from core import calculate_minimal_transactions, calculate_total_spendings, calculate_debt_per_person


class Command(Enum):
    ADD_PERSON = 0
    CALCULATE_TRANSACTIONS = 1
    EXIT = 3


def enter_account() -> Account:
    name = inquirer.text(message="Enter name of the person:").execute()
    spendings = inquirer.number(
        message=f"Enter spendings of {name}:",
        float_allowed=True,
        default=0.0,
        min_allowed=0
    ).execute()
    return Account(name=name, spendings=float(spendings))


def select_command() -> Command:
    return inquirer.select(
        message="Select an action:",
        choices=[
                Choice(value=Command.ADD_PERSON, name="Add person"),
                Choice(value=Command.CALCULATE_TRANSACTIONS,
                       name="Calculate Transactions"),
                Choice(value=Command.EXIT, name="Exit")
        ],
        default="ADD"
    ).execute()


def total_spendings_panel(group: list[Account]) -> Panel:
    return Panel.fit(
        f"[green]{calculate_total_spendings(group=group):.2f}€", title="Total spendings")


def debt_per_person_panel(group: list[Account]) -> Panel:
    return Panel.fit(
        f"[yellow]{calculate_debt_per_person(group=group):.2f}€", title="Debt per person")


def print_input_information(group: list[Account]):
    debtPerPerson = debt_per_person_panel(group)
    total = total_spendings_panel(group)
    print()
    print(Columns([total, debtPerPerson]))


def print_due_transactions(transactions: list[Transaction]):
    table = Table(
        title="[b]Following Transactions have to be made:", leading=1)

    table.add_column("From", style="yellow")
    table.add_column("")
    table.add_column("To", style="blue")
    table.add_column("Amount", style="green")

    for transaction in transactions:
        table.add_row(transaction.source.name, "-->",
                      transaction.destination.name, f"{transaction.amount:.2f}€")

    print()
    print(table)


def print_group(group: list[Account]):
    table = Table(title="[b]All these people had fun together:", leading=1)

    table.add_column("Name", style="yellow")
    table.add_column("Spendings", style="green")

    for member in group:
        table.add_row(
            member.name, f"{member.spendings:.2f}€"
        )

    print()
    print(table)


def main():
    running = True
    accounts = []

    while running:
        match select_command():
            case Command.ADD_PERSON:
                accounts.append(enter_account())

            case Command.CALCULATE_TRANSACTIONS:
                transactions = calculate_minimal_transactions(accounts)
                print_group(group=accounts)
                print_input_information(group=accounts)
                print_due_transactions(transactions=transactions)
                running = False

            case Command.EXIT:
                running = False
