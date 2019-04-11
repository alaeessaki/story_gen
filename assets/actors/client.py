import random
import json

class client() :
    def __init__(self):
        self.greeting = None
        
    #this method generate the greeting conversation     
    def hello (self):

        #reading json file
        with open("assets/data/data.json","r") as f:
            s= f.read()
        data = json.loads(s)

        #pick a random greeting word
        w = []
        for i in data['hello']['hi']:
            w.append(i) 
        self.hi = random.choice(w)  

        #write in file
        with open("stories/story.doc","a") as f:
            f.write("\n" + "client " + "\"" + self.hi + "\"" + "\n")

    #this method generate the first conversation like : "how are you doing..."
    def hwd (self):

        #open json file
        with open('assets/data/data.json',"r") as f:
            s= f.read()
        data = json.loads(s)

        #pick a random sentense
        w = []
        for i in data['hwd']['hwd']:
            w.append(i) 
        self.hwrd = random.choice(w)

        #write in file
        with open("stories/story.doc","a") as f:
            f.write("client " + "\"" + self.hwrd + "\"" + "\n")

    #this method generate a thanking sentense
    def tk(self):

        #read the json file
        with open('assets/data/data.json',"r") as f:
            s= f.read()
        data = json.loads(s)

        #generate a random sentense
        w = []
        for i in data['tk']['tk2']:
            w.append(i) 
        self.ty = random.choice(w)

        #write in file
        with open("stories/story.doc","a") as f:
            f.write("client " + "\"" + self.ty + "\"" + "\n")

    #this methode generate the first question 
    def qt1(self):
        
        #open json file
        with open('assets/data/data.json',"r") as f:
            s = f.read()
        data = json.loads(s)
        w = []
        x = []
        y = []

        #generate a random topic
        for i in data['qt']['qt1']:
            w.append(i) 
        r = random.choice(w)
        self.r = r #self.r will get a value of a topic 

        #generate a random topic relative to the first topic
        for i in data['qt']['qt1'][r]:
            x.append(i)
        k = random.choice(x)
        self.k = k  #self.k will get a value of a topic

        #generate a random topic relative to the first and the second topic
        for i in data['qt']['qt1'][r][k]:
            y.append(i)
        self.cv1 = random.choice(y) #self.cv1 gets the first question 

        #write in file
        with open("stories/story.doc","a") as f:
            f.write("client " + "\"" + self.cv1 + "\"" +"\n")

    #this method generate the other conversations
    def qt2(self,r, k, convos, w):
        
        #####################################################
        # r values :                                        #
        #   "afi" : "asking for insurance"                  #
        #   "aai" : "asking about insurance"                #
        #   "dat" : "declare a statement"                   #
        # k values :                                        #
        #   client.k                                        #
        # convos values                                     #
        #   agent.convos : the number of the conversation   #
        # w value:                                          #
        # agent.convo : the agent questions                 #
        #####################################################



        #read json file
        with open('assets/data/data.json',"r") as f:
            s = f.read()
        data = json.loads(s)
        m = []
        t = 0

        #the first topic
        if r == "afi":
            if "car" in k:
                l = "car"
            elif "motorcycle" in k : 
                l = "motorcycle"
            elif "truck" in k : 
                l = "truck"

            #this loup stock the responds of agent questions in a list called m and affect it in self.convo2
            while t<len(w):
                m.append(random.choice(data['qt']['qt2'][r][l][convos][w[t]]))
                t+=1
            self.convo2 = m

        #the second topic
        elif r == "aai":

            #this loup stock the responds of agent questions in a list called m and affect it in self.convo2
            while t<len(w):
                m.append(random.choice(data['qt']['qt2'][r][k][convos][w[t]]))
                t+=1
            self.convo2 = m
        
        #the third topic
        elif r == "dat":
            if "fee" in k :
                l = "paying insurance fee"
            elif "checking-out" in k:
                l = "check out"
            
            #this loup stock the responds of agent questions in a list called m and affect it in self.convo2
            while t<len(w):
                m.append(random.choice(data['qt']['qt2'][r][l][convos][w[t]]))
                t+=1
            self.convo2 = m

            
        



        

        
