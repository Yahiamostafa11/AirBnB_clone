import shlex
import re
import json


def parse_argument(args):
    """Parse an argument"""
    # search for {}
    data = ""
    match = re.search(r'{.*}', args)
    if match:
        try:
            data = json.loads(match.group())
            args = re.sub(r'{.*}', '', args)
        except json.JSONDecodeError:
            print("Invalid JSON format")
    args = shlex.split(args)
    if data:
        args.append(data)
    else:
        args = [int(arg) if arg.isdigit()
                else arg
                for arg in args]  # Convert numbers to integers if possible
    return args


if __name__ == "__main__":
    # test strings
    print(parse_argument('{ "name" : "satamony" } hello world'))
    print(parse_argument('hello world { "name" : "satamony" }'))
    print(parse_argument('satamony'))
    print(parse_argument(''))

    # test numbers
    print(parse_argument('1 2 "3" 4'))
