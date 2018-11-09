import numpy as np
import os,sys

ROOT_DIR = os.path.abspath("../")
sys.path.append(ROOT_DIR)

from core.rlCuber import *
env = rlcuber()
print("Observation = {} ".format(env.observation_space.n))
print("Action = {} ".format(env.action_space.n))
#Initialize table with all zeros
Q = np.zeros([env.observation_space.n,env.action_space.n])
# Set learning parameters
learningrate = .625
discountfactor = .9
num_episodes = 100000
rewardList = []
for i in range(num_episodes):
    #Reset environment and get first new observation
    s = env.reset()
    print("============= ep. "+str(i)+" =============")
    rewardAll = 0
    d = False
    j = 0
    shigh = 0
    #The Q-Table learning algorithm
    while j < 999:
        j+=1
        #Choose an action by greedily (with noise) picking from Q table
        a =np.argmax(Q[s,:] + np.random.randn(1,env.action_space.n)*(1./(i+1)))
        #Get new state and reward from environment
        s1,r,d = env.step(a)
        #Update Q-Table with new knowledge
        Q[s,a] = Q[s,a] + learningrate*(r + discountfactor*np.max(Q[s1,:]) - Q[s,a])
        rewardAll += r
        s = s1
        print("Action = {} State = {} Reward = {}".format(a,s,r))
        if d == True:
            break
    rewardList.append(rewardAll)
    env.render()
print(Q)