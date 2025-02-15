print("Demarrage 'MENU.py'")
def MENU_clear():
    hint("",1)
    hint("",2)
    hint("",3)
    hint("",4)
def MENU_menuPrincipal():
    MENU_clear()
    hint(str(setting.nomBox)+"-"+str(setting.numeroBox)+"|"+str(int(setting.rezalNet))+str(int(setting.rezalOn))+str(int(setting.rezalMode))+"|V"+str(setting.version),1)
    MENU_getMenu(config.menuPrincipal)
def MENU_menuAdmin():
    MENU_getCode(config.codeAdmin,"menuAdmin")
    MENU_getMenu(config.menuAdmin)
def MENU_menuModerateur():
    MENU_getCode(config.codeModerateur,"menuModerateur")
    MENU_getMenu(config.menuModerateur)
def MENU_menuHelpeur():
    MENU_getCode(config.codeHelpeur,"menuHelpeur")
    MENU_getMenu(config.menuHelpeur)
def MENU_menuVP():
    MENU_getCode(config.codeVP,"menuVP")
    MENU_getMenu(config.menuVP)
def MENU_menuUser():
    MENU_getCode(config.codeUser,"menuUser")
    MENU_getMenu(config.menuUser)
def MENU_setNumeroBox():
    NUM=""
    hint("ENTREZ LE NUMERO BOX",4)
    while True:
        _touche=CLAVIER_get()
        if (_touche==10):
            try:
                DATA_setVariable("numeroBox",int(NUM))
                return
            except:
                pass
        elif (_touche in [46,127]):
            if (len(NUM)!=0):
                NUM=NUM[0:-1]
            else:
                pass
        elif(_touche in [48,49,50,51,52,53,54,55,56,57]):
            NUM=(str(NUM)+chr(_touche))
        elif (_touche==47):
            REZAL_restart()
        elif (_touche==42):
            REZAL_reboot()
        elif (_touche==45):
            REZAL_exit()
        hint("NUMERO: "+NUM,4)
def MENU_setRezalMode():
    DATA_setVariable('rezalMode',not(setting.rezalMode))
    hint(str(not(setting.rezalMode))+" -> "+str(setting.rezalMode),4)
    CLAVIER_get()
def MENU_setIPServeur():
    IP=""
    hint("IP: "+str(setting.connection["host"]),4)
    while True:
        _touche=CLAVIER_get()
        if (_touche==10):
            if IP=="":
                return
            if len(IP.split("."))>=4:
                DATA_setVariable('connection["host"]',IP)
                return
            else:
                IP=IP+"."
        elif (_touche in [46,127]):
            if (len(IP)!=0):
                IP=IP[0:-1]
            else:
                pass
        elif (_touche in [48,49,50,51,52,53,54,55,56,57]):
            IP=str(IP)+chr(_touche)
        elif (_touche==47):
            return REZAL_restart()
        elif (_touche==42):
            REZAL_reboot()
        elif (_touche==45):
            REZAL_exit()
        hint("IP: "+IP,4)
def MENU_setLoginBDD():
    return
def MENU_setMDPBDD():
    return
def MENU_MAJGitClone():
    if setting.rezalNet:
        hint("Direction /home/pi",4)
        os.chdir("/home/pi")
        hint("Suppr FONCTIONS",4)
        os.system("sudo rm -r PICONFLEX2000-FONCTIONS")
        hint("git clone FONCTIONS",4)
        if os.system("sudo git clone https://github.com/REZALKIN/PICONFLEX2000-FONCTIONS.git")!=0:
            hint("Echec git clone",4)
            REZAL_exit()
        hint("Suppr CLIENT",4)
        os.system("sudo rm -r PICONFLEX2000-CLIENT")
        hint("git clone CLIENT",4)
        if os.system("sudo git clone https://github.com/REZALKIN/PICONFLEX2000-CLIENT.git")!=0:
            hint("Echec git clone",4)
            REZAL_exit()
        hint("git clone reussi! :)",4)
        REZAL_restart()
    else:
        hint("Pas d'internet",4)
        CLAVIER_get()
        hint("",4)
