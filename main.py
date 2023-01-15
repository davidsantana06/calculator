from calculator import Calculator
from operation import Operation
#from Text import Text
import re as regex

def get_msg(index):
    msg = ''

    match(index):
        # 0 :: Panel
        # 1 :: Good bye
        # 2 :: Invalid input
        # 3 :: No operations
        # 4 :: Invalid X
        # 5 :: Invalid Y
        case 0:
            msg = '|------------ CALCULATOR ------------|' + \
                '\n|     SELECT ONE OPERATION BELOW     |' + \
                '\n| 1) SUM | 2) SUBTRACT | 3) MULTIPLY |' + \
                '\n| 4) DIVIDE | 5) POWER | 6) HISTORY  |' + \
                '\n|      0) STOP THE APPLICATION       |' + \
                '\n|------------------------------------|'
        case 1:
            msg = '+-+-+-+-+-+-' + \
                '\n+ GOOD BYE -' + \
                '\n+-+-+-+-+-+-'
        case 2:
            msg = '| INVALID INPUT! |'
        case 3:
            msg = '| NO OPERATIONS REGISTRED! |'
        case 4:
            msg = '| INVALID X! |'
        case 5:
            msg = '| INVALID Y! |'

    if (index < 2):
        return msg
    else:
        hyphens = (('-' * (len(msg) // 2 - 4)), ('-' * len(msg)))
        return ('{0} ADVISE {1}\n{2}\n{3}'.format(hyphens[0], hyphens[0], msg, hyphens[1]))

def main():
    calculator = Calculator()
    operations = []
    stop = False

    while not stop:
        print('\n' + get_msg(0))
        operation_number = input('_Operation: ')
        valid_operation = operation_number >= '0' and operation_number <= '6'
        result = ''

        if (valid_operation):
            if (operation_number == '0'):
                result = get_msg(1)
                stop = True
            elif (operation_number == '6'):
                if (len(operations) == 0):
                    result = get_msg(3)
                else:
                    biggest_string = len(str(operations[0]))
                    operations_str = ''

                    for i in range(len(operations)):
                        operations_str += (str(operations[i]) + '\n')

                        if (len(str(operations[i])) > biggest_string):
                            biggest_string = len(str(operations[i]))

                    hyphens = [('-' * (biggest_string - 8)),
                               ('-' * biggest_string)]
                    result = 'HISTORY {0}\n{1}{2}'.format(hyphens[0], operations_str, hyphens[1])
            else:
                x = input('\n_Insert X: ')
                while not x.isnumeric():
                    print('\n' + get_msg(4))
                    x = input('\n_Insert X: ')

                y = input('_Insert Y: ')
                while not y.isnumeric():
                    print('\n' + get_msg(5))
                    y = input('\n_Insert Y: ')

                if (x.isnumeric() and y.isnumeric()):
                    operation = ''

                    match (operation_number):
                        case '1':
                            operation = '{0} + {1} = {2}'.format(x, y, calculator.sum_numbers(float(x), float(y)))
                        case '2':
                            operation = '{0} - {1} = {2}'.format(x, y, calculator.subtract_numbers(float(x), float(y)))
                        case '3':
                            operation = '{0} * {1} = {2}'.format(x, y, calculator.multiply_numbers(float(x), float(y)))
                        case '4':
                            operation = '{0} / {1} = {2}'.format(x, y, calculator.divide_numbers(float(x), float(y)))
                        case '5':
                            operation = '({0})^{1} = {2}'.format(x, y, calculator.power_number(float(x), float(y)))

                    operations.append(Operation((len(operations) + 1), operation))
                    hyphens = [('-' * (len(operation) - 7)),
                               ('-' * len(operation))]
                    result = 'RESULT {0}\n{1}\n{2}'.format(hyphens[0], operation, hyphens[1])
                else:
                    result = get_msg(2)
        else:
            result = get_msg(2)

        print('\n' + result)

main()