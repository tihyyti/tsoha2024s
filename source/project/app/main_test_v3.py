

if __name__ == '__main__':
    # Initialize your Flask app and configure SQLAlchemy
    # ...

    # Query data from views
    bid_genre_list = BidGenreListService.get_all()
    bid_list = BidListService.get_all()

    # Process the data as needed
    for genre in bid_genre_list:
        print(f"Genre: {genre.bidGenreHeader}, Count: {genre.count}, Latest: {genre.
latest}")

    for bid in bid_list:
        print(f"Bid Header: {bid.bidHeaderText}, Started Time: {bid.bidStartedTime}")