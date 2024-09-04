
-- View: BidderBidContent_v3
-- Description: Provides bid content for individual bid headers (both completed and open offers).
    --
    -- bidHeader_id represents the unique identifier for each bid header.
    -- bidder_id corresponds to the initial bidder’s ID.
    -- bidGenre indicates the type of bid (e.g., auction, exchange).
    -- bidHeader provides the header text for the bid.
    -- bidContent contains the actual bid content.
    --
CREATE VIEW BidderBidContent AS
SELECT
    bh.id AS bidHeader_id,
    bh.initialBidder_id AS bidder_id,
    bg.bidGenreHeader AS bidGenre,
    bh.bidHeaderText AS bidHeader,
    bc.bidContent AS bidContent
FROM BidHeader bh
LEFT JOIN BidGenre bg ON (bh.bidGenre_id = bg.id)
LEFT JOIN BidContent bc ON (bh.id = bc.bidHeader_id)
WHERE bc.id IS NOT NULL; -- Filters out bid headers without content
