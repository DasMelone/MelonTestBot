from subprocess import call

call(["pip", "install", "discord.py", "--update"])

import discord
import asyncio
from time import sleep

client = discord.Client()
activated = True

@client.event
async def on_ready():
	print("Eingeloggt als:")
	print(client.user.name)
	print(client.user.id)
	print("--------------")

async def nobot(message):
    sleep(1)
    global activated
    if activated == True:
        if message.content.lower().startswith("deaktivieren"):
            activated = False
            await client.send_message(message.channel, "b :x: deaktiviert")
        else:
            await client.send_message(message.channel, "b :repeat: versuche " + message.content + " als python befehl auszuführen...")
            sleep(1)
            try:
                out = exec(message.content)
                await client.send_message(message.channel, "b :white_check_mark: " +  message.content + " ausgeführt output:")
                sleep(1)
                await client.send_message(message.channel,"b " + str(out))
            except:
                await client.send_message(message.channel, "b :x: Fehler")
                sleep(1)
    elif message.content.lower().startswith("aktivieren"):
        activated = True
        await client.send_message(message.channel, "b :white_check_mark: Aktiviert")

@client.event
async def on_message(message):
    print("on message: " + message.content)
    if message.content.startswith("b "):
        print("bot send")
        pass
    else:
        print("nobot send")
        await nobot(message)

client.run("Mzk4NDA2MjU4NTEzOTM2Mzk2.DS-EdQ.uGka3q4XpuJw0cep3ltKh6CMqd0")
