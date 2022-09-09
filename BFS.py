class BFS:
    def __init__(self):
        self.states=['right','left']
        # self.initial_state=(3,3,'left') #Monjes, Canivales, state
        self.frontier=[(3,3,'left')] ## initial statement 
        self.explored=[]
        self.accomplished_goal= [(0,0,'right'),(0,0,'left')]
        self.operations = [(2,0),(0,2),(1,1),(1,0),(0,1)] ### solo puede tener un maximo de suma de una o dos personas
        ### por lo que se colocaron los siguientes supuestos para sumar o restar

        
    def activity(self):
        while not ((self.accomplished_goal[0] in self.explored) or (self.accomplished_goal[1] in self.explored)):
            new_explored = self.frontier[0] ## nuevo a explorar
            # if not (new_explored in self.explored):
            self.explored.append(new_explored)
            self.frontier=self.frontier[1:] ### para recorrer el primer elemento del arreglo 
            # print('Frontier: ',self.frontier)
            # print('explored ', self.explored)
            self.paths_possible()
        return print('proceso terminado')

    def paths_possible(self,max=3,min=0):
        for C,M in self.operations: #Cannibals, Monjes
            last_explored= self.explored[-1] ## utilizamos el ultimo explorado para poder encontrar los posibles paths
            
            if (last_explored[0]>=min and last_explored[0]<=max) and (last_explored[1]>=min and last_explored[1]<=max):

                if last_explored[2] =='left': ### nos da el sentido/estado de la situación si sea la derecha entonces se resta la cantidad
                    ### que hay en la izquierda
                    ## si se dirige hacia la izquierda se suma la cantidad n de personas ya sea canivales o monjes
                    new_dato = (last_explored[0]-C,last_explored[1]-M,'right')
                else:
                    new_dato = (last_explored[0]+C,last_explored[1]+M,'left')
                
            
            ### esta condición es para que el mínimo no pase de 0 y el max de 3 
            ### la segunda condición es para que no se repita el dato ni en frontier ni explorer
            ### la tercera condición es para que el dato de canivales siempre sea menor que o igual para que continue
                # and  ((new_dato not in self.frontier) and (new_dato not in self.explored)) \
                # and (new_dato[0]<=new_dato[1]) :
                self.frontier.append(new_dato) ### en caso de que no cumpla con el mínimo
                print(self.frontier)

        

    def generate_possible_paths(self,dato,max=3,min=0):
        datos_nuevos =[]
        #si el valor dado no se encuentra
        for C,M in self.operations:
            if dato[2] == 'right':
                new_dato =(dato[0]-C,dato[1]-M,'left')
            else:
                new_dato =(dato[0]+C,dato[1]+M,'right')
                datos_nuevos.append(new_dato)
        return datos_nuevos


# lol = BFS()
# print(lol.generate_possible_paths((2,2,'right')))

lol = BFS()
lol.activity()
print(lol.explored)

# lol = [1,2,3,4,5,1,2,3,4]
# uff = [2,3,4,5]

# tamales=list(filter(lambda x:x not in uff,lol))
# print(tamales)
    

    


    
