from src.load_data import load_data
from src.compare_locations import create_bad_coordinates, calculate_distance, flag_bad_geocodes
from src.visualize import create_map


def main():
    # Load data
    df = load_data("data/raw/locations.csv")

    # Create simulated bad coordinates
    df = create_bad_coordinates(df)

    # Calculate distance between real vs bad coordinates
    df = calculate_distance(df)

    # Flag the results
    df = flag_bad_geocodes(df)

    # Save results to CSV
    df.to_csv("outputs/geocode_results.csv", index=False)

    print("Finished geocode check")
    print("Results saved to outputs/geocode_results.csv")

    # Print summary
    print("\nSummary of geocode flags:")
    print(df["geocode_flag"].value_counts())

    # Create and save map
    m = create_map(df)
    m.save("outputs/geocode_map.html")

    print("Map saved to outputs/geocode_map.html")

    # Preview data
    print("\nSample data:")
    print(df.head())


if __name__ == "__main__":
    main()