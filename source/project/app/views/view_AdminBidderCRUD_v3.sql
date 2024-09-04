
-- View: AdminBidderCRUD_v3
-- Description: Allows admin to manage bidders (users) with CRUD operations.
--
-- bidder_id represents the unique identifier for each bidder.
-- bidderName is the name of the bidder.
-- userRole indicates the role of the user (e.g., registered user, seller, buyer, admin).
-- isBlocked specifies whether the user is blocked from the service.
--
CREATE VIEW AdminUserCRUD AS
SELECT
    a.id AS user_id,
    a.userName,
    r.roleName AS userRole,
    b.blocked AS isBlocked
FROM User a
LEFT JOIN Role r ON (a.role_id = r.id)
ORDER BY a.userName;
