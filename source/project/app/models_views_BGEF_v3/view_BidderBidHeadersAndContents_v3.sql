
-- View: BidderBidHeadersAndContents_v3
-- Description: Comprehensive list of a single bidder's BidHeaders and related BidContents.
 --
 -- bidHeader_id represents the unique identifier for each bid header.
 -- bidder_id corresponds to the initial bidder’s ID.
 -- bidGenre indicates the type of bid (e.g., auction, exchange).
 -- bidHeader provides the header text for the bid.
 -- bidContent contains the actual bid content.
 -- dealStatus specifies whether the deal is agreed or open.
-- Sorting based on the bidTypeCode field in ascending order.
-- The bid type definitions (Compensation: Gear only = 1, Gear plus money = 2, Money only = 3, Free = 4) is
-- reflected when sorting.

CREATE VIEW BidderBidHeadersAndContents AS
SELECT
    bh.id AS bidHeader_id,
    bh.initialBidder_id AS bidder_id,
    bg.bidGenreHeader AS bidGenre,
    bh.bidHeaderText AS bidHeader,
    bc.bidContent AS bidContent,
    CASE
        WHEN be.agreedDeal THEN 'Agreed'
        ELSE 'Open'
    END AS dealStatus
FROM BidHeader bh
LEFT JOIN BidGenre bg ON (bh.bidGenre_id = bg.id)
LEFT JOIN BidContent bc ON (bh.id = bc.bidHeader_id)
LEFT JOIN BidExchange be ON (bh.id = be.salesBidHeader_id OR bh.id = be.purchaseBidHeader_id)
WHERE bc.id IS NOT NULL -- Filters out bid headers without content
ORDER BY bh.bidTypeCode ASC, bc.conEditedTime DESC; -- Sorted by bidTypeCode in ascending order