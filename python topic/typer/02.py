
import typer

# create typer app
app = typer.Typer()

@app.command()
def sum(x,y):
    print(int(x)+int(y))

@app.command()
def mul(x:int,y:int):
    print(x*y)

    
if __name__ == "__main__":
    app()

# run 
# python 02.py (Missing command) sum  or  mul ( value x y )
#python 02.py sum 10 4