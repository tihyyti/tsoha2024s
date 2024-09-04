"""
@Service
public class NewsLiService {

    @Autowired
    private NewsLiRepository newsLiRepository;

    private PieceOfNewsHeader pieceOfNewsHeader;
    private NewsGenreList newsGenreList;

    public void createPieceOfNewsHeader(Model model, Long startedBy, Long  genre, String h
        pieceOfNewsHeader = new PieceOfNewsHeader(startedBy, genre, header);
        newsLiRepository.save(pieceOfNewsHeader);
        model.addAttribute("pieceOfNewsHeader", pieceOfNewsHeader);
    }

    public void deletePieceOfNewsHeader(Long pieceOfNewsHeaderId) {
        newsLiRepository.delete(pieceOfNewsHeaderId);
    }

    public void getOnePieceOfNewsHeader(Model model, Long pieceOfNewsHeaderId) {
        //pieceOfNewsHeader = newsLiRepository.findOne(pieceOfNewsHeaderId);
        //Do update here !
        //pieceOfNewsHeaderRepository.save(pieceOfNewsHeader); //UPDATE/WRITE
        model.addAttribute("pieceOfNewsHeader", newsLiRepository.findOne(pieceOfNewsHeader
    }

    public void getAllPieceOfNewsHeaders(Model model) {
        model.addAttribute("pieceOfNewsHeaders", newsLiRepository.findAll());
    }
    public void findContentsPerPieceOfNewsHeader(Model model) {
        model.addAttribute("contentsPerPieceOfNewsHeader", pieceOfNewsHeader.getPieceOfNew
());
    }

Here are the service classes for BidHeader, BidContent, GearGroup, Gear, and BidExchange based on the PostgreSQL 16 script provided earlier.

These service classes provide methods to create, read, update, and
delete records for BidHeader, BidContent, GearGroup, Gear, and
BidExchange."""

#BidHeaderService

class BidHeaderService:
    @staticmethod
    def create_bid_header(initialBidder, bidGnre, bidHder, numberOfBids, startedTime):
        new_bid_header = BidHeader(initialBidder=initialBidder, bidGnre=bidGnre, bidHder=bidHder, numberOfBids=numberOfBids, startedTime=startedTime)
        db.session.add(new_bid_header)
        db.session.commit()
        return new_bid_header

    @staticmethod
    def get_bid_header_by_id(bid_header_id):
        return BidHeader.query.get(bid_header_id)

    @staticmethod
    def update_bid_header(bid_header_id, **kwargs):
        bid_header = BidHeader.query.get(bid_header_id)
        for key, value in kwargs.items():
            setattr(bid_header, key, value)
        db.session.commit()
        return bid_header

    @staticmethod
    def delete_bid_header(bid_header_id):
        bid_header = BidHeader.query.get(bid_header_id)
        db.session.delete(bid_header)
        db.session.commit()

#BidContentService

class BidContentService:
    @staticmethod
    def create_bid_content(bidderID, bidHead, bidderName, bidContent, editedTime):
        new_bid_content = BidContent(bidderID=bidderID, bidHead=bidHead, bidderName=bidderName, bidContent=bidContent, editedTime=editedTime)
        db.session.add(new_bid_content)
        db.session.commit()
        return new_bid_content

    @staticmethod
    def get_bid_content_by_id(bid_content_id):
        return BidContent.query.get(bid_content_id)

    @staticmethod
    def update_bid_content(bid_content_id, **kwargs):
        bid_content = BidContent.query.get(bid_content_id)
        for key, value in kwargs.items():
            setattr(bid_content, key, value)
        db.session.commit()
        return bid_content

    @staticmethod
    def delete_bid_content(bid_content_id):
        bid_content = BidContent.query.get(bid_content_id)
        db.session.delete(bid_content)
        db.session.commit()

#GearGroupService

class GearGroupService:
    @staticmethod
    def create_gear_group(gearGroup, bidderID, gearGroupHeader):
        new_gear_group = GearGroup(gearGroup=gearGroup, bidderID=bidderID, gearGroupHeader=gearGroupHeader)
        db.session.add(new_gear_group)
        db.session.commit()
        return new_gear_group

    @staticmethod
    def get_gear_group_by_id(gear_group_id):
        return GearGroup.query.get(gear_group_id)

    @staticmethod
    def update_gear_group(gear_group_id, **kwargs):
        gear_group = GearGroup.query.get(gear_group_id)
        for key, value in kwargs.items():
            setattr(gear_group, key, value)
        db.session.commit()
        return gear_group

    @staticmethod
    def delete_gear_group(gear_group_id):
        gear_group = GearGroup.query.get(gear_group_id)
        db.session.delete(gear_group)
        db.session.commit()

#GearService

class GearService:
    @staticmethod
    def create_gear(gearCode, gearStatus, bidderID, bidHead, gearName, gearDetails, gearStory, amountOffered, origPrice, comments, editedTime):
        new_gear = Gear(gearCode=gearCode, gearStatus=gearStatus, bidderID=bidderID, bidHead=bidHead, gearName=gearName, gearDetails=gearDetails, gearStory=gearStory, amountOffered=amountOffered, origPrice=origPrice, comments=comments, editedTime=editedTime)
        db.session.add(new_gear)
        db.session.commit()
        return new_gear

    @staticmethod
    def get_gear_by_id(gear_id):
        return Gear.query.get(gear_id)

    @staticmethod
    def update_gear(gear_id, **kwargs):
        gear = Gear.query.get(gear_id)
        for key, value in kwargs.items():
            setattr(gear, key, value)
        db.session.commit()
        return gear

    @staticmethod
    def delete_gear(gear_id):
        gear = Gear.query.get(gear_id)
        db.session.delete(gear)
        db.session.commit()

#BidExchangeService

class BidExchangeService:
    @staticmethod
    def create_bid_exchange(salesBidder, purchaseBidder, equipmentOffer, equipmentRequested, agreedDeal, dealTimestamp):
        new_bid_exchange = BidExchange(salesBidder=salesBidder, purchaseBidder=purchaseBidder, equipmentOffer=equipmentOffer, equipmentRequested=equipmentRequested, agreedDeal=agreedDeal, dealTimestamp=dealTimestamp)
        db.session.add(new_bid_exchange)
        db.session.commit()
        return new_bid_exchange

    @staticmethod
    def get_bid_exchange_by_id(bid_exchange_id):
        return BidExchange.query.get(bid_exchange_id)

    @staticmethod
    def update_bid_exchange(bid_exchange_id, **kwargs):
        bid_exchange = BidExchange.query.get(bid_exchange_id)
        for key, value in kwargs.items():
            setattr(bid_exchange, key, value)
        db.session.commit()
        return bid_exchange

    @staticmethod
    def delete_bid_exchange(bid_exchange_id):
        bid_exchange = BidExchange.query.get(bid_exchange_id)
        db.session.delete(bid_exchange)
        db.session.commit()
