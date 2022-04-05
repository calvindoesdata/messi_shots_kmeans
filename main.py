import os

from read_files import Data
from modeller import KMeansModel
from plot_data import Plotter

match_dir_path = 'StatsBomb_data/matches/11/'
event_dir_path = 'StatsBomb_data/events/'
player_of_interest = 'Lionel Andrés Messi Cuccittini'
elbow_test_range = 15
optimal_n_clusters = 10

if __name__ == '__main__':
    # Create an output directory for plot images, if the directory does not exist
    if not os.path.exists('output'):
        os.mkdir('output')

    # Instantiate the Data class to collect all xy shot location coordinates
    print('Gathering all shot location data for {}'.format(player_of_interest))
    messi_data = Data(match_dir_path=match_dir_path, event_dir_path=event_dir_path).shot_event_file_iterator(
        player_name=player_of_interest)

    # Identify the optimal n_clusters for the K-Means model using the elbow method
    print('Beginning elbow test of the K-Means algorithm')
    inertia_results = []
    for n in range(1, elbow_test_range + 1):
        elbow_result = KMeansModel(xy_data=messi_data, num_of_clusters=n, verbosity=0).model_data()
        inertia_results.append(elbow_result.inertia_)
        print('Number of clusters = {}, number of iterations = {}, inertia = {}'.format(
            n, elbow_result.n_iter_, elbow_result.inertia_))

    # Plot elbow chart results
    inertia_plot = Plotter()
    inertia_plot_parameters = inertia_plot.plot_inertia(x_values=list(range(1, elbow_test_range + 1)),
                                                        y_values=inertia_results)
    inertia_plot.save_figure([inertia_plot_parameters], save_location='output/messi_shots_elbow_chart.png')

    print('Now running the K-Means clustering algorithm with the optimal n_clusters value')
    # Fit the model with optimal n_clusters to Messi's xy shot location coordinates
    kmeans = KMeansModel(xy_data=messi_data, num_of_clusters=optimal_n_clusters, verbosity=2)
    kmeans_results = kmeans.model_data()
    print('Number of clusters = {}, number of iterations = {}, inertia = {}'.format(
            optimal_n_clusters, kmeans_results.n_iter_, kmeans_results.inertia_))

    # Gather the K-Means model fitting results into useful variables for plotting
    cluster_coords = kmeans.cluster_coordinates_dataframe(kmeans_results.labels_)
    cluster_centres = kmeans.cluster_centres_lists(kmeans_results.cluster_centers_)

    # Plot the clusters and their centre points calculated from the K-Means model
    main_plot = Plotter()
    label_plot = main_plot.plot_scatter(x_coords=cluster_coords['x'], y_coords=cluster_coords['y'],
                                        hue=cluster_coords['cluster'], plot_with_cmap=True, colour_palette='orange',
                                        marker='o', s=20, zorder=1)
    centre_plot = main_plot.plot_scatter(x_coords=cluster_centres[0], y_coords=cluster_centres[1],
                                         plot_with_cmap=False, marker="X", s=40, edgecolor='black', color='red',
                                         legend=True, label='cluster centre', zorder=3)
    main_plot.save_figure(plots=[label_plot, centre_plot], save_location='output/messi_shots_clusters.png')

