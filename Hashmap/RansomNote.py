class RansomNote:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNoteLetters = {}

        # Initialize dictionary to contain all the letters of the note
        for letter in ransomNote:
            if letter not in ransomNoteLetters:
                ransomNoteLetters[letter] = 0
            ransomNoteLetters[letter] += 1

        # If the letter appears in the magazine, subtract it from the dict
        for letter in magazine:
            if letter in ransomNoteLetters:
                ransomNoteLetters[letter] -= 1

        for letter in ransomNoteLetters:
            # If that letter was not found in the magazine but was in the note
            # The count will be at least one.
            if ransomNoteLetters[letter] > 0:
                return False

        return True
