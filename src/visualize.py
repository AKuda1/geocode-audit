import folium


def create_map(df):
    center_lat = df["lat"].mean()
    center_lon = df["lon"].mean()

    m = folium.Map(location=[center_lat, center_lon], zoom_start=5)

    for i, row in df.iterrows():
        real_point = (row["lat"], row["lon"])
        bad_point = (row["bad_lat"], row["bad_lon"])
        flag = row["geocode_flag"]

        if flag == "OK":
            color = "green"
        elif flag == "Review":
            color = "orange"
        else:
            color = "red"

        popup_text = (
            f"City: {row['city']}<br>"
            f"State: {row['state']}<br>"
            f"Distance (miles): {row['distance_miles']:.2f}<br>"
            f"Flag: {flag}"
        )

        folium.CircleMarker(
            location=real_point,
            radius=4,
            color="blue",
            fill=True,
            fill_opacity=0.8,
            popup="Correct location"
        ).add_to(m)

        folium.CircleMarker(
            location=bad_point,
            radius=5,
            color=color,
            fill=True,
            fill_opacity=0.8,
            popup=popup_text
        ).add_to(m)

        folium.PolyLine(
            locations=[real_point, bad_point],
            color=color,
            weight=2,
            opacity=0.7
        ).add_to(m)

    return m