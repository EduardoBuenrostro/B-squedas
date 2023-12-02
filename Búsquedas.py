"""La primera parte es sencilla, simplemente representamos el grafo por medio
de un diccionario, la llave sera el número de nodo mientras que el contenidos
sera sus nodos sucesores seguidos de la distancia que hay hacia ellos, es 
importante mencionar que están acomodados  en forma horaria
"""
grafo = {
    1 : {6 : 117, 13 : 697, 4 : 687},
    2 : {22 : 171, 12 : 127, 9 : 246},
    3 : {14 : 317, 23 : 235, 19 : 626, 18 : 291},
    4 : {9 : 202, 1 : 687, 13 : 98},
    5 : {15 : 220, 11 : 697},
    6 : {16 : 278, 1 : 117},
    7 : {27 : 475, 8 : 662, 11 : 694},
    8 : {27 : 255, 15 : 309, 7 : 662},
    9 : {28 : 320, 2 : 246, 17 : 302, 4 : 202, 24 : 214},
    10 : {16 : 365, 12 : 54},
    11 : {7 : 694, 5 : 697},
    12 : {10 : 54, 2 : 127},
    13 : {4 : 98, 1 : 697, 24 : 446},
    14 : {23 : 499, 3 : 317},
    15 : {8 : 309, 24 : 286, 5 : 220},
    16 : {19 : 95, 25 : 118, 20 : 123, 6 : 278, 26 : 66, 10 : 365},
    17 : {26 : 236, 9 : 302},
    18 : {14 : 328, 3 : 291, 21 : 89},
    19 : {23 : 391, 16 : 95, 3 : 626},
    20 : {25 : 33, 16 : 123},
    21 : {18 : 89, 22 : 449, 28 : 380, 27 : 262},
    22 : {23 : 401, 2 : 171, 28 : 190, 21 : 449},
    23 : {14 : 499, 19 : 391, 22 : 401, 3 : 235},
    24 : {9 : 214, 13 : 446, 15 : 286},
    25 : {},
    26 : {16 : 66, 17 : 236},
    27 : {21 : 262, 28 : 407, 8 : 255, 7 : 475},
    28 : {27 : 407, 21 : 380, 22 : 190, 2 : 131, 9 : 320, 8 : 310},
    }
