import click
# from .core import locker

@click.command()
@click.option('-e', default='', help='csv file to be encrypted')

def say_hello(e):
    click.echo("Hello {}!".format(e))

if __name__ == '__main__':
    say_hello()