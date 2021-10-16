class car(object):

    def __init__(self,model,company,color,speed_limit):
        self.model=model
        self.company=company
        self.color=color
        self.speed_limit=speed_limit

    def start(self):
        print("car is started")
        
    def stop(self):
        print("car is Stopped")

    def accelarate(self):
        print("car is accelarated")

bugatti=car("veryon","bugatti","purple",450)        

print(bugatti.color)
bugatti.start()