"""
Igualmente creamos un diccionario para las distancias entre cada nodo 
la llave es el número de nodo, mientras que los elementos son el nodo 
al que se va a hacer referencia y seguidamente la distancia  del nodo 
desde el nodo llave a él.
"""
distancias = {
    1 : {1:0,2:908,3:117,4:687,5:1651,6:117,7:1882,8:1310,9:889,10:760,11:2348,12:782,13:697,14:1370,15:1431,16:395,17:697,18:1328,19:490,20:481,21:1244,22:810,23:881,24:1145,25:513,26:461,27:1407,28:1000},
    2 : {1:908,2:0,3:515,4:448,5:970,6:791,7:1013,8:441,9:246,10:181,11:1707,12:127,13:546,14:928,15:750,16:513,17:316,18:600,19:540,20:636,21:511,22:171,23:572,24:460,25:631,26:497,27:538,28:131},
    3 : {1:117,2:515,3:0,4:886,5:1373,6:999,7:117,8:844,9:684,10:559,11:1811,12:541,13:984,14:317,15:1153,16:721,17:739,18:291,19:626,20:813,21:300,22:344,23:235,24:898,25:780,26:704,27:642,28:534},
    4 : {1:687,2:448,3:886,4:0,5:922,6:804,7:1404,8:832,9:202,10:479,11:1619,12:426,13:98,14:1319,15:702,16:744,17:504,18:991,19:817,20:867,21:902,22:542,23:943,24:416,25:862,26:678,27:929,28:522},
    5 : {1:1651,2:970,3:1373,4:922,5:0,6:1540,7:1191,8:529,9:720,10:997,11:697,12:943,13:952,14:1463,15:220,16:1262,17:1022,18:1148,19:1335,20:1385,21:1046,22:1029,23:1430,24:506,25:1380,26:1195,27:784,28:839},
    6 : {1:117,2:791,3:999,4:804,5:1540,6:0,7:1765,8:1193,9:840,10:643,11:2237,12:665,13:814,14:1253,15:1320,16:278,17:580,18:1211,19:373,20:364,21:1127,22:693,23:764,24:1034,25:396,26:344,27:1290,28:883},
    7 : {1:1882,2:1013,3:117,4:1404,5:1191,6:1765,7:0,8:662,9:1202,10:1194,11:694,12:1140,13:1502,14:1154,15:971,16:1407,17:1329,18:826,19:1553,20:1610,21:737,22:1072,23:1352,24:1257,25:1605,26:1432,27:475,28:882},
    8 : {1:1310,2:441,3:844,4:832,5:529,6:1193,7:662,8:0,9:630,10:622,11:1223,12:568,13:930,14:934,15:309,16:915,17:757,18:606,19:981,20:1038,21:517,22:500,23:901,24:595,25:1033,26:938,27:255,28:310},
    9 : {1:889,2:246,3:684,4:202,5:720,6:840,7:1202,8:630,9:0,10:277,11:1417,12:223,13:300,14:1117,15:500,16:542,17:302,18:789,19:615,20:665,21:700,22:340,23:741,24:214,25:660,26:476,27:727,28:320},
    10 : {1:760,2:181,3:559,4:479,5:997,6:643,7:1194,8:622,9:277,10:0,11:1694,12:54,13:577,14:774,15:777,16:365,17:180,18:729,19:392,20:480,21:664,22:215,23:616,24:491,25:483,26:349,27:719,28:312},
    11 : {1:2348,2:1707,3:1811,4:1619,5:697,6:2237,7:694,8:1223,9:1417,10:1694,11:0,12:1640,13:1649,14:1848,15:917,16:1959,17:1719,18:1520,19:2032,20:2082,21:1431,22:1766,23:2046,24:1203,25:2077,26:1893,27:1169,28:1576},
    12 : {1:782,2:127,3:541,4:426,5:943,6:665,7:1140,8:568,9:223,10:54,11:1640,12:0,13:523,14:756,15:723,16:387,17:202,18:711,19:414,20:510,21:646,22:197,23:598,24:437,25:505,26:371,27:665,28:258},
    13 : {1:697,2:546,3:984,4:98,5:952,6:814,7:1502,8:930,9:300,10:577,11:1649,12:523,13:0,14:1417,15:732,16:842,17:602,18:1089,19:915,20:965,21:1000,22:640,23:1041,24:446,25:960,26:776,27:1027,28:620},
    14 : {1:1370,2:928,3:317,4:1319,5:1463,6:1253,7:1154,8:934,9:1117,10:774,11:1848,12:756,13:1417,14:0,15:1250,16:975,17:954,18:328,19:890,20:1077,21:417,22:559,23:499,24:1331,25:1044,26:1041,27:679,28:797},
    15 : {1:1431,2:750,3:1153,4:702,5:220,6:1320,7:971,8:309,9:500,10:777,11:917,12:723,13:732,14:1250,15:0,16:1042,17:802,18:928,19:1115,20:1165,21:826,22:809,23:1210,24:286,25:1160,26:976,27:564,28:619},
    16 : {1:395,2:513,3:721,4:744,5:1262,6:278,7:1407,8:915,9:542,10:365,11:1959,12:387,13:842,14:975,15:1042,16:0,17:302,18:933,19:95,20:123,21:849,22:416,23:486,24:756,25:118,26:66,27:1012,28:605},
    17 : {1:697,2:316,3:739,4:504,5:1022,6:580,7:1329,8:757,9:302,10:180,11:1719,12:202,13:602,14:954,15:802,16:302,17:0,18:913,19:397,20:425,21:844,22:395,23:796,24:516,25:420,26:236,27:854,28:447},
    18 : {1:1328,2:600,3:291,4:991,5:1148,6:1211,7:826,8:606,9:789,10:729,11:1520,12:711,13:1089,14:328,15:928,16:933,17:913,18:0,19:960,20:1056,21:89,22:514,23:526,24:1003,25:1051,26:898,27:351,28:469},
    19 : {1:490,2:540,3:626,4:817,5:1335,6:373,7:1553,8:981,9:615,10:392,11:2032,12:414,13:915,14:890,15:1115,16:95,17:397,18:960,19:0,20:187,21:895,22:446,23:391,24:829,25:154,26:161,27:1043,28:636},
    20 : {1:481,2:636,3:813,4:867,5:1385,6:364,7:1610,8:1038,9:665,10:480,11:2082,12:510,13:965,14:1077,15:1165,16:123,17:425,18:1056,19:187,20:0,21:972,22:538,23:578,24:879,25:33,26:189,27:1135,28:728},
    21 : {1:1244,2:511,3:300,4:902,5:1046,6:1127,7:737,8:517,9:700,10:664,11:1431,12:646,13:1000,14:417,15:826,16:849,17:844,18:89,19:895,20:972,21:0,22:449,23:615,24:914,25:967,26:852,27:262,28:380},    
    22 : {1:810,2:171,3:344,4:542,5:1029,6:693,7:1072,8:500,9:340,10:215,11:1766,12:197,13:640,14:559,15:809,16:416,17:395,18:514,19:446,20:538,21:449,22:0,23:401,24:554,25:533,26:360,27:597,28:190},
    23 : {1:881,2:572,3:235,4:943,5:1430,6:764,7:1352,8:901,9:741,10:616,11:2046,12:598,13:1041,14:499,15:1210,16:486,17:796,18:526,19:391,20:578,21:615,22:401,23:0,24:955,25:545,26:552,27:877,28:591},
    24 : {1:1145,2:460,3:898,4:416,5:506,6:1034,7:1257,8:595,9:214,10:491,11:1203,12:437,13:446,14:1331,15:286,16:756,17:516,18:1003,19:829,20:879,21:914,22:554,23:955,24:0,25:874,26:690,27:850,28:534},
    25 : {1:513,2:631,3:780,4:862,5:1380,6:396,7:1605,8:1033,9:660,10:483,11:2077,12:505,13:960,14:1044,15:1160,16:118,17:420,18:1051,19:154,20:33,21:967,22:533,23:545,24:874,25:0,26:184,27:1130,28:723},
    26 : {1:461,2:497,3:704,4:678,5:1195,6:344,7:1432,8:938,9:476,10:349,11:1893,12:371,13:776,14:1041,15:976,16:66,17:236,18:898,19:161,20:189,21:852,22:360,23:552,24:690,25:184,26:0,27:957,28:550},
    27 : {1:1407,2:538,3:642,4:929,5:784,6:1290,7:475,8:255,9:727,10:719,11:1169,12:665,13:1027,14:679,15:564,16:1012,17:854,18:351,19:1043,20:1135,21:262,22:597,23:877,24:850,25:1130,26:957,27:0,28:407},
    28 : {1:1000,2:131,3:534,4:522,5:839,6:883,7:882,8:310,9:320,10:312,11:1576,12:258,13:620,14:797,15:619,16:605,17:447,18:469,19:636,20:728,21:380,22:190,23:591,24:534,25:723,26:550,27:407,28:0},
    }
