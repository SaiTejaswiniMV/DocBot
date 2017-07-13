#------------------------Symptoms---------------------------------------------#
viralfever=["fever","get chills","have itchy throat","have cough","have slight body aches","have a mild headache","have weakness"]
commoncold=["cold","have runny or stuffy nose","have sore throat","have cough"," have slight body aches","have a mild headache","sneeze continously","have fever"]
dengue=["fever","get sudden high fever","get severe headaches","get pain behind the eyes","get severe joint and muscle pain","get vomiting","have skin rashes","have mild bleeding in nose,gums"]
asthma=["cough","get frequent cough, especially at night","feel like losing your breath easily or shortness of breath","feel very tired or weak when exercising","have wheezing problem","feel tired, easily upset, grouchy, or moody","have any signs of a cold or allergies (sneezing, runny nose, cough, nasal congestion, sore throat, and headache)","have trouble sleeping"]
arthritis=["get pain in joints","get pain in back, hands, heel, lower back, muscles, neck, or wrist","get early morning joint stiffness or swelling","always get tired","have a general feeling of being unwell","get mild fevers or night sweats","get skin rashes"]
migraines=["severe headache"," it lasts for long time(say lasts from 4 hours to 3 days)","have sensitivity to light, noise, or smells" ," vomit", "have loss of appetite" ,"have  upset stomach or belly pain."]
diabetes=["diabetic","have high glocouse level in blood","have frequent urination","have weakness or tiredness","get more thirsty/hungry","get numbness of toes and fingers","loose your weight","have blurred vision","r wounds take longer time to heal"]
acidity=["stomach pain","is it burning in the  stomach","is it burning in the throat","have restlessness","have indigestion problem","have constipation"]
#jaundice=["fever","have yellowing of skin","have headache and joint pains","have loss of appetite, nausea, vomiting","have irritating rashes "]
sym = {'viralfever': viralfever, 'commoncold': commoncold,'dengue':dengue,'asthma':asthma,'arthritis':arthritis,'migraines':migraines,'diabetes':diabetes,'acidity':acidity}
#------------------------Remedies------------------------------------------#
viralfevermed=["viralfever","If you're uncomfortable, take acetaminophen (Tylenol, others), ibuprofen (Advil, Motrin IB, others) or aspirin. Read the label carefully for proper dosage, and be careful not to take more than one medication containing acetaminophen, such as some cough and cold medicines. Call the doctor if the fever doesn't respond to the medication, is consistently 103 F (39.4 C) or higher, or lasts longer than three days."]
commoncoldmed=["commoncold","Antibiotics are almost never needed to treat a common cold.Use Acetaminophen (Tylenol) and ibuprofen (Advil, Motrin) help lower fever and relieve muscle aches.Use cough syrups only when your cough becomes too painful.Drink plenty of fluids, get enough sleep."]
denguemed=["dengue","No specific treatment for dengue fever exists. Drink plenty of fluids to avoid dehydration high fever. Acetaminophen (Tylenol, others) can alleviate pain and reduce fever. Avoid pain relievers that can increase bleeding complications — such as aspirin, ibuprofen (Advil, Motrin IB, others) and naproxen sodium (Aleve, others).If you have severe dengue fever, you may need supportive care in a hospital"]
asthmamed=["asthma","You may take the following medicines :Humidified oxygen by mask,Salbutamol(10mg)+Ipratropium bromide(0.5mg),Hydrocortisone hemisuccinate (100mg),Cap Amoxicillin (500mg) BDS"]
arthritismed=["arthritis"," Commonly used arthritis medications include:Analgesics (reduce pain) include acetaminophen(Tylenol, others), tramadol (Ultram, Ultracet, others) and narcotics containing oxycodone (Percocet, Oxycontin, others) or hydrocodone (Norco, Vicoprofen).NSAIDs (reduce both pain and inflammation) include ibuprofen (Advil, Motrin IB, others) and naproxen sodium (Aleve).Counterirritants like creams and ointments containing menthol or capsaicin.Physical therapy can be helpful for some types of arthritis.Acupuncture,Glucosamine,Yoga,Massage are alternative remedies.Some types of arthritis may require sugery, so it is better to consult a doctor."]
migrainesmed=["migraine","You may take acetaminophen or naproxen along with a triptan and Ergotamine to stop migraine.To prevent migraine take Anticonvulsants(topiramate), Antidepressants(amitriptyline),Antihistamine(cyproheptadine),Beta-blockers(propranolol),Acupuncture,Massage,Cognitive behavioral therapy etc are alternative remedies."]
diabetesmed=["diabetes","The medication varies based on the type of diabetes, so it is better to consult a doctor and take his/her advice."]
aciditymed=["acidity","You can take PANTODAC-DSR(tablets) or Gelusil(syrup or capsules).Eating bananas,cloves or drinking jeera water may also reduce acidity."]
med={'viralfever':viralfevermed,'commoncold':commoncoldmed,'dengue':denguemed,'asthma':asthmamed,'arthritis':arthritismed,'migraines':migrainesmed,'diabetes':diabetesmed,'acidity':aciditymed}
#-----------------------------------------Confirmation of diesease------------------------------------------------------#

	   
	    
