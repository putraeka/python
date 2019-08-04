# Tutorial dari https://youtu.be/JwtqwOKCXYs?list=PLJ39kWiJXSizF1shhf2rHi-aA1yjt7rtX

import click

@click.command()

# Multiple arguments
@click.argument('number1',type=int)
@click.argument('number2',type=int)
@click.argument('method',default='+')

def main(number1,number2,method):
    if method == '+':
        # result = int(number1) + int(number2)
        # jika sudah menentukan typenya tidak perlu lagi dideklarasikan di variable
        result = number1 + number2
        click.echo(result)
    elif method == '-':
        result = number1 - number2
        click.echo(result)
    elif method == '/':
        result = number1 / number2
        click.echo(result)
        
if __name__ == "__main__":
    main()