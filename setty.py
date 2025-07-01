# ==============================================EXERCISES==============================================
# 🛒 1. Grocery Store – Find Common Items in Carts
# Exercise:
# You have two shopping carts. Each contains a list of items. Use sets to find:

# Items both people are buying # eggs, butter

# Items only one of them is buying   # milk, bread, cheese, yoghurt

# All items either of them is buying # milk, bread, eggs, butter, cheese, yoghurt

cart1 = ["milk", "bread", "eggs", "butter"]
cart2 = ["eggs", "butter", "cheese", "yogurt"]


set1 = set(cart1)
set2 = set(cart2)

common_items = set1.intersection(set2)

unique_items = set1.symmetric_difference(set2)

all_items = set1.union(set2)
print("Common items:", common_items)  
print("Unique items:", unique_items)  
print("All items:", all_items)


# 🎟️ 2. Movie Club – Count Unique Movies Watched
# Exercise:
# Three friends watched movies over the weekend. Each of them lists the movies they saw. Use sets to find out:

# How many unique movies were watched in total.

# alice = {"Inception", "Titanic", "Joker"}
# bob = {"Joker", "Interstellar", "Inception"}
# carol = {"Avatar", "Titanic", "Joker"}

# Answer: "Inception", "Titanic", "Joker", "Interstellar", "Avatar"

alice = {"Inception", "Titanic", "Joker"}
bob = {"Joker", "Interstellar", "Inception"}
carol = {"Avatar", "Titanic", "Joker"}


unique_movies = alice.union(bob, carol)
print("Unique movies watched:", unique_movies)

# 🧑‍🤝‍🧑 3. Party Invite List – Avoid Duplicates
# Exercise:
# You’re creating a guest list. Some names were added twice by mistake. Use a set to fix this.

# guest_list = ["Alice", "Bob", "Charlie", "Alice", "Bob", "Diana"]

guest_list = ["Alice", "Bob", "Charlie", "Alice", "Bob", "Diana"]
unique_guests = set(guest_list)
print("unique guest", unique_guests)

# 🏫 4. Students in Clubs – Who’s in Both?
# Exercise:
# In a school, some students are in the science club, and some are in the music club. Find students who are in both.

science_club = {"John", "Mia", "Liam", "Olivia"}
music_club = {"Emma", "Liam", "Noah", "Olivia"}


both_clubs = science_club.intersection(music_club)
print("Students in both clubs:", both_clubs)
# ==============================================EXERCISES==============================================