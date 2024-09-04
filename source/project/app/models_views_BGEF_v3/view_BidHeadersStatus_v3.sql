
-- View: BidHeadersStatus
-- Description: Lists bidder's open and sold BidHeaders, sorted by timestamp (latest agreed deal first).

  -- bidHeader_id represents the unique identifier for each bid header.
  -- bidder_id corresponds to the initial bidder’s ID.
  -- bidGenre indicates the type of bid (e.g., auction, exchange).
  -- bidHeader provides the header text for the bid.
  -- bidStartTime is the timestamp when the bid started.
  -- lastEditedTime represents the timestamp when the bid content was last edited.
  -- isSold indicates whether the bid is mutually agreed upon (sold).

CREATE VIEW BidHeadersStatus AS
SELECT
    bh.id AS bidHeader_id,
    bh.initialBidder_id AS bidder_id,
    bg.bidGenreHeader AS bidGenre,
    bh.bidHeaderText AS bidHeader,
    bh.bidStartedTime AS bidStartTime,
    bc.conEditedTime AS lastEditedTime,
    be.agreedDeal AS isSold
FROM BidHeader bh
LEFT JOIN BidGenre bg ON (bh.bidGenre_id = bg.id)
LEFT JOIN BidContent bc ON (bh.id = bc.bidHeader_id)
LEFT JOIN BidExchange be ON (bh.id = be.salesBidHeader_id OR bh.id = be.purchaseBidHeader_id)
WHERE bc.id IS NOT NULL -- Filters out bid headers without content
ORDER BY be.dealTimestamp DESC, bc.conEditedTime DESC;
