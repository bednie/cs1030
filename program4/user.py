# User holds data for five attributes: first name, last name, user ID, email, and phone number
class User:
    
    # Constructor
    def __init__(self, firstName, lastName, userId, userEmail, userPhoneNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.userId = userId
        self.userEmail = userEmail
        self.userPhoneNumber = userPhoneNumber

    # Print summary of attributes of User
    def DescribeUser(self):
        print("First Name: " + self.firstName + "\n" +
                "Last Name: "+ self.lastName + "\n" +
                "User ID: "+ self.userId + "\n" +
                "Phone Number: "+ self.userPhoneNumber + "\n" +
                "Email Address: "+ self.userEmail + "\n")

    # Setters and getters below:
    def getFirstName(self):
        return self.firstName

    def setFirstName(self, newFirstName):
        self.firstName = newFirstName
    
    def getLastName(self):
        return self.lastName

    def setLastName(self, newLastName):
        self.lastName = newLastName
    
    def getUserId(self):
        return self.userId

    def setUserId(self, newUserId):
        self.userId = newUserId

    def getUserEmail(self):
        return self.userEmail

    def setUserEmail(self, newUserEmail):
        self.userEmail = newUserEmail

    def getUserPhoneNumber(self):
        return self.userPhoneNumber

    def setUserPhoneNumber(self, newUserPhoneNumber):
        self.userPhoneNumber = newUserPhoneNumber


