-- --SCHEMA: db_BGEFv4_SCHEMAv2
-- --DROP SCHEMA IF EXISTS "db_bgefv4_schemav2" ;
-- -- CREATE SCHEMA IF NOT EXISTS "db_bgefv4_schemav2" AUTHORIZATION POSTGRES;

-- -- CREATE TABLE db_bgefv4_schemav2.CLIENT (
-- -- 	ID SERIAL NOT NULL PRIMARY KEY,
-- -- 	USERNAME VARCHAR(50) NOT NULL UNIQUE,
-- -- 	PASSWORD VARCHAR(25) DEFAULT NULL,
-- -- 	EMAIL VARCHAR(80) DEFAULT NULL,
-- -- 	SECONDARYEMAIL VARCHAR(80) DEFAULT NULL,
-- -- 	USERICON_URL INT, -- Link to user's icon-metadatafile
-- -- 	ROLE_ID INT NOT NULL,
-- -- 	BLOCKED BOOLEAN DEFAULT FALSE,
-- -- 	LATESTBIDHEADER_ID INT,

-- -- ALTER TABLE db_bgefv4_schemav2.CLIENT
-- -- --DROP COLUMN USERICON_URL;
-- -- ALTER TABLE db_bgefv4_schemav2.CLIENT
-- -- RENAME COLUMN USERICON_url TO USERICON_ID;
-- -- UPDATE db_bgefv4_schemav2.CLIENT
-- -- SET USERICON_ID = CAST(USERICON_ID AS INT);
-- ALTER TABLE db_bgefv4_schemav2.CLIENT
-- ADD CONSTRAINT fk_ROLE
-- 	FOREIGN KEY (ROLE_ID) REFERENCES db_bgefv4_schemav2.ROLE(ID);
-- -- ALTER TABLE db_bgefv4_schemav2.CLIENT
-- -- ADD CONSTRAINT fk_IMAGEMETADATA
-- -- 	FOREIGN KEY (USERICON_ID) REFERENCES db_bgefv4_schemav2.IMAGEMETADATA (ID);
-- ALTER TABLE db_bgefv4_schemav2.CLIENT
-- ADD CONSTRAINT fk_BIDHEADER
-- 	FOREIGN KEY (LATESTBIDHEADER_ID) REFERENCES db_bgefv4_schemav2.BIDHEADER (ID);
-- -- );