def MENU_githubPull():
    if setting.rezalNet:
        hint("Direction FONCTIONS",4)
        os.chdir("/home/pi/PICONFLEX2000-FONCTIONS")
        hint("git pull FONCTIONS",4)
        if os.system("sudo git pull")!=0:
            hint("Echec pull FONCTIONS",4)
            REZAL_exit()
        hint("Direction CLIENT",4)
        os.chdir("/home/pi/PICONFLEX2000-CLIENT")
        hint("git pull CLIENT",4)
        if os.system("sudo git pull")!=0:
            hint("Echec pull CLIENT",4)
            REZAL_restart()
        hint("git pull reussi ! :)",4)
        REZAL_restart()
    else:
        hint("Pas d'internet",4)
        CLAVIER_get()
        hint("",4)
def MENU_getCode(code,texte):
    _txt=""
    while True:
        hint(texte,3)
        hint("CODE: "+"*"*len(_txt),4)
        _touche=CLAVIER_get()
        if (_touche in [46,127]):
            if (len(_txt)!=0):
                _txt=_txt[0:-1]
            else:
                pass
        elif(_touche in [48,49,50,51,52,53,54,55,56,57]):
            _txt=str(_txt)+chr(_touche)
        elif (_touche==47):
            REZAL_restart()
        elif (_touche==42):
            REZAL_reboot()
        elif (_touche==45):
            REZAL_exit()
        try:
            if int(_txt) ==code or int(_txt)==codeGuinche:
                return
        except:
            pass
def MENU_getMontant(argent):
    montant=""
    while True:
        if (montant==""):
            hint("ENTRER LE MONTANT",4)
            montant=0
        else:
            hint("Montant: "+STRING_montant(montant),4)
        if setting.nomBox[0]=="C":
            hint(STRING_montant(argent)+" -> "+STRING_montant(int(montant)+argent),2)
        elif setting.nomBox[0]=="K":
            hint(STRING_montant(argent)+" -> "+STRING_montant(int(montant)-argent),2)
        _touche=CLAVIER_getRFID()
        if (_touche==0):#carte retiree
            return 0
        elif (_touche==10):#_touche entrer
            if (montant==""):
                pass
            elif (int(montant)<config.minMontant):
                hint("Montant Trop bas",4)
                sleep(1)
            elif ((int(montant)+argent>config.maxMontant)and((setting.nomBox[0]=="C"))):
                hint("Total Trop haut",4)
                sleep(1)
            elif ((int(montant)>config.maxTransaction)and((setting.nomBox[0]=="C"))):
                hint("Montant Trop haut",4)
                sleep(1)
            else:
                return int(montant)
        elif (_touche in [46,127]):#touches del/backspace
            if (len(montant)!=0):
                montant=montant[0:-1]
            else:
                pass
        elif(_touche in [48,49,50,51,52,53,54,55,56,57]):#touches 0,1,2,3,4,5,6,7,8,9
            montant=str(montant)+chr(_touche)
        elif (_touche==43):#_touche +
            if (montant==""):
                montant=str(500)
            elif (int(montant)<500):
                montant=str(500)
            elif (int(montant)<1000):
                montant=str(1000)
            elif (int(montant)<2000):
                montant=str(2000)
            elif (int(montant)<5000):
                montant=str(5000)
            elif (int(montant)<10000):
                montant=str(10000)
            elif (int(montant)<20000):
                montant=str(20000)
            elif (int(montant)<50000):
                montant=str(50000)
        elif (_touche==45):#_touche -
            if (montant==""):
                montant=""
            elif (int(montant)>50000):
                montant=str(50000)
            elif (int(montant)>20000):
                montant=str(20000)
            elif (int(montant)>10000):
                montant=str(10000)
            elif (int(montant)>5000):
                montant=str(5000)
            elif (int(montant)>2000):
                montant=str(2000)
            elif (int(montant)>1000):
                montant=str(1000)
            elif (int(montant)>500):
                montant=str(500)
        elif (_touche==42):#_touche *
            REZAL_reboot()
        elif (_touche==47):
            return REZAL_restart()
