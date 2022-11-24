import argparse
from hijack import hijack


def main():
    argparser = argparse.ArgumentParser()

    argparser.add_argument(
        "-s",
        "--hijackee",
        type=str,
        help="Target file to hijack",
        required=True,
        dest="hijackee",
    )

    argparser.add_argument(
        "-d",
        "--dest",
        type=str,
        help="Destination of hijacked file",
        required=True,
        dest="destination",
    )

    argparser.add_argument(
        "-o",
        "--overwrite",
        type=bool,
        help="Overwrite target file if it exists already",
        default=False,
        dest="overwrite_existing",
    )

    args = hijack.HijackArgs.from_args(argparser.parse_args())

    hijack.hijack_file(
        hijackee=args.hijackee,
        destination=args.destination,
        overwrite_existing=args.overwrite_existing,
    )


if __name__ == "__main__":
    main()