"""En resumen esta funcion regresa los sucesores
toma como entrada un grafo (en forma de diccionario) y un nodo inicial.
La función devuelve una lista con los descendientes (también conocidos
como sucesores) del nodo inicial en el grafo."""
def nodos_sucesor(grafo, nodo_inicial):
    descendientes = []
    """La función comprueba si el nodo inicial está en el grafo y, si es así, 
    itera a través de los elementos del diccionario asociado a ese nodo. 
    Cada elemento representa un arco del nodo inicial a un nodo descendiente,
    y se añade el nodo descendiente a la lista de descendientes."""
    if nodo_inicial in grafo:
        for nodo, arco in grafo[nodo_inicial].items():
            descendientes.append(nodo)
    """Si el nodo inicial no está en el grafo, la función simplemente devuelve una lista vacía."""
    return descendientes

"""
La función distancia toma como entrada un grafo, y dos nodos, nodo_inicial 
y nodo_final. La función devuelve la distancia entre el nodo_inicial y el 
nodo_final en el grafo, que se calcula iterando a través de los nodos 
adyacentes del nodo_inicial."""
def distancia(grafo, nodo_inicial, nodo_final):
    distancia = 0
    """se comprueba si los nodos están presentes en el grafo."""
    if nodo_inicial in grafo and nodo_final in grafo:
        for nodo, dis in grafo[nodo_inicial].items():
            if nodo == nodo_final:
                distancia = dis
    """se comprueba si el nodo adyacente es el nodo_final.
    Si es así, la distancia entre los nodos se establece en 
    la línea 6 a partir del valor del arco que conecta los 
    nodos en el grafo.
    """
    return distancia
