
-- View: InitialBidderBids_v3
-- Description: Provides information on initial bidders and their bids for equipment exchange.

--bidHeader_id represents the unique identifier for each bid header.
--bidder_id corresponds to the initial bidder’s ID.
--bidGenre indicates the type of bid (e.g., auction, exchange).
--bidHeader provides the header text for the bid.
--bidStartTime is the timestamp when the bid started.
--bidContent contains the actual bid content.

CREATE VIEW InitialBidderBids AS
SELECT
    bh.id AS bidHeader_id,
    bh.initialBidder_id AS bidder_id,
    bg.bidGenreHeader AS bidGenre,
    bh.bidHeaderText AS bidHeader,
    bh.bidStartedTime AS bidStartTime,
    bc.bidContent AS bidContent
FROM BidHeader bh
LEFT JOIN BidGenre bg ON (bh.bidGenre_id = bg.id)
LEFT JOIN BidContent bc ON (bh.id = bc.bidHeader_id)
WHERE bc.id IS NOT NULL; -- Filters out bid headers without content




