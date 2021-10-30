import discord
from discord.ext import commands
import asyncio

token_file=open("key.txt","r")
token = token_file.read()

#list_numbers = ['1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','6️⃣','7️⃣','8️⃣','9️⃣']


class Joueur(object):

    def __init__(self, nom, symbole):
        self.nom = nom
        self.symbole = symbole

description = '''Bot Python'''
bot = commands.Bot(command_prefix='!', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def hello(ctx):
    list_numbers = ['1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','6️⃣','7️⃣']
    accept_decline = await ctx.send("Test")
    for i in list_numbers :
        emoji = i
        a = await accept_decline.add_reaction(emoji)
    print(a)
    reaction = discord.utils.get(accept_decline.reactions)

    print(reaction)
    gameLoop = True
    while gameLoop == True :
        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) in list_numbers

        try:
            reaction, user = await bot.wait_for('reaction_add', timeout=60.0, check=check)
            await reaction.remove(user)
            await reaction.remove(bot.user)
            print(bot.user)
            print("yo")
        except asyncio.TimeoutError:
            print("ROOO")
            await ctx.send("Temps écouler, partie terminé")
            gameLoop = False
            break
    


@bot.command()
async def puissance4(ctx):
    list_numbers = ['1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','6️⃣','7️⃣']
    # init variables
    joueur_tours = 1
    etage_0 = 0
    etage_1 = 0
    etage_2 = 0
    etage_3 = 0
    etage_4 = 0
    etage_5 = 0
    etage_6 = 0

    # init liste
    colonne_0 = ["⚫", "⚫", "⚫", "⚫", "⚫", "⚫"]
    colonne_1 = ["⚫", "⚫", "⚫", "⚫", "⚫", "⚫"]
    colonne_2 = ["⚫", "⚫", "⚫", "⚫", "⚫", "⚫"]
    colonne_3 = ["⚫", "⚫", "⚫", "⚫", "⚫", "⚫"]
    colonne_4 = ["⚫", "⚫", "⚫", "⚫", "⚫", "⚫"]
    colonne_5 = ["⚫", "⚫", "⚫", "⚫", "⚫", "⚫"]
    colonne_6 = ["⚫", "⚫", "⚫", "⚫", "⚫", "⚫"]
    list_joueur = []
    list_colonne = [colonne_0, colonne_1, colonne_2,
                    colonne_3, colonne_4, colonne_5, colonne_6]
    list_etage = [etage_0, etage_1, etage_2,
                  etage_3, etage_4, etage_5, etage_6]

    # sys nom et symbole
    joueurs = Joueur("a", "🔴")
    list_joueur.append(joueurs)
    joueurs = Joueur("B", "🟡")
    list_joueur.append(joueurs)
    message = "1️⃣2️⃣3️⃣4️⃣5️⃣6️⃣7️⃣\n{}{}{}{}{}{}{}\n{}{}{}{}{}{}{}\n{}{}{}{}{}{}{}\n{}{}{}{}{}{}{}\n{}{}{}{}{}{}{}\n{}{}{}{}{}{}{}".format(
        list_colonne[0][5],list_colonne[1][5],list_colonne[2][5],list_colonne[3][5],list_colonne[4][5],list_colonne[5][5],list_colonne[6][5],
        list_colonne[0][4],list_colonne[1][4],list_colonne[2][4],list_colonne[3][4],list_colonne[4][4],list_colonne[5][4],list_colonne[6][4],
        list_colonne[0][3],list_colonne[1][3],list_colonne[2][3],list_colonne[3][3],list_colonne[4][3],list_colonne[5][3],list_colonne[6][3],
        list_colonne[0][2],list_colonne[1][2],list_colonne[2][2],list_colonne[3][2],list_colonne[4][2],list_colonne[5][2],list_colonne[6][2],
        list_colonne[0][1],list_colonne[1][1],list_colonne[2][1],list_colonne[3][1],list_colonne[4][1],list_colonne[5][1],list_colonne[6][1],
        list_colonne[0][0],list_colonne[1][0],list_colonne[2][0],list_colonne[3][0],list_colonne[4][0],list_colonne[5][0],list_colonne[6][0]
        )
    plateau = await ctx.send(message)    
    gameLoop = True
    for i in list_numbers :
        await plateau.add_reaction(i)

    while gameLoop == True:

        # sys de tours
        if joueur_tours == 0:
            joueur_tours = 1

        elif joueur_tours == 1:
            joueur_tours = 0


        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) in list_numbers

        try:
            reaction, user = await bot.wait_for('reaction_add', timeout=60.0, check=check)
            await reaction.remove(user)
        except asyncio.TimeoutError:
            await ctx.send("Temps écouler, partie terminé")
            gameLoop = False
            break

        if str(reaction.emoji) == '1️⃣':
            emplacement = 0
        elif str(reaction.emoji) == '2️⃣':
            emplacement = 1
        elif str(reaction.emoji) == '3️⃣':
            emplacement = 2
        elif str(reaction.emoji) == '4️⃣':
            emplacement = 3
        elif str(reaction.emoji) == '5️⃣':
            emplacement = 4
        elif str(reaction.emoji) == '6️⃣':
            emplacement = 5
        elif str(reaction.emoji) == '7️⃣':
            emplacement = 6

        list_colonne[emplacement][list_etage[emplacement]] = list_joueur[joueur_tours].symbole
        list_etage[emplacement] += 1
        message = "1️⃣2️⃣3️⃣4️⃣5️⃣6️⃣7️⃣\n{}{}{}{}{}{}{}\n{}{}{}{}{}{}{}\n{}{}{}{}{}{}{}\n{}{}{}{}{}{}{}\n{}{}{}{}{}{}{}\n{}{}{}{}{}{}{}".format(
        list_colonne[0][5],list_colonne[1][5],list_colonne[2][5],list_colonne[3][5],list_colonne[4][5],list_colonne[5][5],list_colonne[6][5],
        list_colonne[0][4],list_colonne[1][4],list_colonne[2][4],list_colonne[3][4],list_colonne[4][4],list_colonne[5][4],list_colonne[6][4],
        list_colonne[0][3],list_colonne[1][3],list_colonne[2][3],list_colonne[3][3],list_colonne[4][3],list_colonne[5][3],list_colonne[6][3],
        list_colonne[0][2],list_colonne[1][2],list_colonne[2][2],list_colonne[3][2],list_colonne[4][2],list_colonne[5][2],list_colonne[6][2],
        list_colonne[0][1],list_colonne[1][1],list_colonne[2][1],list_colonne[3][1],list_colonne[4][1],list_colonne[5][1],list_colonne[6][1],
        list_colonne[0][0],list_colonne[1][0],list_colonne[2][0],list_colonne[3][0],list_colonne[4][0],list_colonne[5][0],list_colonne[6][0]
        )
        await plateau.edit(content=message)

        # On verifie la victoire sur le bas
        etage = list_etage[emplacement]
        etage -= 1
        nb_symbole = 1
        while list_colonne[emplacement][etage] == list_joueur[joueur_tours].symbole:
            etage -= 1
            if etage < 0:
                break
            nb_symbole += 1

        if nb_symbole >= 4:
            break

        # On verifie la victoire sur la gauche
        emplacement_save = emplacement
        nb_symbole = 1
        emplacement_save -= 1
        etage = list_etage[emplacement]
        etage -= 1
        while list_colonne[emplacement_save][etage] == list_joueur[joueur_tours].symbole:
            emplacement_save -= 1
            nb_symbole += 1
            nb_symbole += 1
            if etage < 0:
                break

        if nb_symbole >= 4:
            break

        # On verifie la victoire sur la droite
        emplacement_save = emplacement
        emplacement_save += 1
        etage = list_etage[emplacement]
        etage -= 1
        if emplacement_save < 7:
            while list_colonne[emplacement_save][etage] == list_joueur[joueur_tours].symbole:
                emplacement_save += 1
                nb_symbole += 1
                if etage < 0:
                    break
                if emplacement_save > 6:
                    break
        if nb_symbole >= 4:
            break

        # On verifie la victoire sur la diagonale haut droite
        nb_symbole = 1
        emplacement_save = emplacement
        emplacement_save += 1
        etage = list_etage[emplacement]
        if emplacement_save < 7:
            while list_colonne[emplacement_save][etage] == list_joueur[joueur_tours].symbole:
                emplacement_save += 1
                etage += 1
                nb_symbole += 1
                if emplacement_save > 6:
                    break

        if nb_symbole >= 4:
            break

        # On verifie la victoire sur la diagonale bas gauche
        emplacement_save = emplacement
        emplacement_save -= 1
        etage = list_etage[emplacement]
        etage -= 2
        print(list_colonne[emplacement_save][etage])
        while list_colonne[emplacement_save][etage] == list_joueur[joueur_tours].symbole:
            emplacement_save -= 1
            etage -= 1
            nb_symbole += 1
            if etage < 0:
                break
        if nb_symbole >= 4:
            break

        # On verifie la victoire sur la diagonale haut gauche
        nb_symbole = 1
        emplacement_save = emplacement
        emplacement_save -= 1
        etage = list_etage[emplacement]
        while list_colonne[emplacement_save][etage] == list_joueur[joueur_tours].symbole:
            emplacement_save -= 1
            etage += 1
            nb_symbole += 1
            if etage > 5:
                break

        if nb_symbole >= 4:
            break

        # On verifie la victoire sur la diagonale bas droite
        emplacement_save = emplacement
        emplacement_save += 1
        etage = list_etage[emplacement]
        etage -= 2
        if emplacement_save < 7:
            while list_colonne[emplacement_save][etage] == list_joueur[joueur_tours].symbole:
                emplacement_save += 1
                etage -= 1
                nb_symbole += 1
                if etage < 0:
                    break
                if emplacement_save > 6:
                    break

            if nb_symbole >= 4:
                break
        

    print(list_joueur[joueur_tours].nom, "a gagner")
    messagefin = list_joueur[joueur_tours].nom + " a gagner"
    await ctx.send(messagefin)
    
    plateau = await plateau.channel.fetch_message(plateau.id)  # Can be None if msg was deleted
    print(plateau.reactions)
    for i in plateau.reactions:
        print(i)
        i.remove
    
    return joueur_tours



bot.run(token)
