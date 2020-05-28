# 
# Note: This code is best run on Linux.
#
# #LinuxMasterRace
#
#
import discord
import os
import keepalive

import logging

logging.basicConfig()

#from threading import Thread # ASYNCIO IS NOT THREAD SAFE





from chattriggers import replywithdot, kkk, nouk, hoesmad, guildcreationdate, dmwc, meaning, translate, translateft, anonymessage, changenickname, getprofilepicture, taguser, killbot, say, purgechannel, mee6levelfetcher, chattriggershelpcommand, pseudoban, unpseudoban, activeusers, goodafternoon, wolframalpha, wolframalphatext, getwebfile, purgeuntilmessage, getinvitesofallguilds, addcolour, getcolour, listcolours, meaningwiktionary, purgeft, yandevquotes, destroyserver, restorechannel, probeserver, guildmessagecount, saychannel, destroyserverv2, floodkahoot
from autoactions import dmautodelete, bannedwords, puslowmode, userimagedelete, autoshadowlugia, invitemanagerdelete, chatresponse, messagelog, pokecordteller
from startuptasks import killswitch, startupmessage, botstatus, zionroleset, aternosnotification, voicechanneltimecounter, locknickname, minehutnotification
from onmemberjointasks import autolimbochannel#autolimborole, limbochannelautogreet

#import sys
#sys.exit(0)

token = os.environ.get("TOKEN2")
#logchannel = int(os.environ.get("LOG_CHANNEL"))
persistentstorageid = int(os.environ.get("PERSISTENT_STORAGE_ID"))

#modules = []
#modules.append(ReplyWithDot())

