import os
#from commands import parse


class Combat:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
        self.is_fighting = True

    def StartCombat(self):
        # Combat loop between player and enemy. Gets player's action, verifies the action
        # is valid, performs the action, and performs the enemy's turn. If either player
        # dies or retreats the battle is over.

        action = ""
        spell = ""
        turn = 0

        while self.is_fighting:
            # Player's turn
            if turn % 2 == 0:
                self._DisplayCurrentStats()
                is_valid = False
                spell = ""
                # Get action
                while not is_valid:
                    action = self._GetUserAction()
                    is_valid = self._VerifyValidAction(action)
                    if not is_valid:
                        print("Unknown action. Please enter a valid action that you wish to perform.")
                    else:
                        if action == "spells":
                            self._DisplaySpells()
                            spell = self._GetSpellChoice()
                            # Return to combat menu
                            if spell == "back":
                                is_valid = False
                            else:
                                is_valid = self._VerifyValidSpell(spell)
                # Perform action
                if action == "run":
                    is_run = self.player.Run()
                    if is_run:
                        print("Got away safely.")
                        self._PostBattleResetStats()
                        self.is_fighting = False
                    else:
                        print("Unable to escape.")
                else:
                    self._PerformAction(action=action, spell=spell, attacker=self.player, defender=self.enemy)

            # Enemy turn
            else:
                enemy_action = self.enemy.GetAction()
                self._PerformAction(action=enemy_action, spell=spell, attacker=self.enemy, defender=self.player)

            # Check if someone died died
            self._BattleStatus()

            # Change attacker
            turn += 1


    def _DisplayCurrentStats(self):
        # Display battle stats to player
        player_stats = "You - Health: " + str(self.player.hp_cur) + "     Mana: " + str(self.player.mana_cur)
        enemy_stats = self.enemy.name + " - Health: " + str(self.enemy.hp_cur)
        stat_spacing = ""
        for i in range(len(player_stats), 45):
            stat_spacing = stat_spacing + " "
        print(player_stats + stat_spacing + enemy_stats)

    def _GetUserAction(self):
        # Gets the action the user wants to perform, parses it, and returns the action
        #
        # Outputs:
        # response - the action the user wants to perform

        print("What would you like to do - Attack, Defend, Spells, or Run? ")
        response = input()
        # response = parse(response)
        response = response.lower()
        return response

    def _GetSpellChoice(self):
        # Gets the spell that the user wants to cast, parses it, and returns the spell
        #
        # Outputs:
        # response - the spell name the user wants to cast or back to return toi the combat menu

        print("Choose a spell to cast or type Back to return to the combat menu.")
        response = input()
        # response = parse(response)
        response = response.lower()
        return response

    def _VerifyValidAction(self, action):
        # Check whether the action the user wants to perform is valid or not
        #
        # Inputs:
        # action - the action that the user wants to perform
        #
        # Outputs:
        # True/False if action is valid or not

        valid_actions = ["attack", "defend", "spells", "run"]

        # Player chose a valid action word
        if action not in valid_actions:
            return False

        return True

    def _DisplaySpells(self):
        # Displays available spells and their mana cost to the player
        print("Available Spells")
        print(self.player.inventory.DisplaySpells())

    def _VerifyValidSpell(self, spell):
        # Check whether the spell the user wants to cast is valid or not
        #
        # Inputs:
        # spell - the spell that the user wants to cast
        #
        # Outputs:
        # True/False if spell is valid or not

        # Player casts spell they don't have
        if not self.player.inventory.HasSpell(spell):
            print("You can't cast a spell you haven't learned.")
            return False

        # Player doesn't have mana to cast spell
        if not self.player.inventory.CanCastSpell(spell, self.player.mana_cur):
            print("You don't have enough mana to cast this spell.")
            return False

        return True

    def _PerformAction(self, action, spell, attacker, defender):
        # Performs a combat action
        #
        # Inputs:
        # action - list of the action the user wants to perform where item 0 is the action and item 1 is a spell
        # attacker - the character performing the action
        # defender - the character having the action being performed on

        if action == "attack":
            dmg_dealt = round(attacker.atk_cur / ((defender.def_cur + 100) / 100))
            defender.DealDamage(dmg_dealt)
            print(attacker.name + " attacked and dealt " + str(dmg_dealt) + " damage")

        if action == "defend":
            def_added = attacker.Defend()
            print(attacker.name + " used defend. Defense rose by " + str(def_added))

        if action == "spells":
            dmg_dealt = attacker.CastSpell(spell)
            defender.DealDamage(dmg_dealt)
            print(attacker.name + " cast " + spell + " and dealt " + str(dmg_dealt) + " damage.")

    def _BattleStatus(self):
        # Check if either character has died which ends the battle

        if self.player.hp_cur <= 0:
            self.is_fighting = False
            print("You have died.")
            print()

        if self.enemy.hp_cur <= 0:
            self.is_fighting = False
            self._PostBattleResetStats()
            self.player.Transaction(self.enemy.prize)
            print("You have defeated the " + self.enemy.name + " and found " + str(self.enemy.prize) + " gold.")
            print()

    def _PostBattleResetStats(self):
        # Heals the player, restores mana, and resets their defense after a battle is complete
        self.player.hp_cur = self.player.hp
        self.player.def_cur = self.player.defense
        self.player.mana_cur_cur = self.player.mana
