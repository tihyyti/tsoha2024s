
-- View: AdminUserRolesAndLastBidHeaders_v3
-- Description: Lists all users sorted by roles and includes details of their last initialized BidHeader.
  --
  -- bidder_id represents the unique identifier for each bidder.
  -- bidderName is the name of the bidder.
  -- userRole indicates the role of the user (e.g., registered user, seller, buyer, admin).
  -- lastBidHeader provides the header text of the user’s last initialized BidHeader.
  --
CREATE VIEW AdminUserRolesAndLastBidHeaders AS
SELECT
    a.id AS user_id,
    a.bidderName,
    r.roleName AS userRole,
    bh.bidHeaderText AS lastBidHeader,
    bh.bidStartedTime AS lastBidStartTime
FROM User a
LEFT JOIN Role r ON (a.role_id = r.id)
LEFT JOIN BidHeader bh ON (a.id = bh.initialBidder_id)
WHERE bh.id IS NOT NULL -- Filters out users without initialized BidHeaders
ORDER BY r.roleName, a.userName;