# 🤖 Discord Bot Documentation

## 🚀 Project Overview
This project is a Discord bot built using the `discord.py` library. It includes basic features such as:
- Responding with latency (`ping` command)  
- Displaying user information (`userinfo` command)  
- Clearing messages in a channel (`clear` command)  
- Error handling for common command issues

---

## 📁 File Structure

```plaintext
├── bot.py  # Main bot implementation
```

---

## 🔧 Requirements

- Python 3.x
- `discord.py` library

### **Installation**
To install the required library, run:
```bash
pip install discord.py
```

---

## 🛠️ How to Run
1. **Configure the Bot Token:**  
   Replace the token in the code:
   ```python
   bot.run("YOUR_BOT_TOKEN")
   ```
2. **Run the Bot:**  
   Execute the bot script:
   ```bash
   python bot.py
   ```
3. **Invite the Bot:**  
   Use this URL format to invite your bot to a server:
   ```
   https://discord.com/api/oauth2/authorize?client_id=YOUR_CLIENT_ID&permissions=8&scope=bot
   ```

---

## 📜 Code Explanation

### **Bot Configuration**
```python
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)
```
The bot is configured to use the prefix `!` and has message-related intents enabled.

---

### **Commands**

#### **1. `!ping`**
Sends the bot's latency as a response.
```python
@bot.command()
async def ping(ctx):
    latency = round(bot.latency * 1000)
    embed = discord.Embed(title="Pong! 🏓", description=f"Latency: {latency}ms", color=discord.Color.blue())
    await ctx.send(embed=embed)
```

#### **2. `!userinfo [@member]`**
Displays information about a user.
```python
@bot.command()
async def userinfo(ctx, member: discord.Member = None):
    member = member or ctx.author
    embed = discord.Embed(title=f"{member.name}'s Info", color=discord.Color.green())
    embed.set_thumbnail(url=member.avatar.url if member.avatar else member.default_avatar.url)
    embed.add_field(name="ID", value=member.id, inline=True)
    embed.add_field(name="Joined At", value=member.joined_at.strftime("%Y-%m-%d %H:%M:%S"), inline=True)
    embed.add_field(name="Created At", value=member.created_at.strftime("%Y-%m-%d %H:%M:%S"), inline=True)
    await ctx.send(embed=embed)
```
_Defaults to the command user if no member is mentioned._

#### **3. `!clear [amount]`**
Clears a specified number of messages (default is 5).
```python
@bot.command()
async def clear(ctx, amount: int = 5):
    if not ctx.author.guild_permissions.manage_messages:
        return await ctx.send("You lack the required permissions.")
    await ctx.channel.purge(limit=amount + 1)
    await ctx.send(f"Cleared {amount} messages.", delete_after=5)
```

---

### **Error Handling**
```python
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Missing required arguments for the command.")
    elif isinstance(error, commands.CommandNotFound):
        await ctx.send("Invalid command. Use `!help` for a list of commands.")
    else:
        await ctx.send("An unexpected error occurred.")
        raise error
```

---

## ⚠️ Important Notes
- Replace the bot token with your **actual bot token**.
- Ensure the bot has the necessary permissions when added to a server.
- The `clear` command requires `Manage Messages` permission.

---

## 📚 Resources
- [Discord.py Documentation](https://discordpy.readthedocs.io/en/stable/)
- [Discord Developer Portal](https://discord.com/developers/applications)

---

## 🏗️ Command Summary

| Command  | Description                                  |
|----------|----------------------------------------------|
| `!ping`  | Returns the bot's latency.                   |
| `!userinfo [@member]` | Displays the information of a user. |
| `!clear [amount]` | Clears a specific number of messages.  |

---

## 📝 Improvements
- Add role-based access control for commands.
- Implement logging for better debugging.
- Add more fun commands, like games or trivia.

---

## 💭 Quotes
> "Code is like humor. When you have to explain it, it’s bad." — Cory House

---

## 🖊️ Author
**Muhammad Ahmad Nadeem**

Feel free to connect for questions or suggestions!

---

## 🌟 Acknowledgments
Special thanks to the Discord developer community for inspiration and guidance.
