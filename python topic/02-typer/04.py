
import typer

# create typer app

def sum(x,y):
    print(int(x)+int(y))

def mul(x:int,y:int):
    print(x*y)

    
if __name__ == "__main__":
    app = typer.Typer() #  1 - create app typer 
    app.command()(sum)  # creaete command
    app.command()(mul)  # create command
    app()               #Run app

# Plan B ( syntax )
# if u want to use def with our typer # with out change Def 
#run # py 04.py sum 5 10