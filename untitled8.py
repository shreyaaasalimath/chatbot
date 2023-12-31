# -*- coding: utf-8 -*-
"""Untitled8.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10ZhPGzqpHYnqUlKPsxdClTvQTDeSSM4U
"""

import requests
from bs4 import BeautifulSoup
import re

# Define the URL to scrape
url = "https://brainlox.com/courses/category/technical"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract course information
    course_data = []

    # Find course elements in the HTML (customize as per the website structure)
    courses = soup.find_all("div", class_="courses-content")

    for course in courses:
        title = course.find("h3").text.strip()
        description = course.find("p").text.strip()
        course_url = course.find("a")["href"].strip()

        # Preprocess the data (remove HTML tags, extra spaces, special characters, etc.)
        title = re.sub(r'\s+', ' ', title)  # Remove extra spaces
        description = re.sub(r'\s+', ' ', description)  # Remove extra spaces
        description = re.sub(r'<[^>]*>', '', description)  # Remove HTML tags

        # Add the cleaned data to the list
        course_data.append({
            "title": title,
            "description": description,
            "url": course_url
        })

    # Print the scraped and preprocessed data
    for course in course_data:
        print("Title:", course["title"])
        print("Description:", course["description"])
        print("URL:", course["url"])
        print("\n")

else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)

# Initialize lists to store preprocessed data
preprocessed_titles = []
preprocessed_descriptions = []
preprocessed_urls = []

# Iterate through the scraped data and preprocess it
for title, description, url in zip(title,description, course_url):
    # Clean and preprocess the title
    preprocessed_title = title.strip().lower()

    # Clean and preprocess the description
    preprocessed_description = description.strip().lower()

    # Preserve the URL as is
    preprocessed_url = url

    # Append the preprocessed data to the respective lists
    preprocessed_titles.append(preprocessed_title)
    preprocessed_descriptions.append(preprocessed_description)
    preprocessed_urls.append(preprocessed_url)

# Now, you have preprocessed course information in the lists preprocessed_titles, preprocessed_descriptions, and preprocessed_urls.

# Sample course data (replace with your actual dataset)
course_data = [
    {"title": "Course A", "description": "Learn web development with HTML and CSS."},
    {"title": "Course B", "description": "Master Java programming for web applications."},
    {"title": "Course C", "description": "Introduction to machine learning and AI."},
]

# Function to recommend courses based on keywords
def recommend_courses(keywords):
    recommended_courses = []
    for course in course_data:
        course_description = course["description"].lower()
        if all(keyword.lower() in course_description for keyword in keywords):
            recommended_courses.append(course)
    return recommended_courses

# Chatbot interaction loop
while True:
    user_input = input("User: ")

    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Chatbot: Goodbye!")
        break

    user_keywords = user_input.split()  # Split user input into keywords
    recommended_courses = recommend_courses(user_keywords)

    if recommended_courses:
        print("Chatbot: I recommend the following courses:")
        for recommended_course in recommended_courses:
            print(f"Title: {recommended_course['title']}")
            print(f"Description: {recommended_course['description']}\n")
    else:
        print("Chatbot: I couldn't find any relevant courses for your input. Please ask something else.")

!python3 -m venv myenv
!source myenv/bin/activate
!pip install azure-cli
!az --version

import sys
print(sys.version)