def MENU_getCommande(argent):
    reference=""
    produit=""
    montant=0
    nombre=1
    while True:
        if reference=="":
            hint("ENTRER UNE REFERENCE",4)
            nombre=1
            produit=""
            montant=0
        else:
            try:
                produit,montant=setting.produits[int(reference)]
                hint(reference+": "+produit,4)
            except:
                produit=""
                montant=0
                nombre=1
                hint(reference+": INEXISTANT",4)
        montant=-montant*nombre
        if argent+montant>=0:
            hint(STRING_montant(argent)+" -> "+STRING_montant(int(argent)+montant)+" ("+str(nombre)+")",2)
        else:
            hint("Argent insuffisant",4)
        _touche=CLAVIER_getRFID()
        if (_touche==0):#carte retiree
            return (montant,nombre,produit,0)
        elif (_touche==10):#_touche entrer
            if (reference==""):
                pass
            else:
                if (str(produit)==""):
                    pass
                elif argent+montant>=0:
                    return (int(reference),nombre,produit,montant)
                else:
                    hint("Montant insuffisant",4)
        elif (_touche in [46,127]):#_touche del/backspace
            if (len(reference)!=0):
                reference=reference[0:-1]
            else:
                pass
        elif(_touche in [48,49,50,51,52,53,54,55,56,57]):#touches 0,1,2,3,4,5,6,7,8,9
            if len(reference)<3:
                reference=str(reference)+chr(_touche)
        elif (_touche==43):#_touche +
            nombre=min(9,max(nombre+1,1))#ajoute une produit
        elif (_touche==45):#_touche -
            nombre=min(9,max(nombre-1,1))#retire un produit
        elif (_touche==47):
            return REZAL_restart()
        elif (_touche==42):
            REZAL_reboot()
def MENU_getMenu(MENUS):
    _num=0
    _menu=MENUS[0]
    _touche=1
    while True:
        if _touche==0:#Carte retiree
            return
        elif(_touche in [48,49,50,51,52,53,54,55,56,57]):#touches numpad
            _num=int(chr(_touche))
        elif _touche==10:#Touche entrer
            if _menu!=MENUS[0]:
                exec('MENU_'+_menu+'()')
                return MENU_getMenu(MENUS)
            else:
                return
        elif (_touche==47):#Touche /
            REZAL_restart()
        elif (_touche==42):#Touche *
            REZAL_reboot()
        try:
            _menu=MENUS[_num]
        except:
            _menu=MENUS[0]
        hint("Menu "+MENUS[0],2)
        if _menu!=MENUS[0]:
            hint(_menu,3)
        else:
            hint("",3)
        _touche=CLAVIER_getNotRFID()
def MENU_resetBDD():
    return
def MENU_viewMAC():
    hint(setting.MAC,4)
    CLAVIER_get()
def MENU_viewIP():
    hint(setting.IP,4)
    CLAVIER_get()
def MENU_viewIPServeur():
    hint(setting.connection["host"],4)
    CLAVIER_get()
def MENU_viewPing():
    hint("PING INTERNET: ...",4)
    hint("PING INTERNET: "+str(REZAL_pingInternet()),4)
    CLAVIER_get()
    hint("PING SERVEUR: ...",4)
    hint("PING SERVEUR: "+str(REZAL_pingServeur()),4)
    CLAVIER_get()
def MENU_resetCarteRFID():
    hint("PRESENTEZ LA CARTE",4)
    RFID_resetCarte()
    RFID_waitRetireCarte()
def MENU_resetCarteBDD():
    UID=RFID_getUID()
    SQL_EXECUTE(QUERRY_setMontant(UID,0))
    SQL_EXECUTE(QUERRY_addLog(setting.numeroBox,setting.nomBox,"RESET CARTE BDD",str(UID)))
    RFID_waitRetireCarte()
def MENU_resetLogQuerry():
    os.system("sudo rm /home/pi/PICONFLEX2000-LOGS/LOG_QUERRY.txt")
    CLAVIER_get()
def MENU_resetLogSQL():
    os.system("sudo rm /home/pi/PICONFLEX2000-LOGS/LOG_SQL.txt")
    CLAVIER_get()
def MENU_resetLogError():
    os.system("sudo rm /home/pi/PICONFLEX2000-LOGS/LOG_ERROR.txt")
    CLAVIER_get()
def MENU_resetLogs():
    os.system("sudo rm -r /home/pi/PICONFLEX2000-LOGS")
    CLAVIER_get()
def MENU_setNomBox():
    return
def MENU_fusionCartes():
    return
def MENU_setCaisse():
    setting.nomBox="C"
def MENU_setKve():
    setting.nomBox="K"
def MENU_supprimerTransaction():
    return
def MENU_resetCarte():
    RFID_resetCarte()
    SQL_EXECUTE(QUERRY_setMontant(RFID_getUID(),0))
    SQL_EXECUTE(QUERRY_addLog(setting.numeroBox,setting.nomBox,"RESET CARTE BDD",str(RFID_getUID())))
    RFID_waitRetireCarte()
def MENU_repairCarte():
    return
