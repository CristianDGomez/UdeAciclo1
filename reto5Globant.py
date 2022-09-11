import csv
import json

def solucion():
    #ESTA ES LA FUNCIÓN A LA QUE LE DEBES GARANTIZAR LOS RETORNOS REQUERIDOS EN EL ENUNCIADO.
    archivo=open("GLOBANT.csv")
    x=csv.reader(archivo)
    Date=[]
    Open=[]
    High=[]
    Low=[]
    Close=[]
    Adj_close=[]
    Volume=[]
    
    next(x,None)
    for columna in x:
        Date.append(columna[0])
        Open.append(float(columna[1]))
        High.append(float(columna[2]))
        Low.append(float(columna[3]))
        Close.append(float(columna[4]))
        Adj_close.append(float(columna[5]))
        Volume.append(int(columna[6]))
        
    archivo.close()
    comportamiento=[]
    media=[]
    j=0
    q=0
    k=0
    for i in range(len(Open)):
        resta=Close[i]-Open[i]
        media.append(0.5*(High[i]-Low[i]))
        if resta>0:
            comportamiento.append("SUBE")
            j=j+1
        elif resta<0:
            comportamiento.append("BAJA")
            q=q+1
        elif resta==0:
            comportamiento.append("ESTABLE")
            k=k+1
        
    with open("analisis_archivo.csv", "w") as file:
        file.write("Fecha\tComportamiento de la accion\tPunto medio HIGH-LOW\n")
        
        for i in range(len(Date)):
            file.write('%s\t' % Date[i])
            file.write('%s\t' % comportamiento[i])
            file.write('%s\n' % media[i])
        file.close()
    
    date={}
    lowest=min(Low)
    highest=max(High)
    for i in range(len(Date)):
        if lowest==Low[i]:
            date["date_lowest_price"]=Date[i]
            date["lowest_price"]=Low[i]
        if highest==High[i]:
            date["date_highest_price"]=Date[i]
            date["highest_price"]=High[i]
    
    date["cantidad_veces_sube"]=j
    date["cantidad_veces_baja"]=q
    date["cantidad_veces_estable"]=k
    
    with open("detalles.json", "w") as file:
        json.dump(date,file)
        
print(solucion)