-- -- CREATE TABLE db_bgefv4_schemav2.ROLE (	
-- -- 	ID SERIAL NOT NULL PRIMARY KEY,
-- -- 	ROLENAME VARCHAR(80) NOT NULL UNIQUE,
-- -- 	REGISTEREDUSER BOOLEAN DEFAULT FALSE,
-- -- 	SELLERROLE BOOLEAN DEFAULT FALSE,
-- -- 	BUYERROLE BOOLEAN DEFAULT FALSE,
-- -- 	ADMINROLE BOOLEAN DEFAULT FALSE
-- -- );
-- -- CREATE TABLE db_bgefv4_schemav2.BIDGENRE (
-- -- 	ID SERIAL NOT NULL PRIMARY KEY,
-- -- 	BIDGENREHEADER VARCHAR(100) NOT NULL UNIQUE,
-- -- 	USER_ID INT,
-- -- 	LASTBIDHEADER_ID INT,
-- -- 	NUMBEROFBIDS INT NOT NULL
-- -- FOREIGN KEY (USER_ID) REFERENCES CLIENT (ID),
-- -- FOREIGN KEY (LASTBIDHEADER_ID) REFERENCES BIDHEADER (ID)
-- ALTER TABLE db_bgefv4_schemav2.BIDGENRE
-- ADD CONSTRAINT fk_CLIENT
-- 	FOREIGN KEY (USER_ID) REFERENCES db_bgefv4_schemav2.CLIENT (ID);
-- ALTER TABLE db_bgefv4_schemav2.BIDGENRE
-- ADD CONSTRAINT fk_BIDHEADER
-- 	FOREIGN KEY (LASTBIDHEADER_ID) REFERENCES db_bgefv4_schemav2.BIDHEADER (ID);
-- -- );
-- -- CREATE TABLE db_bgefv4_schemav2.BIDHEADER (
-- -- 	ID SERIAL NOT NULL PRIMARY KEY,
-- -- 	USER_ID INT,
-- -- 	BIDGENRE_ID INT,
-- -- 	BIDTYPECODE INT,
-- -- 	BIDSTATUS INT,
-- -- 	BIDCONTENT_ID INT,
-- -- 	BIDHEADERTEXT VARCHAR(100) NOT NULL UNIQUE,
-- -- 	BIDEXCHANGE1_ID INT,
-- -- 	BIDEXCHANGE2_ID INT,
-- -- 	BIDEXCHANGE3_ID INT,
-- -- 	BIDEXCHANGE4_ID INT,
-- -- 	BIDEXCHANGE5_ID INT,
-- -- 	BIDSTARTEDTIME TIMESTAMP NOT NULL,
-- -- 	BIDENDINGTIME TIMESTAMP NOT NULL,
-- -- 	HDREDITEDTIME TIMESTAMP NOT NULL
-- 	-- FOREIGN KEY (USER_ID) REFERENCES CLIENT(ID),
-- 	-- FOREIGN KEY (BIDGENRE_ID) REFERENCES BIDGENRE (ID),
-- 	-- FOREIGN KEY (BIDCONTENT_ID) REFERENCES BIDCONTENT (ID),
-- 	-- FOREIGN KEY (BIDEXCHANGE1_ID) REFERENCES BIDEXCHANGE (ID),
-- 	-- FOREIGN KEY (BIDEXCHANGE2_ID) REFERENCES BIDEXCHANGE (ID),
-- 	-- FOREIGN KEY (BIDEXCHANGE3_ID) REFERENCES BIDEXCHANGE (ID),
-- 	-- FOREIGN KEY (BIDEXCHANGE4_ID) REFERENCES BIDEXCHANGE (ID),
-- 	-- FOREIGN KEY (BIDEXCHANGE5_ID) REFERENCES BIDEXCHANGE (ID)
-- -- );
-- ALTER TABLE db_bgefv4_schemav2.BIDHEADER
-- ADD CONSTRAINT fk_CLIENT
-- 	FOREIGN KEY (USER_ID) REFERENCES db_bgefv4_schemav2.CLIENT (ID);
-- ALTER TABLE db_bgefv4_schemav2.BIDHEADER
-- ADD CONSTRAINT fk_BIDGENRE
-- 	FOREIGN KEY (BIDGENRE_ID) REFERENCES db_bgefv4_schemav2.BIDGENRE (ID);
-- ALTER TABLE db_bgefv4_schemav2.BIDHEADER
-- ADD CONSTRAINT fk_BIDCONTENT
-- 	FOREIGN KEY (BIDCONTENT_ID) REFERENCES db_bgefv4_schemav2.BIDCONTENT (ID);
-- ALTER TABLE db_bgefv4_schemav2.BIDHEADER
-- ADD CONSTRAINT fk_BIDEXCHANGE1
-- 	FOREIGN KEY (BIDEXCHANGE1_ID) REFERENCES db_bgefv4_schemav2.BIDEXCHANGE (ID);
-- ALTER TABLE db_bgefv4_schemav2.BIDHEADER
-- ADD CONSTRAINT fk_BIDEXCHANGE2
-- 	FOREIGN KEY (BIDEXCHANGE2_ID) REFERENCES db_bgefv4_schemav2.BIDEXCHANGE (ID);
-- ALTER TABLE db_bgefv4_schemav2.BIDHEADER
-- ADD CONSTRAINT fk_BIDEXCHANGE3
-- 	FOREIGN KEY (BIDEXCHANGE3_ID) REFERENCES db_bgefv4_schemav2.BIDEXCHANGE (ID);
-- ALTER TABLE db_bgefv4_schemav2.BIDHEADER
-- ADD CONSTRAINT fk_BIDEXCHANGE4
-- 	FOREIGN KEY (BIDEXCHANGE4_ID) REFERENCES db_bgefv4_schemav2.BIDEXCHANGE (ID);
-- ALTER TABLE db_bgefv4_schemav2.BIDHEADER
-- ADD CONSTRAINT fk_BIDEXCHANGE5
-- 	FOREIGN KEY (BIDEXCHANGE5_ID) REFERENCES db_bgefv4_schemav2.BIDEXCHANGE (ID);


