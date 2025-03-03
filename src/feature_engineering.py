class FeatureExtractor:
    """
    A class for extracting features from MBTI personality type strings.
    
    Attributes:
        mbti_type (str): A 4-character MBTI type string (e.g., 'ENTP', 'ISFJ').
    """

    def __init__(self, mbti_type: str):
        """
        Initializes the FeatureExtractor with an MBTI type.

        Args:
            mbti_type (str): A 4-character MBTI type string (e.g., 'ENTP', 'ISFJ').
        """
        if len(mbti_type) != 4 or not mbti_type.isalpha():
            raise ValueError("MBTI type must be a 4-character string containing only letters.")
        
        self.mbti_type = mbti_type.lower()  # Ensure consistency

    def encode_mbti(self) -> dict:
        """
        Encodes the MBTI type into numerical features.

        MBTI Personality Type Encoding:
        - Extraversion (E) = 1, Introversion (I) = 0
        - Sensing (S) = 1, Intuition (N) = 0
        - Thinking (T) = 1, Feeling (F) = 0
        - Judging (J) = 1, Perceiving (P) = 0

        Returns:
            dict: A dictionary containing encoded MBTI features.
        """
        return {
            "is_extraversion": int(self.mbti_type[0] == 'e'),
            "is_sensing": int(self.mbti_type[1] == 's'),
            "is_thinking": int(self.mbti_type[2] == 't'),
            "is_judging": int(self.mbti_type[3] == 'j')
        }

