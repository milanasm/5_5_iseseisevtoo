#Ül9
import random

def lapsed():
    n=int(input("Sisestage laste arv: "))
    nimed=[]
    keskmised_hinnad=[]

    for i in range(n):
        nimi=input(f"Sisestage lapse nimi {i+1}: ")
        nimed.append(nimi)
        score=round(random.uniform(1, 5), 2)
        keskmised_hinnad.append(score)

    return nimed, keskmised_hinnad

def Sorted_names(nimed, keskmised_hinnad):
    sorted_names=sorted(zip(nimed, keskmised_hinnad))
    print("\nLaste nimed koos hinnetega:")
    for name, score in sorted_names:
        print(f"{name} - {score}")

def Best_students(nimed, keskmised_hinnad):
    max_score=max(keskmised_hinnad)
    best_students=[]
    for i in range(len(nimed)):
        if keskmised_hinnad[i]==max_score:
            best_students.append(nimed[i])
    if best_students:
        print("Suurepärane üliõpilane(d):", ', '.join(best_students))
    else:
        print("Suurepäraseid õpilasi pole.")

def Avg_score(nimed, keskmised_hinnad):
    avg_score=sum(keskmised_hinnad)/len(keskmised_hinnad)
    print(f"Kõigi laste keskmine hinnang: {avg_score:.2f}")

def Konkreetse_lapse_keskmine_hinnang(nimed, keskmised_hinnad):
    name_to_find=input("Sisestage otsimiseks lapse nimi: ")
    counter=0
    for i in range(len(nimed)):
        if nimed[i]==name_to_find:
            print(f"{name_to_find}-{keskmised_hinnad[i]}")
            counter=counter+1
    if counter==0:
        print(f"Last nimega {name_to_find} ei leitud.")


#Menu
nimed, keskmised_hinnad=lapsed()

while True:
    print("\n1 - Kuvage laste nimed koos hinnetega")
    print("2 - Näidake suurepärast õpilast, kui neid on")
    print("3 - Leidke kõigi laste keskmine hinne")
    print("4 - Leidke nime järgi konkreetse lapse hinne")
    print("5 - Välju")
    
    v=input("Valik: ")
    
    if v=="1":
        Sorted_names(nimed, keskmised_hinnad)
    elif v=="2":
        Best_students(nimed, keskmised_hinnad)
    elif v=="3":
        Avg_score(nimed, keskmised_hinnad)
    elif v=="4":
        Konkreetse_lapse_keskmine_hinnang(nimed, keskmised_hinnad)
    elif v=="5":
        break
    else:
        print("Vale valik. Proovi uuesti.")