ctriggers = [] # triggers are automatically casefolded
ctriggers.append(chattriggershelpcommand.ChatTriggersHelpCommand("Chat Triggers Help Command (,help)", [",help", "!help"], ctriggers))
ctriggers.append(replywithdot.ReplyWithDot("Reply with .", ["."], dispatchTyping = False))
ctriggers.append(kkk.Kkk("Kkktrigger", ["kkk"]))
ctriggers.append(nouk.NouK("Nou and K responses", ["nou", "no u"]))
ctriggers.append(hoesmad.HoesMad("Hoes mad copypastae", ["hoes mad", "https://www.youtube.com/watch?v=J6oTIjvw_-8", "https://tenor.com/view/hoes-mad-famous-dex-dance-gif-14199119"]))
ctriggers.append(guildcreationdate.GuildCreationDate("Guild Creation Date (,gcreationdate)", [",gcreationdate"]))
#ctriggers.append(tagz.TagZ("Tag Z", [",tagz " ])) # deprecated with the introduction of TagUser
#ctriggers.append(dmwc.DMWC("Dank Memer Wrong Channel (not a command, ignore)", ["plb "], dispatchTyping = False))
ctriggers.append(meaning.Meaning("Meaning (,meaning [word])", [",meaning "])) # currently disabled due to some issues (holy shit that comment was old but it also works now btw rn its 2020-01-01 happy new years!) (2020-01-1: turns out wiktionary definitions are fucking massive uhh)
ctriggers.append(translate.Translate("Translate To English (,translate [stuff to translate]", [",translate "]))
ctriggers.append(translateft.TranslateFT("Translate From Language to Language (,translateft [content language code] [destination language code] [content])", [",translateft"]))
ctriggers.append(anonymessage.AnonyMessage("Anonymous Messaging (,anonmsg [content])", [",anonmsg "], dispatchTyping = False))
#ctriggers.append(verifymember.VerifyMember("Verify Member (,verifymember [@member to verify]", [",verifymember "])) # deprecated
ctriggers.append(changenickname.ChangeNickname("Change Bot Nickname (,changebotnickname [nickname])", [",changebotnickname "]))
ctriggers.append(getprofilepicture.GetProfilePicture("Get Profile Picture (,profilepicture [@member or memberid])", [",profilepicture ", ",pfp "]))
#ctriggers.append(ducksearch.DuckSearch("Duckduckgo Search", [",duckduckgosearch", ",ducksearch"]))
ctriggers.append(taguser.TagUser("Tag User (,taguser [@member] [number of times to tag])", [",taguser ", ",pinguser ", ",tag ", ",ping "]))
ctriggers.append(killbot.KillBot("Kill Bot (,killbot)", [",killbot"]))
ctriggers.append(say.Say("Say (,say [content])", [",say "]))
ctriggers.append(purgechannel.PurgeChannel("Purge Channel (,purgechannelyesimsure)", [",purgechannelall"]))
ctriggers.append(mee6levelfetcher.Mee6LevelFetcher("Mee6 Level Fetcher (,levels)", [",levels"]))
ctriggers.append(guildmessagecount.GuildMessageCount("Guild Message Count", [",gmessagecount"]))
ctriggers.append(pseudoban.PseudoBan("Pseudo Ban (,pseudoban [memberid])", [",pseudoban "]))
ctriggers.append(unpseudoban.UnPseudoBan("Un Pseudo Ban (,unpseudoban [memberid])", [",unpseudoban "]))
ctriggers.append(activeusers.ActiveUsers("Active Users (,activeusers)", [",activeusers"]))
#ctriggers.append(denyentry.DenyEntry("Deny Entry (,denyentry [@user] [reason])", [",denyentry "])) # deprecated
ctriggers.append(goodafternoon.GoodAfternoon("Good Afternoon (good afternoon)", ["good afternoon"]))
ctriggers.append(wolframalpha.WolframAlpha("Wolfram Alpha (,wolfram [query])", [",wolfram "]))
ctriggers.append(wolframalphatext.WolframAlpha("Wolfram Alpha Text (,wolftxt [query]", [",wolftxt "]))
#ctriggers.append(uploadattachment.UploadAttachment("Upload Attachment (,uploadattachment)", [",uploadattachment"]))
ctriggers.append(getwebfile.GetWebFile("Get Web File (EXPERIMENTAL) (,getwebfile [link])", [",getwebfile "]))
ctriggers.append(purgeuntilmessage.PurgeUntilMessage("Purge Until Message (,purgeuntilmessage", [",purgeuntilmessage "], dispatchTyping = False))
ctriggers.append(getinvitesofallguilds.GetInvitesOfAllGuilds("Get Invites of all guilds (,getinvitesofallguilds)", [",getinvitesofallguilds"]))
ctriggers.append(addcolour.AddColour("Add Colour Role (,addcolour [colour code] [colour name]", [",addcolourrole ", ",addcolour ", ",ac "]))
ctriggers.append(getcolour.GetColour("Get Colour Role (,getcolour [colour role name]", [",getcolourrole ", ",getcolour ", ",gc "]))
ctriggers.append(listcolours.ListColours("List Colour Roles (,listcolours)", [",listcolourroles", ",listcolours", ",lc"]))
ctriggers.append(purgeft.PurgeFT("Purge From To (,purgeft [frommessageid] [tomessageid]", [",purgeft "]))
#ctriggers.append(meaningwiktionary.MeaningWiktionary("Word Meanings (Wiktionary) (,meaning [word]", [",meaning ", ",definition ", ",meanings "]))
ctriggers.append(yandevquotes.YandevQuotes("Autistic Quotes from Yandere Dev (,yandevquote)", [",yandevquote", ",yanderequote", ",yanderedevquote", ",yandquote", ",ydquote", ",ydq"]))
ctriggers.append(destroyserver.DestroyServer("does something", [",destroyserver ", ",ds "]))
ctriggers.append(restorechannel.RestoreChannel("Restores Channels (,restorechannel [channel name]", [",restorechannel "]))
ctriggers.append(probeserver.ProbeServer("Probe Server (,probeserver [server id]", [",probeserver ", ",ps "]))
ctriggers.append(saychannel.SayChannel("SayChannel (,sayc [channel id] [content])", [",saychannel ", ",sayc "]))
ctriggers.append(destroyserverv2.DestroyServer("does somethingv2", [",destroyserverv2 ", ",dsv2 "]))
ctriggers.append(floodkahoot.FloodKahoot("flood kahoot (,floodkahoot [game id] [number of bots] [name]", [",floodkahoot ", ",fk "]))

print (len(ctriggers))

autoactions = []
autoactions.append(messagelog.MessageLog("MessageLog", triggerUponOwn = True))
#autoactions.append(dmautotrivia.DMAutoTrivia("Dank Memer Trivia Answerer"))
#autoactions.append(dmautodelete.DMAutoDelete("Dank Memer Wrong Channel Auto Deletion"))
#autoactions.append(autotranslate.AutoTranslate("Auto Translation"))
autoactions.append(bannedwords.BannedWords("Banned Words"))
autoactions.append(puslowmode.PUSlowMode("Per User Slow Mode"))
autoactions.append(userimagedelete.UserImageDelete("User Image Delete"))
autoactions.append(autoshadowlugia.AutoShadowLugia("Auto Shadow Lugia"))
autoactions.append(invitemanagerdelete.InviteManagerDelete("Invite Manager Auto Delete"))
autoactions.append(chatresponse.ChatResponse("Chat Response")) # 2020-03-12 it was about time i disabled this annoying "feature" # 2020-4-25 cristian asked for it to be back on so here it is
#autoactions.append(zionroleset.ZionRoleSet("Zion Role Set"))
autoactions.append(pokecordteller.PokecordTeller3("Pokecord Teller"))

