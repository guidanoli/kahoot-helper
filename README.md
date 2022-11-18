# Helper Python Script for Making Kahoots

This script is aimed to help create kahoot games where you have a set of options $O$ and a set of questions $Q$ where for every $q \in Q$ there is exactly one right answer $ans(q) \in O$ and at most three different wrong answers $o \in O \setminus \\{ ans(q) \\}$. The input is formatted in YAML in the following format. Note that every answer must be contained in the set of options.

```yaml
options:
  - first option
  - second option
  - ...
  - n-th option
questions:
  - q: first question
    a: answer to first question
  - q: second question
    a: answer to second question
  - ...
  - q: m-th question
    a: answer to m-th question
```

The script randomizes the order of questions and answers automatically with a seemingly random seed every time. For every question, it waits for the user to enter the letter `c` as input to continue. It then prints the question to the standard output, copies it to the clipboard, and waits for 5 seconds until the next step. This time period can be changed by the `--wait-time` command line option. After that, it iterates through the 4 options and does the same three things: prints it, copies it to the clipboard, and waits for the same amount of time. This loop proceeds for all questions. At any point, the user can type `r` instead of  `c` to tell the script to repeat the last step, in case the user could not paste a value in time. The user can also configure a delay period after typing `c` (to continue to the next question) through the ``--countdown-time`` command line option.

## Setup

```sh
pip install -r requirements.txt
```

## Example

```sh
python main.py sample.yml
```

## Help

```sh
python main.py --help
```
