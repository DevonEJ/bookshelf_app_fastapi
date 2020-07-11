import enum


class Role(str, enum.Enum):
    admin: str = "administrator"
    customer: str = "customer"
