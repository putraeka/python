# Tutorial dari https://youtu.be/5Ntb3FceAiM?list=PLJ39kWiJXSizF1shhf2rHi-aA1yjt7rtX

import click

@click.command()
# Jika prompt=True maka yang muncul diprompt adalah option dari --name yaitu name
# @click.option('--name',prompt=True)

# Tapi jika prompt dimasukkan string, maka yang muncul adalah string itu sendiri
@click.option('--name',prompt="Masukkan nama")

# Untuk hide password saat dipencet masukkan value hide_input=True
# Jika ingin konfirmasi password (alias 2x masukin password) masukkan confirmation_prompt=True
@click.option('--passw',prompt=True,hide_input=True,confirmation_prompt=True)

def main(name,passw):
    click.echo(f'Nama saya adalah : {name}')
    click.echo(f'Dan passwordmu {passw}')

if __name__ == "__main__":
    main()