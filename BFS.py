class BFS:

    #funcion inicial
    def __init__(self):
        #states: el lado en el que se encuentra el bote
        self.states=['left','right']
        #frontier: estado inicial  
        #frontier(# Caniables, # Misioneros, states)
        self.frontier=[(3,3,'left')] 
        #explored = lista de nodos explorados
        self.explored=[] 
        #accomplished_goal: estado meta al mover todos los misioneros y canibales del izquierdo ---> a derecho
        #****Preguntar porque se mantienen ambos estados como meta*****
        self.accomplished_goal= [(0,0,'right'),(0,0,'left')] 
        #no_reached_goal: bandera de tipo boolean para verificar si se ha llegado al estado deseado 'accomplished_goal'
        self.no_reached_goal = True 
        #operations: lista de operacones permitidas donde solo permite 1 o 2 personas por viaje
        #(2,0) 2 Canibales, 0 Misioneros
        #(0,2) 0 Canibales, 2 Misioneros
        #(1,1) 1 Canibal, 1 Misionero
        #(1,0) 1 Canibal, 0 Misioneros
        #(0,1) 0 Canibales, 1 Misionero
        self.operations = [(2,0),(0,2),(1,1),(1,0),(0,1)] 

    #Funcion 'activity' que hace una llamada recursiva mientras la meta definida por la funcion 'init' no se ha alcanzado.
    def activity(self):        
        while self.no_reached_goal:
            #variable 'new_to_explore' permite crear un nodo por explorar apartir del primer nodo definido en la lista 'frontier' (3,3,'left')
            new_to_explore = self.frontier[0]
            #funcion 'paths_possible' genera la siguiente transicion/accion y agrega un nuevo nodo a frontier
            self.paths_possible(boat_state=new_to_explore[-1],current_state=new_to_explore)
        
            #'if' condicion para considerar el caso cuando no existe ningun nodo explorado
            # 'else' condicion para explorar cuando ya existe al menos un nodo explorado
            if len(self.explored) ==0 : ### estado inicial
                #agrega los nodos frontier[0] y frontier[1] a la lista de nodos explorados.
                self.explored.append([self.frontier[0],self.frontier[1]])
                self.frontier=self.frontier[2:] ## desplazar un elemento de la lista
            
            else:
                #new_explored: genera una variable local para almacenar un nodo temporal para explorar
                new_explored = [0,0] ### inicializar una variable exploración
                #index_new_element obtiene la posicion del nodo actual (left, right)
                index_new_element=self.states.index(new_to_explore[-1])     ### identificar la posición del arreglo ejemplo
                #la variable 'new_explored' definida para guardas un nodo se le asigna el indice definido en index_new_element
                #el valor del nodo 'new_explored' obtiene el valor de new_to_explored=self.frontier[0]
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

                #Condicion para agregar un nodo a la lista de nodos explorado, siempre y cuando cumpla con las especificaciones
                #   sum(new_to_explore[:2]) not in list(map(lambda x:sum(x[:2]),self.explored[-1]))
                #   1. Verifica que el nodo explorado no se encuentre en los nodos de los explorados.
                #
                #   abs(sum(new_explored[0][:2]) - sum(new_explored[1][:2]))<=2
                #   2. Verifica que se este transportando un máximo de dos personas
                if (sum(new_to_explore[:2]) not in list(map(lambda x:sum(x[:2]),self.explored[-1]))) \
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
                
                self.frontier=self.frontier[1:]
                """
                ## esta sección se utiliza para desplazar el primer elemento de la lista del frontier
                ### debido a que ya se pasó al explorer.
                """

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

    #paths_possible(self, boat_state, current_state, max, min, new_explored)
    #   self: use self for the first argument to instance methods
    #   boat_state: es el estado actual del bote, derecha o izquierda 
    #   current_state: es el estado actual en el que se encuentra el juego es decir la combinacion de #Misioneros, #Canibales, boat_state
    #   max: maximo numero de personas en el bote
    #   min: minimo numero de personas en el bote
    #   new_explored: nuevo estado que se va a explorar partiendo del estado actual 'current_state'

    def paths_possible(self,boat_state,current_state,max=3,min=0,new_explored=None):
        # 'new_data' es una lista de posibles acciones que se pueden realizar a partir del estado actual
        new_data=[]
        # loop creado para generar los posibles movimientos/transiciones considerando el numero de canibales (C) y misioneros (M) del estado actual
        for C,M in self.operations: #Cannibals, Misioneros
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




        self.frontier = self.frontier + new_data  ## se concatena lo del frontien con la nueva data generada
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

case1 = BFS() # se asigna a una variable la clase BFS
case1.activity()  ## manda a llamar la función activity de la clase BFS
case1.draw_images()  ### manda a llamar la función draw_images de la clase BFS
    


    