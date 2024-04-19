import requests

def categoria(n):
    if n ==1:
        url='https://swapi.dev/api/people/'
    elif n==2:
        url='https://swapi.dev/api/planets/'
    elif n==3:
        url='https://swapi.dev/api/films/'
    elif n==4:
        url='https://swapi.dev/api/species/'
    elif n==5:
        url='https://swapi.dev/api/vehicles/'
    elif n==6:
        url='https://swapi.dev/api/starships/'
        
    return url


# Definir qual a categoria da busca
tipo=int(input('Escolha uma das categorias: '+#Pede para o usuário escolher a categoria.
               '\nPeople(1):'+
               '\nPlanets(2):'+
               '\nFilms(3):'+
               '\nSpecies(4):'+
               '\nVehicles(5):'+
               '\nStarships(6): '))
# Definir qual elemento é buscado 
num=str(int(input('Digite um número identificador: ')))

# Buscar os dados do que foi selecionado
response=requests.get(categoria(tipo)+num+'/')
#Criar o Arquivo
try:
    file_name=response.json()['name']+'.txt'
except:
    file_name=response.json()['title']+'.txt'

file=open(file_name,"w")

for i in response.json().keys():
    print(i+':')    
    file.write(i+': \n')
    if type(response.json()[i])==list:
        
        for ele in response.json()[i]:
            resp=requests.get(ele)
            
            try:
                print('-',resp.json()['name'])
                file.write('- '+resp.json()['name']+'\n')
            except:
                print('-',resp.json()['title'])
                file.write('- '+resp.json()['title']+'\n')
                
    elif 'https' in response.json()[i]:
        re=requests.get(response.json()[i])
        print('- '+re.json()['name'])
        file.write('- '+re.json()['name']+'\n')
        
    else:
        print('-',response.json()[i])
        int_treatment=str(response.json()[i])
        file.write('- '+int_treatment+'\n')
        
file.close()

                
    
