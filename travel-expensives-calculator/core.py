from models import Account, Transaction


def calculate_total_spendings(group: list[Account]) -> float:
    """Calculate the total spendings of a group.

    Examples:
        >>> calculate_total_spendings([Account("lily", 20.0), Account("james", 22.0)])
        42.0

    Args:
        group: A travel group.

    Returns:
        Total spendings of the group.
    """
    return sum(account.spendings for account in group)


def calculate_debt_per_person(group: list[Account]) -> float:
    """Calculate how much money each person of a group should contribute.

    Examples:
        >>> calculate_debt_per_person([Account("lily", 20.0), Account("james", 22.0)])
        21.0

    Args:
        group: A travel group.

    Returns:
        Debt per person.
    """
    if group == []:
        return 0.0

    return calculate_total_spendings(group=group) / len(group)


def calculate_minimal_transactions(group: list[Account]) -> list[Transaction]:
    """Calculate the transactions that have to made, in order to spread spending amongst a group. Algorithm designates person with most spendings to be the bank. Everybody in debt pays to the bank. Everybody who misses money gets it from the bank.

    Examples:
        >>> calculate_minimal_transactions([Account("lily", 20.0), Account("james", 22.0)])
        [Transaction(src=Account("lily", 20.0), dest=Account("james", 22.0), amount=1.0)]

    Args:
        group: A travel group.

    Returns:
        A List of Transactions that have to be made.
    """
    transactions = []

    no_transactions_necessary = len(group) < 2
    if no_transactions_necessary:
        return transactions

    debt_per_person = calculate_debt_per_person(group=group)
    bank = max(group, key=lambda account: account.spendings)

    for member in group:
        if member == bank:
            continue

        if (member.spendings > debt_per_person):
            transactions.append(Transaction(
                bank, member, member.spendings - debt_per_person))
            continue

        if (member.spendings < debt_per_person):
            transactions.append(Transaction(
                member, bank, debt_per_person - member.spendings))

    return transactions