"""Esta función simplemente es para declarar como se hara la busqueda 
(Sentido horario o antihorario)"""
def direccion(descendientes, sentido):
    def direccion(descendientes, sentido):
    # Si el sentido es "antihorario", se devuelve la lista de descendientes invertida
        if sentido == "antihorario":
            return descendientes[::-1]
    # Si el sentido es "horario", se devuelve la lista de descendientes tal como está
        else:
            return descendientes
"""Implementa el algoritmo de búsqueda en amplitud (BFS) para encontrar 
    una ruta desde el nodo inicial hasta el nodo final en un grafo.
    Como parametros usaremos los diccionarios usados anteriormente """
def busquedaAncho(grafo, nodo_inicial, nodo_final, sentido = "h"):
    """La variable abiertos es un diccionario que contiene los nodos 
    que se han visitado, donde la clave es el nodo y el valor es una 
    lista con dos elementos. El primer elemento indica si el nodo ha
    sido visitado (0 si no se ha visitado, 1 si ya se visitó) y el 
    segundo elemento indica el nodo predecesor en la ruta.
    """
    abiertos = {nodo_inicial:[0,0]}
    """ almacenar los nodos en orden """
    ruta = []
    """ es una lista vacía que se usará para almacenar los nodos visitados en orden inverso """
    reversa = []
    """En el bucle while se realiza la búsqueda en amplitud. En cada iteración se busca el 
    nodo que no ha sido visitado y que tiene la menor profundidad. Luego se marca como 
    visitado (cambiando su valor a 1 en abiertos) y se exploran todos sus sucesores. Si 
    alguno de los sucesores no ha sido visitado, se agrega a la lista abiertos con el valor
    [0, actual] donde actual es el nodo actual. 
    """
    while len(abiertos) != 0:
        for nodo, valor in reversed(abiertos.items()):
            if valor[0] == 0:
                actual = nodo

        ante = abiertos[actual][1]
        abiertos[actual]=[1,ante]
        """decidimos hacer la tabla por medio de prints"""
        print("Nodo Actual: ",actual)
        print("N :  R  A")
        for nodo, ra in abiertos.items():
            print(nodo , ':' , ra)
        print("")
        """en cada iteracion se comprueba el estado del 
        nodo para saber si se ha llegado al objetivo"""
        if actual == nodo_final:
            aux = actual
            while aux != nodo_inicial:
                reversa.append(aux)
                aux = abiertos[aux][1]
            reversa.append(nodo_inicial)
            ruta=reversa[::-1]
            """Si el nodo actual es igual al nodo final, se construye 
            la ruta a través de la lista reversa, invirtiendo el orden 
            y almacenándola en la lista ruta."""
            ruta_s = ",".join(str(elemento) for elemento in ruta)
            print("Ruta:",ruta_s)
            break;
        """verifica si el nodo actual es igual al nodo final. Si es así, 
        significa que se ha encontrado una ruta y se procede a construirla.
        """
        if actual != nodo_final:
            sucesores = nodos_sucesor(grafo, actual)
            if sentido == "antihorario":
                sucesores = direccion(sucesores, "antihorario")
            """verifica si hay sucesores para el nodo actual y, si los hay, 
            los agrega al conjunto de nodos abiertos. Este proceso se repite 
            hasta que se encuentre el nodo final o se hayan explorado todos 
            los nodos posibles."""
            if len(sucesores) != 0:
                for c in sucesores:
                    if c not in abiertos:
                        abiertos[c] = [0,actual]
