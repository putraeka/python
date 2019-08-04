# Sambungan tutorial customcli2.py

import click

@click.command()

# Jika nargs=-1 maka bisa dimasukkan lebih dari 1 value kedalam arguments tersebut
@click.argument('source',nargs=-1)
@click.argument('destination',nargs=1)

def main(source,destination):
    for f in source:
        click.echo(f'moving {f} to folder {destination}')

if __name__ == "__main__":
    main()