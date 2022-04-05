import pandas as pd

from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler


class KMeansModel:
    def __init__(self, xy_data, num_of_clusters: int, verbosity: int):
        self.scaler = MinMaxScaler()
        self.xy_data = xy_data
        self.num_of_clusters = num_of_clusters
        self.verbosity = verbosity
        self.kmeans_model = KMeans(n_clusters=self.num_of_clusters, n_init=1, verbose=self.verbosity)
        self.normalised_xy = self.scaler.fit_transform(self.xy_data)

    def model_data(self):
        """
        This method fits the kmeans model to the input data.
        """
        fitted_model = self.kmeans_model.fit(self.normalised_xy)

        return fitted_model

    def cluster_coordinates_dataframe(self, cluster_label_list):
        """
        This method constructs a Pandas DataFrame from the original xy coordinates. For each coordinate pair
        columns are added for the cluster label and individually for the x and y coordinates.

        The resulting DataFrame will be used to plot the fitted kmeans model results.
        :param cluster_label_list: list of cluster labels from the fitted kmeans model
        :return:
            df_clusters_coordinates: Pandas DataFrame of xy coordinates and cluster labels
        """
        denormalised_xy_data = self.scaler.inverse_transform(self.normalised_xy).tolist()
        df_clusters_coordinates = pd.DataFrame(zip(denormalised_xy_data, cluster_label_list), columns=['xy', 'cluster'])
        df_clusters_coordinates['x'] = [x[0] for x in df_clusters_coordinates['xy']]
        df_clusters_coordinates['y'] = [y[1] for y in df_clusters_coordinates['xy']]

        return df_clusters_coordinates

    def cluster_centres_lists(self, normalised_cluster_centres_array):
        """
        This method creates separate lists for the x and y coordinates of the cluster centres calculated from the
        fitted  kmeans model.
        :param normalised_cluster_centres_array: ndarray of cluster centres
        :return:
            cluster_centres_x_list: list of x coordinates of cluster centres
            cluster_centres_y_list: list of y coordinates of cluster centres
        """
        cluster_centres_array = self.scaler.inverse_transform(normalised_cluster_centres_array)
        cluster_centres_x_list = [x[0] for x in cluster_centres_array]
        cluster_centres_y_list = [y[1] for y in cluster_centres_array]

        return cluster_centres_x_list, cluster_centres_y_list
