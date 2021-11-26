import json
from datetime import datetime

import alpaca_trade_api as tradeapi
import time
import discord
import requests
from alpaca_trade_api.rest import TimeFrame
from discord.ext import commands

TOKEN = ''
bot = discord.Client()
bot = commands.Bot(command_prefix='!')
api = tradeapi.REST(
    '',
    '',
    'https://paper-api.alpaca.markets'
)
account = api.get_account()

def buy_stock(symbol , qty , side , type , time_in_force):
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side=side,
        type=type,
        time_in_force=time_in_force
    )

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='buy')
async def buy(ctx , symbol , quantaty):
    try:
        buy_stock(symbol, int(quantaty), 'buy', 'market', 'gtc')
        await ctx.send(f"Bought {int(quantaty)} {symbol}")
    except Exception as e:
        await ctx.send(e)

@bot.command(name='sell')
async def sell(ctx , symbol , quantaty):
    try:
        buy_stock(symbol, int(quantaty), 'sell', 'market', 'gtc')
        await ctx.send(f"Sold {int(quantaty)} {symbol}")
    except Exception as e:
        await ctx.send(e)

@bot.command(name='balance')
async def balance(ctx):
    aapi = tradeapi.REST(
        '',
        '',
        ''
    )
    aaccount = aapi.get_account()
    await ctx.send(f"{aaccount.buying_power}$")

@bot.command(name='bal')
async def balance(ctx):
    ayy = tradeapi.REST(
        '',
        '',
        ''
    )
    ayaccount = ayy.get_account()
    await ctx.send(f"{ayaccount.buying_power}$")

@bot.command(name='profit')
async def profit(ctx):
    eapi = tradeapi.REST(
        '',
        '',
        ''
    )
    eaccount = eapi.get_account()
    a = float(eaccount.buying_power) - 200000
    await ctx.send(f"PROFIT : {a}")
#buy_stock('AAPL', 1, 'buy', 'market', 'gtc')
if __name__ == '__main__':
    bot.run(TOKEN)