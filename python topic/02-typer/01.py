#pip install typer

import typer

def hello(messge):
    print(f'messge   {messge}')

if __name__ == "__main__": # syntax to start from hello # for example when start new app start from password page -_:
    #hello('ahmed')
    typer.run(hello)
# to change parmeter 
#python ./01.py --help
# to run ( python 01.py 'ahmed' )
