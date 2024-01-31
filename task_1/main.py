from pulp import LpProblem, LpMaximize, LpVariable

problem = LpProblem("MaximizeProduction", LpMaximize)

x = LpVariable("LemonadeUnits", lowBound=0, cat="Integer")
y = LpVariable("FruitJuiceUnits", lowBound=0, cat="Integer")

problem += x + y, "TotalProduction"

water_units = 100
sugar_units = 50
lemon_juice_units = 30
fruit_puree_units = 40

problem += 2 * x + y <= water_units, "WaterConstraint"
problem += x <= sugar_units, "SugarConstraint"
problem += x <= lemon_juice_units, "LemonJuiceConstraint"
problem += 2 * y <= fruit_puree_units, "FruitPureeConstraint"

problem.solve()

print(f"Optimal production of Lemonade: {int(x.varValue)} units")
print(f"Optimal production of Fruit Juice: {int(y.varValue)} units")
print(f"Total production: {int(x.varValue) + int(y.varValue)} units")
