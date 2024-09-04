
-- Roles
INSERT INTO Role (Name) VALUES ('ordinary'), ('admin');

-- Bidders
INSERT INTO Bidder (bidderName, password, email, secondary_email, userIcon_url, role_id, blocked)
VALUES
    ('ordinary_user', 'password123', 'ordinary@example.com', NULL, 'https://example.com/icons/ordinary.png', 1,
false),
    ('admin_user', 'adminpass', 'admin@example.com', NULL, 'https://example.com/icons/admin.png', 2, false);

-- Bid Genres
INSERT INTO BidGenre (bidGenre, bidder, bidGenreHeader)
VALUES
    (1, 1, 'Guitars'),
    (2, 2, 'Drums'),
    (3, 1, 'Keyboards');

-- Bid Headers
INSERT INTO BidHeader (initialBidder, bidGnre, bidHder, numberOfBids, startedTime)
VALUES
    (1, 1, 'Guitar Auction', 0, '2023-05-01 10:00:00'),
    (2, 2, 'Drum Sale', 0, '2023-05-02 11:30:00');

-- Bid Content
INSERT INTO BidContent (bidderID, bidHead, bidderName, bidContent, editedTime, bundleImage_url, bundleImageText)
VALUES
    (1, 1, 'ordinary_user', 'Offering vintage Gibson guitar', '2023-05-01 10:15:00', NULL, NULL),
    (2, 2, 'admin_user', 'Yamaha drum set with cymbals', '2023-05-02 12:00:00', NULL, NULL);

-- Gear Groups
INSERT INTO GearGroup (gearGroup, bidderID, gearGroupHeader)
VALUES
    (1, 1, 'Electric Guitars'),
    (2, 2, 'Acoustic Guitars');

-- Gear Items
INSERT INTO Gear (gearCode, gearStatus, bidderID, bidHead, gearName, gearDetails, gearStory, amountOffered,
origPrice, comments, editedTime, gearImage_url, gearImageText)
VALUES
    (1, 1, 1, 1, 'Fender Stratocaster', 'Sunburst finish, maple neck', 'Vintage guitar', 1000, 1500, 'Great
condition', '2023-05-01 10:30:00', NULL, NULL),
    (2, 1, 2, 2, 'Martin D-28', 'Rosewood back and sides', 'High-end acoustic', 2000, 2500, 'Includes hard case',
'2023-05-02 12:30:00', NULL, NULL);

