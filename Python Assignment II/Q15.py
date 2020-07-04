# Imagine you are designing a banking application. What would a customer look like?
# What attributes would she have? What methods would she have?

class CustomerInfo:

    customerList = [{"Name": "Aashish Tuladhar", "Acc": "121020110", "Gender": "Male", "Balance": 20000}, 
                    {"Name": "Prakritee Maharjan", "Acc": "121020111", "Gender": "Female", "Balance": 15000}
                   ]
    minimumBalance = 100

    def __init__(self, accName, accNumber):
        self.accName = accName
        self.accNumber = accNumber
        
    def getInfo(self):
        customer = next((item for item in self.customerList if item["Acc"] == self.accNumber and item["Name"] == self.accName), None)
        if (customer is not None):
            print(f"Details: \nA/C: {customer.get('Acc')} \nOwner: {customer.get('Name')} \nGender: {customer.get('Gender')} \nBalance: {customer.get('Balance')}")
        else:
            print(f"No customer {self.accName} found")

    @classmethod
    def balance(classObject):
        return classObject.minimumBalance

customer = CustomerInfo("Aashish Tuladhar", "121020110")
customer.getInfo()


print("Minimum balance:",CustomerInfo.balance())