from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfTransformer

category_map = {'misc.forsale': 'Sales', 'rec.motorcycles': 'Motorcycles', 
        'rec.sport.baseball': 'Baseball', 'sci.crypt': 'Cryptography', 
        'sci.space': 'Space'}
		
training_data = fetch_20newsgroups(subset='train', categories=category_map.keys(), shuffle=True, random_state=7)
vectorizer = CountVectorizer()
X_train_termcounts = vectorizer.fit_transform(training_data.data)
print "\nDimensions of training data: ", X_train_termcounts.shape

input_data = [
    "The curveballs of right handed pitchers tend to curve to the left", 
    "Caesar cipher is an ancient form of encryption",
    "This two-wheeler is really good on slippery roads"
]

tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_termcounts)

classifier = MultinomialNB.fit(X_train_tfidf, training_data.target)
X_input_termcounts = vectorizer.transform(input_data)
X_input_tfidf = tfidf_transformer.transform(X_input_termcounts)
predicted_categories = classifier.predict(X_input_tfidf)
for sentence, category in zip(input_data, predicted_categories):
	print '\nInput:', sentence, "\nPredicted category:", category_map[training_data.target_names[category]]

