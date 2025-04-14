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




#Ül6

def sisseastumine():
    n=int(input("Sisestage abiturientide arv: "))
    abiturendid=[]
    punktid=[]

    for i in range(n):
        nimi=input(f"Sisestage abiturendi nimi {i+1}: ")
        punkt=float(input(f"Sisestage {nimi} punktid: "))
        abiturendid.append(nimi)
        punktid.append(punkt)

    return abiturendid,punktid

def kuvada_nimed_ja_punktid(abiturendid,punktid):
    for i in range(len(abiturendid)):
        for j in range(i+1, len(abiturendid)):
            if abiturendid[i]>abiturendid[j]:
                abiturendid[i],abiturendid[j]=abiturendid[j],abiturendid[i]
                punktid[i],punktid[j]=punktid[j],punktid[i]

    print("\nAbiturientide nimekiri tähestikulises järjekorras:")
    for i in range(len(abiturendid)):
        print(f"{abiturendid[i]} - {punktid[i]}")

def vastuvõetud_nimekiri(abiturendid, punktid):
    k=int(input("Mitu inimest võetakse vastu? "))
    nimed=abiturendid[:]
    punktid_copy=punktid[:]

    for i in range(len(punktid_copy)):
        for j in range(i+1, len(punktid_copy)):
            if punktid_copy[i]<punktid_copy[j]:
                punktid_copy[i],punktid_copy[j]=punktid_copy[j],punktid_copy[i]
                nimed[i],nimed[j]=nimed[j],nimed[i]

    print("\nVastuvõetud:")
    for i in range(min(k, len(nimed))):
        print(f"{nimed[i]} - {punktid_copy[i]}")

def halvimad_tulemused(abiturendid, punktid):
    n=int(input("Mitu halvimat tulemust kuvada? "))
    nimed=abiturendid[:]
    punktid_copy=punktid[:]

    for i in range(len(punktid_copy)):
        for j in range(i+1, len(punktid_copy)):
            if punktid_copy[i]>punktid_copy[j]:
                punktid_copy[i],punktid_copy[j]=punktid_copy[j],punktid_copy[i]
                nimed[i],nimed[j]=nimed[j],nimed[i]

    print(f"\n{n} halvimat tulemust:")
    for i in range(min(n, len(nimed))):
        print(f"{nimed[i]} - {punktid_copy[i]}")

def keskmine_vastuvõetute_punktid(punktid):
    k=int(input("Mitu inimest võeti vastu? "))
    punktid_copy=punktid[:]

    for i in range(len(punktid_copy)):
        for j in range(i+1, len(punktid_copy)):
            if punktid_copy[i]<punktid_copy[j]:
                punktid_copy[i],punktid_copy[j]=punktid_copy[j],punktid_copy[i]

    vastuvõetud=punktid_copy[:k]
    if vastuvõetud:
        keskmine=sum(vastuvõetud)/len(vastuvõetud)
        print(f"Sisseastunute keskmine punktisumma: {keskmine:.2f}")
    else:
        print("Vastuvõetud puuduvad.")

#Menu
abiturendid, punktid=sisseastumine()

while True:
    print("\n1 - Kuvage abiturientide nimed koos punktidega tähestikulises järjekorras")
    print("2 - Näidake vastuvõetud isikute nimekiri")
    print("3 - Leidke n halvimat tulemust")
    print("4 - Arvutage vastuvõetute keskmine")
    print("5 - Välju")

    valik=input("Valik: ")

    if valik=="1":
        kuvada_nimed_ja_punktid(abiturendid, punktid)
    elif valik=="2":
        vastuvõetud_nimekiri(abiturendid, punktid)
    elif valik=="3":
        halvimad_tulemused(abiturendid, punktid)
    elif valik=="4":
        keskmine_vastuvõetute_punktid(punktid)
    elif valik=="5":
        print("Programm lõpetati.")
        break
    else:
        print("Vale valik. Proovi uuesti.")

