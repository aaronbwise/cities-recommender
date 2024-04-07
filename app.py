from website import create_app
import pickle
from model import CityRecommender

recommender = pickle.load(open("model.pkl", "rb"))

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
