class BFS:
    def __init__(self):
        self.states=['left','right']
        # self.initial_state=(3,3,'left') #Monjes, Canivales, state
        self.frontier=[(3,3,'left')] ## initial statement 
        self.explored=[]
        self.accomplished_goal= [(0,0,'right'),(0,0,'left')]
        self.no_reached_goal = True
        self.operations = [(2,0),(0,2),(1,1),(1,0),(0,1)] ### solo puede tener un maximo de suma de una o dos personas
        ### por lo que se colocaron los siguientes supuestos para sumar o restar
        # self.activity()
        # self.draw_images()


    def activity(self):        
        while self.no_reached_goal:
            # print('weas',self.frontier)
            new_to_explore = self.frontier[0] ## nuevo a explorar [[(3,3,'left'),[(3,2,'left')]]]+
            # print(new_to_explore)
            self.paths_possible(boat_state=new_to_explore[-1],current_state=new_to_explore)
            # print('frontier',self.frontier)
            # print('explore',self.explored)
        
            if len(self.explored) ==0 : ### estado inicial
                self.explored.append([self.frontier[0],self.frontier[1]])
                self.frontier=self.frontier[2:] ## desplazar un elemento de la lista
            
            else:
                # last_explored = self.explored[-1] ## [(),()]
                new_explored = [0,0] ### inicializar una variable exploración
                index_new_element=self.states.index(new_to_explore[-1])     ### identificar la posición del arreglo ejemplo
                new_explored[index_new_element] = new_to_explore
                new_explored[new_explored.index(0)] =self.explored[-1][new_explored.index(0)]
                # verified_statement = len(list(filter(lambda x:(x[-1]!=new_to_explore[-1]) and (len(list(filter(lambda y:y in x[:2],new_to_explore[:2])))<1),last_explored))) #[3,3,'right']

                if sum(new_to_explore[:2]) not in list(map(lambda x:sum(x[:2]),self.explored[-1])) and new_explored[-1]==new_explored[-1]:
                    self.explored.append(new_explored)
                self.frontier=self.frontier[1:]

            ## nuevo a explorar [[(3,3,'left'),[(3,2,'left')]]]+
                ## Esto lo que hace es poder hacer un mapeo para verificar si ya se cumplió el objetivo y con eso cambiar el estado del goal
                ### verificar como se comporta esto en caso de solo tener un arreglo [] y no tener multiples arreglos para mapear 
                if len(list(filter(lambda x:(self.accomplished_goal[0] in x or self.accomplished_goal[0] in x),self.explored)))>0:
                    self.no_reached_goal=False

        return print('proceso terminado')

    def paths_possible(self,boat_state,current_state,max=3,min=0,new_explored=None):
        new_data=[]
        for C,M in self.operations: #Cannibals, Monjes
            last_explored= current_state ## utilizamos el ultimo explorado para poder encontrar los posibles paths
            if boat_state=='left': ### nos da el sentido/estado de la situación si sea la derecha entonces se resta la cantidad
                ### que hay en la izquierda
                ## si se dirige hacia la izquierda se suma la cantidad n de personas ya sea canivales o monjes
                new_dato = (last_explored[0]-C,last_explored[1]-M,'right')
            else:
                new_dato = (last_explored[0]+C,last_explored[1]+M,'left')
            
        
        ### esta condición es para que el mínimo no pase de 0 y el max de 3 
        ### la segunda condición es para que no se repita el dato ni en frontier ni explorer
        ### la tercera condición es para que el dato de canivales siempre sea menor que o igual para que continue
        #new_dato not in self.explored

            # print('lista de totales que se repiten',list(filter(lambda x:new_dato in x,self.explored)))
#new_dato not in self.frontier and 
            # sum(new_dato[:2] in list(map(lambda:sum(x[:2])))
            #myList = [i for i in range(10) if i%2 == 0]
            # suma de los dos elementos sum(new_dato[:2]) 2 
            # variable = list(map(lambda x: sum(x[:2]))) [1,2]
            # self.states.index(variable[variable.index(suma_ultimo_dato)]) 'left'
            # 

                

            #### guardamos el estado que nos interesa ya sea right o left en la última posición de la lista


            if (not (new_dato[0]<min or new_dato[1]<min or new_dato[0]>max or new_dato[1]>max))\
                and ((len(list(filter(lambda x: new_dato in x,self.explored))))==0) \
                and ((new_dato[0]<=new_dato[1] and new_dato[2]=='right') or ((new_dato[0]>=new_dato[1] and new_dato[2]=='left'))):
                new_data.append(new_dato) ### te regresa el último dato encontrado
        
        self.frontier = self.frontier + new_data
        return   ## se concatena lo del frontienr con la nueva data genrada


        

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

    def draw_images(self):
        self.view = []
        for i,j in self.explored:
            self.view.append(i)
            self.view.append(j)
        for C,M,B in self.view: #cannivales, monjes, bote
            state='--------()'
            if B=='left':
                state = "()--------"
           #
            info = (C,M,abs(C-3),abs(M-3))
            print(C*'C',M*'M',state,abs(C-3)*'C',abs(M-3)*'M',info)

        print('---------------------------'*2)
        for i in self.explored:
            print(i)

case1 = BFS()
# print(case1.generate_possible_paths((3,3,'right')))
case1.activity()
case1.draw_images()
    


    
