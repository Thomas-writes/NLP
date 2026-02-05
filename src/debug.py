import pycutest
import os, shutil


def main():
    benchmark = pycutest.find_problems(degree=[0, 3])
    print(benchmark)
    pycutest.import_problem(benchmark[1])

    
main()