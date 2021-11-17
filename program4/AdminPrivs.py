from admin import Admin

# Create three instances of Admin and test various methods 
sutton = Admin("Ray", "Sutton", "900876123", "ray.sutton25252@msudenver.edu", "+8604097387")
sutton.set_privilege('CAN_ADD','CAN_POST','CAN_BAN')
sutton.show_privileges()

b_e = Admin("B", "E", "900123654", "be1234@msudenver.edu", "+1234567")
b_e.set_privilege('CAN_ADD','CAN_HIDE','CAN_LOCK','CAN_UNLOCK')
b_e.show_privileges()

supreme_admin = Admin('Supreme', 'Admin', '','','')
supreme_admin.set_all_privileges()
supreme_admin.show_privileges()