"""el codigo usa los mismos parametros que el anterior, secambiara 
el funcionamiento interno """
def busquedaProfundidad(grafo, nodo_inicial, nodo_final, sentido = "h"):
    abiertos = {nodo_inicial:[0,0]}
    ruta = []
    reversa = []
    #es un bucle que se ejecuta mientras haya nodos abiertos.
    while len(abiertos) != 0:
        """se utiliza para encontrar el nodo que se va a explorar a 
        continuación. Busca el primer nodo que tenga el valor 0, 
        que significa que está abierto."""
        for nodo, valor in (abiertos.items()):
            if valor[0] == 0:
                actual = nodo
        # cierra el nodo actual y guarda su nodo padre en la lista de abiertos.
        ante = abiertos[actual][1]
        abiertos[actual]=[1,ante]
        # Los siguientes comentarios e impresiones de pantalla muestran el estado actual de la búsqueda.
        print("Nodo Actual: ",actual)
        print("N :  R  A")
        for nodo, ra in abiertos.items():
            print(nodo , ':' , ra)
        print("")
        """Si encontramos el nodo final, se reconstruye la ruta de manera 
        similar a como se hizo en el algoritmo de búsqueda en anchura."""
        if actual == nodo_final:
            aux = actual
            while aux != nodo_inicial:
                reversa.append(aux)
                aux = abiertos[aux][1]
            reversa.append(nodo_inicial)
            ruta=reversa[::-1]
                
            ruta_s = ",".join(str(elemento) for elemento in ruta)
            print("Ruta:",ruta_s)
            break;
        """Si el nodo actual no es el nodo final, se buscan sus 
        sucesores con nodos_sucesor(grafo, actual) y se almacenan 
        en la lista sucesores."""
        if actual != nodo_final:
            sucesores = nodos_sucesor(grafo, actual)
            if sentido == "h":
                sucesores = direccion(sucesores, "antihorario")
    
            if len(sucesores) != 0:
                for c in sucesores:
                    if c not in abiertos:
                        abiertos[c] = [0,actual]
"""
Este código implementa el algoritmo de búsqueda de máxima pendiente para 
encontrar el camino con la mayor pendiente en un grafo."""
def maximaPendiente(grafo, distancias, nodo_inicial, nodo_final, sentido = "h"):
    abiertos = {nodo_inicial:[distancia(distancias,nodo_inicial,nodo_final),0]}
    ruta = []
    reversa = []
    actual = nodo_inicial
    previo = 0
    contador = 0
    """En cada iteración, el código evalúa el nodo actual y sus sucesores,
    y actualiza la lista de nodos abiertos con la información correspondiente"""
    while len(abiertos) != 0:
        #imprime los valores 
        print("Nodo Actual: ",actual)
        print("N : Costo A")
        for nodo, ra in abiertos.items():
            print(nodo , ':' , ra)
        print(" ")

        previo = actual
