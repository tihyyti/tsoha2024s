
from flask import Blueprint, render_template
from __init__ import db, logger
from flask import jsonify
from jinja2 import Environment, FileSystemLoader
from datetime import datetime

users_bidheaders_by_status_bp = Blueprint('user_bids_by_bidstatus', __name__)

# User's BidHeaders listed and grouped based on BidHeader status
@users_bidheaders_by_status_bp.route('/bh')
def user_bids_by_bidstatus():
    logger.debug('Entering user_bids_by_bidstatus route')
    conn = None
    cursor = None
    try:
        # Establish the connection
        conn = db.engine.raw_connection()
        cursor = conn.cursor()

        query = "SELECT vw_user_bids_by_bidstatus.bidstatus, array_agg(row_to_json(vw_user_bids_by_bidstatus)) FROM vw_user_bids_by_bidstatus GROUP BY vw_user_bids_by_bidstatus.bidstatus"

        logger.debug(f'Executing query: {query}')
        cursor.execute(query)
        user_bids_by_bidstatus = cursor.fetchall()
        logger.debug(f'Query executed successfully, fetched {len(user_bids_by_bidstatus)} records')
        print(user_bids_by_bidstatus)  # Debugging line
    except Exception as e:
        logger.error(f'Error executing query: {e}')
        return render_template("error.html", notification=f"Error executing query: {e}")
    finally:
        if cursor:
            cursor.close()
            logger.debug('Cursor closed')
        if conn:
            conn.close()
            logger.debug('Connection closed')

    return render_template('view_user_bidheaders_listed_by_status.html', user_bids_by_bidstatus=user_bids_by_bidstatus)

if __name__ == "__main__":
    from __init__ import create_app
    app = create_app()
    app.run(debug=True)


# from flask import Blueprint, render_template
# from __init__ import db
# import logging

# users_bidheaders_by_status_bp = Blueprint('user_bids_by_bidstatus', __name__)

# # Configure logging
# logging.basicConfig(level=logging.DEBUG)
# logger = logging.getLogger(__name__)

# # User's BidHeaders listed and grouped based on BidHeader status
# @users_bidheaders_by_status_bp.route('/bh')
# def user_bids_by_bidstatus():
#     logger.debug('Entering user_bids_by_bidstatus route')
#     conn = None
#     cursor = None
#     try:
#         # Establish the connection
#         conn = db.engine.raw_connection()
#         cursor = conn.cursor()
#         query = "SELECT * FROM vw_user_bids_by_bidstatus"
#         logger.debug(f'Executing query: {query}')
#         cursor.execute(query)
#         user_bids_by_bidstatus = cursor.fetchall()
#         logger.debug(f'Query executed successfully, fetched {len(user_bids_by_bidstatus)} records')
#     except Exception as e:
#         logger.error(f'Error executing query: {e}')
#         return render_template("error.html", notification=f"Error executing query: {e}")
#     finally:
#         if cursor:
#             cursor.close()
#             logger.debug('Cursor closed')
#         if conn:
#             conn.close()
#             logger.debug('Connection closed')

#     return render_template('view_users_bidheaders_listed_by_status.html', users_bids_by_bidstatus=user_bids_by_bidstatus)

# if __name__ == "__main__":
#     # from __init__ import create_app
#     app = create_app()
#     app.run(debug=True)


# # from flask import Blueprint, render_template
# # from __init__ import db

# # users_bidheaders_by_status_bp = Blueprint('user_bids_by_bidstatus', __name__)

# # # User's BidHeaders listed and grouped based on BidHeader status
# # @users_bidheaders_by_status_bp.route('/')
# # def user_bids_by_bidstatus():
# #     try:
# #         # Establish the connection
# #         conn = db.engine.raw_connection()
# #         cursor = conn.cursor()
# #         query = "SELECT * FROM vw_user_bids_by_bidstatus"
# #         cursor.execute(query)
# #         app.logger.debug('Home page accessed, query = vw_user_bids_by_bidstatus')
# #         user_bids_by_bidstatus = cursor.fetchall()
# #     except Exception as e:
# #         return render_template("error.html", notification=f"Error executing query: {e}")
# #     finally:
# #         if cursor:
# #             cursor.close()
# #         if conn:
# #             conn.close()

# #     return render_template('view_user_bidheaders_listed_by_status.html', user_bids_by_bidstatus=user_bids_by_bidstatus)

# # if __name__ == "__main__":
# #     from __init__ import create_app
# #     app = create_app()
# #     app.run(debug=True)


# # # from flask import Blueprint, render_template, redirect, url_for
# # # from __init__ import db
# # # import templates
# # #
# # # users_bidheaders_by_status_bp = Blueprint('user_bids_by_bidstatus', __name__)
# # #
# # User's BidHeaders listed and grouped based on BidHeader status
# # # @users_bidheaders_by_status_bp.route('/')
# # # def user_bids_by_bidstatus():
# #     # conn = None
# #     # cursor = None
# #     # try:
# #         Establish the connection
# #         # conn = db
# #         # cursor = conn.cursor()
# #         # query = "SELECT * FROM vw_user_bids_by_bidstatus"
# #         # cursor.execute(query)
# #         # user_bids_by_bidstatus = cursor.fetchall()
# #     # except Exception as e:
# #         # # return render_template("error.html", notification=f"Error executing query: {e}")
# #     # finally:
# #         # if cursor:
# #             # cursor.close()
# #         # if conn:
# #             # conn.close()
# # #
# #     # # return render_template('view_user_bidheaders_listed_by_status.html', user_bids_by_bidstatus=user_bids_by_bidstatus)
# # #
# # # if __name__ == "__main__":
# #     # from my_flask_app import create_app
# #     # app = create_app()
# #     # app.run(debug=True)
# # #