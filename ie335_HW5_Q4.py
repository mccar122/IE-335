# HW 5 Q4 LP:
# min 8a1 + 6a2 + 5a3 + 7a4 + 6b1 + 5b2 + 3b3 + 4b4 + 6c1 + 7c2 + 5c3 + 6c4 + 6d1 + 7d2 + 5d3 + 6d4
# s.t
#     
# 
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
a1 = m.addVar(lb=0, name ="a1")
a2 = m.addVar(lb=0, name ="a2")
a3 = m.addVar(lb=0, name ="a3")
a4 = m.addVar(lb=0, name ="a4")

b1 = m.addVar(lb=0, name ="b1")
b2 = m.addVar(lb=0, name ="b2")
b3 = m.addVar(lb=0, name ="b3")
b4 = m.addVar(lb=0, name ="b4")

c1 = m.addVar(lb=0, name ="c1")
c2 = m.addVar(lb=0, name ="c2")
c3 = m.addVar(lb=0, name ="c3")
c4 = m.addVar(lb=0, name ="c4")

d1 = m.addVar(lb=0, name ="d1")
d2 = m.addVar(lb=0, name ="d2")
d3 = m.addVar(lb=0, name ="d3")
d4 = m.addVar(lb=0, name ="d4")


# Set the objective function
m.setObjective(8*a1 + 6* a2 + 5*a3 + 7*a4 + 6*b1 + 5*b2 + 3*b3 + 4*b4 + 6*c1 + 7*c2 + 5*c3 + 6*c4 + 6*d1 + 7*d2 + 5*d3 + 6*d4, GRB.MINIMIZE)
    
#Add Constraints
m.addConstr( a1 + a2 + a3 + a4 == 1, "c0") # -12, -40 infeasible
m.addConstr( (b1 + b2 + b3 + b4) == 1, "c1")
m.addConstr( (c1 + c2 + c3 + c4) == 1, "c2")
m.addConstr( (d1 + d2 + d3 + d4) ==1, "c3")
m.addConstr( (a1 + b1 + c1 + d1) == 1, "c4")
m.addConstr( (a2 + b2 + c2 + d2) == 1, "c5")
m.addConstr( (a3 + b3 + c3 + d3) == 1, "c6")
m.addConstr( (a4 + b4 + c4 + d4) == 1, "c7")

# Solve the model
m.optimize()
    
# Print the feasible solution if optimal.
if m.status == GRB.Status.OPTIMAL:
    print('Obj Function:', m.objVal)
    print("Optimal Solution:", m.objVal)
    for v in m.getVars():
        print(v.varName, v.x)
# Another way to print the variable
    #print(x.varName, x.x)
    #print(y.varName, y.x)        
else:
    print(m.status)
#print(f"################################################################")
#####################################################################

##from gurobipy import *
#import gurobipy as gp
#from gurobipy import GRB

## Create a new Gurobi Model
#m = gp.Model("lp")  

## Create two new variables
## (GRB.CONTINUOUS, GRB.BINARY, GRB.INTEGER, GRB.SEMICONT, or GRB.SEMIINT)
#x = m.addVar(lb=0, ub=float('inf'), vtype=GRB.CONTINUOUS, name ="x")
#y = m.addVar(lb=0, ub=float('inf'), vtype=GRB.CONTINUOUS, name ="y")
#z = m.addVar(lb=0, ub=float('inf'), vtype=GRB.CONTINUOUS, name ="z")

## z = m.addVars(10, vtype=GRB.CONTINUOUS, name = "z")
    
## Set the objective function
#m.setObjective (60*x + 25*y + 20*z, GRB.MAXIMIZE)
    
##Add Constraints
#m.addConstr(8*x + 6*y  + z      <= 50, "c0") # -12, -40 infeasible
#m.addConstr(4*x + 2*y  + 1.5*z  <= 20, "c1")
#m.addConstr(2*x + 1.5*y + 0.5*z <= 10,  "c2")
#m.addConstr(0*x +  1*y  + 0*z   <= 5,  "c3")
    
## Solve the model
#m.optimize()
    
## Print the feasible solution if optimal.
#if m.status == GRB.Status.OPTIMAL:
 #   print('Obj Function:', m.objVal)
  #  for v in m.getVars():
   #     print(v.varName, v.x)
## Another way to print the variable
#    print("Optimal Solution:", m.objVal)
#    print(x.varName, x.x)
#    print(y.varName, y.x)
#    print(z.varName, z.x)        
#else:
#    print(m.status)
#    x.RC
#    y.RC
#    z.RC