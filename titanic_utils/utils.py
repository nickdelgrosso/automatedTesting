

def convert_pounds_for_inflation_from_1912(value_old: float, conversion_rate: float = 134.99) -> float:
    """
    Returns the value of pounds in today's currency, when given a pound value from 1912 (when the titanic sank).

    Conversion rate taken from https://www.in2013dollars.com/uk/inflation/1912?amount=1
    """
    return value_old * conversion_rate


def is_adult(age: float, threshold: int = 18) -> bool:
    """
    Returns whether a person should be considered an adult, based on the age of the person
    """
    return age >= threshold