#Luego, selecciona el sucesor con el costo más bajo y lo establece como el nuevo nodo actual. 
        for nodo, valor in reversed(abiertos.items()):
            if (valor[0] <= abiertos[actual][0]):
                actual = nodo
        """Si se produce un ciclo (es decir, el nodo actual es igual al nodo anterior), 
        el código construye la ruta parcial y la imprime. """
        if (actual == previo) and contador > 0:
            error = True
        else:
            error = False
            
        contador += 1

        if error == True:
            aux = actual
            while aux != nodo_inicial:
                reversa.append(aux)
                aux = abiertos[aux][1]
            reversa.append(nodo_inicial)
            ruta=reversa[::-1]
            ruta_s = ",".join(str(elemento) for elemento in ruta)
            print("Ruta parcial:",ruta_s)
            break
#Si el nodo actual es igual al nodo final, el código construye la ruta óptima y la imprime
        if actual == nodo_final:
            print("Nodo Actual: ",actual)
            aux = actual
            while aux != nodo_inicial:
                reversa.append(aux)
                aux = abiertos[aux][1]
            reversa.append(nodo_inicial)
            ruta=reversa[::-1]
            ruta_s = ",".join(str(elemento) for elemento in ruta)
            print("Ruta:",ruta_s)
            break
#Si el nodo actual no es igual al nodo final, el código continúa con la búsqueda. 
        if actual != nodo_final:
            sucesores = nodos_sucesor(grafo, actual)
            if sentido == "antihorario":
                sucesores = direccion(sucesores, "antihorario")
    
            if len(sucesores) != 0:
                for c in sucesores:
                    if c not in abiertos:
                        abiertos[c] = [distancia(distancias,c,nodo_final),actual]
"""El algoritmo de escalada simple es un algoritmo de búsqueda heurística que 
se utiliza para encontrar el mínimo local en una función. En este caso, estamos 
utilizando una función que representa el costo de ir desde el nodo inicial hasta 
el nodo final a través del grafo.
"""   
def escaladaSimple(grafo, distancias, nodo_inicial, nodo_final, sentido = "h"):
    abiertos = {nodo_inicial:[distancia(distancias,nodo_inicial,nodo_final),0]}
    ruta = []
    reversa = []
    actual = nodo_inicial
    previo = 0
    contador = 0
    """En este algoritmo, comenzamos desde el nodo inicial y generamos 
    sucesores. Luego, elegimos el sucesor con el costo más bajo y
    lo convertimos en el nodo actual. """
    if actual != nodo_final:
        sucesores = nodos_sucesor(grafo, actual)
        if sentido == "antihorario":
            sucesores = direccion(sucesores, "antihorario")
    """Continuamos haciendo esto hasta que el nodo actual es el nodo final
    o hasta que no hay más sucesores con un costo menor que el nodo actual."""
    while len(abiertos) != 0:
