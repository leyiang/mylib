import argparse

class ArgParse:
    def __init__(self) -> None:
        self.parser = argparse.ArgumentParser()

    def add_bool(self, *args):
        self.parser.add_argument(
            *args,
            action=argparse.BooleanOptionalAction
        )

    def parse_args(self):
        return self.parser.parse_args()
