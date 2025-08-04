#if else anidado
lloviznar=True
tempe = int(input("Ingrese temperatura:")) #le pido al usuario la temperatura 
if tempe<12 and lloviznar== True: #si la temperatura es menor a 12 y llueve
    print("llevar paraguas y un abrigo") #llevar paraguas y abigo
elif tempe > 12 and lloviznar == False: #si la temp es menor a 12 y no llueve 
    print("llevar solo abrigo") #solo llevar abrigo
else: # si ninguna se cumple no llevar nada
    print("No llevar paraguas ni abrigo")