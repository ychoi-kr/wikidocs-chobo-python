def run_tests(read_function, program_name):
    test_cases = [
        ("와일드 윙: 110cm 이상", ("와일드 윙", 110, None)),
        ("점프 타워: 140cm 이하", ("점프 타워", None, 140)),
        ("플라이벤처: 140cm~195cm", ("플라이벤처", 140, 195)),
        ("툼 오브 호러: -", ("툼 오브 호러", None, None)),
        ("매직 휠: 120cm 이상 150cm 이하", ("매직 휠", 120, 150)),
    ]

    failed_tests = []

    for i, (input_text, expected_output) in enumerate(test_cases):
        result = read_function(input_text)
        if result != expected_output:
            failed_tests.append((i + 1, input_text, expected_output, result))
        print(f"Test case {i + 1} passed." if result == expected_output else f"Test case {i + 1} failed.")

    if failed_tests:
        print(f"\n{program_name} - Summary of failed tests:")
        for test_case, input_text, expected_output, result in failed_tests:
            print(f"Test case {test_case} failed: input({input_text}) expected {expected_output}, got {result}")

# 각 프로그램의 read 함수를 import
from ridereader_basic import read as read_basic
from ridereader_for import read as read_for
from ridereader_lambda import read as read_lambda

def test_ridereader_basic():
    print("Testing ridereader_basic.py")
    run_tests(read_basic, "ridereader_basic.py")

def test_ridereader_for():
    print("Testing ridereader_for.py")
    run_tests(read_for, "ridereader_for.py")

def test_ridereader_lambda():
    print("Testing ridereader_lambda.py")
    run_tests(read_lambda, "ridereader_lambda.py")

if __name__ == "__main__":
    test_ridereader_basic()
    test_ridereader_for()
    test_ridereader_lambda()
