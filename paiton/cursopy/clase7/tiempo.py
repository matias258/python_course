#Hora de ir a casa
import time
from datetime import datetime


date = datetime.now()

def casa(date):
    if date > 19:
        print("Es hora de ir a casa")
    else:
        print("faltan ",19-date,"para volver a casa")




