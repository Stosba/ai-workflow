import argparse
import sys

from convert.converter import convert
from convert.errors import UnknownUnitError, IncompatibleUnitsError


def main():
    parser = argparse.ArgumentParser(description="Convert units")
    parser.add_argument("value", type=float, help="Value to convert")
    parser.add_argument("from_unit", type=str, help="Source unit")
    parser.add_argument("to_unit", type=str, help="Target unit")
    args = parser.parse_args()

    try:
        result = convert(args.value, args.from_unit, args.to_unit)
    except UnknownUnitError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except IncompatibleUnitsError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    print(f"{args.value} {args.from_unit} = {result} {args.to_unit}")


if __name__ == "__main__":
    main()
