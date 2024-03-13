import difflib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import numpy as np
from ast import literal_eval
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

data = pd.read_csv("newaa.csv",on_bad_lines='skip')

tfidf = TfidfVectorizer(stop_words='english')
data['description'] = data['description'].fillna('')
tfidf_matrix = tfidf.fit_transform(data['description'])

cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

indices = pd.Series(data.index, index=data['title']).drop_duplicates()

def get_recommendations(title, cosine_sim=cosine_sim):
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    newIndices = [i[0] for i in sim_scores]
    
    return data['title'].iloc[newIndices]

features = ['author', 'setting', 'genres']

def clean_data(x):
    if isinstance(x, list):
        return [str.lower(i.replace(" ", "")) for i in x]
    else:
        if isinstance(x, str):
            return str.lower(x.replace(" ", ""))
        else:
            return ''
for feature in features:
    data[feature] = data[feature].apply(clean_data)

def create_soup(x):
    return ' '.join(x['author']) + ' ' + ' '.join(x['setting']) + ' ' + x['genres'] + ' ' 

data['soup'] = data.apply(create_soup, axis=1)


count = CountVectorizer(stop_words='english')
count_matrix = count.fit_transform(data['soup'])
cosine_sim2 = cosine_similarity(count_matrix, count_matrix)
data = data.reset_index()
indices = pd.Series(data.index, index=data['title'])

def combine(title):
    titleList = data['title'].tolist()
    title1= difflib.get_close_matches(title, titleList, n=1)
   
    s = ''.join(title1)
    finalRecs = get_recommendations(s, cosine_sim2)
    
    recsArray = finalRecs
    recsList = recsArray.tolist()
    return recsList