#se imprimen los valores 
        print("Nodo Actual: ",actual)
        print("N : Costo A")
        for nodo, ra in abiertos.items():
            print(nodo , ':' , ra)
        print(" ")
        previo = actual
        if contador != 0:
            for nodo in sucesores:
                if abiertos[nodo][0] <= abiertos[actual][0]:
                    actual = nodo
                    break

        """Si llegamos a un punto donde no hay sucesores con un 
        costo menor que el nodo actual, nos detenemos y tomamos la 
        ruta que tomamos hasta ese punto como nuestra solución. """
        if (actual == previo) and contador > 0:
            error = True
        else:
            error = False
            
        contador += 1

        if error == True:
            aux = actual
            while aux != nodo_inicial:
                reversa.append(aux)
                aux = abiertos[aux][1]
            reversa.append(nodo_inicial)
            ruta=reversa[::-1]
            ruta_s = ",".join(str(elemento) for elemento in ruta)
            print("Ruta parcial:",ruta_s)
            break
        """ verifica si la variable actual no es el nodo final. Si 
        es así, se obtienen los sucesores del nodo actual y se verifica 
        si el sentido de búsqueda es antihorario para ajustar la dirección 
        en caso necesario."""
        if actual == nodo_final:
            print("Nodo Actual: ",actual)
            aux = actual
            while aux != nodo_inicial:
                reversa.append(aux)
                aux = abiertos[aux][1]
            reversa.append(nodo_inicial)
            ruta=reversa[::-1]
            ruta_s = ",".join(str(elemento) for elemento in ruta)
            print("Ruta:",ruta_s)
            break
        """se ejecuta si el nodo actual no es igual al nodo final. 
        Si es así, se itera sobre cada sucesor del nodo actual para 
        verificar si el costo de la función heurística de ese sucesor 
        es menor o igual que el costo heurístico del nodo actual. """
        if actual != nodo_final:
            sucesores = nodos_sucesor(grafo, actual)
            if sentido == "antihorario":
                sucesores = direccion(sucesores, "antihorario")
    
            if len(sucesores) != 0:
                for c in sucesores:
                    if c not in abiertos:
                        abiertos[c] = [distancia(distancias,c,nodo_final),actual]
"""
Este código es una implementación del algoritmo de búsqueda A* para encontrar la 
ruta más corta entre dos nodos en un grafo."""
def primeroMejor(grafo, distancias, nodo_inicial, nodo_final, sentido = "h"):
    abiertos = {nodo_inicial:[0,0,distancia(distancias,nodo_inicial,nodo_final),distancia(distancias,nodo_inicial,nodo_final),0]}
    ruta = []
    reversa = []
    actual = nodo_inicial
    previo = 0
    contador = 0

    if actual != nodo_final:
        sucesores = nodos_sucesor(grafo, actual)
        if sentido == "antihorario":
            sucesores = direccion(sucesores, "antihorario")
            
    while len(abiertos) != 0:

        print("Nodo Actual: ",actual)
        print("N :  A  G + H  = F   CERRADO")
        for nodo, ra in abiertos.items():
            print(nodo , ':' , ra)
        print(" ")
        
        previo = actual
        
        
        if contador != 0:
            for nodo in sucesores:
                if abiertos[nodo][3] <= abiertos[actual][3]:
                    actual = nodo
                
        ante = abiertos[actual][0]
        abiertos[actual]=[ante,distancia(distancias, ante, actual),distancia(distancias, actual, nodo_final),int((distancia(distancias, ante, actual))+int(distancia(distancias, actual, nodo_final))),1]
                
        if (actual == previo) and contador > 0:
            error = True
        else:
            error = False
            
        contador += 1

        if error == True:
            aux = actual
            while aux != nodo_inicial:
                reversa.append(aux)
                aux = abiertos[aux][0]
            reversa.append(nodo_inicial)
            ruta=reversa[::-1]
            ruta_s = ",".join(str(elemento) for elemento in ruta)
            print("Ruta parcial:",ruta_s)
            break
        
        if actual == nodo_final:
            print("Nodo Actual: ",actual)
            aux = actual
            while aux != nodo_inicial:
                reversa.append(aux)
                aux = abiertos[aux][0]
            reversa.append(nodo_inicial)
            ruta=reversa[::-1]
            ruta_s = ",".join(str(elemento) for elemento in ruta)
            print("Ruta:",ruta_s)
            break

        if actual != nodo_final:
            sucesores = nodos_sucesor(grafo, actual)
            if sentido == "antihorario":
                sucesores = direccion(sucesores, "antihorario")
    
            if len(sucesores) != 0:
                for c in sucesores:
                    if c not in abiertos:
                        abiertos[c] = [actual,distancia(distancias, c, actual),distancia(distancias, c, nodo_final),int((distancia(distancias, c, actual))+int(distancia(distancias, c, nodo_final))),0]