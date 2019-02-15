CREATE DATABASE NationalParks;

CREATE TABLE STATE(
   ID INTEGER PRIMARY KEY     NOT NULL,
   NAME           TEXT    NOT NULL,
   CODE            CHAR(2)     NOT NULL
);

CREATE TABLE NATIONAL_PARK(
   ID INTEGER PRIMARY    KEY     NOT NULL,
   NAME              TEXT    NOT NULL,
   NAME_IN_REPORT    TEXT    NOT NULL,
   PARK_TYPE         TEXT,
   STATE_CD          CHAR(2),
   STATE_ID     INTEGER REFERENCES STATE(ID),
   CITY              TEXT,
   DESCRIPTION       TEXT
);

CREATE TABLE NATIONAL_PARK_DATA(
   ID INTEGER PRIMARY    KEY     NOT NULL,
   PARK_ID              INTEGER REFERENCES NATIONAL_PARK(ID),
   PARK_NAME_IN_REPORT    TEXT,
   YEAR         INTEGER,
   Recreational_Visits INTEGER,
   Non_Recreational_Visits INTEGER,
   Misc_Overnights INTEGER, 
   Concessioner_Camping INTEGER,
   Tent_Overnights INTEGER,
   RV_Overnights INTEGER,
   BackCountry_Overnights INTEGER,
   Non_Recreational_Overnights INTEGER,
   Non_Recreational_Hours INTEGER,
   Recreational_Hours INTEGER
);

commit;
