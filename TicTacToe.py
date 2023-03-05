while True:
    print("""
------------------   
   TIC TAC TOE
------------------   

    1.- Jugar
    2.- Salir
    
    """)
    try:
        menu = int(input("Eliga una opción: "))
        if menu == 1:
            #Tablero
            filauno = ["1","2","3"]
            filados = ["4","5","6"]
            filatres = ["7","8","9"]
            
            mapa = [filauno,filados,filatres]

            #Rotador de turnos
            ciclo = 0

            while True:
                ciclo += 1
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                for i in mapa:
                    print(i)
                if ciclo%2 == 0:
                    turno = 'O'
                else:
                    turno = 'X'

                #Si el ciclo llega a 5 significa que ya puede haber un ganador y por esto lo evaluamos todas las combinaciones desde el quinto ciclo.
                if ciclo >= 5:
                    if turno == "X":
                        if filauno[0] == "O" and filauno[1] == "O" and filauno[2] == "O":
                            print("\n\n\n--------------------------------------\n\tGANASTE JUGADOR [O]\n--------------------------------------")
                            break
                        elif filados[0] == "O" and filados[1] == "O" and filados[2] == "O":
                            print("\n\n\n--------------------------------------\n\tGANASTE JUGADOR [O]\n--------------------------------------")
                            break
                        elif filatres[0] == "O" and filatres[1] == "O" and filatres[2] == "O":
                            print("\n\n\n--------------------------------------\n\tGANASTE JUGADOR [O]\n--------------------------------------")
                            break
                        elif filauno[0] == "O" and filados[0] == "O" and filatres[0] == "O":
                            print("\n\n\n--------------------------------------\n\tGANASTE JUGADOR [O]\n--------------------------------------")
                            break
                        elif filauno[1] == "O" and filados[1] == "O" and filatres[1] == "O":
                            print("\n\n\n--------------------------------------\n\tGANASTE JUGADOR [O]\n--------------------------------------")
                            break
                        elif filauno[2] == "O" and filados[2] == "O" and filatres[2] == "O":
                            print("\n\n\n--------------------------------------\n\tGANASTE JUGADOR [O]\n--------------------------------------")
                            break
                        elif filauno[0] == "O" and filados[1] == "O" and filatres[2] == "O":
                            print("\n\n\n--------------------------------------\n\tGANASTE JUGADOR [O]\n--------------------------------------")
                            break
                        elif filauno[2] == "O" and filados[1] == "O" and filatres[0] == "O":
                            print("\n\n\n--------------------------------------\n\tGANASTE JUGADOR [O]\n--------------------------------------")
                            break
                    else:
                        if filauno[0] == "X" and filauno[1] == "X" and filauno[2] == "X":
                            print("\n\n\n--------------------------------------\n\tGANASTE JUGADOR [X]\n--------------------------------------")
                            break
                        elif filados[0] == "X" and filados[1] == "X" and filados[2] == "X":
                            print("\n\n\n--------------------------------------\n\tGANASTE JUGADOR [X]\n--------------------------------------")
                            break
                        elif filatres[0] == "X" and filatres[1] == "X" and filatres[2] == "X":
                            print("\n\n\n--------------------------------------\n\tGANASTE JUGADOR [X]\n--------------------------------------")
                            break
                        elif filauno[0] == "X" and filados[0] == "X" and filatres[0] == "X":
                            print("\n\n\n--------------------------------------\n\tGANASTE JUGADOR [X]\n--------------------------------------")
                            break
                        elif filauno[1] == "X" and filados[1] == "X" and filatres[1] == "X":
                            print("\n\n\n--------------------------------------\n\tGANASTE JUGADOR [X]\n--------------------------------------")
                            break
                        elif filauno[2] == "X" and filados[2] == "X" and filatres[2] == "X":
                            print("\n\n\n--------------------------------------\n\tGANASTE JUGADOR [X]\n--------------------------------------")
                            break
                        elif filauno[0] == "X" and filados[1] == "X" and filatres[2] == "X":
                            print("\n\n\n--------------------------------------\n\tGANASTE JUGADOR [X]\n--------------------------------------")
                            break
                        elif filauno[2] == "X" and filados[1] == "X" and filatres[0] == "X":
                            print("\n\n\n--------------------------------------\n\tGANASTE JUGADOR [X]\n--------------------------------------")
                            break
                try:
                    print(f"Jugador [{turno}]")
                    x = int(input("Eliga su posicion: "))
                    if x == 1 or x == 2 or x == 3:
                        if x == 1:
                            filauno.remove("1")
                            filauno.insert(0,turno)
                        elif x == 2:
                            filauno.remove("2")
                            filauno.insert(1,turno)
                        else:
                            filauno.remove("3")
                            filauno.insert(2,turno)
                    elif x == 4 or x == 5 or x == 6:
                        if x == 4:
                            filados.remove("4")
                            filados.insert(0,turno)
                        elif x == 5:
                            filados.remove("5")
                            filados.insert(1,turno)
                        else:
                            filados.remove("6")
                            filados.insert(2,turno)
                    elif x == 7 or x == 8 or x == 9:
                        if x == 7:
                            filatres.remove("7")
                            filatres.insert(0,turno)
                        elif x == 8:
                            filatres.remove("8")
                            filatres.insert(1,turno)
                        else:
                            filatres.remove("9")
                            filatres.insert(2,turno)
                    else:
                        break
                                        
                except:
                    print("Error")
                    continue
        elif menu == 2:
            print("""
         ****ADIOS****
---------------------------------
       !!!Hasta Luego!!! <3       
---------------------------------            
    """)
            break
        else:
            print("""
       ****!!!ERROR!!!****
---------------------------------------
    Ingrese una opción dentro del menú        
---------------------------------------
    """)
            continue
    except:
        print("""
       ****!!!ERROR!!!****
---------------------------------
    Ingrese una opción valida        
---------------------------------
    """)
        continue