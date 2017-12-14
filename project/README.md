# What Makes Songs Popular?
[CS-401 ADA](http://isa.epfl.ch/imoniteur_ISAP/!itffichecours.htm?ww_i_matiere=2046272383&ww_x_anneeAcad=2017-2018&ww_i_section=249847&ww_i_niveau=&ww_c_langue=en) - [EPFL](http://epfl.ch)
> Project of Applied Data Analysis Course - 2017/2018

Project Web page: [Web for Songs-Project](https://goo.gl/VFLoC5)

# Abstract
> Music is a moral law. It gives soul to the universe, wings to the mind, flight to the imagination, and charm and gaiety to life and to everything. _-Plato_

This project aims to analyze the trends towards songs' popularity in recent years. We want to define metrics that can lead to prediction of songs' popularity in billboard. To achive this, we use [Million Song Dataset](https://labrosa.ee.columbia.edu/millionsong/) that has collection of audio features and metadata of popular songs.

Through this project, we would like to show how people tend to listen to songs, e.g. by considering the singers/artist, genres, lyrics. Then we also want to know whether herding bias happens, i.e. somebody listening songs from same artist, and we eager to observe frequent words and occurences of impolite words (slang words) across popular songs' lyrics.

The project's main goal is to prove how society reacts to songs' quality over time. We expect to see the challenges of music popularity towards time.

# Project Structure
------------

    ├── main.ipynb                           : The main notebook for the our songs project, accumulating all answers for research questions (Question 1-3).
    ├── README.md                            : The README guideline and explanation for our work.
    ├── 00raw_datasets_observation.ipynb     : Notebook contains initial observation for Million Songs datasets.
    ├── 00raw_datasets_preprocessings.ipynb  : Notebook contains initial preprocessing for raw datasets files.
    ├── Part1.ipynb                          : (Specific) Answers and explanations for Question block 1.
    ├── Part2.ipynb                          : (Specific) Answers and explanations for Question block 2.
    ├── Part3.ipynb                          : (Specific) Answers and explanations for Question block 3.
    |
    ├── datasets
    │   ├── pickle_files                     : Directory containing files of raw datasets, with pickle format & reduced in size.
    │   ├── processed_pickle_files           : Directory containing processed (reduced & filtered) datasets.
    │   ├── raw_files                        : Directory containing raw datasets files (h5, csv, txt formats).
    │
    ├── maps                                 : Directory containing maps for certain results in html format.
    |
    ├── mock-scripts                         : Directory containing initial scripts for preliminary analysis & data scrapping.
    │
    ├── pictures                             : Directory containing images for certain results.
    │
    ├── report                               : Directory containing templates for final report.
    │
    ├── scripts                              : Directory containing helper scripts for our main.ipynb notebook.


--------

# Dependencies 
In order to reuse our work, there are two dependencies aside from [Conda with Python 3.6](https://www.anaconda.com/download/).
1. Pylast
[Pylast](https://github.com/pylast/pylast) is a Python interface to Last.fm API. To install via pip:
    pip install pylast
2. Folium
[Folium](http://python-visualization.github.io/folium/docs-master/) is awesome library to draw maps in Python. To install via pip:
    pip install folium

# Research questions
Our questions are decomposed into 3 blocks of questions:
## Question Block 1: What could make songs popular

### Q1.1 What is the characteristic/metrics of popular songs?
Songs popularity is defined as "song_hotttnesss" and we want to figure out what attributes of a song that affect song's popularity most.
#### Design of experiment:
* Load the dataset into dataframe & sampling into popular and unpopular songs data.
* Data splitting, training and fitting with RandomForestClassifier
* Show confusion matrix.
* Observe and conclude what are significant attributes/features of popular songs.

### Q1.2 How to distinguish popular and unpopular songs?
Are we comparing data with same distribution of features? If no, we want to emphasize once again, the attributes of popular songs by performing exploratory data analysis.
#### Design of experiment:
* Load the dataset into dataframe & sampling into popular and unpopular songs data.
* Compare and observe the discrete features of popular and unpopular songs.
* Draw map to portray songs distribution accross the world.
* Compare and observe the continuous features of popular and unpopular songs.
* Comment and conclude the exploratory data analysis.

### Q1.3 Can we see the trend in music industry from years to years?
We carefully look into popular genre of popular songs.
#### Design of experiment:
* Load the dataset into dataframe & sampling into popular songs data only.
* Perform join of dataset (sampled msd with msd\_artist_term)
* Plot the top 10 popular genres from 2001 until 2010.
* Observe and comment.

## Question Block 2: What could make singers popular

### Q2.1 Does the herding bias for hearing songs really happen in our society?
Herding bias means somebody would listen to several songs sung by specific singers. When we have a postive impression on the first song we hear from this singer, it's possible that we want to listen to other songs from this singer. And usually it's more likely we would love other songs from him/her, no matter whether he/she is famous.
#### Design of experiment
* Load the dataset into dataframe & sampling
* Quick observation of the dataset
* Map Song_ID to the singer names and observe whether there're songs from the same singer
* Define a way to measure the level of herding bias of the user
* Visualize the level of herding bias
* Observation & Comment
### Q2.2 Do people tend to listen to famous singers rather than the songs themselves?
In other words, we want to see whether the songs sung by popular singers are usually popular.
#### Design of experiment
* Load the dataset into dataframe & data wrangling
* Choose several popular/unpopular singers and extract their songs
* Compare the song_hotttnesss of songs from popular singers and unpopular singers
* Visualize to show the difference of song_hotttnesss between popular singers and unpopular singers
* Observation & Comment 

### Q2.3 Whether the first song of the singer matters for his/her career
In this problem, we also focus on popular singers. We want to see whether the first song of this singer has some correlation with his/her career. To be more precise, we want to see whether the first song of the popular singer is usually popular, and the first songs opens his/her career. In real world, we could really find this phenomenon, for example, the korean singer psy became famous with the song 'gangnam style'.
#### Design of experiment:
* Load the dataset into dataframe
* Data wrangling & Choose several popular/unpopular singers and extract their songs in the first year
* See the meidan of song_hotttnesss in the 1st year of the singers
* Visualize to show the correlation
* Observation & Comment 

## Question Block 3: Quality of popular songs
### Q3.1 Do people care more about lyrics?
We want to see what are most frequent words popular songs.
#### Design of experiment:
* Load the datasets into dataframes.
* Remove stopwords from mxm_lyrics dataset.
* Merge msd\_data with mxm_lyrics
* Plot the overall most frequent words regardless of songs popularity.
* Plot the overall most frequent words across popular songs.
* Plot the overall most frequent words across unpopular songs.

### Q3.2 Can we measure the quality and popularity of a song from its lyrics? Do the popular songs have the good quality of lyrics from literacy view points?
Quality of lyrics in literacy point of view can be observed by measuring the occurences of "slang words".
#### Design of experiment:
* Load list of bad/slang words (obtained from google).
* Count the average ratio of bad/slang words in popular and unpopular songs.
* Observe and comment.
* Justify the result by comparing words density of popular and unpopular songs.

# Data Acqusition & Initial Data Preprocessing
The raw datasets provided by ADA TAs are 280 GB in size and have h5 (HDF) format. The datasets are spreaded in A-Z directories and come along with additional datasets (/AdditionalFiles). From all provided dataset files, we utilize 12 different datasets and store them as 12 pickle files. We decide to use pickle format to boost loading time for later data loading process in notebook.

> Check our notebook for [initial processing of raw files](https://github.com/sanadhis/ITT-ADA-2017/blob/master/project/00raw_datasets_preprocessings.ipynb) and [datasets brief description](https://github.com/sanadhis/ITT-ADA-2017/blob/master/project/00raw_datasets_observation.ipynb) to have more clear insight for our initial data preprocessing methods.

**Note that the datasets' pickle files are relatively big in term of size, thus we do not include them in our repository.**

# Dataset
1. [The Million Song Dataset](https://labrosa.ee.columbia.edu/millionsong/) :
The main dataset, contains one million songs metadata with each song has 52 attributes.
Important fields:
* `song_hotttnesss`: the popularity of a song measured with value of between 0 - 1.
* `track_id`: act as primary key for all songs in dataset.

2. [The musiXmatch Dataset](https://labrosa.ee.columbia.edu/millionsong/musixmatch) :

Contains the lyrics from a subset of the original dataset songs. For every track in this dataset the lyrics are represented using a bag-of-words format obtained by stemming. This will allow us to address the third research question in particular.

FORMAT:

      Single .txt file: mxm_dataset_train.txt
      #   - comment, to ignore
      %   - list of top words, comma-separated
          - normal line, contains track_id, mxm track id,
            then word count for each of the top words, comma-separated
            word count is in sparse format -> ...,<word idx>:<cnt>,...
            <word idx> starts at 1 (not zero!)

3. [The Last.fm Dataset](https://labrosa.ee.columbia.edu/millionsong/lastfm) :
For every songs it gives both a list of tags that defines the song (genre, instruments...) and a list of similar songs alongside the value of the similarity measure that was used. The dataset will come in quiet handy when checking for plagiarism or high ressemblance.

FORMAT:

      Several .json files in different directory (A-Z)
      Keys in .json files:
      'tags'       - style of the song such as rock, hard rock
      'artist'     - name of the singer
      'title'      - name of the song
      'timestamps' - date
      'similar'    - similarity measure of songs, range from 0 to 1 
      
4. [The Echo Nest Taste Profile Subset](https://labrosa.ee.columbia.edu/millionsong/tasteprofile) :
This represents the profiles of real users in which we can find for every profile the play count for some song in the original dataset. It covers about a third of the tracks available in the million songs dataset and will give us a good representation of the musical trend.

FORMAT:

      Single .txt file: train_triplets.txt
      user   - ID of users
      song   - the song they listen
      count  - how many times the user listens to this song

# Issue with Dataset
* For our main datasets, which is "msd_songs", almost ~50% songs do not have "songs\_hotttnesss". This makes us utilize only ~50% of datasets (at maximum).

# A list of internal milestones up until milestone 3
|Week #|Targets|
|---|---|
|Week 1<br>**01.11.2017 - 07.11.2017**|<ul><li>Getting started with cluster processing (spark, hadoop).</li><li> Initial data processing: Reading data, cleaning and wrangling, merging dataset.</li></ul>|
|Week 2<br>**07.11.2017 - 14.11.2017**|<ul><li>Begin to address research questions.</li><li> Initial analysis of data, finding correlations.</li></ul>|
|Week 3<br>**14.11.2017 - 21.11.2017**|<ul><li>Initial mockup for python scripts and notebooks.</li><li> Visualize data in several ways: charts, maps, images, and so on.</li></ul>|
|Week 4<br>**21.11.2017 - 28.11.2017**|<ul><li>Analyze the temporary results.</li><li> Review works and ensure completion for milestone 2.</li></ul>|
|Week 5<br>**28.11.2017 - 05.12.2017**|<ul><li>Final check with our results.</li><li> Initialize our data story.</li></ul>|
|Week 6<br>**05.12.2017 - 12.12.2017**|<ul><li>Work on data story.</li><li> Improve the organization of notebook and improve the space/time efficiency.</li></ul>|
|Week 7<br>**12.12.2017 - 19.12.2017**|<ul><li>Finalize the data story and notebook.</li></ur>|

# Citation for the Dataset
- SecondHandSongs dataset, the official list of cover songs within the Million Song Dataset, 
available at: http://labrosa.ee.columbia.edu/millionsong/secondhand
- Thierry Bertin-Mahieux, Daniel P.W. Ellis, Brian Whitman, and Paul Lamere. 
The Million Song Dataset. In Proceedings of the 12th International Society
for Music Information Retrieval Conference (ISMIR 2011), 2011.

## Team - ITT
[Project Repository Page](https://github.com/sanadhis/ITT-ADA-2017/tree/master/project)
- Cheng-Chun Lee ([@wlo2398219](https://github.com/wlo2398219)) : (cheng-chun.lee@epfl.ch)
- Sanadhi Sutandi ([@sanadhis](https://github.com/sanadhis)) : (i.sutandi@epfl.ch)
- Skander Hajri ([@Skan000](https://github.com/Skan000)) : (skander.hajri@epfl.ch)
