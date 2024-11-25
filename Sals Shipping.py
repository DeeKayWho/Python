weight = 50

###################    ground shipping   ##################

ground_ship_flat = 20

if weight > 10:
    cost_pp_gr = 4.75
elif weight > 6 and weight <= 10:
    cost_pp_gr = 4.00
elif weight > 2 and weight <= 6:
    cost_pp_gr = 3.00
elif weight <= 2:
    cost_pp_gr = 1.50

total_ground_ship_cost = (cost_pp_gr * weight + ground_ship_flat)
# -------------------------------------------------------------------

###################   Ground Shipping Premium    #################

total_ground_ship_premium_cost = 125.00

print("^^^^^^||||  By the way ground shipping Premium is 125.00 !!! ||||^^^^^^")

# --------------------------------------------------------------------

###################   Drone Shipping *New*     ######################

drone_ship_flat = 0

if weight > 10:
    cost_pp_dr = 14.25
elif weight > 6 and weight <= 10:
    cost_pp_dr = 12.00
elif weight > 2 and weight <= 6:
    cost_pp_dr = 9.00
elif weight <= 2:
    cost_pp_dr = 4.50

total_drone_ship_cost = (cost_pp_dr * weight + drone_ship_flat)
# --------------------------------------------------------------------

###################   Drone Shipping *New* = Cheapest    ######################
if total_drone_ship_cost < total_ground_ship_cost and total_drone_ship_cost < 125.00:
    total_saved_negative_dr = total_drone_ship_cost - total_ground_ship_cost
    total_saved_dr = total_saved_negative_dr * -1
    print("Our Recommended Option is Our New Drone Shipping!!!")
    print("This will save you $", total_saved_dr)
    print("When compared to our standard Ground Shipping Delivery!!!")
# --------------------------------------------------------------------

###################   Ground Shipping = Cheapest   ######################
elif total_ground_ship_cost < total_drone_ship_cost and total_ground_ship_cost < 125.00:
    total_saved_negative_gr = total_ground_ship_cost - total_drone_ship_cost
    total_saved_gr = total_saved_negative_gr * -1
    print()
    print("Our Recommended Option is Our Signature Ground Shipping!!!")
    print()
    print("Total: ""$", total_ground_ship_cost)
    print()
    print()
    print("!! Save More When you Ship less ~ with New Drone Delivery!!")
# --------------------------------------------------------------------

###################   Ground Shipping Pemium = Cheapest     ######################
else:
    print()
    print("Our Recommended Option is Our MEGA Fast Ground Shipping Premium!!!")
    print()
    print("Total: ""$", "125.00")
    print()
    print()
    print("!! Save More When you Ship less ~ with New Drone Delivery!!")

# Thanks For Reading My Code ~ Josh Dk