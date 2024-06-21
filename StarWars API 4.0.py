import requests
from tabulate import tabulate

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


def items(n):
    if n == 1:
        items_list = [
        ['1', 'Luke Skywalker'], ['2', 'C-3PO'], ['3',  'R2-D2'],
        ['4', 'Darth Vader'], ['5',  'Leia Organa'], ['6',  'Owen Lars'],
        ['7', 'Beru Whitesun lars'], ['8', 'R5-D4'], ['9', 'Biggs Darklighter'],
        ['10', 'Obi-Wan Kenobi'], ['11', 'Anakin Skywalker'], ['12', 'Wilhuff Tarkin'],
        ['13', 'Chewbacca'], ['14', 'Han Solo'], ['15', 'Greedo'],
        ['16', 'Jabba Desilijic Tiure'], ['18',  'Wedge Antilles'], ['19', 'Jek Tono Porkins'], 
        ['20', 'Yoda'], ['21', 'Palpatine'], ['22', 'Boba Fett'],
        ['23', 'IG-88'], ['24', 'Bossk'], ['25', 'Lando Calrissian'],
        ['26', 'Lobot'], ['27', 'Ackbar'], ['28', 'Mon Mothma' ],
        ['29', 'Arvel Crynyd'], ['30', 'Wicket Systri Warrick'], ['31', 'Nien Nunb'],
        ['32', 'Qui-Gon Jinn'], ['33', 'Nute Gunray'], ['34', 'Finis Valorum'],
        ['35', 'Padmé Amidala'], ['36', 'Jar Jar Binks'], ['37', 'Roos Tarpals'],
        ['38', 'Rugor Nass'],   ['39', 'Ric Olié'],   ['40', 'Watto'],
        ['41', 'Sebulba'], ['42', 'Quarsh Panaka'], ['43', 'Shmi Skywalker'],
        ['44', 'Darth Maul'], ['45', 'Bib Fortuna'], ['46', 'Ayla Secura'],
        ['47', 'Ratts Tyerel'], ['48', 'Dud Bolt'], ['49', 'Gasgano'], 
        ['50', 'Ben Quadinaros'], ['51', 'Mace Windu'], ['52', 'Ki-Adi-Mundi'], 
        ['53', 'Kit Fisto'], ['54', 'Eeth Koth'], ['55', 'Adi Gallia'],
        ['56', 'Saesee Tiin'], ['57', 'Yarael Poof'], ['58', 'Plo Koon'], 
        ['59', 'Mas Amedda'], ['60', 'Gregar Typho'], ['61', 'Cordé'],
        ['62', 'Cliegg Lars'], ['63', 'Poggle the Lesser'], ['64', 'Luminara Unduli'], 
        ['65', 'Barriss Offee'], ['66', 'Dormé'], ['67', 'Dooku'],
        ['68', 'Bail Prestor Organa'], ['69', 'Jango Fett'], ['70', 'Zam Wesell'],
        ['71', 'Dexter Jettster'], ['72', 'Lama Su'], ['73', 'Taun We'], 
        ['74', 'Jocasta Nu'], ['75', 'R4-P17'], ['76',  'Wat Tambor'],
        ['77', 'San Hill'], ['78', 'Shaak Ti'], ['79', 'Grievous'],
        ['80', 'Tarfful'], ['81', 'Raymus Antilles'], ['82', 'Sly Moore'],
        ['83', 'Tion Medon']]
        
        header = ['ID', 'Name']
        
    elif n==2:
        items_list = [
            ['1', 'Tatooine'], ['2', 'Alderaan'], ['3', 'Yavin IV'], ['4', 'Hoth'],
            ['5', 'Dagobah'], ['6', 'Bespin'], ['7', 'Endor'], ['8', 'Naboo'],
            ['9', 'Coruscant'], ['10', 'Kamino'], ['11', 'Geonosis'], ['12', 'Utapau'],
            ['13', 'Mustafar'], ['14', 'Kashyyyk'], ['15', 'Polis Massa'], ['16', 'Mygeeto'],
            ['17', 'Felucia'], ['18', 'Cato Neimoidia'], ['19', 'Saleucami'], ['20', 'Stewjon'],
            ['21', 'Eriadu'], ['22', 'Corellia'], ['23', 'Rodia'], ['24', 'Nal Hutta'],
            ['25', 'Dantooine'], ['26', 'Bestine IV'], ['27', 'Ord Mantell'], ['28', 'unknown'],
            ['29', 'Trandosha'], ['30', 'Socorro'], ['31', 'Mon Cala'], ['32', 'Chandrila'],
            ['33', 'Sullust'], ['34', 'Toydaria'], ['35', 'Malastare'], ['36', 'Dathomir'],
            ['37', 'Ryloth'], ['38', 'Aleen Minor'], ['39', 'Vulpter'], ['40', 'Troiken'],
            ['41', 'Tund'], ['42', 'Haruun Kal'], ['43', 'Cerea'], ['44', 'Glee Anselm'],
            ['45', 'Iridonia'], ['46', 'Tholoth'], ['47', 'Iktotch'], ['48', 'Quermia'],
            ['49', 'Dorin'], ['50', 'Champala'], ['51', 'Mirial'], ['52', 'Serenno'],
            ['53', 'Concord Dawn'], ['54', 'Zolan'], ['55', 'Ojom'], ['56', 'Skako'],
            ['57', 'Muunilinst'], ['58', 'Shili'], ['59', 'Kalee'], ['60', 'Umbara']
            ]
        
        header = ['ID', 'Planet']
        
    elif n==3:
        items_list = [
            ['1',  'A New Hope'],
            ['2',  'The Empire Strikes Back'],
            ['3',  'Return of the Jedi'],
            ['4', 'The Phantom Menace'],
            ['5', 'Attack of the Clones'],
            ['6', 'Revenge of the Sith']
                      ]
        
        header = ['ID', 'Film']
        
    elif n==4:
        items_list = [
            ['1', 'Human'], ['2', 'Droid'], ['3', 'Wookie'], ['4', 'Rodian'],
            ['5', 'Hutt'], ['6', "Yoda's species"], ['7', 'Trandoshan'],
            ['8','Mon Calamari'], ['9', 'Ewok'], ['10', 'Sullustan'],
            ['11', 'Neimodian'], ['12', 'Gungan'], ['13', 'Toydarian'],
            ['14', 'Dug'], ['15', "Twi'lek"], ['16', 'Aleena'], ['17', 'Vulptereen'],
            ['18', 'Xexto'], ['19', 'Toong'], ['20', 'Cerean'], ['21', 'Nautolan'],
            ['22', 'Zabrak'], ['23', 'Tholothian'], ['24', 'Iktotchi'],
            ['25', 'Quermian'], ['26', 'Kel Dor'], ['27', 'Chagrian'],
            ['28', 'Geonosian'], ['29', 'Mirialan'], ['30', 'Clawdite'],
            ['31', 'Besalisk'], ['32', 'Kaminoan'], ['33', 'Skakoan'],
            ['34', 'Muun'], ['35', 'Togruta'], ['36', 'Kaleesh'],['37', "Pau'an"]
            ]
        
        header = ['ID', 'Specie']
    elif n==5:
        items_list = [
            ['4', 'Sand Crawler'], ['6', 'T-16 skyhopper'], ['7', 'X-34 landspeeder'],
            ['8', 'TIE/LN starfighter'], ['14', 'Snowspeeder'], ['16', 'TIE bomber'],
            ['18', 'AT-AT'], ['19', 'AT-ST'], ['20', 'Storm IV Twin-Pod cloud car'],
            ['24', 'Sail barge'], ['25', 'Bantha-II cargo skiff'],
            ['26', 'TIE/IN interceptor'], ['30', 'Imperial Speeder Bike'],
            ['33', 'Vulture Droid'], ['34', 'Multi-Troop Transport'], 
            ['35', 'Armored Assault Tank'], ['36', 'Single Trooper Aerial Platform'],
            ['37', 'C-9979 landing craft'], ['38', 'Tribubble bongo'],
            ['42', 'Sith speeder'], ['44', 'Zephyr-G swoop bike'],
            ['45', 'Koro-2 Exodrive airspeeder'],['46', 'XJ-6 airspeeder']
                      ]
        
        header = ['ID', 'Vehicle']
        
    elif n==6:
        items_list = [
            ['2', 'CR90 corvette'], ['3', 'Star Destroyer'],
            ['5', 'Sentinel-class landing craft'], ['9', 'Death Star'],
            ['10', 'Millennium Falcon'], ['11', 'Y-wing'], ['12', 'X-wing'],
            ['13', 'TIE Advanced x1'], ['15', 'Executor'], ['17', 'Rebel transport'],
            ['21', 'Slave 1'], ['22', 'Imperial shuttle'],
            ['23', 'EF76 Nebulon-B escort frigate'], ['27', 'Calamari Cruiser'],
            ['28', 'A-wing'], ['29', 'B-wing'], ['31', 'Republic Cruiser'],
            ['32', 'Droid control ship'], ['39', 'Naboo fighter'],
            ['40', 'Naboo Royal Starship'], ['41', 'Scimitar'], 
            ['43', 'J-type diplomatic barge'], ['47', 'AA-9 Coruscant freighter'],
            ['48', 'Jedi starfighter'], ['49', 'H-type Nubian yacht'],
            ['52', 'Republic Assault ship'], ['58', 'Solar Sailer'],
            ['59', 'Trade Federation cruiser'], ['61', 'Theta-class T-2c shuttle'],
            ['63', 'Republic attack cruiser'], ['64', 'Naboo star skiff'],
            ['65', 'Jedi Interceptor'], ['66', 'arc-170'], ['68', 'Banking clan frigte'],
            ['74', 'Belbullab-22 starfighter'], ['75', 'V-wing']
]
        
        header = ['ID', 'Starships']
        
    return print(tabulate(items_list, headers = header, tablefmt = "grid"))
# Define whta's the searching category
tipo=int(input('Please Chose the category you wish to search: '+ 
               '\n 1- People'+
               '\n 2- Planets'+
               '\n 3- Films'+
               '\n 4- Species'+
               '\n 5- Vehicles'+
               '\n 6- Starships'+
               '\n Type the Numer of the desired category-- '))

items(tipo)
num=str(int(input('Type the ID of the Item: ')))


response = requests.get(categoria(tipo)+num+'/')

try:
    file_name = response.json()['name']+'.txt'
except:
    file_name = response.json()['title']+'.txt'

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
                
    elif type(response.json()[i]) == str and 'https' in response.json()[i]:
        re=requests.get(response.json()[i])
        try:
            print('- '+re.json()['name'])
            file.write('- '+re.json()['name']+'\n')
        except:
            print('- '+re.json()['title'])
            file.write('- '+re.json()['title']+'\n')
    else:
        print('-',response.json()[i])
        int_treatment=str(response.json()[i])
        file.write('- '+int_treatment+'\n')
        
    
        
file.close()

                
    
