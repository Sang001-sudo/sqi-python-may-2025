import requests
from bs4 import BeautifulSoup
from collections import Counter


url = "https://www.scrapethissite.com/pages/simple/"

try:
    res = requests.get(url)
except requests.RequestException as e:
    print(f"Somthing went wrong: {e}")
else:
    if res.status_code == 200:
        soup = BeautifulSoup(res.content, "html.parser")
        countries = [country.text.replace("\n", "").strip() for country in soup.select("h3.country-name")]
        capitals = [capital.text for capital in soup.select("div.country-info span.country-capital")]
        populations = [int(population.text) for population in soup.select("div.country-info span.country-population")]
        areas = [float(area.text) for area in soup.select("div.country-info span.country-area")]
        
        print(f"1. Total numbers of countries: {len(countries)}\n")
        
        
        max_population = max(populations)
        min_population = min(populations)
        
        country_with_max_population = " "
        country_with_min_population = " "
        
        for country, population in zip(countries, populations):
            if population >= max_population:
                country_with_max_population = country
                max_population = population
            
            if population <= min_population:
                country_with_min_population += f"{country}, "
                min_population = population
        
        print(f"2.\nThe country with the largest population: {country_with_max_population}")
        print(f"The country with the smallest population: {country_with_min_population}\n")
        
        average_population = sum(populations) / len(countries)
        
        print(f"3. The average population of all countries: {average_population}\n")
        
        country_population_density = []
        for population, area in zip(populations, areas):
            try:
                density = population / area
            except ZeroDivisionError:
                continue
            else:
                country_population_density.append(density)
         
        top_3_max_density = sorted(country_population_density)[max(0, len(country_population_density) - 3):]    
        top_3_countries_with_the_highest_density = []
        
        for country, density in zip(countries, country_population_density):
            if density in top_3_max_density:
                top_3_countries_with_the_highest_density.append(country)
        
        print(f"4. The top 3 countries with the highest density: {top_3_countries_with_the_highest_density}\n")
        
        capitalcity_startwith_letter_a = [{country: capital} for country, capital in zip(countries, capitals) if capital.startswith("A")]
        
        print(f"5. All countries whose capital city starts with the letter 'A': \n")
        pprint(capitalcity_startwith_letter_a)
        print("\n")
        
        
        
        countries_area_greater_than_1000000 = [country for country, area in zip(countries,areas) if area > 1000000]
        countries_area_less_than_500 = [country for country, area in zip(countries,areas) if area < 500]
        
        print(f"6. Countries with an area greater than 1,000,000 km²:\n{countries_area_greater_than_1000000}\n")
        print(f"7. Countries with an area less than 500 km²:\n{countries_area_less_than_500}\n")
        
        
        print(f"8. country that has 0 population:\n{country_with_min_population}")
        
        
    else:
        print(f"Error code: {res.status_code}")
        