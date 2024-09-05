from typing import Dict, List


class GenrePreferenceService:
    """
    Service to determine preferred genres for a user based on age and gender.
    """

    def __init__(self):
        self.genre_mapping = GenreMapping()

    def get_age_range(self, age: int) -> str:
        """
        Get the age range for a given age.

        :param age: User's age.
        :return: Age range as a string.
        """
        if age < 20:
            return "10-19"
        elif age < 30:
            return "20-29"
        elif age < 40:
            return "30-39"
        elif age < 50:
            return "40-49"
        elif age < 60:
            return "50-59"
        else:
            return "60+"

    def get_user_preferred_genres(self, age: int, gender: str) -> List[str]:
        """
        Get preferred genres for a given user.

        :param age: User's age.
        :param age: User's gender.
        :return: List of preferred genres.
        """
        age_range = self.get_age_range(age)
        return self.genre_mapping.get_preferred_genres(age_range, gender)


class GenreMapping:
    """
    Model to hold the genre preferences mapping for different age ranges and genders.
    """

    def __init__(self):
        self.mapping = self._create_genre_mapping()

    def _create_genre_mapping(self) -> Dict[str, Dict[str, List[str]]]:
        """
        Create a mapping of age ranges and gender to preferred music genres.

        :return: Dictionary mapping age ranges and gender to preferred genres.
        """
        return {
            "10-19": {
                "M": ["pop", "k-pop", "hip-hop", "edm", "anime", "dubstep",
                      "dance", "j-pop", "punk-rock", "party"],
                "F": ["pop", "k-pop", "hip-hop", "j-pop", "dance",
                      "singer-songwriter", "party", "indie", "anime",
                      "electro"],
                "X": ["pop", "k-pop", "hip-hop", "j-pop", "dance",
                      "singer-songwriter", "party", "indie", "anime", "electro"]
            },
            "20-29": {
                "M": ["electronic", "house", "indie", "funk", "latin", "rock",
                      "singer-songwriter", "dancehall", "alternative",
                      "reggae"],
                "F": ["pop", "indie", "latin", "r-n-b", "house", "funk", "rock",
                      "dancehall", "electronic", "ska"],
                "X": ["pop", "indie", "latin", "r-n-b", "house", "funk", "rock",
                      "dancehall", "electronic", "ska"]
            },
            "30-39": {
                "M": ["jazz", "soul", "indie-pop", "psych-rock", "garage",
                      "blues", "r-n-b", "acoustic", "ska", "disco"],
                "F": ["jazz", "soul", "indie", "funk", "singer-songwriter",
                      "blues", "ska", "acoustic", "disco", "folk"],
                "X": ["jazz", "soul", "indie", "funk", "singer-songwriter",
                      "blues", "ska", "acoustic", "disco", "folk"]
            },
            "40-49": {
                "M": ["rock", "classic-rock", "gospel", "jazz", "punk", "funk",
                      "folk", "ska", "show-tunes", "soul"],
                "F": ["classic-rock", "gospel", "jazz", "soul", "folk",
                      "show-tunes", "punk", "ska", "funk", "rock"],
                "X": ["classic-rock", "gospel", "jazz", "soul", "folk",
                      "show-tunes", "punk", "ska", "funk", "rock"]
            },
            "50-59": {
                "M": ["classical", "blues", "gospel", "country", "folk",
                      "bluegrass", "soul", "tango", "jazz", "opera"],
                "F": ["classical", "gospel", "blues", "country", "folk",
                      "opera", "bluegrass", "soul", "jazz", "tango"],
                "X": ["classical", "gospel", "blues", "country", "folk",
                      "opera", "bluegrass", "soul", "jazz", "tango"]
            },
            "60+": {
                "M": ["classical", "folk", "oldies", "gospel", "blues", "jazz",
                      "opera", "rock-n-roll", "country", "piano"],
                "F": ["classical", "folk", "oldies", "gospel", "opera", "blues",
                      "country", "jazz", "rock-n-roll", "piano"],
                "X": ["classical", "folk", "oldies", "gospel", "opera", "blues",
                      "country", "jazz", "rock-n-roll", "piano"]
            }
        }

    def get_preferred_genres(self, age_range: str, gender: str) -> List[str]:
        """
        Get preferred genres for a given age range and gender.

        :param age_range: Age range of the user.
        :param gender: Gender of the user.
        :return: List of preferred genres.
        """
        return self.mapping[age_range][gender]