-- CREATE TABLE db_bgefv4_schemav2.BIDCONTENT (
-- 	ID SERIAL NOT NULL PRIMARY KEY,
-- 	BIDHEADER_ID INT,
-- 	BIDCONTENT VARCHAR(500) NOT NULL,
-- 	GEAR1_ID INT,
-- 	GEAR2_ID INT,
-- 	GEAR3_ID INT,
-- 	GEAR4_ID INT,
-- 	GEAR5_ID INT,
-- 	GEAR6_ID INT,
-- 	GEAR7_ID INT,
-- 	GEAR8_ID INT,
-- 	GEAR9_ID INT,
-- 	GEAR10_ID INT,
-- 	CONEDITEDTIME TIMESTAMP NOT NULL,
-- 	BUNDLEIMAGE_ID INT, -- Link to bundle image metadata file
-- 	BUNDLESOUND_ID INT -- Links to bundle sound sample metadata file
-- 	-- FOREIGN KEY (BIDHEADER_ID) REFERENCES BIDHEADER (ID),
-- 	-- FOREIGN KEY (BUNDLEIMAGE_ID) REFERENCES IMAGEMETADATA (ID),
-- 	-- FOREIGN KEY (BUNDLESOUND_ID) REFERENCES SOUNDCLIPMETADATA (ID),
-- 	-- FOREIGN KEY (GEAR1_ID) REFERENCES GEAR (ID),
-- 	-- FOREIGN KEY (GEAR2_ID) REFERENCES GEAR (ID),
-- 	-- FOREIGN KEY (GEAR3_ID) REFERENCES GEAR (ID),
-- 	-- FOREIGN KEY (GEAR4_ID) REFERENCES GEAR (ID),
-- 	-- FOREIGN KEY (GEAR5_ID) REFERENCES GEAR (ID),
-- 	-- FOREIGN KEY (GEAR6_ID) REFERENCES GEAR (ID),
-- 	-- FOREIGN KEY (GEAR7_ID) REFERENCES GEAR (ID),
-- 	-- FOREIGN KEY (GEAR8_ID) REFERENCES GEAR (ID),
-- 	-- FOREIGN KEY (GEAR9_ID) REFERENCES GEAR (ID),
-- 	-- FOREIGN KEY (GEAR10_ID) REFERENCES GEAR (ID)
-- );
-- ALTER TABLE db_bgefv4_schemav2.BIDHEADER
-- ADD CONSTRAINT fk_BIDHEADER
-- 	FOREIGN KEY (USER_ID) REFERENCES db_bgefv4_schemav2.BIDHEADER (ID);
-- ALTER TABLE db_bgefv4_schemav2.BIDHEADER
-- ADD CONSTRAINT fk_IMAGEMETADATA
-- 	FOREIGN KEY (BIDGENRE_ID) REFERENCES db_bgefv4_schemav2.IMAGEMETADATA(ID); 
-- ALTER TABLE db_bgefv4_schemav2.BIDHEADER
-- ADD CONSTRAINT fk_SOUNDCLIPMETADATA
-- 	FOREIGN KEY (BIDCONTENT_ID) REFERENCES db_bgefv4_schemav2.SOUNDCLIPMETADATA (ID);
-- ALTER TABLE db_bgefv4_schemav2.BIDCONTENT
-- ADD CONSTRAINT fk_GEAR1
-- 	FOREIGN KEY (GEAR1_ID) REFERENCES db_bgefv4_schemav2.GEAR (ID);
-- ALTER TABLE db_bgefv4_schemav2.BIDCONTENT
-- ADD CONSTRAINT fk_GEAR2
-- 	FOREIGN KEY (GEAR2_ID) REFERENCES db_bgefv4_schemav2.GEAR (ID);
-- ALTER TABLE db_bgefv4_schemav2.BIDCONTENT
-- ADD CONSTRAINT fk_GEAR3
-- 	FOREIGN KEY (GEAR3_ID) REFERENCES db_bgefv4_schemav2.GEAR (ID);
-- ALTER TABLE db_bgefv4_schemav2.BIDCONTENT
-- ADD CONSTRAINT fk_GEAR4
-- 	FOREIGN KEY (GEAR4_ID) REFERENCES db_bgefv4_schemav2.GEAR (ID);
-- ALTER TABLE db_bgefv4_schemav2.BIDCONTENT
-- ADD CONSTRAINT fk_GEAR5
-- 	FOREIGN KEY (GEAR5_ID) REFERENCES db_bgefv4_schemav2.GEAR (ID);
-- ALTER TABLE db_bgefv4_schemav2.BIDCONTENT
-- ADD CONSTRAINT fk_GEAR6
-- 	FOREIGN KEY (GEAR6_ID) REFERENCES db_bgefv4_schemav2.GEAR (ID);
-- ALTER TABLE db_bgefv4_schemav2.BIDCONTENT
-- ADD CONSTRAINT fk_GEAR7
-- 	FOREIGN KEY (GEAR7_ID) REFERENCES db_bgefv4_schemav2.GEAR (ID);
-- ALTER TABLE db_bgefv4_schemav2.BIDCONTENT
-- ADD CONSTRAINT fk_GEAR8
-- 	FOREIGN KEY (GEAR8_ID) REFERENCES db_bgefv4_schemav2.GEAR (ID);
-- ALTER TABLE db_bgefv4_schemav2.BIDCONTENT
-- ADD CONSTRAINT fk_GEAR9
-- 	FOREIGN KEY (GEAR9_ID) REFERENCES db_bgefv4_schemav2.GEAR (ID);
-- ALTER TABLE db_bgefv4_schemav2.BIDCONTENT
-- ADD CONSTRAINT fk_GEAR10
-- 	FOREIGN KEY (GEAR10_ID) REFERENCES db_bgefv4_schemav2.GEAR (ID);


