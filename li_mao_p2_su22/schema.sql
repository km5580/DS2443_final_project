CREATE TABLE [AccountAdmin] (
  [AdminStuff] TEXT NOT NULL,
  [AdmiinFirstName] TEXT NOT NULL,
  [AdminLastName] TEXT NOT NULL,
  [AdminState] TEXT NOT NULL,
  [AdminCity] TEXT NOT NULL,
  [AdminZip] INTEGER NOT NULL,
  [AccountName] TEXT NOT NULL,
  PRIMARY KEY ([AccountName])
)
GO

CREATE TABLE [Company] (
  [CompanyCode] INTEGER NOT NULL,
  PRIMARY KEY ([CompanyCode])
)
GO

CREATE TABLE [Associate] (
  [Name] TEXT NOT NULL,
  [Date] TEXT NOT NULL,
  [Type] TEXT NOT NULL,
  PRIMARY KEY ([Name])
)
GO

CREATE TABLE [BillingAccount] (
  [Name] TEXT NOT NULL,
  [BillingAddress] TEXT NOT NULL,
  [City] TEXT,
  [Zip] TEXT,
  [State] TEXT
)
GO

CREATE TABLE [Related] (
  [RelationType] TEXT,
  [AccountName1] TEXT,
  [AccountName2] TEXT
)
GO

CREATE TABLE [AccountHasAdmin] (
  [AdminName] TEXT,
  [AccountName] TEXT
)
GO

CREATE TABLE [Account] (
  [AccountName] TEXT NOT NULL,
  [LocationAddress] TEXT NOT NULL,
  [LocationCity] TEXT NOT NULL,
  [LocationZip] TEXT NOT NULL,
  [LocationState] TEXT,
  [CompanyCode] INTEGER,
  PRIMARY KEY ([AccountName])
)
GO

CREATE TABLE [AssociateRelation] (
  [Type] TEXT,
  [Associate1] TEXT,
  [Associate2] TEXT
)
GO

CREATE TABLE [AssociateIsCustomer] (
  [CustomerName] INTEGER,
  [AssociateName] INTEGER
)
GO

CREATE TABLE [Employed] (
  [AccountName] TEXT,
  [CustomerName] TEXT
)
GO

CREATE TABLE [AccountAlias] (
  [AliasSource] TEXT,
  [StartDate] TEXT,
  [AccountName] TEXT,
  [ContractNum] INTEGER
)
GO

CREATE TABLE [ContractBenefit] (
  [PlanName] TEXT,
  [Rider] TEXT,
  [ID] INTEGER NOT NULL,
  [BenefitPolicy] TEXT,
  [SeriesName] TEXT,
  [ContractNum] INTEGER,
  PRIMARY KEY ([ID])
)
GO

CREATE TABLE [ ContractPremium] (
  [Type] TEXT,
  [Code] INTEGER NOT NULL,
  [AssociateName] TEXT,
  [manners] TEXT,
  [ BenefitId] INTEGER,
  PRIMARY KEY ([Code])
)
GO

CREATE TABLE [CustomerHasBenefit] (
  [CustomerName] TEXT,
  [BenefitID] INTEGER
)
GO

CREATE TABLE [CustomerFor] (
  [Customer1] INTEGER,
  [Customer2] INTEGER
)
GO

CREATE TABLE [Contract] (
  [ContractNumber] INTEGER,
  [PolicyPayer] TEXT,
  PRIMARY KEY ([ContractNumber])
)
GO

CREATE TABLE [ContractPartyRole] (
  [Role] TEXT,
  [Description] TEXT,
  [CustomerName] TEXT,
  [ContractNumber] INTEGER
)
GO

CREATE TABLE [Customer] (
  [Name] TEXT NOT NULL,
  [Suffix] INTEGER NOT NULL,
  [Dob] INTEGER NOT NULL,
  PRIMARY KEY ([Name])
)
GO

CREATE TABLE [ManagerContract] (
  [WritingNumnber] INTEGER,
  [IssueDate] TEXT,
  [SitCode] INTEGER,
  [State] TEXT,
  [AssociateName] TEXT
)
GO

CREATE TABLE [AccountHasManagercontract] (
  [Type] TEXT,
  [AccountName] TEXT,
  [ContractWritingNum] INTEGER
)
GO

CREATE TABLE [AccountUsesBillingAccount] (
  [AccountName] TEXT,
  [BacctName] TEXT,
  [Business Type] TEXT,
  [StartDate] TEXT
)
GO

