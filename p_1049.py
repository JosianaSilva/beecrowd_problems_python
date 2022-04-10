class_1 = input()
class_2 = input()
class_3 = input()

animal = ""
if (class_1 == "vertebrado"):
    if(class_2 == "ave"):
        if (class_3 == "carnivoro"):
            animal = "aguia"
        elif (class_3 == "onivoro"):
            animal = "pomba"
    elif(class_2 == "mamifero"):
        if (class_3 == "onivoro"):
            animal = "homem"
        elif (class_3 == "herbivoro"):
            animal = "vaca"
elif (class_1 == "invertebrado"):
    if(class_2 == "inseto"):
        if (class_3 == "hematofago"):
            animal = "pulga"
        elif (class_3 == "herbivoro"):
            animal = "lagarta"
    elif(class_2 == "anelideo"):
        if (class_3 == "hematofago"):
            animal = "sanguessuga"
        elif (class_3 == "onivoro"):
            animal = "minhoca"

#print(animal, end=' ')
print('{}'.format(animal))