import sqlite3


class RatingDBHandler():

	
	conn = sqlite3.connect('rating.db')
	def init(self):
		self.createDealerRatingTable()
		pass

	def  createDealerRatingTable(self):
		self.conn.execute('''CREATE TABLE IF NOT EXISTS DEALER_REVIEW_RATING
         (DealerID INT PRIMARY KEY     NOT NULL,
         UserID           TEXT    NOT NULL,
         RatingSentiment  TEXT     NOT NULL,
         OverAllRating INT NOT NULL
         );''')
		print ("createDealerRatingTable")
		pass

	def __del__(self):
		self.conn.close()

	def stroreRating(self,DealerId,currentRating):
		# Connect to the test db 
		pass	

	def getUserRating(self,DealerId):
		pass

	def  evalauteDealerOverAllRating(self,currentSentiment,DealerId):
		print ("evalauteDealerOverAllRating")
		savedRating, totalUser = getUserRating(DealerId)
		#
		pass

