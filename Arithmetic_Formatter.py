import re
import sys

def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def AlignTexts(num1, num2, answer, operator, display_result=False):
    len1 = len(str(num1))
    len2 = len(str(num2))
    res_len = len(str(answer))

    max_len = max(len1, len2, res_len)
    num1_str = str(num1).rjust(max_len)
    num2_str = operator + str(num2).rjust(max_len - 1)
    answer_str = str(answer).rjust(max_len)

    result_str = num1_str + "\n" + num2_str + "\n" + '-' * max_len + "\n"
    if display_result:
        result_str += answer_str

    return result_str

def check_digit(string_arr):
    for string in string_arr:
        # Remove the operators from the string
        cleaned_string = ''.join(c for c in string if c.isdigit())
        # Check if the cleaned string is a digit
        if not cleaned_string.isdigit():
            raise ValueError("Error: Numbers must only contain digits.")
            

def Arithmetic_Formater(string_array, reveal_answer = False):
    if len(string_array) > 5:
        raise ValueError("Error: Too many problems")
    
    check_digit(string_array)

    math_operators = {"+" : addition, "-" : subtraction}
    operator_not_allowed = {'*', "/"}

    for string in string_array:
        arithmetic = re.findall(r'\d+|\+|\-|\*|\/', string)
        numbers = [int(x) for x in arithmetic if x.isdigit()]
        math_operator = [x for x in arithmetic if not x.isdigit()]   

        if math_operator[0] not in math_operators:
            raise ValueError("Error: Operator must be '+' or '-'")

        if len(str(numbers[0])) > 4 or len(str(numbers[1])) > 4:
            raise ValueError("Error: Numbers cannot be more than four digits") 

        if math_operator[0] in math_operators:
            answer = math_operators[math_operator[0]] (numbers[0], numbers[1])
            data = AlignTexts(numbers[0], numbers[1], answer, math_operator[0], reveal_answer)
            print(data)
        print("\n")

if __name__ == "__main__":
    Arithmetic_Formater(["32 + 698", "3801 - 2", "45 + 43"], True)
    sys.stdout.flush()
    