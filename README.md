## Geocode Validation Project
### Overview

This project identifies inaccurate geographic coordinates by comparing stored geocodes against expected location data and measuring spatial error. It is designed to simulate real-world data quality issues that impact routing, logistics, and location-based decision making.

### Objective

To detect and flag incorrect geocodes using distance-based validation and visualize discrepancies on an interactive map.

### Dataset
US cities dataset (Kaggle) https://www.kaggle.com/datasets/mohamedyabdelaziz/us-cities
Includes: city, state, latitude, longitude, ZIP code
### Methodology
- Load location dataset
- Generate simulated incorrect geocodes
- Calculate distance between correct and stored coordinates
- Classify records into:
OK,
Review,
Bad
- Export results to CSV
- Visualize discrepancies using an interactive map
### Technologies Used
- python
- pandas
- geopy
- folium
### Output

#### CSV Report

Contains calculated distances and classification flags

#### Interactive Map

- Blue = correct location
- Green = accurate
- Orange = needs review
- Red = incorrect
Lines show deviation between expected and actual coordinates
### Example Use Case

This workflow can be applied to:

- Route optimization
- Territory alignment
- Address validation
- Data quality monitoring in logistics and operations
### Key Insight

Small errors in geocodes can significantly impact routing efficiency and operational decision-making. This project demonstrates a scalable approach to identifying and prioritizing these discrepancies.

### Future Improvements
- Integrate real address geocoding APIs
- Add clustering for route optimization
- Build dashboard for monitoring geocode quality
- Automate data validation pipeline
