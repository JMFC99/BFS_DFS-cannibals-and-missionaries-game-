class BFS:
    def __init__(self):
        self.states=['right','left']
        # self.initial_state=(3,3,'left') #Monjes, Canivales, state
        self.frontier=[(3,3,'left')] ## initial statement 
        self.explored=[]
        self.accomplished_goal= [(0,0,'right'),(0,0,'left')]
        self.operations = [(2,0),(0,2),(1,1),(1,0),(0,1)]

        
    def activity(self):
        while not ((self.accomplished_goal[0] in self.explored) or (self.accomplished_goal[1] in self.explored)):
            new_explored = self.frontier[0] ## nuevo a explorar
            if not (new_explored in self.explored):
                self.explored.append(self.frontier[0])
                self.frontier=self.frontier[1:] ### para recorrer el primer elemento del arreglo 
        pass


    def generate_possible_paths(self,dato,max=3,min=0):
        datos_nuevos =[]
        #si el valor dado no se encuentra
        for C,M in self.operations:
            if dato[2] == 'right':
                new_dato =(dato[0]-C,dato[1]-M)
            else:
                new_dato =(dato[0]+C,dato[1]+M)
            
            if not (new_dato[0]<min or new_dato[1]<min or new_dato[0]>max or new_dato[1]>max):
                datos_nuevos.append(new_dato)
        return datos_nuevos


lol = BFS()
print(lol.generate_possible_paths((2,3,'right')))

    
    

    


    