CREATE TABLE [BillingAdmin] (
  [AdminRole] TEXT NOT NULL,
  [AdminDescription] TEXT,
  [BillingName] TEXT,
  [AdminName] TEXT
)
GO

ALTER TABLE [Related] ADD FOREIGN KEY ([AccountName1]) REFERENCES [Account] ([AccountName])
GO

ALTER TABLE [Related] ADD FOREIGN KEY ([AccountName2]) REFERENCES [Account] ([AccountName])
GO

ALTER TABLE [AccountHasAdmin] ADD FOREIGN KEY ([AccountName]) REFERENCES [Account] ([AccountName])
GO

ALTER TABLE [AccountHasAdmin] ADD FOREIGN KEY ([AdminName]) REFERENCES [AccountAdmin] ([AccountName])
GO

ALTER TABLE [Account] ADD FOREIGN KEY ([CompanyCode]) REFERENCES [Company] ([CompanyCode])
GO

ALTER TABLE [AssociateRelation] ADD FOREIGN KEY ([Associate1]) REFERENCES [Associate] ([Name])
GO

ALTER TABLE [AssociateRelation] ADD FOREIGN KEY ([Associate2]) REFERENCES [Associate] ([Name])
GO

ALTER TABLE [AssociateIsCustomer] ADD FOREIGN KEY ([AssociateName]) REFERENCES [Associate] ([Name])
GO

ALTER TABLE [AssociateIsCustomer] ADD FOREIGN KEY ([CustomerName]) REFERENCES [Customer] ([Name])
GO

ALTER TABLE [Employed] ADD FOREIGN KEY ([AccountName]) REFERENCES [Account] ([AccountName])
GO

ALTER TABLE [Employed] ADD FOREIGN KEY ([CustomerName]) REFERENCES [Customer] ([Name])
GO

ALTER TABLE [AccountAlias] ADD FOREIGN KEY ([AccountName]) REFERENCES [Account] ([AccountName])
GO

ALTER TABLE [AccountAlias] ADD FOREIGN KEY ([ContractNum]) REFERENCES [Contract] ([ContractNumber])
GO

ALTER TABLE [ContractBenefit] ADD FOREIGN KEY ([ContractNum]) REFERENCES [Contract] ([ContractNumber])
GO

ALTER TABLE [ ContractPremium] ADD FOREIGN KEY ([AssociateName]) REFERENCES [Associate] ([Name])
GO

ALTER TABLE [ ContractPremium] ADD FOREIGN KEY ([ BenefitId]) REFERENCES [ContractBenefit] ([ID])
GO

ALTER TABLE [CustomerHasBenefit] ADD FOREIGN KEY ([BenefitID]) REFERENCES [ContractBenefit] ([ID])
GO

ALTER TABLE [CustomerHasBenefit] ADD FOREIGN KEY ([CustomerName]) REFERENCES [Customer] ([Name])
GO

ALTER TABLE [CustomerFor] ADD FOREIGN KEY ([Customer1]) REFERENCES [Customer] ([Name])
GO

ALTER TABLE [CustomerFor] ADD FOREIGN KEY ([Customer2]) REFERENCES [Customer] ([Name])
GO

ALTER TABLE [ContractPartyRole] ADD FOREIGN KEY ([CustomerName]) REFERENCES [Customer] ([Name])
GO

ALTER TABLE [ContractPartyRole] ADD FOREIGN KEY ([ContractNumber]) REFERENCES [Contract] ([ContractNumber])
GO

ALTER TABLE [ManagerContract] ADD FOREIGN KEY ([AssociateName]) REFERENCES [Associate] ([Name])
GO

ALTER TABLE [AccountHasManagercontract] ADD FOREIGN KEY ([ContractWritingNum]) REFERENCES [ManagerContract] ([WritingNumnber])
GO

ALTER TABLE [AccountHasManagercontract] ADD FOREIGN KEY ([AccountName]) REFERENCES [Account] ([AccountName])
GO

ALTER TABLE [AccountUsesBillingAccount] ADD FOREIGN KEY ([AccountName]) REFERENCES [Account] ([AccountName])
GO

ALTER TABLE [AccountUsesBillingAccount] ADD FOREIGN KEY ([BacctName]) REFERENCES [BillingAccount] ([Name])
GO

ALTER TABLE [BillingAdmin] ADD FOREIGN KEY ([AdminName]) REFERENCES [AccountAdmin] ([AdmiinFirstName])
GO

ALTER TABLE [BillingAdmin] ADD FOREIGN KEY ([BillingName]) REFERENCES [BillingAccount] ([Name])
GO
