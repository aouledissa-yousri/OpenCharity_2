from datetime import date, datetime
import core.models.User as User
import core.models.Donation as Donation

class DonationCampaign: 

    def __init__(self, id, title, description, beneficiary, donations=[], openStatus=True):
        self.__id = id
        self.__title = title
        self.__description = description
        self.__beneficiary = beneficiary
        self.__donations = donations
        self.__openStatus = openStatus
        self.__dateCreated = date.today()

    def getId(self):
        return self.__id
    
    def getTitle(self):
        return self.__title

    def getDescription(self):
        return self.__description
    
    def getBeneficiary(self):
        return self.__beneficiary
    
    def getDonations(self):
        return self.__donations
    
    def getOpenStatus(self):
        return self.__openStatus

    def getDateCreated(self):
        return self.__dateCreated.isoformat()

    def getData(self):
        return {
            "id": self.getId(),
            "title": self.getTitle(),
            "description": self.getDescription(),
            "beneficiary": self.getBeneficiary(),
            "donations": self.getDonations(),
            "openStatus": self.getOpenStatus(),
            "dateCreated": self.getDateCreated()
        }
    

    def setTitle(self, title: str):
        self.__title = title
    
    def setDescription(self, description: str):
        self.__description = description
    
    def setId(self, id: str):
        self.__id = id
    
    def setOpenStatus(self, openStatus: bool):
        self.__openStatus = openStatus
    
    def addDonation(self, donor: User, donation: Donation):
        self.__donations[donor.getWalletAddress()] = donation

    def update(self, title: str = None, description: str = None, openStatus: bool = None):
        if title is not None:
            self.setTitle(title)
        if description is not None:
            self.setDescription(description)
        if openStatus is not None:
            self.setOpenStatus(openStatus)    
