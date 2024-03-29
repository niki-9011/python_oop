from project import Player


class Guild:

    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player):
        if player.guild == "Unaffiliated":
            player.guild = self.name
            self.players.append(player)

            return f"Welcome player {player.name} to the guild {self.name}"

        elif player.guild == self.name:
            return f"Player {player.name} is already in the guild."

        else:
            return f"Player {player.name} is in another guild."

    def kick_player(self, player_name):
        for player in self.players:
            if player.name == player_name:
                self.players.remove(player)
                player.guild = "Unaffiliated"

                return f"Player {player.name} has been removed from the guild."

        return f"Player {player_name} is not in the guild."


    def guild_info(self):
        result = [f"Guild: {self.name}"]
        [result.append(p.player_info()) for p in self.players]

        return "\n".join(result)

player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())
