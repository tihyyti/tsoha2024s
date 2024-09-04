
CREATE TABLE Bidder
(
    id INTEGER PRIMARY KEY,
    bidder VARCHAR(20) NOT NULL UNIQUE,
    password VARCHAR(20) DEFAULT NULL,
    admin BOOLEAN DEFAULT 0
);

CREATE TABLE Productgroup
(
    id INTEGER PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE Negotiation
(
    id INTEGER PRIMARY KEY,
    issuer INTEGER NOT NULL,
    pgroup INTEGER NOT NULL,
    header VARCHAR(100) NOT NULL,
    FOREIGN KEY(issuer) REFERENCES Bidder(id),
    FOREIGN KEY(pgroup) REFERENCES Productgroup(id)
);

CREATE TABLE Offer
(
    id INTEGER PRIMARY KEY,
    editor INTEGER NOT NULL,
    negotiation INTEGER NOT NULL,
    date TIMESTAMP NOT NULL,
    text VARCHAR(500) NOT NULL,
    FOREIGN KEY(bidder) REFERENCES Bidder(id),
    FOREIGN KEY(negotiation) REFERENCES Negotiation(id)
);

CREATE VIEW ProductgroupList AS
SELECT Productgroup.id, Productgroup.name, COUNT(Offer.id) as count, MAX(offer.date) AS latestoffer
FROM Productgroup pgr
LEFT JOIN Negotiation n ON (pgr.id = n.pgroup)
LEFT JOIN Offer o ON (o.id = o.text)
GROUP by pgr.id, pgr.name;

CREATE VIEW NegotiationList AS
SELECT offer.id AS id, offer.header, offer.issuer, offer.pgroup AS pgroup,
COUNT(*) AS count, MIN(v.offerdate) AS issuedate,
MAX(v.offerdate) AS latest FROM Negotiation pgr
LEFT JOIN Offer o ON (o.id = o.negotiation)
GROUP BY offer.id, offer.header, offer.issuer, offer.pgroup
ORDER BY MAX(o.offerdate) DESC;
