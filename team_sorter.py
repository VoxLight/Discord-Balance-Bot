from discord.ext import commands
from config import get_config
import team


settings = get_config("settings.ini")
perms = settings["PERMISSIONS"]

class Sorter:

	def __init__(self, bot):
		self.bot = bot

	def scrim(ctx):
		if ctx.message.author.id == 132603064220778496:
			return True

		for role in ctx.message.author.roles:
			if role.name in perms["roles"]:
				return ctx.message.channel.id in perms['channels']

	@commands.command(brief="Creates two balanced teams.")
	@commands.check(scrim)
	async def balance(self, ctx):
		print("Tried to balance")
		# create an array of the first ten messages that are digits only
		members = []
		async for msg in ctx.channel.history(reverse=True):
			if len(members) < 10:
				if msg.content.isdigit():
					print("added1")
					members.append([int(msg.content), msg.author.name])

		# if we dont have enough players when the command is used, announce it and stop the function from continueing
		if len(members) < 10:
			await ctx.send(f"Sorry, not enough players yet to balance teams.")
			return
		team1, team2 = team.balance_teams(team.sort_players(members))
		print("tried to say")
		print(team.team_string(team1, team2))
		ctx.send(team.team_string(team1, team2))



	@commands.command(brief="Creates two unbalanced teams.")
	@commands.check(scrim)
	async def unbalance(self, ctx):
		# create an array of the first ten messages that are digits only
		members = []
		async for msg in ctx.channel.history(reverse=True):
			if len(members) < 10:
				if msg.content.isdigit():
					members.append([int(msg.content), msg.author.name])

		# if we dont have enough players when the command is used, announce it and stop the function from continueing
		if len(members) < 10:
			await ctx.send(f"Sorry, not enough players yet to stack teams.")
			return

		team1, team2 = team.stack_teams(team.sort_players(members))
		ctx.send(team.team_string(team1, team2))


	@commands.command(brief="Creates two random teams.")
	@commands.check(scrim)
	async def random(self, ctx):
		# create an array of the first ten messages that are digits only
		members = []
		async for msg in ctx.channel.history(reverse=True):
			if len(members) < 10:
				if msg.content.isdigit():
					members.append([int(msg.content), msg.author.name])

		# if we dont have enough players when the command is used, announce it and stop the function from continueing
		if len(members) < 10:
			await ctx.send(f"Sorry, not enough players yet to make random teams.")
			return

		team1, team2 = team.random_teams(team.sort_players(members))
		ctx.send(team.team_string(team1, team2))

def setup(bot):
	bot.add_cog(Sorter(bot))
