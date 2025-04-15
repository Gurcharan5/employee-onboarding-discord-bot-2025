# Employee Onboarding Discord Bot 2025
A discord bot that allows you to add people who can only access channels with specific roles.

# How to use it
The code is commented so you can add your own bot token, member roles and default admin value

Once you have added your details, the commands are as follows:
- !onboard *idnumber* *@member* - Here you have the person onboard themselves using their ID number and tagging themselves
![image](https://github.com/user-attachments/assets/ad43102f-681e-44d6-ac83-7ed17ad87dcb)
- !add *memberid* *name* *role* - Here you can add a new person to be onboarded. Please note the memberid MUST be a number and giving anyone the admin role will allow them to add members.
![image](https://github.com/user-attachments/assets/a85a0b4f-6785-4769-9fad-2a021a6e42d2)

# Important information
A basic understanding of how to create and add a discord bot is required for you to use this code.
If you are needing other roles to be added - for example if you want designers to have their own chats as well - you can edit the onboard function in the following way:
- After the

               if employee[2] == "admin":
                   await ctx.send("You may onboard a new employee using the '!add ID NAME POSITION' command.")
- Add another if statement in the following way
  
                if employee[2] == "NAME_OF_ROLE":
                    role = discord.utils.get(ctx.guild.roles, name="NAME_OF_ROLE")
                    await member.add_roles(role)
  
  - Replace NAME_OF_ROLE with the role you want to give
    