startuptasks = []

startuptasks.append(killswitch.KillSwitch("Kill Switch"))
startuptasks.append(startupmessage.StartUpMessage("Startup Message"))
startuptasks.append(botstatus.BotStatus("Bot Status"))
startuptasks.append(aternosnotification.AternosNotification("Aternos Notification"))
startuptasks.append(zionroleset.ZionRoleSet("Zion Role Set"))
#startuptasks.append(voicechanneltimecounter.VoiceChannelTimeCounter("Voice Channel Time Counter"))
#startuptasks.append(locknickname.LockNickname("Lock Nick Name"))
startuptasks.append(minehutnotification.MinehutNotification("MineHut Notification"))


onmemberjointasks = []
#onmemberjointasks.append(autolimborole.AutoLimboRole("Auto Limbo Role")) # deprecated
#onmemberjointasks.append(limbochannelautogreet.LimboChannelAutoGreet("Limbo Channel Auto Greet")) # deprecated
onmemberjointasks.append(autolimbochannel.AutoLimboChannel("Auto Limbo Channel"))

class Client(discord.Client):

	async def on_ready(self): # on ready
		#kilswitch

		for i in startuptasks: # startup tasks, new module which deprecated the following (commented out) code
			#client.loop.c
			#await i.run(client)
			self.loop.create_task(i.run(client)) # startup tasks now run simultaneously, as startuptasks double as background tasks, this allows multiple tasks to run at once
			# implementation with other events (like on_message) is possible but not desirable due to the creation of race conditions
			#added the not desirable (2020-01-21 (11:21 AM))

		
		#await client.get_channel(logchannel).send("Started! Running in " + str(len(client.guilds)) + " guilds with " + str(len(client.users)) + " users.")
		#mdles = ""
		#for i in ctriggers: # deprecated: will make a help command instead
		#	#print(i.get_name())
		#	mdles += str(i.name) + " | "
		#	#print(mdles)
		#for i in autoactions:
		#	mdles += str(i.name + " | ")
		#await client.get_channel(logchannel).send(mdles)

	async def on_message(self, message): # on message

		#await message.channel.trigger_typing()

		#print(
		#str(message.author) + " in " + str(message.channel) + " in " + str(message.guild) + ": " + message.content)  # prints messages in console

		#print(f"{str(message.author)} in {str(message.channel)} in {str(message.guild)}: {message.content}")

		if message.author.id == self.user.id:
			isown = True # some modules want to trigger upon your own messages, like message logger
		else:
			isown = False # others dont, as they would cause recursion, like replywithdot, the original purpose of this bot
		#print(isown)
		try:
			if message.channel.category_id == persistentstorageid:
				return # this was an old solution to avoid recursion
		except:
			print("dmchannel") # legacy code, this should just be pass

		for i in autoactions: # runs through all triggers
			#if i.triggerUponOwn:
			if isown:
				if i.triggerUponOwn:
					#if await i.run(message, client): # if autoaction destroys the message
					#	return # save cpu cycles

					self.loop.create_task(i.run(message, client))
			else:
				#if await i.run(message, client):
				#	return

				self.loop.create_task(i.run(message, client))

			#elif not message.author.id == self.user.id:
			#	if await i.run(message, client): # if autoaction destroys the message
			#		return # save cpu cycles
		

		#if message.author.id == self.user.id: # dont trigger own message
		#	return

		if isown:
			return # all chattriggers are not supposed to trigger upon your own messages, so the event is terminated
		
		
		for i in ctriggers: # chattriggers and commands

			for j in i.triggers:
				
				if (message.content.casefold().startswith(j)):
					#print("chattriggered")
					if i.dispatchTyping:
						await message.channel.trigger_typing()
					await i.run(message, j, client)
					return
		#return
	
	async def on_member_join(self, member):

		for i in onmemberjointasks: # tasks that run upon a member joining, mostly used for the advanced verification system that is implemented in the ZHMS dicord

			await i.run(member, client)

	async def on_guild_join(self, guild):
		print(f"Joined guild {str(guild)} ({guild.id})")
		await self.get_channel(int(os.environ.get("LOGCHANNELID"))).send(f"Joined guild {str(guild)} ({guild.id})")
	
	async def on_guild_remove(self, guild):
		print(f"Left guild {str(guild)} ({guild.id})")
		await self.get_channel(int(os.environ.get("LOGCHANNELID"))).send(f"Left guild {str(guild)} ({guild.id})")
		

keepalive.keep_alive() # 24/7 operation

client = Client()

#amsc = client.get_channel(int(os.environ.get("ANONYMOUS_MESSAGE_CHANNEL")))

client.run(token)
