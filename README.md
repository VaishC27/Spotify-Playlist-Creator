# Time-Traveling Spotify Playlist Creator

Ever wanted to dive back into the musical abyss of the past? Well, this Python script allows you to create a Spotify playlist from the Billboard Hot 100 chart of any given date. It's like a time machine, but without all the paradoxes and catastrophic consequences. 

## Features

- **Web Scraping**: Fetches the Billboard Hot 100 songs for a specified date.
- **Spotify Integration**: Creates a private playlist on your Spotify account with those songs.
- **Error Handling**: Skips songs that aren't found on Spotify (because some hits are just too underground, even for Spotify).

## Requirements

- Python 3.7+
- Spotipy library
- BeautifulSoup library
- Requests library
- A Spotify Developer account (because we're not hacking Spotify... yet)

## Installation

1. **Clone the repo**

```bash
git clone https://github.com/yourusername/spotify-time-travel-playlist.git
cd spotify-time-travel-playlist

