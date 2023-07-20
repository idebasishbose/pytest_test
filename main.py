from utils import str_to_bool
import typer
from typing import Optional
from typing_extensions import Annotated


def main(name: Annotated[Optional[str], typer.Argument()] = ''):
    print(str_to_bool(name))


if __name__ == "__main__":
    typer.run(main)
