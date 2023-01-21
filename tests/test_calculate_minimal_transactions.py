from pytest_unordered import unordered

from module.core import calculate_minimal_transactions
from module.models import Transaction, Account


def test_one_person():
    person = Account("Cevin", 60.0)
    expexted = []

    actual = calculate_minimal_transactions([person])

    assert actual == expexted


def test_two_persons_with_spendings():
    person1 = Account("Cevin", 60.0)
    person2 = Account("Nils", 70.0)
    expected = [Transaction(person1, person2, 5.0)]

    actual = calculate_minimal_transactions([person1, person2])

    assert actual == unordered(expected)


def test_two_persons_with_without_spendings():
    person1 = Account("Cevin", 0.0)
    person2 = Account("Nils", 70.0)
    expected = [Transaction(person1, person2, 35.0)]

    actual = calculate_minimal_transactions([person1, person2])

    assert actual == unordered(expected)


def test_multiple_persons_mixed_spendings():
    person1 = Account("Cevin", 60.0)
    person2 = Account("Nils", 70.0)
    person3 = Account("Chris", 200.0)
    person4 = Account("Nora")
    person5 = Account("Jana")
    person6 = Account("Robin")
    accounts = [person1, person2, person3, person4, person5, person6]
    expected = [
        Transaction(person3, person1, 5.0),
        Transaction(person3, person2, 15.0),
        Transaction(person4, person3, 55.0),
        Transaction(person5, person3, 55.0),
        Transaction(person6, person3, 55.0)
    ]

    actual = calculate_minimal_transactions(accounts=accounts)

    assert actual == unordered(expected)
