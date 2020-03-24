import socket, threading, itertools, os, time
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from queue import Queue
from datetime import datetime

class ClientThread(threading.Thread):

    id_iter = itertools.count(start=1)
    L = []

    def add(self):
        cnt = 0
        for i in range(len(self.L)):
            if self.L[i] == 0:
                self.L[i]=self.id
                break
            cnt+=1
        if cnt == len(self.L):
            self.L.append(self.id)

    def remove(self):
        for i in range(len(self.L)):
            if self.L[i] == self.id:
                self.L[i]=0

    def check(self):
        for i in range(len(self.L)):
            if self.L[i] == self.id:
                return i
                      
                
    def __init__(self,clientAddress,clientsocket,out_q):
        self.info = clientAddress
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        self.id = next(self.id_iter)
        self.q=out_q
        #ajout de l'id du thread client dans la queue
        self.add()
        self.idf = self.check()+1
        out_q.put(self.idf)
        print ("Nouvelle connexion ajoutée: ", self.info)
        
    def run(self):
        try:
            print ("Connexion depuis : ", self.info)
            self.csocket.send(bytes("Bienvenue dans le serveur d'irrigation intelligente\nQuittez le serveur en envoyant 'bye'",'utf-8'))
            msg = ''
            cnt=0    
            f=open("log_"+str(self.idf)+".txt","w")
            f.write("0,0,0,0\n")
            newGraph = GraphThread(self.q)
            newGraph.start()
            while True:
                f=open("log_"+str(self.idf)+".txt","a")
                data = self.csocket.recv(2048)
                msg = data.decode()
                if msg=='bye':
                    break
                print ("Message du client ",self.info," :", msg)
                #self.csocket.send(bytes("Entrez une donnée: \n",'UTF-8'))
                #écriture des données associé au client dans un fichier log
                t = datetime.now().strftime("%H:%M:%S")
                #prendre en compte l'humidité de l'air et la température
                f.write(str(cnt)+","+msg+"\n")
                cnt+=1
        except:
            self.remove()
            newGraph.running = False
            print ("Le client", clientAddress , " s'est déconnecté.")

class GraphThread(threading.Thread):
    def __init__(self,in_q):
        threading.Thread.__init__(self)
        self.id = in_q.get()

    def graph(self):
        plt.clf()
        x, z, v, y = np.loadtxt('log_'+str(self.id)+'.txt', delimiter=',',unpack=True)
        y = 100 - (100*y/1000)
        y = (y-30)*2
        
        plt.plot(x,y, label='KY70')
        plt.xlabel('Temps')
        plt.ylabel('Indice d\'humidité (%)')
        plt.title('Taux d\'humidité de sol sur le secteur '+str(self.id))
        plt.legend()
        plt.savefig("log_"+str(self.id)+"a.png")
        plt.clf()
        
        plt.plot(x,z, label='DHT11')
        plt.xlabel('Temps')
        plt.ylabel('Indice d\'humidité (%)')
        plt.title('Taux d\'humidité de l\'air sur le secteur '+str(self.id))
        plt.legend()
        plt.savefig("log_"+str(self.id)+"b.png")
        plt.clf()
        
        plt.plot(x,v, label='DHT11')
        plt.xlabel('Temps')
        plt.ylabel('Température (°C)')
        plt.title('Température sur le secteur '+str(self.id))
        plt.legend()
        plt.savefig("log_"+str(self.id)+"c.png")
        
    def run(self):
        self.running = True
        time.sleep(2.0)
        startTime = time.time()
        print("Graph for client"+str(self.id)+" and ky70\n")
        while self.running:
            self.graph()
            t0 = datetime.now().strftime("%H:%M:%S")
            print(t0+" : Graph generated for the Client "+str(self.id))
            time.sleep(5.0-((time.time()-startTime)%5.0))
        print("GraphThread for Client "+str(self.id)+" has been interrupted\n")
        
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('',15555))
print("Le serveur d'irrigation intelligente s'est démarré avec succès")
print("En attente de requêtes clients")
while True:
    server.listen(5)
    clientsock, clientAddress = server.accept()
    q = Queue()
    newClient = ClientThread(clientAddress, clientsock,q)
    newClient.start()
