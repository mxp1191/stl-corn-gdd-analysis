import functions_framework
from google.cloud import bigquery

@functions_framework.http
def refresh_corn_gdd(request):
    client = bigquery.Client()

    query = """
    SELECT
      CAST(_TABLE_SUFFIX AS INT64) AS year,
      SUM(
        GREATEST(
          (LEAST(max, 86.0) + GREATEST(min, 50.0)) / 2 - 50.0,
          0
        )
      ) AS total_season_gdd,
      SUM(prcp) AS total_precip_inches,
      CASE
        WHEN SUM(
          GREATEST(
            (LEAST(max, 86.0) + GREATEST(min, 50.0)) / 2 - 50.0,
            0
          )
        ) >= 2700 THEN TRUE
        ELSE FALSE
      END AS reached_maturity_threshold
    FROM `bigquery-public-data.noaa_gsod.gsod*`
    WHERE stn = '724340'
      AND wban = '13994'
      AND max < 999.9 AND min < 999.9
      AND prcp < 99.9
      AND mo IN ('04','05','06','07','08','09')
      AND _TABLE_SUFFIX BETWEEN '1994' AND '2023'
    GROUP BY year
    ORDER BY year
    """

    job_config = bigquery.QueryJobConfig(
        destination="project-6fff1571-3c36-42ca-889.corn_analysis.corn_gdd_results",
        write_disposition="WRITE_TRUNCATE"
    )

    query_job = client.query(query, job_config=job_config)
    query_job.result()

    return "Refresh complete."
