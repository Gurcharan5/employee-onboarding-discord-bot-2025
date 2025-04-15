import discord
from discord.ext import commands
import sqlite3

# Enter your bot token here
BOT_TOKEN=""

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    conn=sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS employees
                   (id INTEGER PRIMARY KEY, name TEXT, position TEXT, onboarded BOOLEAN)''')
    # Change the admin values to your own
    # cursor.execute("INSERT INTO employees (id, name, position, onboarded) VALUES (?,?,?,?)", (0,"Admin", "admin", False))
    conn.commit()
    conn.close()
    

@bot.command()
async def onboard(ctx, number: int, member: discord.Member):
    await ctx.send(f'Onboarding employee with ID: {number}')
    
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees WHERE id=?", (number,))
    employee = cursor.fetchone()
    
    if employee:
        if employee[3]: 
            await ctx.send(f'Employee {employee[1]} is already onboarded.')
        else:
            cursor.execute("UPDATE employees SET onboarded=1 WHERE id=?", (number,))
            conn.commit()
            # Change the name="" to the name of the role you want to give to access the employee channels
            role = discord.utils.get(ctx.guild.roles, name="employee")
            await member.add_roles(role)
            await ctx.send('We kindly request for you to change your server nickname to your employee name followed by your ID.')
            await ctx.send(f'Please change your nickname to {employee[1]} #{number}')
            await ctx.send(f'Welcome to the team!')
            

            if employee[2] == "admin":
                await ctx.send("You may onboard a new employee using the '!add ID NAME POSITION' command.")
    
    else:
        await ctx.send("No employee found with that ID.")

    conn.close()

@bot.command()
async def add(ctx, number: int, name: str, position: str):
    await ctx.send(f'Adding employee with ID: {number}, Name: {name}, Position: {position}')
    
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO employees (id, name, position, onboarded) VALUES (?, ?, ?, ?)", (number, name, position, False))
    conn.commit()
    conn.close()

    await ctx.send(f'Employee {name} with ID {number} and position {position} has been added.')


            
    
    
bot.run(BOT_TOKEN)