-- CREATE TABLE db_bgefv4_schemav2.GEAR (
-- 	ID SERIAL NOT NULL PRIMARY KEY,
-- 	GEARBRAND VARCHAR(30) NOT NULL,
-- 	GEARCODE INT,
-- 	GEARSTATUS INT,
-- 	BIDHEADER_ID INT,
-- 	GEARNAME VARCHAR(100) NOT NULL,
-- 	GEARDETAILS TEXT,
-- 	GEARSTORY TEXT,
-- 	AMOUNTOFFERED INT NOT NULL,
-- 	APPROXVALUE FLOAT DEFAULT 0.00,
-- 	USER_ID INT,
-- 	COMMENTS TEXT,
-- 	EDITEDTIME TIMESTAMP NOT NULL,
-- 	GEARIMAGE_ID INT, -- Links to gear image metadata file
-- 	SOUNDCLIP_ID INT -- Links to gear sound sample metadata file
-- 	-- FOREIGN KEY (USER_ID) REFERENCES CLIENT (ID),
-- 	-- FOREIGN KEY (BIDHEADER_ID) REFERENCES BIDHEADER (ID),
-- 	-- FOREIGN KEY (GEARIMAGE_ID) REFERENCES IMAGEMETADATA (ID),
-- 	-- FOREIGN KEY (SOUNDCLIP_ID) REFERENCES SOUNDCLIPMETADATA (ID)
-- );

-- ALTER TABLE db_bgefv4_schemav2.GEAR
-- ADD CONSTRAINT fk_CLIENT
-- 	FOREIGN KEY (USER_ID) REFERENCES db_bgefv4_schemav2.CLIENT (ID);
-- ALTER TABLE db_bgefv4_schemav2.GEAR
-- ADD CONSTRAINT fk_BIDHEADER
-- 	FOREIGN KEY (BIDHEADER_ID) REFERENCES db_bgefv4_schemav2.BIDHEADER(ID); 
-- ALTER TABLE db_bgefv4_schemav2.GEAR
-- ADD CONSTRAINT fk_IMAGEMETADATA
-- 	FOREIGN KEY (GEARIMAGE_ID) REFERENCES db_bgefv4_schemav2.IMAGEMETADATA(ID); 
-- ALTER TABLE db_bgefv4_schemav2.GEAR
-- ADD CONSTRAINT fk_SOUNDCLIPMETADATA
-- 	FOREIGN KEY (SOUNDCLIP_ID) REFERENCES db_bgefv4_schemav2.SOUNDCLIPMETADATA(ID); 

-- 	-- FOREIGN KEY (GEARIMAGE_ID) REFERENCES IMAGEMETADATA (ID),
-- 	-- FOREIGN KEY (SOUNDCLIP_ID) REFERENCES SOUNDCLIPMETADATA (ID)

-- CREATE TABLE db_bgefv4_schemav2.BIDEXCHANGE --This table will allow bidders to exchange equipment based on their bids.
-- (
-- 	ID SERIAL NOT NULL PRIMARY KEY,
-- 	SALESBIDDER_ID INT NOT NULL, -- ID of the initial bidder (sales-bidder)
-- 	SALESBIDHEADER_ID INT NOT NULL, -- ID of the sales offer header
-- 	PURCHASEBIDDER_ID INT NOT NULL, -- ID of the bidder making the purchase offer
-- 	PURCHASEBIDHEADER_ID INT NOT NULL, -- ID of the purchase offer header
-- 	AGREEDDEAL BOOLEAN DEFAULT FALSE, -- Indicates if the deal is mutually agreed upon
-- 	DEALTIMESTAMP TIMESTAMP NOT NULL -- Timestamp when the deal was made
-- 	-- FOREIGN KEY (SALESBIDDER_ID) REFERENCES CLIENT (ID),
-- 	-- FOREIGN KEY (SALESBIDHEADER_ID) REFERENCES BIDHEADER (ID),
-- 	-- FOREIGN KEY (PURCHASEBIDDER_ID) REFERENCES CLIENT(ID), 
-- 	-- FOREIGN KEY (PURCHASEBIDHEADER_ID) REFERENCES BIDHEADER (ID)
-- );

