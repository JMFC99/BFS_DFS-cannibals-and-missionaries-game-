class DFS:
    def __init__(self):
        self.states=['left','right']## se establece en un principio que cada tipo de estado tiene el primer
        # elemento como izquierda y el segundo elemento derecha
        self.frontier=[(3,3,'left')] ## initial statement 
        self.explored=[] # inital statement
        self.accomplished_goal= [(0,0,'right'),(0,0,'left')] ## esto es lo que se busca llegar
        self.no_reached_goal = True ## se maneja un estado inicial que nos permite verificar si se llegó o no al objetivo
        self.operations = [(2,0),(0,2),(1,1),(1,0),(0,1)] ### solo puede tener un maximo de suma de una o dos personas, 
        # por lo que estos son los posibles estados que pueden suceder durante el viaje 

    def activity(self):        
        while self.no_reached_goal:
            new_to_explore = self.frontier.pop() ## nuevo a explorar 
            '''
            para hacer más facil el tomar la primera de una lista lo que se hizo en este caso es lo siguiente: 
            example = [(3,3,'left'),(1,2,'right')] 
            al existir un append que termina anexando los elementos encontrados al final, entonces del final
            hacia el principio se está obteniendo el que se va a explorar
            '''
            self.paths_possible(boat_state=new_to_explore[-1],current_state=new_to_explore)
        
            if len(self.explored) ==0 : ### estado inicial
                self.explored.append([new_to_explore,self.frontier[0]])
            
            else:
                new_explored = [0,0] ### inicializar una variable exploración
                index_new_element=self.states.index(new_to_explore[-1])     ### identificar la posición del arreglo ejemplo
                new_explored[index_new_element] = new_to_explore # se asigna 
                '''
                explicación de la linea de arriba
                por ejemplo [(3,3,'left'),(2,3,'right')] si el nuevo a explorar (frontier) es (2,2,right) termina siendo 
                right o left, lo que se hace es colocar ese cambio en la posición del ejemplo en este caso
                teniendo el resultado de [(3,3,left),(2,2,right)]
                '''

                new_explored[new_explored.index(0)] =self.explored[-1][new_explored.index(0)]
                '''
                esta sección lo que hace el lugar restante se asigna el valor que no se cambió
                ejemplo: 
                --> [(3,3,left),(2,3,right)]
                --> [(3,3,left),(2,2,right)]
                '''
                if (sum(new_to_explore[:2]) not in list(map(lambda x:sum(x[:2]),self.explored[-1])) \
                    and new_to_explore[-1]==new_to_explore[-1])\
                    and abs(sum(new_explored[0][:2]) - sum(new_explored[1][:2]))<=2:
                    self.explored.append(new_explored)
                
                '''
                la explicación de segnmento de código anterior consiste en lo siguiente: 
                new_to_explore = [2,3,'right']
                self.explored =[(3, 3, 'left'), (1, 3, 'right')], [(3, 3, 'left'), (2, 3, 'right')]
                
                (sum(new_to_explore[:2]) not in list(map(lambda x:sum(x[:2]),self.explored[-1]))
                
                el primer punto suma los dos elementos y por otro lado se hace una lista, donde primero
                se toma el último elemento de la lista self.explored (los ya explorados), después se realiza
                un mapeo para sumar los primeros elementos de cada tupla: 

                iteración 1: 
                3+3 = 6
                iteración 2: 
                2+3 = 5
                
                al tener la suma del nuevo explorado, new_to_explore = 5 y teniendo la lista [6,5]
                se buscó que no se encontrara el elemento en la lista y verificar que tuviera la misma 
                dirección 'right' o 'left' para que no apareciera el error que más abajo se muestra
                el código esta para nada más tomar un lado en este caso tomo en cuenta donde está la barca
                ejemplo salía este estado debido en cierto numero de iteraciones por lo que no es correcto
                
                
                CC MMM  ()------C  (2,3,'left')
                CCC MM  -------() M (3,2,'right')


                la segunda condición :    abs(sum(new_explored[0][:2]) - sum(new_explored[1][:2]))<=2:
                esta parte lo que hace que solamente se puedan anexar a self.explored que en este caso
                son los explorados siempre y cuando solamente se esten transportando un máximo de 2 personas
                por viaje

                '''

                ## Esto lo que hace es poder hacer un mapeo para verificar si ya se cumplió el objetivo y con eso cambiar el estado del goal
                if len(list(filter(lambda x:(self.accomplished_goal[0] in x or self.accomplished_goal[1] in x),self.explored)))>0:
                    self.no_reached_goal=False
                '''
                esta sección lo que hace es cambiar el estado self.no_reached_goal, para cortar el ciclo while
                lo que se verifica primero es filtrar de la lista de explorados si se encuentra tanto [0,0,left] o [0,0,right]
                en los movimientos correspondientes en caso de que sea cierto eso se filtra en una lista
                en caso de ser menor a 1 entonces se cambia el estado a falso. 
                '''

        return print('Grafical Steps'.center(50,'-'))

    def paths_possible(self,boat_state,current_state,max=3,min=0,new_explored=None):
        new_data=[] # creamos una lista para poder anexar todos los posibles nuevos casos
        for C,M in self.operations: #Cannibals, Monjes 
            '''
            las operaciones que realiza es restar/sumar los valores de las tuplas 
            delo asignado a self.operations:
            self.operations = [(2,0),(0,2),(1,1),(1,0),(0,1)] ya con esto tenemos
            asegurado la posicion y a cual se suma o resta

            ejemplo (3,3,'left'). Si tomamos el primero 
            
            '''
            last_explored= current_state ## utilizamos el ultimo explorado para poder encontrar los posibles paths
            if boat_state=='left': 
                """
                ### nos da el sentido/estado de la situación si sea la derecha entonces se resta la cantidad que hay en la izquierda
                ## si se dirige hacia la izquierda se suma la cantidad n de personas ya sea canivales o monjes cambiando 
                el estado anterior que se tomó en cuenta
                """
                new_dato = (last_explored[0]-C,last_explored[1]-M,'right') 
            else:
                new_dato = (last_explored[0]+C,last_explored[1]+M,'left')


            if (not (new_dato[0]<min or new_dato[1]<min or new_dato[0]>max or new_dato[1]>max))\
                and ((len(list(filter(lambda x: new_dato in x,self.explored))))<1)\
                and (new_dato not in self.frontier)\
                and ((new_dato[0]<=new_dato[1] and new_dato[2]=='right') or ((new_dato[0]>=new_dato[1] and new_dato[2]=='left'))):
                new_data.append(new_dato) ### te regresa el último dato encontrado
        
            '''

            Estas son las condiciones para poder almacenar en la lista new_data el dato generado:
                condicion 1: no puede existir valores menores a 0 y mayores a 3
                not (new_dato[0]<min or new_dato[1]<min or new_dato[0]>max or new_dato[1]>max))
                
                condicion 2: ((len(list(filter(lambda x: new_dato in x,self.explored))))<1)
                el nuevo dato encontrado no puede encontrarse en explorer

                condicion 3: (new_dato not in self.frontier)
                el dato tampoco se encuentre en frontier

                condicion 4: ((new_dato[0]<=new_dato[1] and new_dato[2]=='right') or ((new_dato[0]>=new_dato[1] and new_dato[2]=='left')))      
                si el barco se encuentra en la derecha tiene que existir una cantidad menor o igual de canivales a diferencia 
                de los monjes y como las tuplas tienen (C,M,B) canival, Monje, orientación de barco.
                
                Caso 1:
                (new_dato[0]<=new_dato[1] and new_dato[2]=='right')
                Representación: CCMMM------() C

                Caso 2: 
                (new_dato[0]>=new_dato[1] and new_dato[2]=='left')
                Representación: CCCMM()-------M

            
            '''
        print(self.frontier)
        self.frontier = self.frontier + new_data  ## se concatena lo del frontien con la nueva data generada
        print(self.frontier)
        return  


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
            print(C*'C',M*'M',state,abs(C-3)*'C',abs(M-3)*'M',info,end='\n')
        print('Steps'.center(40,'-'))
        for i in self.explored:  ### esta sección permite imprimir 
            print(i)

case1 = DFS() # se asigna a una variable la clase BFS
case1.activity()  ## manda a llamar la función activity de la clase BFS
case1.draw_images()  ### manda a llamar la función draw_images de la clase BFS
    


    