def problem(p):	  
                l=p.split(' ')
                pr=p
                f=[]
                for i in range(len(l)): 
                     if ((l[i]=="have") or (l[i]=="am")):
                                       m=l[i+1:]
                pr=" ".join(m)          
                g=[]
                for i in sym:
                   k=[]
                   for j in sym[i]: 
                         if pr in str(sym[i][0]) :
                               if(pr in j):
                                          continue
                               else:
                                  if j in str(g):
                                          k.append(j)
                                  else:
                                       if "is it " in j:
                                           print("Docbot: ",j,"?")
                                           ans=input("User: ")
                                           k.append(j)
                                       elif " it" in j:
                                           print("Docbot: Does",j,"?")
                                           ans=input("User: ")
                                           if ans=='yes':
                                               k.append(j)
                                       else:
                                               print("Docbot: Do you ",j,"?")
                                               ans=input("User: ")
                                               if ans=='yes':
                                                  k.append(j)      
                   g.append(k)
                   if len(g)==len(sym[i]):
                             break
                h=[]
                for i in range(len(g)) :
                       h.append(len(g[i]))		
                a=h.index(max(h))
                if list(sym.keys())[a] == "diabetes" :
                        if max(h)==len(sym['diabetes']):
                                        print ("Diabetic")
                        else:
                               print("Not diabetic")
                else: 
                      if(max(h)>3):
                              disease=list(sym.keys())[a]
			     # print ("It's  ",list(sym.keys())[a])
                      else:
                            disease="normal"+pr
			      #print ("It's just a normal ",prblm ,"\n")
                      return disease
#-----------------------------------------Medication for diesease------------------------------------------------------#

def medicine(d):
        l=d.split(' ')
        m=[]
        if(len(l)>1):
            for i in range(len(l)): 
                     if (l[i]=="for"):
                                       m=l[i+1:]
            y="".join(m)
            disease=y
        elif (len(l)==1 or len(l)==2) and ("remedy" in l or "medication" in l or "medicine" in l or "cure" in l):
             disease=d
       
        if(disease in med):
                     rem=med[disease][1]
                     #print(rem,disease)
        else: 
                  rem="You got to take rest."
        return rem;
	    
	    
	    
#-------------------------------------------------------------------------------------------------------------------#	    

print("                               DOCBOT                              ")
flag=True
usrHI=input("User: ")
print("Docbot : Hello, I am Docbot ,May I know your name please ?")
usrNm=input("User: ")
print("Docbot :  Hello ",usrNm,", How can I help you?")
prblm = input("User: ")
f=prblm.split(' ')
if(len(f)>1) and ("have" in f or "am" in f):
              dis=problem(prblm)
              print("Docbot: It is ",dis)
          
elif(len(f)>=1) and ("remedy" in f or "medication" in f or "medicine" in f or "cure" in f):
              print("Docbot: ",medicine(prblm))

while flag is True:
              print("Docbot: Any other help?")
              con=input("User :")
              s=con.split(' ')
              if ("No" in s) or ("No,Thanks" in s):
                       flag=False
                       break
              elif(len(s)>1) and ("have" in s or "am" in s):
                         print(con)
                         print("Docbot: It is ",problem(con))
              elif(len(s)>=1) and ("remedy" in s or "medication" in s or "medicine" in s or "cure" in s):
                       print("Docbot: ",medicine(con))
              
print("Docbot: It was my pleasure serving you")
