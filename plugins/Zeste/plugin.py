#!/usr/bin/python
# -*- coding: latin-1 -*-
###
# Copyright (c) 2015, AmarOk
# All rights reserved.
#
#
###

import supybot.conf as conf
import supybot.utils as utils
import supybot.world as world
from supybot.commands import *
import supybot.ircutils as ircutils
import supybot.registry as registry
import supybot.callbacks as callbacks
import random
import os
import urllib
import time

class Zeste(callbacks.Plugin):
    def zeste(self, irc, msg, args):
        """Clem dit une phrase pleine de zeste"""
        line = random.choice(open('quote').readlines())
        line = line[0:len(line)-1]
        irc.reply(line)
        
    def endlesszeste(self, irc, msg, args): 
        """Regarde si un nouveau chapitre est publié sur http://endlesszeste.tk/"""
        page=urllib.urlopen('http://endlesszeste.tk/') 
        strpage=page.read()
        oldChap = int(open('endlesszeste', 'r').read())
        newChap = strpage.count("chapitre-", 0, len(strpage))
        if oldChap != newChap:
            irc.reply('Oh ! Mon histoire avance ! Lisez-la ici : http://endlesszeste.tk/chapitre-' + str(newChap-1))
            os.remove('endlesszeste')
            open('endlesszeste', 'w').write(str(newChap))   
        else:
            irc.reply('Malheureusement, pas de nouveaux chapitres aujourd\'hui. Mais le dernier est ici : http://endlesszeste.tk/chapitre-' + str(newChap-1))     
        
    def vendetta(self, irc, msg, args):
        """Mange Celui-Dont-On-Ne-Doit-Pas-Prononcer-Le-Pseudo qui a tenté de l'assassiner par le passé"""
        if random.randint(0, 100) == 50:
            irc.reply("mange Cornichon", action=True)
        else:
            irc.reply("Pas de vengeance aujourd'hui")
            
    def command(self, irc, msg, args):
        irc.reply("Commandes disponibles :")
        irc.reply("!zeste, !endlesszeste, !vendetta, !articles, !tutos")
        irc.reply("Pour en savoir plus : !help <command>")

Class = Zeste
