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
```

2. **Install dependencies**

```bash
pip install spotipy beautifulsoup4 requests
```

3. **Set up Spotify API credentials**

- Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications) and create an application.
- Note down your `CLIENT_ID` and `CLIENT_SECRET`.

4. **Update your script with your Spotify credentials**

Open `main.py` and replace the `CLIENT_ID` and `CLIENT_SECRET` with your own.

```python
CLIENT_ID = "your_client_id_here"
CLIENT_SECRET = "your_client_secret_here"
```

## Usage

1. **Run the script**

```bash
python main.py
```

2. **Input the desired date**

When prompted, enter the date you want to travel to in the format `YYYY-MM-DD`. 

3. **Enjoy your playlist**

The script will scrape the Billboard Hot 100 for that date, search Spotify for the songs, and create a new playlist in your account. If a song isn't found, it'll skip it because life's too short for unavailable tracks.

## Example

```
Which year do you want to travel to? Type the date in this format YYYY-MM-DD: 1995-08-12
```

If all goes well, you should see a new playlist in your Spotify account named `1995-08-12 Billboard 100`.

## Troubleshooting

- **KeyError: 'user'**: Make sure you're accessing the playlist ID correctly.
- **Authentication errors**: Double-check your Spotify credentials and ensure your redirect URI is properly set.
- **Missing songs**: Some songs might not be available on Spotify. The script will notify you and skip them.

## Disclaimer

This script is for educational purposes only. If you use it to create a playlist of Nickelback songs, that's on you. 

## Contributing

Feel free to fork this repo, make some improvements, and submit a pull request. Just don't break the space-time continuum.

## License

[MIT License](LICENSE)

---

Happy time-traveling! And remember, with great power comes great Spotify playlists.
```

This README file should provide clear instructions and a bit of humor to make the setup process more enjoyable. Feel free to customize it further according to your preferences!

