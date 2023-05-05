# LP:
# min 3x + 5y + 6z
# s.t 
#     2x + y + z <= 4
#     x + 2y + z <= 4
#     x + y + 2z <= 4
#     x + y + z <= 3
#     x,y >= 0

from gurobipy import *

# Create a new Gurobi Model
m = Model( name= "lp")  

# Create two new variables
# (GRB.CONTINUOUS, GRB.BINARY, GRB.INTEGER, GRB.SEMICONT, or GRB.SEMIINT)
x = m.addVar(lb=0, name ="x")
y = m.addVar(lb=0, name ="y")
z = m.addVar(lb=0, name ="z")

# Set the objective function
m.setObjective(3*x + 5*y + 6*z, GRB.MAXIMIZE)
    
#Add Constraints
m.addConstr(2*x + y + z <= 4, "c0") 
m.addConstr(x + 2*y + z <= 4, "c1") 
m.addConstr(x + y + 2*z <= 4, "c2") 
m.addConstr(x + y + z <= 3, "c3") 

# Solve the model
m.optimize()
    
# Print the feasible solution if optimal.
if m.status == GRB.Status.OPTIMAL:
    print("Optimal Solution:", m.objVal)
    for v in m.getVars():
        print(v.varName, v.x)
# Another way to print the variable
    #print("Optimal Solution:", m.objVal)
    #print(x.varName, x.x)
    #print(y.varName, y.x)        
else:
    print(m.status)