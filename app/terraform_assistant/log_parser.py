ERROR_KEYWORDS = [
    "Error",
    "AccessDenied",
    "UnauthorizedOperation",
    "Failed",
    "InvalidClientTokenId",
    "state lock",
    "ConditionalCheckFailedException",
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