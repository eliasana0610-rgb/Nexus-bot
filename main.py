import os
import discord
from discord import app_commands

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.members = True


class NexusBot(discord.Client):
    def __init__(self):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()
        print("Commandes NEXUS synchronisées.")

    async def on_ready(self):
        print(f"NEXUS BOT connecté : {self.user}")


bot = NexusBot()


@bot.tree.command(
    name="status",
    description="Vérifier que NEXUS BOT fonctionne"
)
async def status(interaction: discord.Interaction):
    await interaction.response.send_message(
        "NEXUS BOT est opérationnel !"
    )


@bot.tree.command(
    name="help",
    description="Afficher les commandes"
)
async def help_command(interaction: discord.Interaction):
    await interaction.response.send_message(
        "**NEXUS BOT — Commandes**\n"
        "`/status` : vérifier le fonctionnement\n"
        "`/help` : afficher cette aide"
    )


if not TOKEN:
    raise RuntimeError("DISCORD_TOKEN manquant.")

bot.run(TOKEN)