ERROR_KEYWORDS = [
    "ERROR",
    "FAILURE",
    "Failed",
    "failed",
    "##[error]",
    "Exception",
    "Unable",
    "Timeout",
]


def extract_events(log_text):

    events = []

    for line in log_text.splitlines():

        if any(
            keyword.lower() in line.lower()
            for keyword in ERROR_KEYWORDS
        ):
            events.append(line)

    return events