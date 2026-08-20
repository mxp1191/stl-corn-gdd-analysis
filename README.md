# stl-corn-gdd-analysis

# St. Louis Corn-Season Growing Degree Days

Pulls 30 years (1994–2023) of daily weather data for St. Louis Lambert 
International Airport from NOAA's public GSOD dataset in Google BigQuery, 
and calculates corn-specific Growing Degree Days (GDD) using the standard 
86/50 method commonly used in agricultural extension guidance.

## What it does
- Queries NOAA's public weather dataset (`bigquery-public-data.noaa_gsod`)
- Calculates daily corn GDD, capped at a 50°F floor and 86°F ceiling
- Aggregates to total seasonal GDD per year across the corn growing season (April–September)
- Visualized as a 30-year trend line in Looker Studio

## Files
- `corn_gdd_query.sql` — the core BigQuery SQL query
- `.github/workflows/check-sql.yml` — automated check confirming the SQL file is present and structurally valid on every push

## Notes
- Growing season window (April–September) is a proxy; a more precise version would start GDD accumulation from an actual planting date.
