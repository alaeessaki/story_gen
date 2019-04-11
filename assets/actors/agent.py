import random
import json


#you can learn how this tool works in client class's comments 
#this class works exactly like the client class

class agent() :
    def __init__(self):
        self.greeting = None
    
    #this method generate the greeting conversation     
    def hello (self):
        #reading json file
        with open('assets/data/data.json',"r") as f:
            s= f.read()
        data = json.loads(s)

        #pick a random greeting word
        w = []
        for i in data['hello']['hi']:
            w.append(i) 
        self.hi = random.choice(w)
        
        #write in file
        with open("stories/story.doc","a") as f:
            f.write("agent " + "\"" + self.hi + "\"" + "\n")

    def tk (self):
        with open('assets/data/data.json',"r") as f:
            s= f.read()
        data = json.loads(s)
        w = []
        for i in data['tk']['tk1']:
            w.append(i) 
        self.ty = random.choice(w)
        with open("stories/story.doc","a") as f:
            f.write("agent " + "\"" + self.ty + "\""+"\n")
    
    def qt1(self, r, k, q):
        with open('assets/data/data.json',"r") as f:
            s= f.read()
        data = json.loads(s)
        w = []

        for i in data['qt']['qt1'][r][k][q]:
            w.append(i)
        self.cv1 = random.choice(w)
        
        with open("stories/story.doc","a") as f:
            f.write("agent " + "\"" + self.cv1 + "\"" + "\n")
    def qt2(self, r, k):
        with open('assets/data/data.json',"r") as f:
            s= f.read()
        data = json.loads(s)
        w = []
        x = []
        if r == "afi":
            if "car" in k: 
                l = "car"
            elif "motorcycle" in k : 
                l = "motorcycle"
            elif "truck" in k : 
                l = "truck"
            for i in data['qt']['qt2'][r][l]:
                w.append(i)
            convos = random.choice(w)
            self.convos = convos
            for i in data['qt']['qt2'][r][l][convos]:
                x.append(i)
            self.convo = x

        elif r == "aai":
            for i in data['qt']['qt2'][r][k]:
                w.append(i)
            convos = random.choice(w) 
            self.convos = convos
            for i in data['qt']['qt2'][r][k][convos]:
                x.append(i)
            self.convo = x 
        elif r == "dat":
            if "fee" in k :
                l = "paying insurance fee"
            else : 
                l = "check out"
            for i in data['qt']['qt2'][r][l]:
                w.append(i)
            convos = random.choice(w)
            self.convos = convos
            for i in data['qt']['qt2'][r][l][convos]:
                x.append(i)
            self.convo = x 
            

        

        
