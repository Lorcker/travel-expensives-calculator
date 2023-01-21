from models import Account, Transaction


def calculate_total_spendings(accounts: list[Account]) -> float:
    return sum(account.spendings for account in accounts)


def calculate_debt_per_person(accounts: list[Account]) -> float:
    return calculate_total_spendings(accounts=accounts) / len(accounts)


def calculate_minimal_transactions(accounts: list[Account]) -> list[Transaction]:
    debt_per_person = calculate_debt_per_person(accounts=accounts)
    bank = max(accounts, key=lambda account: account.spendings)
    accounts.remove(bank)

    transactions = []
    for account in accounts:
        if (account.spendings > debt_per_person):
            transactions.append(Transaction(
                bank, account, account.spendings - debt_per_person))
            continue
        if (account.spendings < debt_per_person):
            transactions.append(Transaction(
                account, bank, debt_per_person - account.spendings))

    return transactions
