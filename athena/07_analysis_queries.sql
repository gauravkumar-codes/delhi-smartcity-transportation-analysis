-- =====================================================
-- QUERY 1: Traffic Density Analysis by Location and Time
-- =====================================================

SELECT
    location,
    time,
    ROUND(AVG(traffic_density_index), 2) AS avg_traffic_density
FROM delhi_transport_analysis_db.new_master_dataset
GROUP BY
    location,
    time
ORDER BY
    avg_traffic_density DESC;

-- =====================================================
-- QUERY 2: Distribution of Traffic Accidents by Severity
-- =====================================================

SELECT
    accident_severity,
    COUNT(accident_id) AS total_accidents
FROM delhi_transport_analysis_db.new_master_dataset
WHERE accident_id IS NOT NULL
GROUP BY
    accident_severity
ORDER BY
    total_accidents DESC;

-- =====================================================
-- QUERY 3: Correlation Between Vehicle Volume and AQI
-- =====================================================

SELECT
    location,
    ROUND(AVG(vehicle_count), 2) AS avg_vehicle_count,
    ROUND(AVG(aqi), 2) AS avg_aqi
FROM delhi_transport_analysis_db.new_master_dataset
GROUP BY
    location
ORDER BY
    avg_vehicle_count DESC;

-- =====================================================
-- QUERY 4: Traffic Accident Hotspots by Location
-- =====================================================

SELECT
    location,
    COUNT(accident_id) AS total_accidents,
    SUM(injured) AS total_injured,
    SUM(killed) AS total_killed
FROM delhi_transport_analysis_db.new_master_dataset
WHERE accident_id IS NOT NULL
GROUP BY
    location
ORDER BY
    total_accidents DESC;

-- =====================================================
-- QUERY 5: Vehicle Volume Analysis by Time of Day
-- =====================================================

SELECT
    time,
    SUM(vehicle_count) AS total_vehicle_volume,
    ROUND(AVG(vehicle_count), 2) AS average_vehicle_volume
FROM delhi_transport_analysis_db.new_master_dataset
GROUP BY
    time
ORDER BY
    total_vehicle_volume DESC;
