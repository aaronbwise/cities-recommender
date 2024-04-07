import pandas as pd
import pickle


class CityRecommender:
    def __init__(self, msa_path, name_path):
        self.msa_path = msa_path
        self.name_path = name_path
        self.similarity_df = None
        self.city_name_df = None

    def read_csvs(self):
        """
        Reads the similarity matrix from a CSV file.
        """
        self.similarity_df = pd.read_csv(self.msa_path, index_col=0)
        self.city_name_df = pd.read_csv(self.name_path, index_col=0)

    def predict_msa(self, target_msa, top_n=3):
        """
        Generate recommendations based on the target MSA.

        :param target_msa: The MSA code as a string for which to find similar MSAs.
        :param top_n: Number of top similar MSAs to return.
        :return: A list of tuples containing the recommended MSA codes and their similarity scores.
        """
        if int(target_msa) not in self.similarity_df.index:
            raise ValueError("Target MSA not found in the similarity matrix.")

        # Get similarity scores for the target MSA and sort them
        similarities = self.similarity_df[target_msa].sort_values(ascending=False)

        # Exclude the target MSA from recommendations
        similarities = similarities[similarities.index != int(target_msa)]

        return [msa for msa, _ in similarities.head(top_n).items()]

    def get_city_names(self, msa_codes):
        """
        Get the city name for a given MSA code.

        :param msa_code: The MSA code as a string.
        :return: The city name corresponding to the MSA code.
        """
        return [self.city_name_df.loc[int(code), "Name"] for code in msa_codes]
    
    # Get MSA from city name
    def get_msa_code(self, city_name):
        """
        Get the city name for a given MSA code.

        :param msa_code: The MSA code as a string.
        :return: The city name corresponding to the MSA code.
        """
        return self.city_name_df[self.city_name_df["Name"] == city_name].index[0]
    
    def get_city_pop(self, msa_codes):
        """
        Get the city name for a given MSA code.

        :param msa_code: The MSA code as a string.
        :return: The city name corresponding to the MSA code.
        """
        return [self.city_name_df.loc[int(code), "Pop_Total"] for code in msa_codes]
    
    def get_city_rent(self, msa_codes):
        """
        Get the city name for a given MSA code.

        :param msa_code: The MSA code as a string.
        :return: The city name corresponding to the MSA code.
        """
        return [self.city_name_df.loc[int(code), "Median_Rent"] for code in msa_codes]
    
    def get_city_income(self, msa_codes):
        """
        Get the city name for a given MSA code.

        :param msa_code: The MSA code as a string.
        :return: The city name corresponding to the MSA code.
        """
        return [self.city_name_df.loc[int(code), "Median_Income"] for code in msa_codes]
    
    def get_city_home(self, msa_codes):
        """
        Get the city name for a given MSA code.

        :param msa_code: The MSA code as a string.
        :return: The city name corresponding to the MSA code.
        """
        return [self.city_name_df.loc[int(code), "Median_Home_Value"] for code in msa_codes]
    
    def get_city_wiki_url(self, msa_codes):
        """
        Get the city name for a given MSA code.

        :param msa_code: The MSA code as a string.
        :return: The city name corresponding to the MSA code.
        """
        return [self.city_name_df.loc[int(code), "wiki_url"] for code in msa_codes]
    
    def get_city_wiki_thumbnail_url(self, msa_codes):
        """
        Get the city name for a given MSA code.

        :param msa_code: The MSA code as a string.
        :return: The city name corresponding to the MSA code.
        """
        return [self.city_name_df.loc[int(code), "wiki_thumb_url"] for code in msa_codes]


# Usage example
recommender = CityRecommender("similarity_matrix.csv", "acs_wiki_data.csv")
recommender.read_csvs()  # Read the CSV file to load data into the class

# recommended_msas = ["49820", "10100"]
# test_1 = "Augusta-Richmond County, GA-SC"


# city_names = recommender.get_city_names(recommended_msas)
# msa_code = recommender.get_msa_code(test_1)

# print(f"City names: {city_names}\n MSA code: {msa_code}")

# Make pickle file
pickle.dump(recommender, open("model.pkl", "wb"))
