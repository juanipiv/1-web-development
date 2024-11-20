SECONDS_PER_HOUR = 3600
SECONDS_PER_MINUTE = 60

def seconds_to_interval(seconds):
    hours = int(seconds / SECONDS_PER_HOUR)
    minutes = (seconds % SECONDS_PER_HOUR) // SECONDS_PER_MINUTE
    secs =  seconds - hour * SECONDS_PER_HOUR + minutes * SECONDS_PER_MINUTE
    return (hours, minutes, secs)
