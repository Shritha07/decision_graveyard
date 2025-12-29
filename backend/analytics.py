def mood_pattern(decisions):
    moods = {}
    for d in decisions:
        mood = d.get("mood") or 0  # Handle None values
        moods[mood] = moods.get(mood, 0) + 1
    return moods
