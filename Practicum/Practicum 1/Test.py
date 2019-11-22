from subprocess import Popen, PIPE

################################################################################################################################
# TODO:
# 1) PUT THIS FILE IN THE SAME FOLDER AS THE PYTHON FILE CONTAINING YOUR SOLUTION                                              #
# 2) CHANGE THE NAME OF 'YOUR_SOLUTION_FILE_NAME.py' IN THE run_one_test_case() FUNCTION BELOW TO THE NAME OF YOUR PYTHON FILE #
# 3) RUN THIS FILE                                                                                                             #
################################################################################################################################

# parse the given output string and return the angles for hours and minutes
def parse_output(full_output_string):
    splitted = full_output_string.split(b'\n')
    uitvoer_string = str(splitted[0]).replace('\\r', '')
    try:
        uitvoer = int(uitvoer_string[2:-1])
    except:
        uitvoer = -1
    return uitvoer

# Run one test case with given input and output, return True when test succeeds, False when test fails
# CHANGE 'YOUR_SOLUTION_FILE_NAME.py' TO THE NAME OF YOUR PYTHON FILE!
def run_one_test_case(inp, verwachte_uitvoer):
    process = Popen(["python", "vierkanten.py"], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    (output, err) = process.communicate(inp)
    if len(str(err)) > 3:
        print('Your program threw an ERROR')
        return False
    exit_code = process.wait()
    uitvoer = parse_output(output)
    if (uitvoer == -1):
        print('Check your output format: print exactly one numeric value (no text)')
        return False
    return (uitvoer == verwachte_uitvoer)

# Retrieve a list containing all test_cases
def get_test_cases():
    all_test_cases = []
    all_test_cases.append((b'4\n', 8))
    all_test_cases.append((b'-3\n11\n', 14))
    all_test_cases.append((b'0\n', int(0)))
    all_test_cases.append((b'3\n', 8))
    all_test_cases.append((b'17\n', 18))
    return all_test_cases

# Run all given test_cases
def run_test_cases(all_tests):
    for test_nb in range(len(all_tests)):
        (inp, outp) = all_tests[test_nb]
        test_result = run_one_test_case(inp, outp)
        if (test_result == True):
            print('Test ' + str(test_nb + 1) + ': Succeeded')
        else:
            print('Test ' + str(test_nb + 1) + ': Failed')

# Main part of the program: load all test cases and test them on given solution
all_tests = get_test_cases()
run_test_cases(all_tests)