import os
import json


class Data:
    def __init__(self, match_dir_path, event_dir_path):
        self.match_dir_path = match_dir_path
        self.event_dir_path = event_dir_path

    def match_file_iterator(self):
        """
        This function iterates through all StatsBomb match files in the specified directory and extracts match_ids
        :return:
            match_ids: list of match_ids for the event_file_iterator
        """
        match_ids = []
        for (root, dirs, files) in os.walk(self.match_dir_path, topdown=True):
            for file in files:
                with open(os.path.join(root, file)) as f:
                    data = json.load(f)
                    for match in data:
                        match_ids.append(match['match_id'])

        return match_ids

    def shot_event_file_iterator(self, player_name):
        """
        This function iterates through all StatsBomb match files in the specified directory and extracts the xy
        coordinates of all shot locations by Lionel Messi.
        :return:
            shot_loc_xy_adjusted: list of xy coordinates for onward processing
        """
        shot_loc_xy = []
        for match_file in self.match_file_iterator():
            with open(os.path.join(self.event_dir_path, '{}.json'.format(match_file))) as f:
                data = json.load(f)
                for item in data:
                    if (item['type']['name'] == 'Shot') and \
                            (item['player']['name'] == player_name):
                        shot_loc_xy.append(item['location'])

        # Adjust y coordinates so they appear on the correct side of the visualisation.
        # i.e. flip the pitch vertically through y=40
        shot_loc_xy_adjusted = [[x[0], 80 - x[1] if x[1] > 40 else (40 + (40 - x[1]))] for x in shot_loc_xy]

        return shot_loc_xy_adjusted
