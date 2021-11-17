from user import User

class Admin(User):

    def __init__(self, firstName, lastName, userId, userEmail, userPhoneNumber):

        # Instantiate superclass
        super().__init__(firstName, lastName, userId, userEmail, userPhoneNumber)
        
        # Create list to hold admin user's privileges
        self.privileges = []

        # Create dict of all possible admin privileges 
        self.admin_privileges_dict = {'CAN_POST': "can post",
                                    'CAN_DEL':'can delete',
                                    'CAN_EDIT':'can edit',
                                    'CAN_BAN':'can ban',
                                    'CAN_ADD' : 'can add user',
                                    'CAN_LOCK' : 'can lock posts',
                                    'CAN_UNLOCK' : 'can unlock posts',
                                    'CAN_HIDE' :'can hide posts'}

    # Set privileges 
    def set_privilege(self, *p):
        for i in p:
            self.privileges.append(self.admin_privileges_dict[i])

    # Set full admin privileges
    def set_all_privileges(self):
        [self.privileges.append(self.admin_privileges_dict[i]) for i in self.admin_privileges_dict]

    # Remove admin privileges
    def del_privileges(self):
        self.privileges.clear()

    # Get privileges, returns a list object
    def get_privileges(self):
        return self.privileges

    # Print the admin's name and all privileges
    def show_privileges(self):
        print(f'The admin {self.firstName} {self.lastName} has the following privileges: ')
        [print(str(i)) for i in self.privileges]    