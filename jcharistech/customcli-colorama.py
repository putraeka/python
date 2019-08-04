# Tutorial dari https://youtu.be/MLVTSKZ1wpQ?list=PLJ39kWiJXSizF1shhf2rHi-aA1yjt7rtX

import click

@click.command()
@click.option('--name','-n')

def main(name):
    # click.echo(click.style((f'My name is {name}'),fg='red',bg='white',bold=True))
    # cara yang lebih mudah menggunakan click.secho()
    click.secho((f'My name is {name}'),fg='red',bg='white',bold=True)

if __name__ == "__main__":
    main()