import streamlit as st
import pandas as pd
import datetime
import csv
import os

MOOD_FILE = "mood_log.csv"

def load_mood_data():
    if not os.path.exists(MOOD_FILE):
        return pd.DataFrame(columns=["Date", "Mood"])
    with open(MOOD_FILE, 'r') as f:
        reader = csv.reader(f)
        headers = next(reader, None)
    
    if headers is None or headers != ["Date", "Mood"]:
        # If no headers or incorrect headers, recreate the file
        os.remove(MOOD_FILE)
        return pd.DataFrame(columns=["Date", "Mood"])
    
    return pd.read_csv(MOOD_FILE)


def save_mood_data(date, mood):
    with open(MOOD_FILE, "a") as file:
        writer = csv.writer(file)
        if file.tell() == 0:
            writer.writerow(["Date", "Mood"])
        writer.writerow([date, mood])


st.title("Mood Tracker")

today = datetime.date.today()

st.subheader("How are you feeling today?")

mood = st.selectbox("Select Your Mood", ["Happy", "Sad", "Neutral", "Angry", "Surprised"])

if st.button("Log Mood"):

    save_mood_data(today, mood)
    st.success("Mood Logged Successfully!")
    
    st.subheader("Your Mood Log:")
    mood_data = load_mood_data()
    st.dataframe(mood_data)

data = load_mood_data()

if not data.empty:
    st.subheader("Mood Analysis")

    data["Date"] = pd.to_datetime(data["Date"])

    mood_counts = data.groupby("Mood").count()["Date"]

    st.bar_chart(mood_counts)