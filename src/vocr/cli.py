import platform

import click

from vocr import __title__, __version__


@click.command(name="version")
def version() -> None:
    """Show current version"""
    ver_msg = f"{__title__} v{__version__}"
    click.echo(
        f"{ver_msg}\n"
        f"- os/type: {platform.system().lower()}\n"
        f"- os/kernel: {platform.version()}\n"
        f"- os/arch: {platform.machine().lower()}\n"
        f"- python version: {platform.python_version()}\n"
    )


@click.group(name="cli")
def cli() -> None:
    """vocr's command line interface"""
    pass


cli.add_command(version)
