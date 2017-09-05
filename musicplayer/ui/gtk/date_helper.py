def seconds_to_string(duration):
    """Convert a time in seconds to a mm:ss string
    """
    minutes = duration // 60
    seconds = duration % 60

    return '{:02d}:{:02d}'.format(minutes, seconds)