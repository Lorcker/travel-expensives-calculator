from module.cli import printAccounts, printHeader, printTransactions
from module.models import Account, Transaction


def test_print():
    person1 = Account("Cevin", 60.0)
    person2 = Account("Nils", 70.0)
    person3 = Account("Chris", 200.0)
    person4 = Account("Nora")
    person5 = Account("Jana")
    person6 = Account("Robin")
    accounts = [person1, person2, person3, person4, person5, person6]
    transactions = [
        Transaction(person3, person1, 5.0),
        Transaction(person3, person2, 15.0),
        Transaction(person4, person3, 55.0),
        Transaction(person5, person3, 55.0),
        Transaction(person6, person3, 55.0)
    ]

    printAccounts(accounts=accounts)
    printHeader(accounts=accounts)
    printTransactions(transactions=transactions)
