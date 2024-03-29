import pandas

def find_All(col):
    liste = []
    for x in col.find():
        liste.append(x)
    all = pandas.DataFrame(liste)
    return all

#permet de recuperer les differents types de phases dans une collection
def find_Different_Type_Phase(col):
    list = []
    for x in col.distinct('phase'):
        list.append(x)
    return list

#permet de recuperer les phase avec un filtre
def find_Phase_Filtre(col,param):
    liste = []
    myquery = {'phase': {'$in': param}}
    mydoc = col.find(myquery)
    for x in mydoc:
        liste.append(x)
    all = pandas.DataFrame(liste)
    return all

#utilise les 2 fonction d'au dessus pour tout faire
def find_All_Phase(col,list):
    condition = len(list)
    if (condition == 0):
        fichier = find_All(col)
    else:
        fichier = find_Phase_Filtre(col,list)
    return fichier

def count_all_Phase(col,list):
    dict = {}
    for i in range(len(list)):
        dict[list[i]] = col.count_documents({'phase':list[i]})
    return dict