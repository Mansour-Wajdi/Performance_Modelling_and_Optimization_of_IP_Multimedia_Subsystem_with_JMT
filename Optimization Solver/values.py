##############################
####### normal load ##########
##############################
lambda_01_normal = 0.34916
lambda_03_normal = 0.14716

# Equations (11), (12), (13)
lambda_1_normal = 1.52 * lambda_01_normal + 1.01*lambda_03_normal 
lambda_2_normal = 0.0923 * lambda_01_normal + 0.11*lambda_03_normal
lambda_3_normal = 1.06 * lambda_03_normal + 2.14 * lambda_03_normal


# Utilization 
P_CSCF_Utilization = 0.3397 
I_CSCF_Utilization = 0.048 
S_CSCF_Utilization = 0.5633

# service rate
P_CSCF_service_rate = lambda_1_normal / P_CSCF_Utilization
I_CSCF_service_rate = lambda_2_normal / I_CSCF_Utilization
S_CSCF_service_rate = lambda_3_normal / S_CSCF_Utilization

# print all normal values
print("normal load values :") 
print("lambda_01_normal", lambda_01_normal)
print("lambda_03_normal", lambda_03_normal)
print("lambda_1_normal", lambda_1_normal)
print("lambda_2_normal", lambda_2_normal)
print("lambda_3_normal", lambda_3_normal)
print("P_CSCF_Utilization", P_CSCF_Utilization)
print("I_CSCF_Utilization", I_CSCF_Utilization)
print("S_CSCF_Utilization", S_CSCF_Utilization)
print("P_CSCF_service_rate", P_CSCF_service_rate)
print("I_CSCF_service_rate", I_CSCF_service_rate)
print("S_CSCF_service_rate", S_CSCF_service_rate)

# wrape all values in a dictionary
normal_values = {
    "lambda_01_normal": lambda_01_normal,
    "lambda_03_normal": lambda_03_normal,
    "lambda_1_normal": lambda_1_normal,
    "lambda_2_normal": lambda_2_normal,
    "lambda_3_normal": lambda_3_normal,
}

# cscf values 
cscf_values = {
    "P_CSCF_Utilization": P_CSCF_Utilization,
    "I_CSCF_Utilization": I_CSCF_Utilization,
    "S_CSCF_Utilization": S_CSCF_Utilization,
    "P_CSCF_service_rate": P_CSCF_service_rate,
    "I_CSCF_service_rate": I_CSCF_service_rate,
    "S_CSCF_service_rate": S_CSCF_service_rate,
}

##############################
####### overload #############
##############################

lambda_01_overload = 0.8729
lambda_03_overload =  0.3679

# Equations (11), (12), (13)
lambda_1_overload = 1.52 * lambda_01_overload + 1.01*lambda_03_overload
lambda_2_overload = 0.0923 * lambda_01_overload + 0.11*lambda_03_overload
lambda_3_overload = 1.06 * lambda_03_overload + 2.14 * lambda_03_overload

# wrape all values in a dictionary
overload_values = {
    "lambda_01_overload": lambda_01_overload,
    "lambda_03_overload": lambda_03_overload,
    "lambda_1_overload": lambda_1_overload,
    "lambda_2_overload": lambda_2_overload,
    "lambda_3_overload": lambda_3_overload
}
print("####################") 
print("overload values :") 
print("lambda_01_overload", lambda_01_overload)
print("lambda_03_overload", lambda_03_overload)
print("lambda_1_overload", lambda_1_overload)
print("lambda_2_overload", lambda_2_overload)
print("lambda_3_overload", lambda_3_overload)



p_class1 = 4112/7695
p_class2 = 2504/7695
p_class3 = 1079/7695

lambda_3_class1 = p_class1 * lambda_3_overload
lambda_3_class2 = p_class2 * lambda_3_overload
lambda_3_class3 = p_class3 * lambda_3_overload

print("####################") 
print("les probabilités des classes : ") 

print("p_class1",p_class1) 
print("p_class2",p_class2) 
print("p_class3",p_class3) 

print("lambda_3_class1",lambda_3_class1) 
print("lambda_3_class2",lambda_3_class2)
print("lambda_3_class3",lambda_3_class3)
