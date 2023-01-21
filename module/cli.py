from InquirerPy import inquirer
from InquirerPy.base.control import Choice

from rich import print
from rich.panel import Panel
from rich.table import Table
from rich.columns import Columns

from models import Account, Transaction
from core import calculate_minimal_transactions, calculate_total_spendings, calculate_debt_per_person


def enterAccount():
    name = inquirer.text(message="Enter name of the person:").execute()
    spendings = inquirer.number(
        message=f"Enter spendings of {name}:",
        float_allowed=True,
        default=0.0,
        min_allowed=0
    ).execute()
    return Account(name=name, spendings=float(spendings))


def selectAction():
    return inquirer.select(
        message="Select an action:",
        choices=[
                Choice(value="ADD", name="Add person"),
                Choice(value="CALC", name="Calculate Transactions"),
                Choice(value=None, name="Exit")
        ],
        default="ADD"
    ).execute()


def totalPanel(accounts: list[Account]) -> Panel:
    return Panel.fit(
        f"[green]{calculate_total_spendings(accounts=accounts):.2f}€", title="Total spendings")


def debtPerPersonPanel(accounts: list[Account]) -> Panel:
    return Panel.fit(
        f"[yellow]{calculate_debt_per_person(accounts=accounts):.2f}€", title="Debt per person")


def printHeader(accounts: list[Account]):
    debtPerPerson = debtPerPersonPanel(accounts)
    total = totalPanel(accounts)
    print()
    print(Columns([total, debtPerPerson]))


def printTransactions(transactions: list[Transaction]):
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


def printAccounts(accounts: list[Account]):
    table = Table(title="[b]All these people had fun together:", leading=1)

    table.add_column("Name", style="yellow")
    table.add_column("Spendings", style="green")

    for account in accounts:
        table.add_row(
            account.name, f"{account.spendings:.2f}€")

    print()
    print(table)


def main():
    running = True
    accounts = []

    while running:
        match selectAction():
            case "ADD":
                accounts.append(enterAccount())
            case "CALC":
                printAccounts(accounts=accounts)
                printHeader(accounts=accounts)

                transactions = calculate_minimal_transactions(accounts)
                printTransactions(transactions=transactions)
                running = False
            case other:
                running = False
