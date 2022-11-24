import pathlib
from dataclasses import dataclass
import shutil
import argparse


class HijackException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


@dataclass(frozen=True, slots=True)
class HijackArgs:
    hijackee: pathlib.Path
    destination: pathlib.Path
    overwrite_existing: bool

    @staticmethod
    def from_args(args: argparse.Namespace) -> "HijackArgs":
        return HijackArgs(
            hijackee=pathlib.Path(args.hijackee),
            destination=pathlib.Path(args.destination),
            overwrite_existing=args.overwrite_existing,
        )


def remove_file(path: pathlib.Path):
    if path.is_dir():
        shutil.rmtree(path)

    if path.is_file():
        path.unlink()


def hijack_file(
    hijackee: pathlib.Path,
    destination: pathlib.Path,
    overwrite_existing: bool,
):
    if destination.exists() and not overwrite_existing:
        print("Destination file already exists")
        return

    if not hijackee.exists():
        print("Hijackee does not exist")
        return

    remove_file(destination)

    hijackee.rename(destination)

    hijackee.symlink_to(destination)
