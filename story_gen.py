from assets.actors.client import client
from assets.actors.agent import agent

def story():
    client1 = client()
    agent1 = agent()
    client1.hello()
    agent1.hello()
    client1.hwd()
    agent1.tk()
    client1.tk()   
    client1.qt1()
    agent1.qt1(client1.r, client1.k, client1.cv1)
    agent1.qt2(client1.r, client1.k)
    client1.qt2(client1.r, client1.k, agent1.convos, agent1.convo)
    k = 0
    with open("stories/story.doc","a") as f:

        #checking the topic
        if client1.r == "afi" :
            #checking the gender to use it later to choose the character
            man = ["david","jon","Liam","Noah"]    #to do : use a loop to check the name without knowing which line he is in 
            for i in man:                          # you can use for i in man :                                     #
                if i in client1.convo2[0]:         ## while m<len(client.convo2):
                    gender = "man"                  #    if i in client.convo2[m]:
                    break                           #       gender = "man"
                else:                               #       break
                    gender = "woman"                #    else :
                                                    #        gender = "woman"

            #this loop write the respond of each agent's question
            while k<len(agent1.convo) :
                f.write("agent " + "\"" + agent1.convo[k] + "\"" + "\n" + "client " + "\"" + client1.convo2[k] + "\"" + "\n")
                k+=1
            f.write("gender:"+ gender +"\n")

        elif client1.r == "aai" :
            while k<len(agent1.convo) :
                f.write("agent " + "\""+ agent1.convo[k] + "\""+ "\n" + "client " + "\""+ client1.convo2[k] +"\""+ "\n")
                k+=1

        else :
            if "fee" in client1.k:
                man = ["david","jon","Liam","Noah"]
                for i in man: 
                    if i in client1.convo2[0]:
                        gender = "man"
                        break
                    else:
                        gender = "woman"
                while k<len(agent1.convo) :
                    f.write("agent " + "\"" + agent1.convo[k] + "\"" + "\n" + "client " + "\"" + client1.convo2[k] + "\"" + "\n")
                    k+=1
                f.write("gender:"+ gender +"\n")

            else :
                while k<len(agent1.convo):
                    f.write("agent " + "\"" + agent1.convo[k] + "\"" + "\n" + "client " + "\"" + client1.convo2[k] + "\"" + "\n")
                    k+=1
        
    f.close()

    print("you'll find the stroy in the the stories directory!")
    
story()
