#In this part I'll describe the Simpson paradox using pyAgrum
#le probabilità a noi fornite sono le seguenti:
# #gender: [0.5, 0.5]
# drug|gender = male; (with, without): [0.25, 0.75] 
# drug|gender = female; (with, without): [0.75, 0.25] 
# result|gender  = male, drug = without; (sick, healed): [0.60, 0.40]
# result|gender  = male, drug = with; (sick, healed): [0.80, 0.20]
# result|gender  = female, drug = without; (sick, healed): [0.20, 0.80]
# result|gender  = female, drug = with; (sick, healed): [0.30, 0.70]
import pyAgrum as gum
import pyAgrum.lib.notebook as gnb
#define the Bayesian Network, by putting the relation among variables
m1 = gum.fastBN("Gender{F|M}->Drug{Without|With}->Patient{Sick|Healed}<-Gender")
#define the probabilities of the net
pg = [0.5, 0.5]
pd_gm = [0.25, 0.75]
pd_gf = [0.75, 0.25]
m1.cpt("Gender")[:]= pg
m1.cpt("Drug")[:]= [pd_gf,  # drug|gender = female; (with, without): [0.75, 0.25] 
                      pd_gm]  # drug|gender = male; (with, without): [0.25, 0.75] 

m1.cpt("Patient")[{"Drug":"Without","Gender":"F"}]=[0.20, 0.80]
m1.cpt("Patient")[{"Drug":"With","Gender":"F"}]=[0.30, 0.70]
m1.cpt("Patient")[{"Drug":"Without","Gender":"M"}]=[0.60, 0.40]
m1.cpt("Patient")[{"Drug":"With","Gender":"M"}]=[0.80, 0.20]

gnb.flow.row(m1,m1.cpt("Gender"),m1.cpt("Drug"),m1.cpt("Patient"))


#now, I create a function that show us the final probabilties

def getCuredObservedProba(m1, evs):
    evs0 = dict(evs)           #we create a dictionary where we will save the probabilities
    evs1 = dict(evs)
    evs0["Drug"]="Without" 
    evs1["Drug"]="With"
    return gum.Potential().add()









