
-- View: AdminUserRolesAuthorization_v3
-- Description: Allows admin to authorize users by selecting predefined roles.
--
-- bidder_id represents the unique identifier for each bidder (user).
-- bidderName is the name of the bidder.
-- selectedRole indicates the predefined role selected by the admin.
--
CREATE VIEW AdminUserRolesAuthorization AS
SELECT
    b.id AS bidder_id,
    b.bidderName,
    r.roleName AS selectedRole
FROM Bidder b
CROSS JOIN Role r; -- Generates all possible combinations of users and roles
