from dataclasses import dataclass, field


@dataclass(frozen=True)
class Account:
    """Class for associating a person and it's spendings"""
    name: str
    spendings: float = field(default=0.0, compare=False)


@dataclass(frozen=True)
class Transaction:
    """Class to represent transactions from a person to another person"""
    source: Account
    destination: Account
    amount: float
