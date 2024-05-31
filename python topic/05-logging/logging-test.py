import logging
import sys



#create logger
logger = logging.getLogger('mylogger')
logger.setLevel(logging.DEBUG)  # Set logging level to capture all messages


#hannnder : show information
cmd_handler = logging.StreamHandler(stream=sys.stdout) #update first by first in terminal 
cmd_handler.setLevel(logging.DEBUG)  # Set handler level to capture all messages


#add formater # how can show info
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
cmd_handler.setFormatter(formatter)


# add handder in logger 
logger.addHandler(cmd_handler)


def mylogic(x,y):
    try:
        logger.info(f'divide {x}/{y}')
        result = x/y
        return x/y
    
    except Exception as e:
        logger.error(f' error : {e}')

if __name__ == "__main__":
    mylogic(5,0)
