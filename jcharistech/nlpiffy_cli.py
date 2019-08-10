# Tokenization
# Sentiment
# Entities
# POS
# Word analysis, lemma, stop

# Core Pkgs
import click


# NLP Pkgs
from textblob import TextBlob
from pyfiglet import Figlet
# import spacy
# nlp = spacy.load('en')

@click.group()
@click.version_option(version='0.01',prog_name="NLPiffy CLI")

def main():
    """NLPifyy CLI"""
    pass

# Tokenization
@main.command()
@click.argument('text')
@click.option('--tokentype','-t',help='Specify type of tokenization [word or sentence]')
def tokens(text,tokentype):
    """Tokenization with Textblob"""
    raw_text = TextBlob(text)
    finalized = raw_text.words
    if tokentype == 'word':
        click.secho(f'Your text was : {raw_text}',fg='yellow')
        click.secho(f'Your text now : {finalized}',fg='red')
    elif tokentype == 'sentence':
        click.secho(f'Your text was : {raw_text}',fg='yellow')
        click.secho(f'Your sentence now : {raw_text.sentences}',fg='red')
    else:
        click.secho(f'Your text was : {raw_text}',fg='yellow')
        click.secho(f'Your text now : {finalized}',fg='red')

# Sentiment analysis
@main.command()
@click.argument('text')
def sentiment(text):
    """Sentiment Analysis with Textblob"""
    raw_text = TextBlob(text)
    finalized = raw_text.sentiment
    click.secho(f'Your text was : {raw_text}',fg='yellow')
    click.secho(f'Your sentence now : {finalized}',fg='red')
    
# Part of speech
@main.command()
@click.argument('text')
def part_of_speech(text):
    """Part of speech Tagging """
    raw_text = TextBlob(text)
    finalized = raw_text.pos_tags
    click.secho(f'Your text was : {raw_text}',fg='yellow')
    click.secho(f'Your Part of speech now : {finalized}',fg='blue')

# Reading a file
@main.command()
@click.argument('text',type=click.File('rb'))
@click.argument('analysis',default='wordinfo')
def read_file(text,analysis):
    """Read a file and analysis"""
    mytext = text.read().decode('utf-8')
    file_text = TextBlob(mytext)
    if analysis == 'tokens':
        click.secho(f'Your text was : {mytext}',fg='yellow')
        click.secho(f'Words token : {file_text.words}',fg='red')

# Info
@main.command()
@click.option('--about')
def info(about):
    """Info about NLPiffy"""
    f = Figlet(font='slant')
    print(f.renderText('NLPiffy CLI'))

# Entities
# @main.command()
# @click.argument('text')
# def entities(text):
#     """Entities recognition with Spacy"""
#     raw_text = nlp(text)
#     finalized = [(entity.text,entity.label_) for entity in raw_text.ents]
#     click.secho(f'Your text was : {raw_text}',fg='yellow')
#     click.secho(f'Named Entities : {finalized}',fg='blue')

if __name__ == "__main__":
    main()