import gym
import numpy as np
class RME(gym.Env):
  
  def __init__(self):
    self.state_space = np.arange(0,12)
    self.terminal = [3,7]
    self.action_space = [0,1,2,3]         #up ,left ,right ,down
    self.state = 8                     #initial
    self.prev_state = None
    self.left_bd = [0,4,8]
    self.right_bd = [3,7,11]
    self.lower_bd = [8,9,10,11]
    self.up_bd = [0,1,2,3]


  def seed(self,seed):
    np.random.seed(seed)

  def check_validity(self):

    if(self.state==5 ):
      self.state=self.prev_state
    
  def up(self):

     # it is in left bound and up action
      tr = np.random.random()
      if(tr<0.8 and self.state in self.left_bd):   
        if(self.state!=0) :  self.state = self.state - 4
        else : self.state = self.state

      elif(self.state in self.left_bd):  # action= up , but slip in ortho
        if(np.random.random() < 0.5):
          self.state = self.state+1
        else:
          self.state = self.state
      # it is in right bound and up action
      elif(tr<0.8 and self.state in self.right_bd):    # it is in right bound and up action
        if(self.state not in self.terminal) :  self.state = self.state - 4
        else : self.state = self.state

      elif(self.state in self.right_bd):
        if(np.random.random() < 0.5 and self.state not in self.terminal):
          self.state = self.state-1
        else:
          self.state = self.state

      # it is in upper bound and up action
      elif(tr<0.8 and self.state in self.up_bd):   
        self.state = self.state

      elif(self.state in self.up_bd):
        if(np.random.random() < 0.5 and self.state not in self.terminal):
          self.state = self.state+1
        elif(self.state==0):
          self.state = 0
        elif(state!=3) :
          self.state+=1
        else:
          self.state=self.state

       # it is in bottom bound and up action
      elif(tr<0.8 and self.state in self.lower_bd):   
        self.state = self.state+4

      elif(self.state in self.up_bd):
        if(np.random.random() < 0.5 and self.state not in self.left_bd):  #left transition
          self.state = self.state - 1
        elif(self.state not in self.right_bd):
          self.state = self.state + 1
        else:
          self.state=self.state
      
      else:
        if(tr<0.8):
          self.state+=4
        else:
          if(np.random.random()<0.5):
            self.state+=1
          else: 
            self.state-=1

  def left(self):
    
      tr = np.random.random()
      # it is in left bound and left action
      if(tr<0.8 and self.state in self.left_bd):   
        self.state = self.state

      elif(self.state in self.left_bd):  # action= left , but slip in ortho
        if(np.random.random() < 0.5 and self.state!=0):   # up tansition
          self.state = self.state-4
        elif(np.random.random>0.5 and self.state!=8):  #down transition
          self.state +=4
        else:
          self.state = self.state

      # it is in right bound and left action
      elif(tr<0.8 and self.state in self.right_bd):
         if(self.state!=self.terminal):
           self.state-=1
      elif(self.state in self.right_bd):
         if(np.random.random() < 0.5 and self.state not in terminal): #up transition
           self.state-=4

      # it is in upper boundary and left action
      elif(tr<0.8 and self.state  in self.up_bd):   
        if(self.state != 0 and self.state !=3):
          self.state-=1

      elif(self.state in self.up_bd):  # action= left , but slip in ortho
        if(np.random.random() < 0.5 and self.state!=3):   # down
          self.state = self.state+4

      # it is in lower boundary and left action
      elif(tr<0.8 and self.state  in self.lower_bd): 
        if(self.state!=8):
          self.state-=1
      elif(self.state  in self.lower_bd):
        if(np.random.random() < 0.5):
          self.state-=4

      else:
        if(tr<0.8):
          self.state-=1
        else:
          if(np.random.random()<0.5):
            self.state+=4
          else: 
            seelf.state-=4



  def right(self):

      tr = np.random.random()
      # it is in left bound and right action
      if(tr<0.8 and self.state in self.left_bd): 
        #print("idhar tr<0.8 +1")
        self.state+=1
        #print(self.state)

      elif(tr>0.8 and self.state in self.left_bd):
        if(np.random.random() < 0.5 and self.state!=0):  #up transition
          self.state-=4
          #print(self.state)

        elif(np.random.random() > 0.5 and self.state!=8 ): #down
          self.state+=4


      # it is in right bound and right action
      elif(tr<0.8 and self.state in self.right_bd): 
         self.state = self.state

      elif(self.state in self.right_bd):
        if(np.random.random() < 0.5 and self.state not in self.terminal):
          self.state-=4

      # it is in upper bound and right action
      elif(tr<0.8 and self.state in self.up_bd and self.state!=3): 
         self.state = self.state+1

      elif(self.state in self.up_bd):
        if(np.random.random() < 0.5 and self.state not in self.terminal):  #down slip
          self.state+=4

      # it is in lower bound and right action
      elif(tr<0.8 and self.state in self.lower_bd and self.state!=11): 
         self.state = self.state+1

      elif(self.state in self.lower_bd):
        if(np.random.random() < 0.5 and self.state not in self.terminal):  #up slip
          self.state=-4

      else:
        if(tr<0.8):
          self.state+=1
        else:
          if(np.random.random()<0.5):
            self.state+=4
          else: 
            self.state-=4

      

     

  def down(self):
      tr = np.random.random()
      # it is in left bound and down action
      if(tr<0.8 and self.state in self.left_bd and self.state!=8): 
        self.state+=4
        

      elif(self.state in self.left_bd):
        if(np.random.random() < 0.5 and self.state!=0):  #right transition
          self.state+=1

      # it is in right bound and down action
      elif(tr<0.8 and self.state in self.right_bd): 
        self.state = self.state
        

      elif(self.state in self.right_bd):
        if(np.random.random() < 0.5 and self.state==11):  #left transition
          self.state-=1

      ## it is in upper bound and down action
      elif(tr<0.8 and self.state in self.up_bd and self.state not in terminal): 
        self.state = self.state+4
        

      elif(self.state in self.up_bd):
        if(np.random.random() < 0.5 and self.state!=0 and self.state not in terminal):  #left transition
          self.state-=1
        elif(np.random.random() > 0.5 and self.state not in self.terminal):#right
          self.state+=1

       ## it is in lower bound and down action
      elif(tr<0.8 and self.state in self.lower_bd): 
        self.state = self.state
        

      elif(self.state in self.lower_bd):
        if(np.random.random() < 0.5 and self.state!=8):  #left transition
          self.state-=1
        elif(np.random.random() > 0.5 and self.state!=11):#right
          self.state+=1

      
      else:
        if(tr<0.8):
          self.state+=4
        else:
          if(np.random.random()<0.5):
            self.state+=1
          else: 
            seelf.state-=1
      

      
        




  def step(self,action):

   reward = -0.04


   self.prev_state = self.state

   if(action==0):  # up action
      self.up()

   elif(action==1) : # action is left
      self.left()
      
   elif(action==2) : # action is right
      self.right()

   else : # action is down
      self.down()

   self.check_validity()   # check validity of state 
   if(self.state==3): reward = 1
   elif(self.state==7):reward = -1
   
   return self.state,reward

  def reset(self):
    self.state = 8
    
