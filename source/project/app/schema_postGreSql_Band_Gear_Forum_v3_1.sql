CREATE TABLE Bidder
(
    id SERIAL NOT NULL PRIMARY KEY,
    bidderName VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(25) DEFAULT NULL,
    email VARCHAR(80) DEFAULT NULL,
    secondaryEmail VARCHAR(80) DEFAULT NULL,
    userIcon_Url VARCHAR(80) DEFAULT NULL,  -- Link to user's user's icon metadata file
    role_id INT NOT NULL,
    blocked BOOLEAN DEFAULT FALSE,
    latestBidHeader_id INT,

    FOREIGN KEY(role_id) REFERENCES Role(id),
    FOREIGN KEY(userIcon_url) REFERENCES ImageMetadata(id),
    FOREIGN KEY(latestBidHeader_id) REFERENCES BidHeader(id)
  );

CREATE TABLE Role
(
    id SERIAL NOT NULL PRIMARY KEY,
    roleName VARCHAR(80) NOT NULL UNIQUE,
    registeredUser BOOLEAN DEFAULT FALSE,
    sellerRole BOOLEAN DEFAULT FALSE,
    buyerRole BOOLEAN DEFAULT FALSE,
    adminRole BOOLEAN DEFAULT FALSE
  );

CREATE TABLE BidGenre
(
    id SERIAL NOT NULL PRIMARY KEY,
    bidGenreHeader VARCHAR(100) NOT NULL UNIQUE,
    bidHeader_id INT,
    bidder_id INT,

    FOREIGN KEY(bidder_id) REFERENCES Bidder(id),
    FOREIGN KEY(bidHeader_id) REFERENCES  BidHeader(id)
  );

CREATE TABLE BidHeader
(
    id SERIAL NOT NULL PRIMARY KEY,
    initialBidder_id INT,
    bidGenre_id INT,
    bidTypeCode INT,
    gearGroup_id INT,
    numberOfBids INT NOT NULL,
    bidHeaderText VARCHAR(100) NOT NULL UNIQUE,
    bidStartedTime TIMESTAMP NOT NULL,
    hdrEditedTime TIMESTAMP NOT NULL,

    FOREIGN KEY(initialBidder_id) REFERENCES Bidder(id),
    FOREIGN KEY(bidGenre_id) REFERENCES BidGenre(id),
    FOREIGN KEY(gearGroup_id) REFERENCES GearGroup(id)
  );

CREATE TABLE BidContent
(
    id SERIAL NOT NULL PRIMARY KEY,
    bidder_id INT,
    bidHeader_id INT,
    bidContent VARCHAR(500) NOT NULL,
    conEditedTime TIMESTAMP NOT NULL,
    bundleImage_id INT,  -- Link to bundle image metadata file
    bundleSound_id INT, -- Links to bundle sound sample metadata file

    FOREIGN KEY(bidHeader_id) REFERENCES BidHeader(id),
    FOREIGN KEY(bundleImage_id) REFERENCES ImageMetadata(id),
    FOREIGN KEY(bundleSound_id) REFERENCES SoundClipMetadata(id)
  );

CREATE TABLE GearGroup
(
  id SERIAL NOT NULL PRIMARY KEY,
  bidder_id INT,
  bidHeader_id INT,
  gearGroupHeader VARCHAR(100) NOT NULL UNIQUE,

  FOREIGN KEY(bidder_id) REFERENCES Bidder(id),
  FOREIGN KEY(bidHeader_id) REFERENCES BidHeader(id)
);

