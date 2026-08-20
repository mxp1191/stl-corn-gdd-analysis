SELECT
  CAST(_TABLE_SUFFIX AS INT64) AS year,
  SUM(
    GREATEST(
      (LEAST(max, 86.0) + GREATEST(min, 50.0)) / 2 - 50.0,
      0
    )
  ) AS total_season_gdd
FROM `bigquery-public-data.noaa_gsod.gsod*`
WHERE stn = '724340'
  AND wban = '13994'
  AND max < 999.9 AND min < 999.9
  AND mo IN ('04','05','06','07','08','09')
  AND _TABLE_SUFFIX BETWEEN '1994' AND '2023'
GROUP BY year
ORDER BY year
