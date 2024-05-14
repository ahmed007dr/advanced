
import typer

# create typer app
app = typer.Typer()

@app.command()
def calc(salary:int,employee:bool=False):
    if employee:
        tax = salary*1.14
        print(tax) 
    return(salary*90) 

@app.command()
def sum(x,y):
    pass
if __name__ == "__main__":
    app()


#run #python 03.py calc 100 
#run # python 03.py (value) when only one def
#python 03.py calc 100 --employee  # employee true pramater