CREATE TABLE Gear
(
  id SERIAL NOT NULL PRIMARY KEY,
  gearBrand VARCHAR(30) NOT NULL,
  gearCode INT,
  gearStatus INT,
  gearGroup_id INT,
  bidder_id INT,
  bidHeader_id INT,
  gearName VARCHAR(100) NOT NULL,
  gearDetails TEXT,
  gearStory TEXT,
  amountOffered INT NOT NULL,
  origPurchasePrice FLOAT default 0.00,
  comments TEXT,
  editedTime TIMESTAMP NOT NULL,
  gearImage_id INT,  -- Links to gear image metadata file
  soundClip_id INT, -- Links to gear sound sample metadata file

  FOREIGN KEY(bidder_id) REFERENCES Bidder(id),
  FOREIGN KEY(bidHeader_id) REFERENCES BidHeader(id),
  FOREIGN KEY(gearGroup_id) REFERENCES GearGroup(id),
  FOREIGN KEY(gearImage_id) REFERENCES ImageMetadata(id),
  FOREIGN KEY(soundClip_id) REFERENCES SoundClipMetadata(id)
);

CREATE TABLE BidExchange --This table will allow bidders to exchange equipment based on their bids.
(
    id SERIAL NOT NULL PRIMARY KEY,
    salesBidder_id INT NOT NULL, -- ID of the initial bidder (sales-bidder)
    salesBidHeader_id INT NOT NULL, -- ID of the sales offer header
    purchaseBidder_id INT NOT NULL, -- ID of the bidder making the purchase offer
    purchaseBidHeader_id INT NOT NULL, -- ID of the purchase offer header
    equipmentOffer VARCHAR(250) NOT NULL, -- Description of the equipment offered
    equipmentRequested VARCHAR(250) NOT NULL, -- Description of the equipment requested
    agreedDeal BOOLEAN DEFAULT FALSE, -- Indicates if the deal is mutually agreed upon
    dealTimestamp TIMESTAMP NOT NULL, -- Timestamp when the deal was made

    FOREIGN KEY(salesBidder_id) REFERENCES Bidder(id),
    FOREIGN KEY(salesBidHeader_id) REFERENCES BidHeader(id),
    FOREIGN KEY(purchaseBidder_id) REFERENCES Bidder(id)
    FOREIGN KEY(purchaseBidHeader_id) REFERENCES BidHeader(id),
);

CREATE TABLE ImageMetadata
(
    id SERIAL NOT NULL PRIMARY KEY,
    imageName VARCHAR(100) NOT NULL,
    AxSize VARCHAR(10) NOT NULL,
    resolution VARCHAR(20) NOT NULL,
    image_url VARCHAR(255) NOT NULL -- Link to the actual image file
);

CREATE TABLE SoundClipMetadata
(
    id SERIAL NOT NULL PRIMARY KEY,
    clipName VARCHAR(100) NOT NULL,
    format VARCHAR(10) NOT NULL, -- e.g., '.wav', '.mp3', etc.
    quality VARCHAR(30) NOT NULL, -- e.g., '24-bit WAV', '196 kbps MP3', etc.
    clipLengthInSeconds FLOAT NOT NULL,
    isStereo BOOLEAN NOT NULL,
    sample_url VARCHAR(255) NOT NULL -- Link to the actual sound sample file
);
-- Check following updates:
CREATE VIEW BidGenreList AS
SELECT bg.id, bg.bidGenreHeader, COUNT(bc.id) as count, MAX(bc.editedTime) AS latest
FROM BidGenre bg
LEFT JOIN BidHeader bhr ON (bg.id = bhr.bidGenre_id)
LEFT JOIN BidContent bc ON (bhr.id = bc.bidHeader_id)
GROUP by bg.id, bg.bidGenreHeader_id;

CREATE VIEW BidList AS
SELECT bh.id, bh.initialBidder, bh.bidGenre_id, bh.bidHeader_id,
COUNT(*) AS count, MIN(bc.editedTime) AS edited,
MAX(bc.editedTime) AS latest
FROM BidHeader bh
LEFT JOIN BidContent bc ON (bh.id = bc.bidHeader_id)
GROUP BY bh.id, bh.bidHeader_id, bh.initialBidder, bh.bidGenre_id
ORDER BY MAX(bc.editedTime) DESC;
