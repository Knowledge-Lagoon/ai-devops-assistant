ACTIVE_INCIDENTS = {}


def get_incident_key(
    pod: dict
):

    return (
        f"{pod['cluster']}|"
        f"{pod['namespace']}|"
        f"{pod['pod']}|"
        f"{pod['reason']}"
    )


def incident_exists(
    pod: dict
):

    key = get_incident_key(
        pod
    )

    return key in ACTIVE_INCIDENTS


def register_incident(
    pod: dict,
    ticket_key: str
):

    key = get_incident_key(
        pod
    )

    ACTIVE_INCIDENTS[key] = ticket_key


def get_ticket_key(
    pod: dict
):

    key = get_incident_key(
        pod
    )

    return ACTIVE_INCIDENTS.get(
        key
    )


def clear_incident(
    pod: dict
):

    key = get_incident_key(
        pod
    )

    ACTIVE_INCIDENTS.pop(
        key,
        None
    )