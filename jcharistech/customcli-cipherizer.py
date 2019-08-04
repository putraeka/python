# Tutorial dari https://youtu.be/gLCfLOaIHoQ?list=PLJ39kWiJXSizF1shhf2rHi-aA1yjt7rtX

import click
import random

@click.group()
def main():
    pass

@main.command()
@click.argument('text')
def reverse(text):
    """ Reverse a text """
    click.echo(text[::-1])

@main.command()
@click.argument('text')
def leet(text):
    """ Leet a text """
    chars = {'a':'4','b':'l3','c':'','d':'[', 'e':'3','l':'1','s':'5','t':'7', 'w':'\/\/','o':'0', 't':'+'}
    getchar = lambda c: chars[c] if c in chars else c
    click.echo(''.join(getchar(c) for c in text))

@main.command()
@click.argument('text')
def shufflize(text):
    """ Shufflize a text """
    click.echo(''.join(random.sample(text,len(text))))
    
if __name__ == "__main__":
    main()