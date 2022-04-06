import click

from . import common

@click.group()
def main_group():
    """Test app."""


@main_group.command('run')
def run_command():
    """Run test command."""
    print('This is a test application.')
    user = common.UserData('Marvin')
    user.say_hi()
    print('Test complete, bye!')


if __name__ == '__main__':
    main_group()
