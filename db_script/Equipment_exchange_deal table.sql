 --Let’s extend your existing database schema to include a table that represents
-- the equipment exchange between bidders. We’ll create a table called BidExchange to track these transactions.

-- define the BidExchange table:

CREATE TABLE BidExchange
(
    id SERIAL NOT NULL PRIMARY KEY,
    salesBidder INT NOT NULL, -- ID of the initial bidder (sales-bidder)
    purchaseBidder INT NOT NULL, -- ID of the bidder making the purchase offer
    equipmentOffer VARCHAR(100) NOT NULL, -- Description of the equipment offered
    equipmentRequested VARCHAR(100) NOT NULL, -- Description of the equipment requested
    agreedDeal BOOLEAN DEFAULT FALSE, -- Indicates if the deal is mutually agreed upon
    dealTimestamp TIMESTAMP NOT NULL, -- Timestamp when the deal was made

    FOREIGN KEY(salesBidder) REFERENCES Bidder(id),
    FOREIGN KEY(purchaseBidder) REFERENCES Bidder(id)
);

--Explanation:
--salesBidder and purchaseBidder columns store the IDs of the bidders involved in the exchange.
--equipmentOffer describes the equipment offered by the sales bidder.
--equipmentRequested describes the equipment requested by the purchaser.
--agreedDeal indicates whether both parties have agreed on the deal (initially set to FALSE).
--dealTimestamp records the time when the deal was made.
--Remember to adjust the column definitions according to your specific requirements.
--This table will allow bidders to exchange equipment based on their bids.

Test cases:
These queries will help you validate the functionality of the table.
Remember to replace placeholders like your_bidder_id and your_exchange_id with actual values from your database.

Retrieve Equipment Exchange Deals: This query retrieves information about all equipment exchange deals,
including the equipment offered, requested, and whether the deal is mutually agreed upon:

SELECT id, salesBidder, purchaseBidder, equipmentOffer, equipmentRequested, agreedDeal
FROM BidExchange;

Find Agreed Deals: To retrieve only the deals that are mutually agreed upon, you can add a filter:

SELECT id, salesBidder, purchaseBidder, equipmentOffer, equipmentRequested
FROM BidExchange
WHERE agreedDeal = TRUE;

Check Bidder’s Equipment Exchange History: To see the equipment exchanges for a specific bidder (replace your_bidder_id), use:

SELECT id, salesBidder, purchaseBidder, equipmentOffer, equipmentRequested, agreedDeal
FROM BidExchange
WHERE salesBidder = your_bidder_id OR purchaseBidder = your_bidder_id;

Retrieve Specific Exchange Details: To get details of a specific exchange (replace your_exchange_id), use:

SELECT id, salesBidder, purchaseBidder, equipmentOffer, equipmentRequested, agreedDeal
FROM BidExchange
WHERE id = your_exchange_id;