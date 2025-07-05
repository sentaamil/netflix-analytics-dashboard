
USE netflix_db;

USE netflix_db;

-- 1. Count Movies vs TV Shows
SELECT type, COUNT(*) AS total FROM netflix GROUP BY type;

-- 2. Most Common Rating for Movies and TV Shows
SELECT type, rating, COUNT(*) AS rating_count
FROM netflix
GROUP BY type, rating
ORDER BY type, rating_count DESC;

-- 3. Movies Released in 2020
SELECT * FROM netflix WHERE release_year = 2020 AND type = 'Movie';

-- 4. Top 5 Countries with Most Content
SELECT country, COUNT(*) AS total
FROM netflix
WHERE country IS NOT NULL
GROUP BY country
ORDER BY total DESC
LIMIT 5;

-- 5. Longest Movie
SELECT * 
FROM netflix
WHERE type = 'Movie'
ORDER BY CAST(SUBSTRING_INDEX(duration, ' ', 1) AS UNSIGNED) DESC
LIMIT 1;

-- 6. Content Added in Last 5 Years
SELECT *
FROM netflix
WHERE STR_TO_DATE(date_added, '%M %d, %Y') >= CURDATE() - INTERVAL 5 YEAR;

-- 7. Content by Director ‘Rajiv Chilaka’
SELECT *
FROM netflix
WHERE FIND_IN_SET('Rajiv Chilaka', director) > 0;

-- 8. TV Shows with More Than 5 Seasons
SELECT *
FROM netflix
WHERE type = 'TV Show'
  AND CAST(SUBSTRING_INDEX(duration, ' ', 1) AS UNSIGNED) > 5;

-- 9. Number of Content Items per Genre
SELECT genre, COUNT(*) AS total
FROM (
  SELECT TRIM(SUBSTRING_INDEX(SUBSTRING_INDEX(listed_in, ',', numbers.n), ',', -1)) AS genre
  FROM netflix
  JOIN (
    SELECT 1 n UNION SELECT 2 UNION SELECT 3 UNION SELECT 4
  ) numbers
  ON CHAR_LENGTH(listed_in) - CHAR_LENGTH(REPLACE(listed_in, ',', '')) >= numbers.n - 1
) genres
GROUP BY genre;

-- 10. Top 5 Years with Highest % of Indian Content
SELECT 
  release_year,
  COUNT(*) AS total,
  ROUND(
    COUNT(*) * 100.0 / (SELECT COUNT(*) FROM netflix WHERE country = 'India'), 2
  ) AS percentage
FROM netflix
WHERE country = 'India'
GROUP BY release_year
ORDER BY percentage DESC
LIMIT 5;

-- 11. Movies that Are Documentaries
SELECT *
FROM netflix
WHERE listed_in LIKE '%Documentaries%' AND type = 'Movie';

-- 12. Content Without a Director
SELECT *
FROM netflix
WHERE director IS NULL OR director = '';

-- 13. Movies with ‘Salman Khan’ in Last 10 Years
SELECT *
FROM netflix
WHERE casts LIKE '%Salman Khan%'
  AND release_year >= YEAR(CURDATE()) - 10;

-- 14. Top 10 Actors in Indian Movies
SELECT actor, COUNT(*) AS appearances
FROM (
  SELECT TRIM(SUBSTRING_INDEX(SUBSTRING_INDEX(casts, ',', numbers.n), ',', -1)) AS actor
  FROM netflix
  JOIN (
    SELECT 1 n UNION SELECT 2 UNION SELECT 3 UNION SELECT 4 UNION SELECT 5
  ) numbers
  ON CHAR_LENGTH(casts) - CHAR_LENGTH(REPLACE(casts, ',', '')) >= numbers.n - 1
  WHERE country = 'India'
) AS actors
GROUP BY actor
ORDER BY appearances DESC
LIMIT 10;

-- 15. Good vs Bad Based on Description
SELECT 
  CASE 
    WHEN description LIKE '%kill%' OR description LIKE '%violence%' THEN 'Bad'
    ELSE 'Good'
  END AS category,
  type,
  COUNT(*) AS content_count
FROM netflix
GROUP BY category, type;


