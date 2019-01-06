#TODO implement logic to fetch data using api 
#this class read reviews from local json file and dealer rating 

import json
from const import Car24TechBullzConstants
from dealer import Dealer
from review import Review
from NlpParser import ReviewAnalysy

class Car24TechBullzReviewBuilder:
	"""docstring for Car24TechBullzConstants"""
	all_dealers = {}
	all_reviews = {}
	review_sentiment = {}

	def __init__(self):
		self.getAllDealers()
		self.getReview()
		self.sentimentParser = ReviewAnalysy()
		pass


	def getReview(self):
		#TODO fetch review from social web links
		self.readLocalReview()
		pass

	#TODO remove this function once api is integarted 
	def readLocalReview(self):
		with open(Car24TechBullzConstants.REVIEW_FILE) as data_file:
			data_dict = json.loads(data_file.read())

		for data in data_dict:
			if data["dealerId"] in self.all_reviews:
				self.all_reviews[data["dealerId"]] += ". \n"  + data["review"]
			else:
				self.all_reviews[data["dealerId"]] = data["review"]
		pass

	def getAllDealers(self):
		with open(Car24TechBullzConstants.DEALER_FILE) as data_file:
			data_dict = json.loads(data_file.read())
		for data in data_dict:
			self.all_dealers[data["dealerId"]] = data["dealerName"]
		pass

	def createReviewSentiment(self):
		for obj in self.all_reviews:
			self.review_sentiment[obj] = self.sentimentParser.parseReview(str(self.all_reviews[obj]))
			print "Total rating for  " + self.all_dealers[obj] +" : " + str( (self.calculateOverAllRating(self.review_sentiment[obj])))
		pass

	def calculateOverAllRating(self,sentiment):
		#print sentiment
		#TODO  Use bayesian mean to  compute over all rating
		total_positive_sentiment = sentiment["Positive"] + sentiment["Verypositive"]
		total_negative_sentiment = sentiment["Negative"] + sentiment["Verynegative"]
		#print (total_positive_sentiment + total_negative_sentiment)
		total_sum = total_positive_sentiment + total_negative_sentiment
		rating = 0
		if total_sum > 0:
			rating  =  ((sentiment["score"])  /  (total_positive_sentiment + total_negative_sentiment)) 

		overall_rating = 0.0
		#TODO Improve logic using mean 	
		if (rating < 2.0 and rating > 0):
			overall_rating = 1 
		elif ( rating >= 2 and rating<3 ):
			overall_rating = 2 
		elif (rating>=3 and rating<4 ):
			overall_rating = 2.5
		elif (rating >= 4 and rating < 5):
			overall_rating = 3 
		elif (rating>=5 and rating<6):
			overall_rating= 3.5
		elif (rating>=6 and rating<8):
			overall_rating= 4
		elif (rating>=8 and rating<9):
			overall_rating= 4.5
		elif(rating>=9 and rating<=10):
			overall_rating= 5
		else:
			overall_rating = 0.0
		return overall_rating


if __name__ == '__main__':
	obj = Car24TechBullzReviewBuilder()
	obj.createReviewSentiment()
	
	