-- ALTER TABLE db_bgefv4_schemav2.BIDEXCHANGE
-- ADD CONSTRAINT fk_CLIENT_S
-- 	FOREIGN KEY (SALESBIDDER_ID) REFERENCES db_bgefv4_schemav2.CLIENT (ID);
-- ALTER TABLE db_bgefv4_schemav2.BIDEXCHANGE
-- ADD CONSTRAINT fk_BIDHEADER_S
-- 	FOREIGN KEY (SALESBIDHEADER_ID) REFERENCES db_bgefv4_schemav2.BIDHEADER (ID);
-- ALTER TABLE db_bgefv4_schemav2.BIDEXCHANGE
-- ADD CONSTRAINT fk_CLIENT_P
-- 	FOREIGN KEY (PURCHASEBIDDER_ID) REFERENCES db_bgefv4_schemav2.CLIENT (ID);
-- ALTER TABLE db_bgefv4_schemav2.BIDEXCHANGE
-- ADD CONSTRAINT fk_BIDHEADER_P
-- 	FOREIGN KEY (PURCHASEBIDHEADER_ID) REFERENCES db_bgefv4_schemav2.BIDHEADER (ID);

-- CREATE TABLE db_bgefv4_schemav2.IMAGEMETADATA (
-- 	ID SERIAL NOT NULL PRIMARY KEY,
-- 	IMAGENAME VARCHAR(100) NOT NULL,
-- 	AXSIZE VARCHAR(10) NOT NULL,
-- 	RESOLUTION VARCHAR(20) NOT NULL,
-- 	IMAGE_URL VARCHAR(255) NOT NULL -- Link to the actual image file
-- );

-- CREATE TABLE db_bgefv4_schemav2.SOUNDCLIPMETADATA (
-- 	ID SERIAL NOT NULL PRIMARY KEY,
-- 	CLIPNAME VARCHAR(100) NOT NULL,
-- 	FORMAT VARCHAR(10) NOT NULL, -- e.g., '.wav', '.mp3', etc.
-- 	QUALITY VARCHAR(30) NOT NULL, -- e.g., '24-bit WAV', '196 kbps MP3', etc.
-- 	CLIPLENGTHINSECONDS FLOAT NOT NULL,
-- 	ISSTEREO BOOLEAN NOT NULL,
-- 	SAMPLE_URL VARCHAR(255) NOT NULL -- Link to the actual sound sample file
-- );

--Check following updates:
CREATE VIEW db_bgefv4_schemav2.BIDGENRELIST AS
SELECT
	BG.ID,
	BG.BIDGENREHEADER,
	COUNT(BC.ID) AS COUNT,
	MAX(BC.CONEDITEDTIME) AS LATEST
FROM
	db_bgefv4_schemav2.BIDGENRE BG
	LEFT JOIN db_bgefv4_schemav2.BIDHEADER BHR ON (BG.ID = BHR.BIDGENRE_ID)
	LEFT JOIN db_bgefv4_schemav2.BIDCONTENT BC ON (BHR.ID = BC.BIDHEADER_ID)
GROUP BY
	BG.ID,
	BG.BIDGENREHEADER;

CREATE VIEW db_bgefv4_schemav2.BIDLIST AS
SELECT
	BH.ID,
	BH.USER_ID,
	BH.BIDGENRE_ID,
	BH.BIDTYPECODE,
	BH.BIDSTATUS,
	BH.BIDHEADERTEXT,
	COUNT(*) AS COUNT,
	MIN(BC.CONEDITEDTIME) AS EDITED,
	MAX(BC.CONEDITEDTIME) AS LATEST
FROM
	db_bgefv4_schemav2.BIDHEADER BH
	LEFT JOIN db_bgefv4_schemav2.BIDCONTENT BC ON (BH.ID = BC.BIDHEADER_ID)
GROUP BY
	BH.ID,
	BH.BIDHEADERTEXT,
	BH.USER_ID,
	BH.BIDGENRE_ID
ORDER BY
	MAX(BC.CONEDITEDTIME) DESC;