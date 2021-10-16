import argparse

def convert_base(number: str, from_base: int, to_base: int) -> str:
    """convert integer from `from_base` to `to_base`, where `2 <= from_base, to_base <= 36`"""

    if number == "0": return number

    number_  = int(number, base=from_base)
    negative = number.startswith("-")
    number   = ""

    while number_:
        if (number_ % to_base) >= 10:
            number += chr(ord("A") + (number_ % to_base) - 10)
        else:
            number += chr(ord("0") + (number_ % to_base))

        number_ = int(number_ / to_base)

    if negative: number += '-'

    return number[::-1]

if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("number", type=str)
    parser.add_argument("--from-base", "-f", type=int, choices=range(2, 37))
    parser.add_argument("--to-base", "-t", type=int, choices=range(2, 37))

    args = parser.parse_args()

    print(convert_base(args.number, args.from_base, args.to_base))
