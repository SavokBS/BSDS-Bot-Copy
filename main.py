from discord.ext import commands
import json
bot = commands.Bot(command_prefix = "!")

@bot.event
async def on_ready():
    print(f"Discord Bot started on: {bot.user}")
    
@bot.command()
async def hex2int(ctx, dudka:str=None):
    if dudka == None:
        await ctx.send("hexToConvert is a required argument that is missing.")
    else:
        await ctx.send(int(dudka))
        
@bot.command()
async def int2hex(ctx, dudka:int=None):
    if dudka == None:
        await ctx.send("integerToConvert is a required argument that is missing.")
    else:
        await ctx.send(hex(dudka))
        
@bot.command()
async def ping(ctx):
    await ctx.send(f"Latency: {int(bot.latency * 100)}ms")
    
@bot.command()
async def monke(ctx):
    await ctx.send(":monkey:")

@bot.command()
async def find(ctx, packet):
    try:
       packets = ""
       packetName = ""
       packetID = 0
       packetHexademical = 0x0
       # int(packet)
       dudka = json.loads(open('jsons/packets.json', "r").read())
       for packetick in dudka:
           if packet in dudka[str(packetick)]:
               packetName = dudka[str(packetick)]
               packetID = int(packetick)
               packetHexademical = hex(packetID)
               packets += f"ID: {packetID}, Hexadecimal ID: {packetHexademical}, Packet name: {packetName}\n"
               print("Contains.")
    except: pass
    await ctx.send(packets)
bot.run("token")
