from pycorenlp import StanfordCoreNLP



class ReviewAnalysy:
    
    def __init__(self):
        self.nlp = StanfordCoreNLP('http://localhost:9000')
        pass

    def parseReview(self,review):
        sentence = self.nlp.annotate(review, properties={
            'annotators': 'sentiment',
            'outputFormat': 'json',
            'timeout': 1000,})
        return self.getSentiment(sentence)
    


    def getSentiment(self,sentence):
        cmt_sentiment = self.make_default_sentiment()
        try:
            total_value = 0.0
            for s in sentence["sentences"]:
                total_value += float(s["sentimentValue"])
                cmt_sentiment[s["sentiment"]] += 1
                cmt_sentiment['score'] = total_value
            return cmt_sentiment
        except:
            return cmt_sentiment

    def make_default_sentiment(self):
        dft_sentiment = {"score":0.0, "Positive":0, "Negative":0, "Neutral":0,
                        "Verypositive":0, "Verynegative":0
                        }
        return dft_sentiment

