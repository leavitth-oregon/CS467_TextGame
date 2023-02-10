import os
#from commands import parse


class Combat:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
        self.is_fighting = True

    def StartCombat(self):
        while self.is_fighting:
            is_valid = False
            while not is_valid:
                self._DisplayCurrentStats()
                action = self._GetUserAction()
                is_valid = self._VerifyValidAction(action)
                if not is_valid:
                    input()

            # player turn
            if action[0] == "run":
                is_run = self.player.Run()
                if is_run:
                    self.is_fighting = False
            else:
                self._PerformAction(action, self.player, self.enemy)

            # enemy turn
            enemy_action = self.emeny.GetAction()
            self._PerformAction(enemy_action, self.enemy, self.player)

            self._BattleStatus()

    def _DisplayCurrentStats(self):
        os.system("cls")
        print("Your health is " + str(self.player.hp_cur) + " and your mana is " + str(self.player.mana_cur))
        print("The enemy's health is " + str(self.enemy.hp_cur))
        print()

    def _GetUserAction(self):
        print("Available Spells")
        print(self.player.inventory.DisplayItemList(self.player.inventory.spells, False))
        print()
        print("What would you like to do - Attack, Defend, Cast a spell, or Run? ")
        response = input()
        # response = parse(response)
        return response

    def _VerifyValidAction(self, action):
        valid_actions = ["attack", "defend", "cast", "run"]
        valid = False

        # Player chose a valid action word
        if action[0] in valid_actions:
            valid = True

        # Player needs to have declared a spell
        if action[0] == "cast" and len(action) < 2:
            print("You need to declare what spell you want to cast.")
            valid = False
        else:
            # Player casts spell they don't have
            if action[0] == "cast" and not self.player.inventory.HasSpell(action[1]):
                print("You can't cast a spell you haven't learned.")
                valid = False

            # Player doesn't have mana to cast spell
            if action[0] == "cast" and not self.player.inventory.CanCastSpell(action[1], self.player.mana_cur):
                print("You don't have enough mana to cast this spell.")
                valid = False

        return valid

    def _PerformAction(self, action, attacker, defender):
        print()
        if action[0] == "attack":
            dmg_dealt = round(attacker.atk_cur / ((defender.def_cur + 100) / 100))
            defender.DealDamage(dmg_dealt)
            print(attacker.name + " dealt " + str(dmg_dealt) + " damage to " + defender.name)

        if action[0] == "defend":
            def_added = attacker.Defend()
            print("Defense rose by " + str(def_added))

        if action[0] == "cast":
            dmg_dealt = attacker.CastSpell(action[1])
            defender.DealDamage(dmg_dealt)
            print(attacker.name + " dealt " + str(dmg_dealt) + " damage to " + defender.name)

    def _BattleStatus(self):
        if self.player.hp_cur <= 0:
            self.is_fighting = False
            print("You have died")

        if self.enemy.hp_cur <= 0:
            self.is_fighting = False
            print("You have defeated" + self.enemy.name)
