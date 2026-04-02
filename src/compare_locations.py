import random

def create_bad_coordinates(df):
    random.seed(42)

    bad_lat = []
    bad_lon = []

    for i, row in df.iterrows():
        lat = row["lat"]
        lon = row["lon"]

        if random.random() < 0.3:
            lat = lat + random.uniform(1, 5)
            lon = lon + random.uniform(1, 5)
        elif random.random() < 0.5:
            lat = lat + random.uniform(0.01, 0.1)
            lon = lon + random.uniform(0.01, 0.1)

        bad_lat.append(lat)
        bad_lon.append(lon)

    df["bad_lat"] = bad_lat
    df["bad_lon"] = bad_lon

    return df

from geopy.distance import geodesic

def calculate_distance(df):
    distances = []

    for i, row in df.iterrows():
        real_point = (row["lat"], row["lon"])
        bad_point = (row["bad_lat"], row["bad_lon"])

        distance = geodesic(real_point, bad_point).miles
        distances.append(distance)

    df["distance_miles"] = distances

    return df

def flag_bad_geocodes(df):
    flags = []

    for i, row in df.iterrows():
        distance = row["distance_miles"]

        if distance <= 1:
            flags.append("OK")
        elif distance <= 10:
            flags.append("Review")
        else:
            flags.append("Bad")

    df["geocode_flag"] = flags

    return df