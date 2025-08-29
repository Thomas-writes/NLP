import pycutest

def main():
    problems = pycutest.find_problems()
    print(f"Total problems: {len(problems)}")
    counter = 0
    for name in problems:
        counter += 1
        if counter < 10:
            print(name)

main()
