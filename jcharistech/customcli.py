# Tutorial dari https://youtu.be/riQd3HNbaDk?list=PLJ39kWiJXSizF1shhf2rHi-aA1yjt7rtX

import click

@click.command()

# Basic Option
@click.option('--nama','-n',default='Gembol',help='Masukkan nama Anda')

# Multiple values
@click.option('--salary','-s',nargs=2,help='Your monthly salary',type=int)

# Multiple options
@click.option('--location','-l',help="Your location, can be more than one",multiple=True)

# Argument
@click.argument('greet',default='dev')

def main(nama,salary,location,greet):
    click.echo(f'Hello {greet}')
    print(f'Hello world! My name is {nama} and my salary is {sum(salary)}')
    # click.echo(f'Tinggal di {location}')
    click.echo('\n'.join(location))

if __name__ == "__main__":
    main()