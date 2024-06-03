CREATE DATABASE Preparation_dw
GO
USE Preparation_dw;

-- Création des tables
CREATE TABLE Geography_Dim (
    Geography_Key INT PRIMARY KEY,
    Region NVARCHAR(50),
    Province NVARCHAR(50),
    Municipality NVARCHAR(50),
    Latitude DECIMAL(10,7),
    Longitude DECIMAL(10,7),
    MunicipalityArea INT
);

CREATE TABLE Time_Dim (
    Time_Key INT PRIMARY KEY,
    FullDate DATE,
    Month INT,
    MonthName NVARCHAR(10),
    Quarter NVARCHAR(2),
    Year INT
);

CREATE TABLE Demography_Facts(
    Geography_Key INT,
    Time_Key INT,
    People_Count INT,
    Age INT,
    Gender NVARCHAR(20),
    PRIMARY KEY (Geography_Key, Time_Key),
    FOREIGN KEY (Geography_Key) REFERENCES Geography_Dim(Geography_Key),
    FOREIGN KEY (Time_Key) REFERENCES Time_Dim(Time_Key)
);

CREATE TABLE EmergencyFacts (
    Geography_Key INT,
    Time_Key INT,
    Hospital_Key INT,
    Average_Response_Time NVARCHAR(10),
    PRIMARY KEY (Geography_Key, Time_Key, Hospital_Key),
    FOREIGN KEY (Geography_Key) REFERENCES Geography_Dim(Geography_Key),
    FOREIGN KEY (Time_Key) REFERENCES Time_Dim(Time_Key)
);

CREATE TABLE Hospital_Dim (
    Hospital_Key INT PRIMARY KEY,
    Hospital_Name NVARCHAR(50),
    Hospital_Foundation_date DATE,
    Hospital_Closing_date DATE
);

CREATE TABLE Health_Personnel_Dim (
    Health_Personnel_Key NVARCHAR(5) PRIMARY KEY,
    Hospital_Key INT,
    FirstName NVARCHAR(20),
    LastName NVARCHAR(20),
    Gender NVARCHAR(20),
    ContactNumber NVARCHAR(20),
    Email NVARCHAR(50),
    Address NVARCHAR(20),
    Role NVARCHAR(20),
    ExperienceYears INT,
    EmergencyTraining BIT,
    JoiningDate DATE,
    LeavingDate DATE,
    Departement NVARCHAR(50),
    StartDate DATE,
    EndDate DATE,
    ActiveRow BIT,
    FOREIGN KEY (Hospital_Key) REFERENCES Hospital_Dim(Hospital_Key)
);


CREATE TABLE Hospital_HR_Facts (
    Geography_Key INT,
    Time_Key INT,
    Health_Personnel_Key NVARCHAR(5),
    PRIMARY KEY (Geography_Key, Time_Key, Health_Personnel_Key),
    FOREIGN KEY (Geography_Key) REFERENCES Geography_Dim(Geography_Key),
    FOREIGN KEY (Time_Key) REFERENCES Time_Dim(Time_Key),
    FOREIGN KEY (Health_Personnel_Key) REFERENCES Health_Personnel_Dim(Health_Personnel_Key)
);

CREATE TABLE Beds_Facts (
    Geography_Key INT,
    Time_Key INT,
    Hospital_Key INT,
    Number_Of_Bads INT,
    PRIMARY KEY (Geography_Key, Time_Key, Hospital_Key),
    FOREIGN KEY (Geography_Key) REFERENCES Geography_Dim(Geography_Key),
    FOREIGN KEY (Time_Key) REFERENCES Time_Dim(Time_Key),
    FOREIGN KEY (Hospital_Key) REFERENCES Hospital_Dim(Hospital_Key)
);

CREATE TABLE Road_Network_Facts (
    Geography_Key INT,
    Time_Key INT,
    Road_Length INT,
    PRIMARY KEY (Geography_Key, Time_Key),
    FOREIGN KEY (Geography_Key) REFERENCES Geography_Dim(Geography_Key),
    FOREIGN KEY (Time_Key) REFERENCES Time_Dim(Time_Key)
);

CREATE TABLE Evacuation_Personnel_Dim (
    Evacuation_Personnel_Key INT PRIMARY KEY,
    FirstName NVARCHAR(20),
    LastName NVARCHAR(20),
    Gender NVARCHAR(20),
    ContactNumber NVARCHAR(20),
    Email NVARCHAR(50),
    Address NVARCHAR(50),
    Role NVARCHAR(20),
    ExperienceYears INT,
    EmergencyTraining BIT,
    JoiningDate DATE,
    LeavingDate DATE,
    StartDate DATE,
    EndDate DATE,
    ActiveRow BIT
);

CREATE TABLE EvacuationFacts (
    Geography_Key INT,
    Time_Key INT,
    Evacuation_Personnel_Key INT,
    PRIMARY KEY (Geography_Key, Time_Key, Evacuation_Personnel_Key),
    FOREIGN KEY (Geography_Key) REFERENCES Geography_Dim(Geography_Key),
    FOREIGN KEY (Time_Key) REFERENCES Time_Dim(Time_Key),
    FOREIGN KEY (Evacuation_Personnel_Key) REFERENCES Evacuation_Personnel_Dim(Evacuation_Personnel_Key)
);

CREATE TABLE Barrier_Dim (
    Barrier_Key INT PRIMARY KEY,
    Barrier_Name NVARCHAR(40),
    Maximum_Capacity INT,
    Foundation_Date DATE,
    Closing_Date DATE
);

CREATE TABLE Water_Storage_Facts (
    Barrier_Key INT,
    Geography_Key INT,
    Time_Key INT,
    Water_Volume INT,
    PRIMARY KEY (Barrier_Key, Geography_Key, Time_Key),
    FOREIGN KEY (Barrier_Key) REFERENCES Barrier_Dim(Barrier_Key),
    FOREIGN KEY (Geography_Key) REFERENCES Geography_Dim(Geography_Key),
    FOREIGN KEY (Time_Key) REFERENCES Time_Dim(Time_Key)
);

CREATE TABLE Energy_Facts (
    Geography_Key INT,
    Time_Key INT,
    Diesel_Reserve INT,
    Gasoline_Reserve INT,
    Electricity_Reserve INT,
    Natural_Gas_Reserve INT,
    KEROSENE_Reserve INT,
    Diesel INT,
    Gasoline INT,
    Electricity INT,
    Natural_Gas INT,
    KEROSENE INT,
    PRIMARY KEY (Geography_Key, Time_Key),
    FOREIGN KEY (Geography_Key) REFERENCES Geography_Dim(Geography_Key),
    FOREIGN KEY (Time_Key) REFERENCES Time_Dim(Time_Key)
);

CREATE TABLE Supply_Facts (
    Geography_Key INT,
    Time_Key INT,
    DryGrains_Reserve INT,
    Oils_Reserve INT,
    Legumes_Reserve INT,
    CannedGoods_Reserve INT,
    Flour_Reserve INT,
    Dry_Grains INT,
    Oils INT,
    Legumes INT,
    CannedGoods INT,
    Flour INT,
    PRIMARY KEY (Geography_Key, Time_Key),
    FOREIGN KEY (Geography_Key) REFERENCES Geography_Dim(Geography_Key),
    FOREIGN KEY (Time_Key) REFERENCES Time_Dim(Time_Key)
);