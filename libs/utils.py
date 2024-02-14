from datetime import datetime, timedelta

def get_timestamp_before_x_days(days: int) -> int:
    '''
        Returns the timestamp before given days in milliseconds
    '''
    current_datetime = datetime.now()
    past_datetime = current_datetime - timedelta(days=days)
    return int(past_datetime.timestamp() * 1000)


def convert_time_to_timestamp(timestamp_str: str) -> int:
    # Convert string to datetime object
    datetime_obj = datetime.fromisoformat(timestamp_str[:-6].replace("T", " "))

    # Convert datetime object to Unix timestamp
    return int(datetime_obj.timestamp() * 1000)