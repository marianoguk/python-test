
def read_number(field_name):
    n = 0.0
    while True:
        try:
            n = float(input("\n* Enter value for {} --> ".format(field_name)))
            break
        except ValueError:
            print("\nInvalid number format for {}".format(field_name))
    return n

def read_operation():
    operations = ["+", "-", "*", "/"]
    op = ""
    while True:
        try:
            op = input("\n* Enter operation {} -->  ".format(operations))
            if op in operations:
                break
        except ValueError:
            print("\nInvalid operation. Valid values: ".format(operations))
    return op


def get_calculation_parameters():
    operationMapping = {
        "+": lambda n1, n2: n1 + n2,
        "-": lambda n1, n2: n1 - n2,
        "*": lambda n1, n2: n1 * n2,
        "/": lambda n1, n2: n1 / n2
    }
    symbol = read_operation()
    num1 = read_number("N1")
    num2 = read_number("N2")
    operation = operationMapping[symbol]
    if symbol == "/":
        while num2 == 0:
            print("\nFor division N2 cannot be null. Enter it again")
            num2 = read_number("N2")

    return {"n1": num1, "n2": num2, "operation": {"formula": operation, "symbol": symbol}}

def calculator():
    new_calculation = True
    while new_calculation:
        print("========== CALCULATOR ==================")
        params = get_calculation_parameters()
        op = params["operation"]
        formula = op["formula"]
        n1 = params["n1"]
        n2 = params["n2"]
        print("\n ==> {} {} {} = {}".format(n1, op["symbol"], n2, formula(n1, n2)))
        new_calculation = input("\n New calculation? Y/N --> ") not in ["N", "n"]

while True:
    calculator()