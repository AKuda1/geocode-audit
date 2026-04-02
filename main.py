from src.load_data import load_data
from src.compare_locations import create_bad_coordinates, calculate_distance, flag_bad_geocodes
from src.visualize import create_map


def main():

    df = load_data("data/raw/locations.csv")

    df = create_bad_coordinates(df)

    # Calculate distance between real vs bad coords
    df = calculate_distance(df)

    # Flagging results
    df = flag_bad_geocodes(df)

    df.to_csv("outputs/geocode_results.csv", index=False)

    print("Finished geocode check")
    print("Results saved to outputs/geocode_results.csv")

    print("\nSummary of geocode flags:")
    print(df["geocode_flag"].value_counts())

    m = create_map(df)
    m.save("outputs/geocode_map.html")

    print("Map saved to outputs/geocode_map.html")

    print("\nSample data:")
    print(df.head())


if __name__ == "__main__":
    main()