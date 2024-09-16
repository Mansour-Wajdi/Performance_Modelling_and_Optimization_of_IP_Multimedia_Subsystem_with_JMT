from gurobipy import Model, GRB
from values import normal_values, overload_values

# Initialize the model
model = Model("SystemOfEquations")
# Set the NonConvex parameter to 2
model.params.NonConvex = 2

#params for probabilities 
minProb = 0.1
maxProb = 0.9

# Add variables
p12 = model.addVar(lb=minProb, ub=maxProb, vtype=GRB.CONTINUOUS, name="p12")
p13 = model.addVar(lb=minProb, ub=maxProb, vtype=GRB.CONTINUOUS, name="p13")
p21 = model.addVar(lb=minProb, ub=maxProb, vtype=GRB.CONTINUOUS, name="p21")
p23 = model.addVar(lb=minProb, ub=maxProb, vtype=GRB.CONTINUOUS, name="p23")
p31 = model.addVar(lb=minProb, ub=maxProb, vtype=GRB.CONTINUOUS, name="p31")
p32 = model.addVar(lb=minProb, ub=maxProb, vtype=GRB.CONTINUOUS, name="p32")
p33 = model.addVar(lb=minProb, ub=maxProb, vtype=GRB.CONTINUOUS, name="p33")
p34 = model.addVar(lb=minProb, ub=maxProb, vtype=GRB.CONTINUOUS, name="p34")
p1i = model.addVar(lb=minProb, ub=maxProb, vtype=GRB.CONTINUOUS, name="p1i")

# error variables for the constraints
error_vars = [model.addVar(vtype=GRB.CONTINUOUS, name=f"error_{i}") for i in range(1, 20)]
# Set objective to minimize the sum of error variables
model.setObjective(sum(error_vars), GRB.MINIMIZE)

#  liniarisations
z0 = model.addVar(vtype=GRB.CONTINUOUS, name="z0")
model.addConstr(z0 == p13*p21, "z_definition")
z1 = model.addVar(vtype=GRB.CONTINUOUS, name="z1")
model.addConstr(z1 == p23*p31, "z1_definition")
z2 = model.addVar(vtype=GRB.CONTINUOUS, name="z2")
model.addConstr(z2 == p21*p32, "z2_definition")
z3 = model.addVar(vtype=GRB.CONTINUOUS, name="z3")
model.addConstr(z3 == p12*p21, "z3_definition")
z4= model.addVar(vtype=GRB.CONTINUOUS, name="z4")
model.addConstr(z4 == p23*p12, "z4_definition")
z5= model.addVar(vtype=GRB.CONTINUOUS, name="z5")
model.addConstr(z5 == p12*p31, "z5_definition")
z6= model.addVar(vtype=GRB.CONTINUOUS, name="z6")
model.addConstr(z6 == p21*p12, "z6_definition")
z7= model.addVar(vtype=GRB.CONTINUOUS, name="z7")
model.addConstr(z7 == p13*p32, "z7_definition")
z8= model.addVar(vtype=GRB.CONTINUOUS, name="z8")
model.addConstr(z8 == p12*p33, "z8_definition")

# Introduce an auxiliary variable
aux = model.addVar(vtype=GRB.CONTINUOUS, name="aux")

# Define the auxiliary variable (ensure this is a linear expression)
model.addConstr(aux == z0*(p23+p31), "aux_definition")


# Add constraints for normal load 
model.addConstr(normal_values["lambda_1_normal"] - normal_values["lambda_01_normal"] - p21*normal_values["lambda_2_normal"] - p31*normal_values["lambda_3_normal"] + error_vars[0] ==  0 , "eq1_normal")
model.addConstr(normal_values["lambda_2_normal"] - p12*normal_values["lambda_1_normal"] - p32*normal_values["lambda_3_normal"] + error_vars[1] == 0 , "eq2_normal")
model.addConstr(normal_values["lambda_3_normal"] - normal_values["lambda_03_normal"] - p13*normal_values["lambda_1_normal"] - p23*normal_values["lambda_2_normal"] - p33*normal_values["lambda_3_normal"] + error_vars[2] == 0, "eq3_normal")
model.addQConstr(normal_values["lambda_1_normal"] * (1 - z3 - z1 - p31*aux) - normal_values["lambda_01_normal"] *(1-z1-p33) - normal_values["lambda_03_normal"]*(z2+p31) + error_vars[6] ==  0, "eq6_normal")
model.addQConstr(normal_values["lambda_2_normal"] * (1 - z3 - z1 - p31*aux) - normal_values["lambda_01_normal"] *(p12-z8-z7) - normal_values["lambda_03_normal"]*(z5+p32) + error_vars[7] == 0, "eq7_normal")
model.addQConstr(normal_values["lambda_3_normal"] * (1 - z3 - z1 - p31*aux)  - normal_values["lambda_01_normal"] *(p13+z4) - normal_values["lambda_03_normal"]*(1-z6) + error_vars[8] == 0, "eq8_normal")

# Add constraints for overload
model.addConstr(overload_values["lambda_1_overload"] - overload_values["lambda_01_overload"] - p21*overload_values["lambda_2_overload"] - p31*overload_values["lambda_3_overload"] + error_vars[9] ==  0 , "eq1_overload")
model.addConstr(overload_values["lambda_2_overload"] - p12*overload_values["lambda_1_overload"] - p32*overload_values["lambda_3_overload"] + error_vars[10] == 0 , "eq2_overload")
model.addConstr(overload_values["lambda_3_overload"] - overload_values["lambda_03_overload"] - p13*overload_values["lambda_1_overload"] - p23*overload_values["lambda_2_overload"] - p33*overload_values["lambda_3_overload"] + error_vars[11] == 0, "eq3_overload")
model.addQConstr(overload_values["lambda_1_overload"] * (1 - z3 - z1 - p31*aux) - overload_values["lambda_01_overload"] *(1-z1-p33) - overload_values["lambda_03_overload"]*(z2+p31) + error_vars[12] ==  0, "eq6_overload")
model.addQConstr(overload_values["lambda_2_overload"] * (1 - z3 - z1 - p31*aux) - overload_values["lambda_01_overload"] *(p12-z8-z7) - overload_values["lambda_03_overload"]*(z5+p32) + error_vars[13] == 0, "eq7_overload")
model.addQConstr(overload_values["lambda_3_overload"] * (1 - z3 - z1 - p31*aux)  - overload_values["lambda_01_overload"] *(p13+z4) - overload_values["lambda_03_overload"]*(1-z6) + error_vars[14] == 0, "eq8_overload")

# Add general constraints 
model.addConstr(p12 + p13 + p1i  + error_vars[3] == 1, "eq_cond1")
model.addConstr(p21 + p23  + error_vars[4] == 1, "eq_cond2")
model.addConstr(p31 + p32 + p33 + p34  + error_vars[5] == 1, "eq_cond3")


# Solve the model
model.optimize()

# Check and print the solution
if model.status == GRB.OPTIMAL:
    print("Found optimal solution:")
    for v in model.getVars()[0:18]:
        if abs(v.x) > 0.001:
            print(f"{v.varName} = {v.x}")
        else:
            print(f"{v.varName} = {0}")
elif model.status == GRB.INFEASIBLE:
    print("Model is infeasible.")
else:
    print("Optimization was stopped with status", model.status)
