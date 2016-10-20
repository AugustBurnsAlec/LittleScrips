#--------------------------------------------------------------------------------------------------------------------------------------------------------------]
# Created by: Alec Sherlock
# Date : 3-25-2016
# Description: This program recieves a users Leage of Legends champion and desired guide website through textboxes in a basic GUI. The program then opens the
#              desired guide website for the users champion.
# Version Number: 1.0
#--------------------------------------------------------------------------------------------------------------------------------------------------------------]

#CONSTANT DEFINITIONS---------------------------------
LABELTEXT1 = "Welcome to Alec's League Guide Script"
LABELTEXT2 = 'Enter your Champion Name'
LABELTEXT3 = 'Enter your desired guide website \n( 1 for Lolking 2 for Mobafire )'
#-----------------------------------------------------


#uses tkinter to create GUI and webbrowser to open a web browser based off a given URL
from tkinter import *
import webbrowser

#Fuction that opens the web page
def openUserWebsiteWithChampion():
    champ = userChamp.get()
    site = userWebsite.get()
    champ = champ.lower()
#dictionary of all champions. k , v = champion name, champion release number
    championDict = {'lux': '62', 'kassadin': '27', 'twisted-fate': '28','twistedfate': '28', 'zac': '112', 'skarner': '81', 'akali': '50', 'morgana': '16',
                    'kogmaw': '54', 'ryze': '5', 'yasuo': '117', 'karthus': '21', 'zilean': '17', 'bard': '124', 'azir': '121',
                    'draven': '99', 'fizz': '87', 'cassiopeia': '66', 'ziggs': '92', 'taric': '32', 'fiddlesticks': '38', 'lulu': '95',
                    'illaoi': '128', 'riven': '83', 'velkoz': '118', 'rammus': '24', 'swain': '61', 'pantheon': '44', 'urgot': '58',
                    'orianna': '77', 'miss-fortune': '59','missfortune': '59', 'renekton': '68', 'shyvana': '86', 'wukong': '80', 'thresh': '110', 'rumble': '75',
                    'corki': '31', 'volibear': '88', 'malzahar': '52', 'yorick': '78', 'aurelion-sol': '130', 'aurelionsol': '130', 'poppy': '43',
                    'gnar': '120', 'lissandra': '113', 'udyr': '39', 'ekko': '125', 'soraka': '8', 'dr-mundo': '26','drmundo': '26', 'nidalee': '42', 'vi': '109',
                    'brand': '74', 'ezreal': '47', 'sivir': '7', 'jax': '15', 'lee-sin': '73', 'tristana': '10',
                    'xin-zhao': '55','xinzhao': '55', 'twitch': '20', 'leona': '79', 'hiemerdinger': '40', 'varus': '97', 'fiora': '94', 'trundle': '65', 'master-yi': '3',
                    'talon': '82', 'nami': '108', 'vladimir': '56', 'evelynn': '19', 'sion': '6', 'jinx': '116',
                    'leblanc': '63', 'khazix': '105', 'nautilus': '93', 'gangplank': '30', 'quinn': '111', 'kalista': '122', 'sona': '60', 'sejuani': '91',
                    'masteryi': '3', 'hecarim': '96', 'graves': '85', 'chogath': '22', 'zed': '107', 'jarvan-iv': '71',
                    'aatrox': '114', 'garen': '51', 'nunu': '12', 'zyra': '101', 'vayne': '76', 'lucian': '115', 'jhin': '129', 'annie': '1', 'syndra': '104',
                    'amumu': '23', 'katarina': '36', 'alistar': '4', 'xerath': '84', 'kindred': '127',
                    'jayce': '100', 'elise': '106', 'rengar': '103', 'kayle': '2', 'blitzcrank': '34', 'shaco': '41', 'singed': '18', 'caitlyn': '67', 'tryndamere': '14',
                    'ahri': '89', 'darius': '98', 'teemo': '9', 'braum': '119', 'malphite': '35',
                    'gragas': '45', 'veigar': '33', 'janna': '29', 'mordekaiser': '46', 'tahm-kench': '126','tahmkench': '126', 'ashe': '13', 'nasus': '37', 'warwick': '11', 'reksai': '123',
                    'galio': '57', 'maokai': '70', 'kennen': '49', 'shen': '48', 'viktor': '90',
                    'olaf': '53', 'anivia': '25', 'diana': '102', 'irelia': '64', 'karma': '69', 'nocturne': '72'}

    if site == '1':
        url = 'http://www.lolking.net/champions/'+champ+'#guides'
        webbrowser.open_new_tab(url)
    elif site == '2':
        url = 'http://www.mobafire.com/league-of-legends/champion/'+champ+'-'+championDict[champ]
        webbrowser.open_new_tab(url)
   
#Creating basic GUI
myGUI = Tk()
myGUI.geometry('400x200+100+200')
myGUI.title('The League Guide Script')

#Set to empty value
userChamp = StringVar()
userWebsite = StringVar()



# Labels on GUI
label1 = Label(myGUI, text = LABELTEXT1, fg = 'red').grid(row = 0, column = 1)
label2 = Label(myGUI, text = LABELTEXT2, fg = 'blue').grid(row = 1, column = 1)
label3 = Label(myGUI, text = LABELTEXT3 , fg = 'blue').grid(row = 2, column = 1)

# Text boxes for user input
theUserChampion = Entry(myGUI , textvariable = userChamp).grid(row = 1, column = 2)
theUserWebsite = Entry(myGUI , textvariable = userWebsite).grid(row = 2, column = 2)


#clickable button to open webbrowser
button1 = Button(myGUI , text = 'Open Guide Page', command = openUserWebsiteWithChampion).grid(row = 3, column = 2)





#GUI MAIN LOOP
myGUI.mainloop()
