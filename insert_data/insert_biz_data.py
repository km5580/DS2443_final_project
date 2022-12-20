import mysql.connector

server = 'project4.mysql.database.azure.com'
database = 'project4'
username = 'project4'
password = '12345ssdlh@'
driver= '{ODBC Driver 17 for SQL Server}'
ssl = '/Users/linxia/Downloads/DigiCertGlobalRootCA.crt.pem'

query = """
CREATE TABLE IF NOT EXISTS AccountAdmin (
AdminStuff CHAR(20) NOT NULL,
AdminFirstName CHAR(20) NOT NULL,
AdminLastName CHAR(20) NOT NULL,
AdminState CHAR(20) NOT NULL,
AdminCity CHAR(20) NOT NULL,
AdminZip INTEGER(20) NOT NULL,
AccountName CHAR(20) NOT NULL,
PRIMARY KEY(AccountName)
);

CREATE TABLE IF NOT EXISTS Customer (
Name CHAR(20) NOT NULL,
Suffix CHAR(20) NOT NULL,
Dob CHAR(20) NOT NULL,
PRIMARY KEY(Name)
);

CREATE TABLE IF NOT EXISTS Contract (
ContractNumber INTEGER(20),
PolicyPayer CHAR(20),
PRIMARY KEY(ContractNumber)
);

CREATE TABLE IF NOT EXISTS Company (
CompanyCode INTEGER(20) NOT NULL,
PRIMARY KEY(CompanyCode)
);

CREATE TABLE IF NOT EXISTS Account (
AccountName CHAR(20) NOT NULL,
LocationAddress CHAR(20) NOT NULL,
LocationCity CHAR(20) NOT NULL,
LocationZip CHAR(20) NOT NULL,
LocationState CHAR(20),
CompanyCode INTEGER(20),
FOREIGN KEY(CompanyCode) REFERENCES Company(CompanyCode),
PRIMARY KEY(AccountName)
);

CREATE TABLE IF NOT EXISTS Associate (
Name CHAR(20) NOT NULL,
Date CHAR(20) NOT NULL,
Type CHAR(20) NOT NULL,
PRIMARY KEY(Name)
);

CREATE TABLE IF NOT EXISTS BillingAccount (
Name CHAR(20) NOT NULL,
BillingAddress CHAR(20) NOT NULL,
City CHAR(20),
Zip CHAR(20),
State CHAR(20),
PRIMARY KEY(Name)
);

CREATE TABLE IF NOT EXISTS Related (
RelationType CHAR(20),
AccountName1 CHAR(20) NOT NULL,
AccountName2 CHAR(20) NOT NULL,
FOREIGN KEY(AccountName1) REFERENCES Account(AccountName),
FOREIGN KEY(AccountName2) REFERENCES Account(AccountName)
);

CREATE TABLE IF NOT EXISTS AccountHasAdmin (
AdminName CHAR(20),
AccountName CHAR(20),
FOREIGN KEY(AccountName) REFERENCES Account(AccountName),
FOREIGN KEY(AdminName) REFERENCES AccountAdmin(AccountName)
);


CREATE TABLE IF NOT EXISTS AccountMember (
StartDate CHAR(20),
MemberId INTEGER(20),
AccountName CHAR(20),
FOREIGN KEY(AccountName) REFERENCES Account(AccountName)
);

CREATE TABLE IF NOT EXISTS AssociateRelation (
Type CHAR(20),
Associate1 CHAR(20),
Associate2 CHAR(20),
FOREIGN KEY(Associate1) REFERENCES Associate(Name),
FOREIGN KEY(Associate2) REFERENCES Associate(Name)
);

CREATE TABLE IF NOT EXISTS AssociateIsCustomer (
CustomerName CHAR(20),
AssociateName CHAR(20),
FOREIGN KEY(AssociateName) REFERENCES Associate(Name),
FOREIGN KEY(CustomerName) REFERENCES Customer(Name)
);

CREATE TABLE IF NOT EXISTS Employed (
AccountName CHAR(20),
CustomerName CHAR(20),
FOREIGN KEY(AccountName) REFERENCES Account(AccountName),
FOREIGN KEY(CustomerName) REFERENCES Customer(Name)
);

CREATE TABLE IF NOT EXISTS AccountAlias (
AliasSource CHAR(20),
StartDate CHAR(20),
AccountName CHAR(20),
ContractNum INTEGER(20),
FOREIGN KEY(AccountName) REFERENCES Account(AccountName),
FOREIGN KEY(ContractNum) REFERENCES Contract(ContractNumber)
);

CREATE TABLE IF NOT EXISTS ContractBenefit (
PlanName CHAR(20),
Rider CHAR(20),
ID INTEGER(20) NOT NULL,
BenefitPolicy CHAR(20),
SeriesName CHAR(20),
ContractNum INTEGER(20),
FOREIGN KEY(ContractNum) REFERENCES Contract(ContractNumber),
PRIMARY KEY(ID)
);

CREATE TABLE IF NOT EXISTS ContractPremium (
Type CHAR(20),
Code INTEGER(20) NOT NULL,
AssociateName CHAR(20),
manners CHAR(20),
BenefitId INTEGER(20),
FOREIGN KEY(AssociateName) REFERENCES Associate(Name),
FOREIGN KEY(BenefitId) REFERENCES ContractBenefit(ID),
PRIMARY KEY(Code)
);

CREATE TABLE IF NOT EXISTS CustomerHasBenefit (
CustomerName CHAR(20),
BenefitID INTEGER(20),
FOREIGN KEY(BenefitID) REFERENCES ContractBenefit(ID),
FOREIGN KEY(CustomerName) REFERENCES Customer(Name)
);

CREATE TABLE IF NOT EXISTS CustomerFor (
Customer1 CHAR(20),
Customer2 CHAR(20),
FOREIGN KEY(Customer1) REFERENCES Customer(Name),
FOREIGN KEY(Customer2) REFERENCES Customer(Name)
);

CREATE TABLE IF NOT EXISTS Contract (
ContractNumber INTEGER(20),
PolicyPayer CHAR(20),
PRIMARY KEY(ContractNumber)
);

CREATE TABLE IF NOT EXISTS ContractPartyRole (
Role CHAR(20),
Description CHAR(20),
CustomerName CHAR(20),
ContractNumber INTEGER(20),
FOREIGN KEY(CustomerName) REFERENCES Customer(Name),
FOREIGN KEY(ContractNumber) REFERENCES Contract(ContractNumber)
);

CREATE TABLE IF NOT EXISTS ManagerContract (
WritingNumber INTEGER(20),
IssueDate CHAR(20),
SitCode INTEGER(20),
State CHAR(20),
AssociateName CHAR(20),
PRIMARY KEY(WritingNumber),
FOREIGN KEY(AssociateName) REFERENCES Associate(Name)
);

CREATE TABLE IF NOT EXISTS AccountHasManagerContract (
 Type CHAR(20),
 AccountName CHAR(20),
 ContractWritingNum INTEGER(20),
 FOREIGN KEY(ContractWritingNum) REFERENCES ManagerContract(WritingNumber),
 FOREIGN KEY(AccountName) REFERENCES Account(AccountName)
);

CREATE TABLE IF NOT EXISTS AccountUsesBillingAccount (
 AccountName CHAR(20),
 BacctName CHAR(20),
 BusinessType CHAR(20),
 StartDate DATE,
 FOREIGN KEY(AccountName) REFERENCES Account(AccountName),
 FOREIGN KEY(BacctName) REFERENCES BillingAccount(Name)
);

CREATE TABLE IF NOT EXISTS BillingAdmin (
 AdminRole CHAR(20) NOT NULL,
 AdminDescription CHAR(20),
 BillingName CHAR(20),
 AdminName CHAR(20),
 FOREIGN KEY(AdminName) REFERENCES AccountAdmin(AccountName),
 FOREIGN KEY(BillingName) REFERENCES BillingAccount(Name)
);

INSERT INTO AccountAdmin VALUES ('a','Summer','Li','NY','Rochester',14086,'Kiwi');
INSERT INTO Company VALUES (1001);
INSERT INTO Company VALUES (1002);
INSERT INTO Associate VALUES ('Ann','2021-12-31','A');
INSERT INTO Associate VALUES ('Bob','2020-03-20','B');
INSERT INTO BillingAccount VALUES ('Jason','111 Ave','Rochester','14086','NY');
INSERT INTO BillingAccount VALUES ('Chloe','112 Ave','San Jose','95112','CA');
INSERT INTO Account VALUES ('Kiwi','200 Ave ','Rochester','14086','NY',1001);
INSERT INTO Account VALUES ('Tigre','201 Blvd','San Jose','95112','CA',1001);
INSERT INTO Account VALUES ('Samii','202 Blvd','San Jose','95113','CA',1002);
INSERT INTO Account VALUES ('Jojo','201 Ave','Jersey City','07306','NJ',1002);
INSERT INTO Related VALUES ('a','Tigre','Samii');
INSERT INTO Related VALUES ('c','Kiwi','Jojo');
INSERT INTO AccountHasAdmin VALUES ('Kiwi','Kiwi');
INSERT INTO AccountMember VALUES ('2022-01-01',1,'Kiwi');
INSERT INTO AccountMember VALUES ('2022-01-02',2,'Samii');
INSERT INTO AssociateRelation VALUES ('a','Ann','Bob');
INSERT INTO Customer VALUES ('Chloe','C','2022-10-13');
INSERT INTO Customer VALUES ('Linxia','L','2022-04-25');
INSERT INTO AssociateIsCustomer VALUES ('Chloe','Ann');
INSERT INTO AssociateIsCustomer VALUES ('Linxia','Bob');
INSERT INTO Employed VALUES ('Tigre','Chloe');
INSERT INTO Employed VALUES ('Kiwi','Linxia');
INSERT INTO Contract VALUES (1111,'Cash');
INSERT INTO Contract VALUES (1112,'Card');
INSERT INTO AccountAlias VALUES ('1','2022-01-01','Samii',1111);
INSERT INTO AccountAlias VALUES ('2','2022-01-03','Kiwi',1112);
INSERT INTO ContractBenefit VALUES ('M','Q',1,'full-covered','O',1111);
INSERT INTO ContractBenefit VALUES ('N','W',2,'half_covered','P',1112);
INSERT INTO ContractPremium VALUES ('S',1,'Ann','Z',1);
INSERT INTO ContractPremium VALUES ('A',2,'Bob','X',2);
INSERT INTO ContractPremium VALUES ('D',3,'Ann','C',1);
INSERT INTO CustomerHasBenefit VALUES ('Linxia',1);
INSERT INTO CustomerHasBenefit VALUES ('Chloe',2);
INSERT INTO ContractPartyRole VALUES ('a','a','Linxia',1111);
INSERT INTO ContractPartyRole VALUES ('b','b','Chloe',1112);
INSERT INTO ManagerContract VALUES (111,'2022-12-31',1,'NJ','Ann');
INSERT INTO ManagerContract VALUES (112,'2022-11-11',2,'NY','Ann');
INSERT INTO ManagerContract VALUES (113,'2022-10-31',1,'CA','Bob');
INSERT INTO AccountHasManagerContract VALUES ('1','Tigre',111);
INSERT INTO AccountHasManagerContract VALUES ('2','Samii',112);
INSERT INTO BillingAdmin VALUES ('a','cd','Jason','Kiwi');
INSERT INTO BillingAdmin VALUES ('b','ef','Chloe','Kiwi');
"""

cnx = mysql.connector.connect(user=username, password=password, host=server, port=3306, database=database, ssl_ca=ssl, ssl_disabled=False, autocommit=True)
cursor = cnx.cursor()

try:
    query = filter(None, query.split(';'))

    for i in query:
        if i != "\n":
            cursor.execute(i.strip() + ';')
except mysql.connector.Error as err:
    print("Failed creating database: {}".format(err))
    exit(1)
