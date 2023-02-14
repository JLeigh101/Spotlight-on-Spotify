# Project-1
NU Bootcamp Project 1

Goal:
Analyze the popularity of various artists and songs using the Spotify API and Spotify’s Chart data
-What makes a song popular? Are there certain characteristics that correlate with it being popular?
-Are there any correlations between the audio features of the most popular songs?

Terms to Know:
Spotify keeps track of several different audio features for every song in their catalog including: popularity, tempo, energy, loudness, speechiness, danceability and valence
-URI: Unique (Uniform) Resource Indicator that you can enter in the Spotify Desktop client’s search box to locate an artist, album, or track. 
-Popularity: Measure of a track’s popularity on a scale of 0-100, where 100 is most popular. Calculated based on total number of plays and how recent those plays are. 
-Tempo: An estimate of the track’s beats per minute
-Energy: A value between 0.0-1.0 that measures how the intenseness and activity of the track
-Loudness:  The calculated loudness of track in decibels. The value is an average of the loudness over the entire track.
-Speechiness: A measure of the presence of spoken words in a track ranging from 0.0-1.0. The closer a track is to 1.0, the more the track is exclusively speech. 
-Danceability: A measure of how suitable a track is for dancing based on various song elements. The scale is from 0.0-1.0
-Valence: A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track. Tracks with high valence sound more positive (e.g. happy, cheerful, euphoric), while tracks with low valence sound more negative (e.g. sad, depressed, angry).

Scope:
Using Spotify’s web API as well as the SpotiPy library, we analyzed the top ranked songs from several different artists including:
-Beyonce
-SZA
-Bad Bunny
-Adele
-Morgan Wallen

Process Steps:
-Pull the song data from Spotify API using SpotiPy library
-Wrangle each artists’ data into a dataframe (beydata_df, szadata_df, etc…)
-Merge these dataframes to get a master dataframe containing all of the song data
-Order the master dataframe based on the ‘popularity’ score for each song
-Create scatter plots for the master dataframe to get an idea of the “meta” trends
-Break the master dataframe into tiers based on popularity rank and perform the same analysis
-We broke the dataframe up into 4 roughly equal tiers using the following scores:
    -Top Tier: ‘popularity’ >= 86
    -Second Tier: 80 <= ‘popularity’ < 86
    -Third Tier: 75 <= ‘popularity’ < 80
    -Bottom Tier: 0 <= ‘popularity’ < 75

Limitations:
-We looked at a limited number of artists
-We only looked at the top 9 songs from those artists
-We only looked at a limited number of genres 
-These results may be different based on the genre (i.e. grunge music might have low valence and high popularity?)
-‘Popularity’, as defined by spotify, has a time component to it - it’s a mixture of the total number of plays and how recently those plays occurred. This skews ‘popularity’ towards newer music, while older songs could have a disadvantage if they are no longer being played as much as they once were at their peak. 
    -We could take a look at the same song datasets and sort them by raw number of plays to get a clearer perspective of a songs “true” popularity. Comparing spotify’s ‘popularity’ measurement to it’s raw number of plays could be enlightening and provide a baseline to help contextualize the song’s popularity

Future Work:
-Looking at data from different markets and making comparisons between countries.
-Analyzing larger set of data (more artists, more charts, etc…)
    -We have to manually input an artist’s URI into the initial code in order to pull their song data. If we created a list of artist URIs and cycled through them programmatically, we could analyze a larger dataset without as much manual labor (aka typing)

