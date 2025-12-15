import streamlit as st
import os

st.set_page_config(page_title="Music App", layout="centered")

st.title("🎵 My Music Player")

music_dir = "."
songs = [song for song in os.listdir(music_dir) if song.endswith(".mp3")]

search = st.text_input("🔍 Search Song")

filtered_songs = [s for s in songs if search.lower() in s.lower()]

playlist = st.multiselect("🎶 Create Playlist", filtered_songs)

if playlist:
    song = st.selectbox("▶ Select Song to Play", playlist)
    audio_file = open(song, "rb")
    st.audio(audio_file.read(), format="audio/mp3")
