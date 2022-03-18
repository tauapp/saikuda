import itertools
from _colorama import Fore, Style
import random
import util_io as io
from copy import deepcopy, copy
from fightable import Fightable
from itertools import product

plan = []


# A very simple attack AI that will look three steps ahead and try to maximize damage.
def lookThreeAhead(self: Fightable):
    global plan
    if self.sparable:
        return (False, 0)
    #Formatting
    HEALTH = Fore.RED + "HEALTH" + Style.RESET_ALL
    ENERGY = Fore.BLUE + "ENERGY" + Style.RESET_ALL
    DEFENSE = Fore.GREEN + "DEFENSE" + Style.RESET_ALL

    #If the plan is not finished, continue with the plan.
    if len(plan) > 0:
        action = deepcopy(plan[0])
        del plan[0]
        if action == "rest":
            self.energy += (self.max_energy * 0.2)
            self.energy = min(round(self.energy), self.max_energy)
            io.say(self.name + " rested and recovered 20% of its", ENERGY + "!")
            return (False, 0)
        else:
            #Find the attack that corresponds to the action.
            return self.attack(action)
    else:
        energy = copy(self.energy)
        #Amount of energy increased per rest
        rest_reward = self.max_energy * 0.2

        #Create a simplified list of attack statistics.
        #Each attack is a tuple of the attack intensity and the attack cost.
        attack_list = []
        for attack in self.attack_list:
            attack_list.append((attack.intensity, attack.cost))

        #Find all possible 3-step plans
        all_plans = list(itertools.product([*attack_list, "rest"], repeat=3))

        possible_plans = []

        #Find which plans are possible with the current amount of energy
        for testplan in all_plans:
            avalible_energy = energy
            for action in list(testplan):
                if action == "rest":
                    avalible_energy += rest_reward
                else:
                    #Simulate the cost of an attack
                    avalible_energy -= action[1]
                    if avalible_energy < 0:
                        break
            if avalible_energy >= 0:
                possible_plans.append(testplan)

        #Add for each possible plan, add up the intensity of all the actions in the plan.
        #Find the plan with the most total intensity.
        best_plan = possible_plans[0]
        best_intensity = 0
        for testplan in possible_plans:
            intensity = 0
            for action in testplan:
                if action != "rest":
                    intensity += action[0]
            if intensity > best_intensity:
                best_plan = testplan
                best_intensity = intensity
        plan = []
        for action in best_plan:
            if action != "rest":
                id = attack_list.index(action)
                plan.append(id)
            else:
                plan.append(action)
        return lookThreeAhead(self)