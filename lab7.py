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
import pyAgrum.causal as csl
import pyAgrum.causal.notebook as cslnb
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
    evs0["Drug"]="Without"  #aggiungo al path drug con attributi with e 
    evs1["Drug"]="With"     #without
    return( gum.Potential()
            .add(m1.variablesFromName("Drug")) #I retrive the variables
            .fillWith([gum.getPosterior(m1,target="Patient",evs=evs0)[1], #I retrive the probabilities
                        gum.getPosterior(m1,target="Patient",evs=evs1)[1]
              ])
    )


gnb.sideBySide(getCuredObservedProba(m1,{}),                   #crea le tabelle graficamente
               getCuredObservedProba(m1,{'Gender':'F'}),
               getCuredObservedProba(m1,{'Gender':'M'}),
               captions=["$P(Patient = Healed \mid Drug )$<br/>Taking $Drug$ is observed as efficient to cure",
                         "$P(Patient = Healed \mid Gender=F,Drug)$<br/>except if the $gender$ of the patient is female",
                         "$P(Patient = Healed \mid Gender=M,Drug)$<br/>... or male."])



d1 = csl.CausalModel(m1)   #costruisco il modello poi rappresentabile
cslnb.showCausalModel(d1)



cslnb.showCausalModel(d1, "Patient", doing="Drug", values={"Drug":"Without"} ) #crea anche la tabella

#esercizio 2 
#costruire una rete per il modello cloud, rain, sprinkler, grass wet
m2 = gum.fastBN("Cloud{No|Yes}->Rain{No|Yes}->GrassWet{No|Yes}<-Sprinkler{No|Yes}<-Cloud")

#definisco le probabilità

m2.cpt("Cloud")[:]= [0.5, 0.5]                                         #inserisco i condizionamenti tipo dizionario
m2.cpt("Rain")[{"Cloud":"Yes"}]=[0.2, 0.8]
m2.cpt("Rain")[{"Cloud":"No"}]=[0.9, 0.1]
m2.cpt("Sprinkler")[{"Cloud":"Yes"}]=[0.9, 0.1]
m2.cpt("Sprinkler")[{"Cloud":"No"}]=[0.5, 0.5]
m2.cpt("GrassWet")[{"Rain":"No","Sprinkler":"No"}]=[0.9, 0.1]
m2.cpt("GrassWet")[{"Rain":"Yes","Sprinkler":"No"}]=[0.1, 0.9]
m2.cpt("GrassWet")[{"Rain":"No","Sprinkler":"Yes"}]=[0.1, 0.9]
m2.cpt("GrassWet")[{"Rain":"Yes","Sprinkler":"Yes"}]=[0.05, 0.95]

ie = gum.LazyPropagation(m2)
ie.setEvidence({"Rain":"Yes"})
result = ie.posterior("GrassWet")
print(result)


ie2 = gum.LazyPropagation(m2)
ie2.setEvidence({"Sprinkler":"Yes"})
result2 = ie2.posterior("GrassWet")
print(result2)

ie3 = gum.LazyPropagation(m2)
ie3.setEvidence({"Sprinkler":"No"})
result3 = ie3.posterior("GrassWet")
print(result3)

print(result2[1] - result3[1])











