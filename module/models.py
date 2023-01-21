from dataclasses import dataclass, field


@dataclass
class Account:
    """Class for tracking spendings of a person"""
    name: str
    spendings: float = 0.0


@dataclass
class Transaction:
    """Class to represent transactions from a person to another person"""
    source: Account
    destination: Account
    amount: float
