from mrtopo.logger import log
from mrtopo.translator import open_read


def analyze(mutation_file, results_file):
    log(f'Analyzing results from {results_file}, with mutated topology {mutation_file}')

    mutations = convert_mutated_to_list(mutation_file)
    results = convert_results_to_list(results_file)

    return tie(mutations, results)


def convert_mutated_to_list(mutation_file):
    mutations = []

    _f = open_read(mutation_file)
    _f_l = None

    if _f:
        _f_l = _f.readlines()
    else:
        return _f_l

    sequence = 0
    line = ""
    for _l in _f_l:
        '''
        MrTopo network mutation description file.
        Generated on 15/02/2021
        ----------
        Case 0: Operations.ADDLINK
        Added link ['s4', 's6']
        Modified item(s): ['s4', 's6']
        ----------
        Case 1: Operations.ADDSWITCH
        Added switch MRTOPO_S and added link to s7
        Modified item(s): ['MRTOPO_S', 's7']
        ----------
        '''

        if _l.__contains__('----------'):
            sequence = 1
        elif sequence == 1:
            # operation
            operation = _l.strip().split('.')[1]
            f_number = _l.strip().split(' ')[1]
            line += f"File: mrtopo_gen_topo_{f_number}.py - Operation {operation}."
            sequence += 1
        elif sequence == 2:
            # description
            _d = f'MrTopo performed: {_l.strip().replace(",", "-")}'
            line += _d
            sequence += 1
        elif sequence == 3:
            # modified items
            _d = f'MrTopo modified: {_l.strip().replace(",", "-")}'
            line += _d
            sequence = 0
            mutations.append(line)
            line = ""

    return mutations


def convert_results_to_list(results_file):
    results = []
    complex_res = []

    _f = open_read(results_file)
    _f_l = None

    if _f:
        _f_l = _f.readlines()
    else:
        return _f_l

    flag = False
    line = ""

    cases = []

    for _l in _f_l:
        if _l.__contains__("Executing test with:"):
            test_w = _l.strip().split('.')[0]
            cases.append(test_w[len(test_w)-1])
        if _l.__contains__("Test Execution Summary"):
            flag = True
        elif _l.__contains__("Case Not Executed"):
            flag = False
            line += f"\n{_l}"
            results.append(line)
            line = ""

        if flag:
            line += f"\n{_l}"

    for i in range(len(cases)):
        complex_res.append((cases[i], results[i]))

    complex_res.sort(key=lambda x: x[0])

    out_res = []
    for c in complex_res:
        out_res.append(c[1])

    return results


def tie(mutations, results):
    t_csv = []
    '''
        *************************************
        Test Execution Summary
    
    *************************************
    
     Test Start           : 22 Mar 2021 00:40:18
     Test End             : 22 Mar 2021 00:48:15
     Execution Time       : 0:07:56.713058
     Total Tests Planned  : 8
     Total Tests Run      : 3
     Total Pass           : 2
     Total Fail           : 1
     Total No Result      : 0
     Success Percentage   : 66%
     Execution Percentage : 37%
    
     Case Failed          : [10]
     Case Executed        : [0, 1, 10]
     Case Not Executed    : [11, 12, 22, 2, 32]
    '''

    head_list = ["Case #", "Description", "Test Start", "Test End", "Execution Time", "Total Tests Planned", "Total Tests Run", "Total Pass", "Total Fail", "Total No Result", "Success Percentage", "Execution Percentage",
                 "Case Failed", "Case Executed", "Case Not Executed"]

    header = ""

    for i in range(len(head_list)):
        if i == (len(head_list) - 1):
            header += f"{head_list[i]}"
        else:
            header += f"{head_list[i]},"

    t_csv.append(f"{header}\n")

    for i in range(len(results)):
        out = ""

        for h in head_list:
            if h == "Case #":
                out += f"{i},"
            elif h == "Description":
                out += f"{mutations[i].strip()},"
            elif h == "Test Start" or h == "Test End":
                out += f"{find_line(results[i], h).strip().split(':')[1].strip().replace(',', '-')}{find_line(results[i], h).strip().split(':')[2].strip().replace(',', '-')}" \
                       f"{find_line(results[i], h).strip().split(':')[3].strip().replace(',', '-')},"
            elif h == "Execution Time":
                out += f"{find_line(results[i], h).strip().split(':')[1].strip().replace(',', '-')}{find_line(results[i], h).strip().split(':')[2].strip().replace(',', '-')},"
            elif h == "Case Not Executed":
                out += f"{find_line(results[i], h).strip().split(':')[1].strip().replace(',', '-')}"
            else:
                out += f"{find_line(results[i], h).strip().split(':')[1].strip().replace(',', '-')},"

        t_csv.append(f"{out}\n")

    return t_csv


def find_line(tcase, line):
    for l in tcase.split('\n'):
        if l.__contains__(line):
            return l