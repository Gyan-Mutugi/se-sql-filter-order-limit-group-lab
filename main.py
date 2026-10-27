
import pandas as pd
import sqlite3

# STEP 1: Connect to the databases
conn1 = sqlite3.connect("planets.db")
conn2 = sqlite3.connect("dogs.db")
conn3 = sqlite3.connect("babe_ruth.db")


# STEP 1: Planets with zero moons
df_no_moons = pd.read_sql("""
    SELECT *
    FROM planets
    WHERE num_of_moons = 0;
""", conn1)


# STEP 2: Planets with names containing exactly 7 letters
df_name_seven = pd.read_sql("""
    SELECT name, mass
    FROM planets
    WHERE LENGTH(name) = 7;
""", conn1)


# STEP 3: Planets with mass less than or equal to 1.00
df_mass = pd.read_sql("""
    SELECT name, mass
    FROM planets
    WHERE mass <= 1.00;
""", conn1)


# STEP 4: Planets with at least one moon and mass below 1.00
df_mass_moon = pd.read_sql("""
    SELECT *
    FROM planets
    WHERE num_of_moons >= 1
      AND mass < 1.00;
""", conn1)


# STEP 5: Planets with color containing "blue"
df_blue = pd.read_sql("""
    SELECT name, color
    FROM planets
    WHERE color LIKE '%blue%';
""", conn1)


# STEP 6: Hungry dogs, youngest to oldest
df_hungry = pd.read_sql("""
    SELECT name, age, breed
    FROM dogs
    WHERE hungry = 1
    ORDER BY age ASC;
""", conn2)

# Convert missing names to Python None
df_hungry = df_hungry.astype(object).where(
    pd.notna(df_hungry), None
)

# STEP 7: Hungry dogs aged 2 to 7, alphabetically
# STEP 7: Hungry dogs aged 2 to 7, alphabetically
df_hungry_ages = pd.read_sql("""
    SELECT name, age, hungry
    FROM dogs
    WHERE hungry = 1
      AND age BETWEEN 2 AND 7
    ORDER BY name ASC;
""", conn2)

# STEP 8: Four oldest dogs
df_4_oldest = pd.read_sql("""
    SELECT name, age, breed
    FROM dogs
    ORDER BY age DESC
    LIMIT 4;
""", conn2)

# STEP 9: Total number of years Babe Ruth played
df_ruth_years = pd.read_sql("""
    SELECT COUNT(DISTINCT year) AS total_years
    FROM babe_ruth_stats;
""", conn3)

# STEP 10: Total career home runs
df_hr_total = pd.read_sql("""
    SELECT SUM(HR) AS total_home_runs
    FROM babe_ruth_stats;
""", conn3)


# STEP 11: Number of years played on each team
df_teams_years = pd.read_sql("""
    SELECT team, COUNT(DISTINCT year) AS number_years
    FROM babe_ruth_stats
    GROUP BY team;
""", conn3)


# STEP 12: Teams with average at-bats over 200
df_at_bats = pd.read_sql("""
    SELECT team, AVG(at_bats) AS average_at_bats
    FROM babe_ruth_stats
    GROUP BY team
    HAVING AVG(at_bats) > 200;
""", conn3)