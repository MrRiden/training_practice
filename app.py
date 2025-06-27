import sys
from matcher import match_template

def parse_args(argv):
    args = {}
    for arg in argv:
        if arg.startswith("--"):
            key, value = arg[2:].split("=", 1)
            args[key] = value
    return args

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "get_tpl":
        fields = parse_args(sys.argv[2:])
        result = match_template(fields)
        if isinstance(result, str):
            print(result)
        else:
            print("{")
            for k, v in result.items():
                print(f"  {k}: {v},")
            print("}")
