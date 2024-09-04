
CREATE TABLE Bidder
(
    id INTEGER PRIMARY KEY,
    tunnus VARCHAR(20) NOT NULL UNIQUE,
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
    offerdate TIMESTAMP NOT NULL,
    text VARCHAR(500) NOT NULL,
    FOREIGN KEY(bidder) REFERENCES Bidder(id),
    FOREIGN KEY(negotiation) REFERENCES Negotiation(id)
);

CREATE VIEW ProductgroupList AS
SELECT pgr.id, pgr.name, COUNT(o.id) as count, MAX(offerdate) AS o
FROM Productgroup pgr
LEFT JOIN Negotiation offer ON (pgr.id = offer.pgroup)
LEFT JOIN Offer o ON (offer.id = o.negotiation)
GROUP by pgr.id, pgr.name;

CREATE VIEW NegotiationList AS
SELECT offer.id AS id, offer.header, offer.issuer, offer.pgroup AS pgroup,
COUNT(*) AS viestimaara, MIN(v.offerdate) AS issuedat,
MAX(v.offerdate) AS viimeisin FROM Negotiation pgr
LEFT JOIN Offer o ON (offer.id = o.negotiation)
GROUP BY offer.id, offer.header, offer.issuer, offer.pgroup
ORDER BY MAX(o.offerdate) DESC;
