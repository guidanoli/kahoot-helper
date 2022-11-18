import yaml
import argparse
import random
import time
import pyperclip
import sys


def validate_script(script):
    assert type(script) is dict, script
    assert type(script['options']) is list, script
    for option in script['options']:
        assert type(option) is str, option
    assert type(script['questions']) is list, script
    for question in script['questions']:
        assert type(question) is dict, question
        assert type(question['q']) is str, question
        assert type(question['a']) is str, question
        assert question['a'] in script['options'], question


def randomize_script_order(script):
    random.shuffle(script['options'])
    random.shuffle(script['questions'])


def copy_print_wait(string, t):
    pyperclip.copy(string)
    print('"{}"'.format(string), end='')
    for i in range(t):
        sys.stdout.flush()
        time.sleep(1)
        print('.', end='')
    print()


def countdown(t):
    while True:
        inp = input(">>> Enter 'c' to continue or 'r' to repeat: ").lower()
        if 'c' in inp:
            for i in range(t, 0, -1):
                print(f'{i}... ', end='')
                sys.stdout.flush()
                time.sleep(1)
            print()
            return True
        elif 'r' in inp:
            print()
            return False
        else:
            print(f"Invalid input '{inp}'")


def get_options(answer, options):
    population = list(set(options) - {answer})
    options = random.sample(population, min(3, len(population)))
    options.append(answer)
    random.shuffle(options)
    return options


def run_script(script, countdown_time, wait_time):
    validate_script(script)
    randomize_script_order(script)
    ok = countdown(countdown_time)
    for qi, question in enumerate(script['questions'], 1):
        options = get_options(question['a'], script['options'])
        while True:
            print(f"Question #{qi}: ", end='')
            copy_print_wait(question['q'], wait_time)
            for opti, option in enumerate(options, 1):
                if option == question['a']:
                    print(f"Option #{opti} (answer): ", end='')
                else:
                    print(f"Option #{opti}: ", end='')
                copy_print_wait(option, wait_time)
            print()
            ok = countdown(countdown_time)
            if ok:
                break


def main():
    parser = argparse.ArgumentParser(
        description='Helps automate the process of creating a Kahoot')
    parser.add_argument(
        'yaml_script',
        help='YAML file to be processed as script')
    parser.add_argument(
        '--wait-time',
        type=int,
        default=5,
        help='Number of seconds to wait after copying string to clipboard')
    parser.add_argument(
        '--countdown-time',
        type=int,
        default=0,
        help='Number of seconds to wait before every question')
    args = parser.parse_args()
    with open(args.yaml_script) as fp:
        script = yaml.load(fp, yaml.CLoader)
        run_script(script, args.countdown_time, args.wait_time)


if __name__ == '__main__':
    main()
