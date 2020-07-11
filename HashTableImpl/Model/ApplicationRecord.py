class ApplicationRecord:
    def __init__(self,applicantName,phoneNumber,memberReference,applicationStatus):
        self.applicantName=applicantName;
        self.phoneNumber=phoneNumber;
        self.memberReference=memberReference;
        self.applicationStatus=applicationStatus;
    def __str__(self):
        return self.applicantName+","+self.phoneNumber+","+self.memberReference+","+self.applicationStatus;
