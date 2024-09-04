
-- View: BidderGearList_v3
-- Description: Lists a bidder's gear items sorted by GearGroup.
--
-- gear_id represents the unique identifier for each gear item.
-- gearGroup indicates the GearGroup to which the gear belongs.
-- Other fields like gearBrand, gearCode, gearStatus, gearName, amountOffered, gearImage-link, Sound-link, and
-- lastEditedTime provide relevant information about the gear.
--
CREATE VIEW BidderGearList AS
SELECT
    g.id AS gear_id,
    gg.gearGroupHeader AS gearGroup,
    g.gearBrand,
    g.gearCode,
    g.gearStatus,
    g.gearName,
    g.amountOffered,
    im.image_url AS gearImage_link,
    scm.sample_url AS sound_link,
    g.editedTime AS lastEditedTime
FROM Gear g
LEFT JOIN GearGroup gg ON (g.gearGroup_id = gg.id)
LEFT JOIN ImageMetadata im ON (g.gearImage_id = im.id)
LEFT JOIN SoundClipMetadata scm ON (g.soundClip_id = scm.id)
ORDER BY gg.gearGroupHeader, g.editedTime DESC;
