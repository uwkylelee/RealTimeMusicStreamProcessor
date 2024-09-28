import random
from typing import Dict, Any, List
from faker import Faker

from database_helper.db_manager import PostgresDataManager
from database_helper.models import Tracks, Users
from genre_preference import GenrePreferenceService


class FakeTrackEventGenerator:
    """
    Class to generate realistic fake music streaming and like events
    based on user demographics and track popularity.
    """

    def __init__(self):
        """
        Initialize the generator.

        """
        # Database configuration
        db_config = {
            "host": "musicDB",
            "database": "music_db",
            "port": "5432",
            "user": "pyspark",
            "password": "pyspark1234",
        }

        self.genre_service = GenrePreferenceService()
        self.data_manager = PostgresDataManager(db_config)
        self.tracks = self.data_manager.fetch_all(Tracks)
        self.users = self.data_manager.fetch_all(Users)
        self.fake = Faker()

    def _filter_tracks_by_genres(
        self, preferred_genres: List[str]
    ) -> List[Dict[str, Any]]:
        """
        Filter tracks based on preferred genres.

        :param preferred_genres: List of user's preferred genres.
        :return: List of tracks that match the preferred genres.
        """
        return [track for track in self.tracks if track["genre"] in preferred_genres]

    def _weighted_track_choice(
        self, filtered_tracks: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        Select a track from filtered tracks based on their popularity.

        :param filtered_tracks: List of tracks filtered by preferred genres.
        :return: A randomly selected track, weighted by popularity.
        """
        return random.choices(
            filtered_tracks,
            weights=[track["popularity"] for track in filtered_tracks],
            k=1,
        )[0]

    def generate_event(self) -> Dict[str, Any]:
        """
        Generate a fake music event (streaming or like)
        based on user demographics.
        :return: A fake event with realistic attributes.
        """
        user_info = random.choice(self.users)
        event_type = random.choices(["streaming", "like"], weights=[0.99, 0.01], k=1)[0]

        preferred_genres = self.genre_service.get_user_preferred_genres(
            user_info["age"], user_info["gender"]
        )
        filtered_tracks = self._filter_tracks_by_genres(preferred_genres)

        if not filtered_tracks:
            raise ValueError("No tracks found for the user's preferred genres.")

        selected_track = self._weighted_track_choice(filtered_tracks)

        return {
            "user_id": user_info["user_id"],
            "track_id": selected_track["track_id"],
            "event_timestamp": self.fake.date_time_this_month().isoformat(),
            "event_type": event_type,
        }
