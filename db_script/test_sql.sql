INSERT INTO Bidder (id, id, password, admin) VALUES (0, 'admin', 'admin', 1);
INSERT INTO Bidder (id, id) VALUES (1, 'Teemu');
INSERT INTO Bidder (id, id) VALUES (2, 'Liisa');
INSERT INTO Bidder (id, id) VALUES (3, 'Timo');
INSERT INTO Bidder (id, id) VALUES (4, 'Tapani');

INSERT INTO GearGenre (id, name) VALUES (1, 'Kitarapedaalit');
INSERT INTO GearGenre (id, name) VALUES (2, 'Rummut');

INSERT INTO BidHeader (id, issuer, pgroup, header) VALUES (1, 2, 1, 'Säröpedaalibundle');
INSERT INTO BidHeader (id, issuer, pgroup, header) VALUES (2, 3, 1, 'Vintagekitara ja kielisetti');
INSERT INTO BidHeader (id, issuer, pgroup, header) VALUES (3, 1, 2, 'PA-kamakasa');

INSERT INTO BidContent (bidder, negotiation, BidContentdate, text) VALUES (1, 1, '2017-06-01 18:00:00.000', 'BidContent: VOX Combo');
INSERT INTO BidContent (bidder, negotiation, BidContentdate, text) VALUES (2, 1, '2017-06-01 18:05:00.000', 'BidContent: Roland Combo 30 Watts');
INSERT INTO BidContent (bidder, negotiation, BidContentdate, text) VALUES (3, 1, '2017-06-01 18:07:00.000', 'BidContent: Cretch quitar');
INSERT INTO BidContent (bidder, negotiation, BidContentdate, text) VALUES (4, 1, '2017-06-01 18:10:00.000', 'BidContent: Yamaha-PA');

INSERT INTO BidContent (bidder, negotiation, BidContentdate, text) VALUES (2, 2, '2017-06-01 19:21:00.000', 'Tuoteryhmälistaus');
INSERT INTO BidContent (bidder, negotiation, BidContentdate, text) VALUES (3, 2, '2017-06-01 20:07:00.000', 'Tarjousneuvottelujen listaus tietyllä tuoteryhmälla');
INSERT INTO BidContent (bidder, negotiation, BidContentdate, text) VALUES (4, 2, '2017-06-01 21:49:00.000', 'Tarjousten listaus tietyssä tarjousneuvottelussa');

INSERT INTO BidContent (bidder, negotiation, BidContentdate, text) VALUES (1, 3, '2017-06-01 23:50:00.000', 'Etsin tuhdimpaa soundia');
INSERT INTO BidContent (bidder, negotiation, BidContentdate, text) VALUES (1, 3, '2017-06-01 23:55:00.000', 'Keikoilla kolhiintunut combo vaihdossa');
INSERT INTO BidContent (bidder, negotiation, BidContentdate, text) VALUES (1, 3, '2017-06-01 23:56:00.000', 'Vaihtaisin VOXin Rolandiin');

