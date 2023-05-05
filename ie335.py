# LP:
# min 10x + 26y
# s.t 
#     12x + 40y >= 78
#     6x + 20y >= 39
#     x,y >= 0

from gurobipy import *

# Create a new Gurobi Model
m = Model( name= "lp")  

# Create two new variables
# (GRB.CONTINUOUS, GRB.BINARY, GRB.INTEGER, GRB.SEMICONT, or GRB.SEMIINT)
x = m.addVar(lb=0, name ="x")
y = m.addVar(lb=0, name ="y")

# Set the objective function
m.setObjective(10*x + 25*y, GRB.MINIMIZE)
    
#Add Constraints
m.addConstr(12*x + 40*y >= 78, "c0") # -12, -40 infeasible
m.addConstr( 6*x + 20*y >= 39, "c1")
    
# Solve the model
m.optimize()
    
# Print the feasible solution if optimal.
if m.status == GRB.Status.OPTIMAL:
    print('Obj Function:', m.objVal)
    for v in m.getVars():
        print(v.varName, v.x)
# Another way to print the variable
    print("Optimal Solution:", m.objVal)
    print(x.varName, x.x)
    print(y.varName, y.x)        
else:
    print(m.status)
print(f"################################################################")
#####################################################################

#from gurobipy import *
import gurobipy as gp
from gurobipy import GRB

# Create a new Gurobi Model
m = gp.Model("lp")  

# Create two new variables
# (GRB.CONTINUOUS, GRB.BINARY, GRB.INTEGER, GRB.SEMICONT, or GRB.SEMIINT)
x = m.addVar(lb=0, ub=float('inf'), vtype=GRB.CONTINUOUS, name ="x")
y = m.addVar(lb=0, ub=float('inf'), vtype=GRB.CONTINUOUS, name ="y")
z = m.addVar(lb=0, ub=float('inf'), vtype=GRB.CONTINUOUS, name ="z")

# z = m.addVars(10, vtype=GRB.CONTINUOUS, name = "z")
    
# Set the objective function
m.setObjective (60*x + 25*y + 20*z, GRB.MAXIMIZE)
    
#Add Constraints
m.addConstr(8*x + 6*y  + z      <= 50, "c0") # -12, -40 infeasible
m.addConstr(4*x + 2*y  + 1.5*z  <= 20, "c1")
m.addConstr(2*x + 1.5*y + 0.5*z <= 10,  "c2")
m.addConstr(0*x +  1*y  + 0*z   <= 5,  "c3")
    
# Solve the model
m.optimize()
    
# Print the feasible solution if optimal.
if m.status == GRB.Status.OPTIMAL:
    print('Obj Function:', m.objVal)
    for v in m.getVars():
        print(v.varName, v.x)
# Another way to print the variable
    print("Optimal Solution:", m.objVal)
    print(x.varName, x.x)
    print(y.varName, y.x)
    print(z.varName, z.x)        
else:
    print(m.status)
    x.RC
    y.RC
    z.RC