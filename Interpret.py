import pickle
import pandas as pd
from fastai.tabular.all import untar_data, URLs
def main():
    path = untar_data(URLs.ML_100k)
    # merge on the end rather than before training. Movie names are useless to computer -__-
    movies = pd.read_csv(path/'u.item', delimiter='|', encoding='latin-1', usecols=(0,1), names=('movie', 'title'), header=None)
    ratings = pd.read_csv(path/'u.data', delimiter='\t', header=None, names = ['user', 'movie', 'rating', 'timestamp']) 
    ratings = ratings.drop(['timestamp'], axis = 1)
    table = ratings.merge(movies)
    with open("model3.pkl", "rb") as file:
        data = pickle.load(file)
    item_bias = data.item_bias.squeeze()
    idxs = item_bias.argsort()[:5]
    for i in idxs:
        low_bias = table[table['movie'] == i.item()]
        print(low_bias['title'].unique())
if __name__ =="__main__":
    main() 