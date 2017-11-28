# What Makes Songs Popular?
[CS-401 ADA](http://isa.epfl.ch/imoniteur_ISAP/!itffichecours.htm?ww_i_matiere=2046272383&ww_x_anneeAcad=2017-2018&ww_i_section=249847&ww_i_niveau=&ww_c_langue=en) - [EPFL](http://epfl.ch)
> Project of Applied Data Analysis Course - 2017/2018

# Abstract
This project aims to analyze the trends towards songs' popularity from years to years. We want to define metrics that can lead to prediction of songs' popularity in billboard. To achive this, we use [Million Song Dataset](https://labrosa.ee.columbia.edu/millionsong/) that has collection of audio features and metadata of popular songs.

Through this project, we would like to show how people tend to listen to songs, e.g. by considering the singers/artist, genres, lyrics. Then we also want to know whether herding bias happens, i.e. somebody listening songs from same artist, and the quality of popular songs by considering the lyrics (frequent words, slang words).

> Music is a moral law. It gives soul to the universe, wings to the mind, flight to the imagination, and charm and gaiety to life and to everything. _-Plato_

The project's main goal is to prove how society reacts to songs' quality over time. We expect to see the challenges of music industry towards time.

# Project Structure
------------

    ├── main.ipynb                           : The main notebook for the our songs project, answering research questions.
    ├── README.md                            : The README guideline and explanation for our work.
    ├── 00raw_datasets_observation.ipynb     : Notebook contains initial observation for Million Songs datasets.
    ├── 00raw_datasets_preprocessings.ipynb  : Notebook contains initial preprocessing for raw datasets files.
    ├── Part1.ipynb                          : Answers and explanations for Question block 1.
    ├── Part2.ipynb                          : Answers and explanations for Question block 2.
    ├── Part3.ipynb                          : Answers and explanations for Question block 3.
    |
    ├── datasets
    │   ├── pickle_files                     : Directory containing files of raw datasets, with pickle format & reduced in size.
    │   ├── processed_pickle_files          : Directory containing processed (reduced & filtered) datasets.
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
    ├── scripts                              : Directory containing helpers script for our main.ipynb notebook.


--------

# Data Aqusition & Initial Data Preprocessing
The raw datasets provided by ADA TAs are 280 GB in size and have h5 (HDF) format. The datasets is spreaded in A-Z directories and contains additional datasets (/AdditionalFiles). From all provided dataset files, we utilize 12 different datasets and store them as pickle files. We choose to use pickle format to boost loading time for later load the data in notebook.

> Check our notebook for [initial processing of raw files](https://github.com/sanadhis/ITT-ADA-2017/blob/master/project/00raw_datasets_preprocessings.ipynb) and [datasets brief description](https://github.com/sanadhis/ITT-ADA-2017/blob/master/project/00raw_datasets_observation.ipynb) to have more clear insight for our initial data preprocessing methods.

For our main datasets, "msd_songs", we filter one million song entries by removing songs without hotttnesss and then get about five hundred thousands songs (reduced almost half). The rest of processing are adjusted with each of our questions' need.

**Note that the datasets' pickle files are relatively big in term of size, thus we do not include it in our repository**

# Research questions
Our questions are decomposed into 3 blocks of questions:
## Question Block 1: What could make songs popular

### Q1.1 What is the characteristic/metrics of popular songs?
#### Design of experiment:

### Q1.2 What are the challenges that music industry faces?
#### Design of experiment:

### Q1.3 Can we analyze and predict the trend in music industry from years to years?
#### Design of experiment:

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
#### Design of experiment:

### Q3.2 Can we measure the quality and popularity of a song from its lyrics? Do the popular songs have the good quality of lyrics from literacy view points?
#### Design of experiment:

# Dataset
1. [The SecondHandSongs Dataset](https://labrosa.ee.columbia.edu/millionsong/secondhand) :

FORMAT:
      
      Single .txt file: shs_dataset_train.txt
      #                    - comment, ignore
      %a,b,c, title        - beginning of a clique. a,b,c are work IDs (negative if not available)
      TID<SEP>AID<SEP>perf - track ID from the MSD (plus artist ID and SHS performance)
It contains a mapping between original songs and cover songs contained in the million songs dataset in the form of cliques. This will mainly help us to answer the second question mentionned above.

2. [The musiXmatch Dataset](https://labrosa.ee.columbia.edu/millionsong/musixmatch) :

FORMAT:

      Single .txt file: mxm_dataset_train.txt
      #   - comment, to ignore
      %   - list of top words, comma-separated
          - normal line, contains track_id, mxm track id,
            then word count for each of the top words, comma-separated
            word count is in sparse format -> ...,<word idx>:<cnt>,...
            <word idx> starts at 1 (not zero!)

Which contains the lyrics from a subset of the original dataset songs. For every track in this dataset the lyrics are represented using a bag-of-words format obtained by stemming. This will allow us to address the third research question in particular.

3. [The Last.fm Dataset](https://labrosa.ee.columbia.edu/millionsong/lastfm) :

FORMAT:

      Several .json files in different directory (A-Z)
      Keys in .json files:
      'tags'       - style of the song such as rock, hard rock
      'artist'     - name of the singer
      'title'      - name of the song
      'timestamps' - date
      'similar'    - similarity measure of songs, range from 0 to 1 
      
For every songs it gives both a list of tags that defines the song (genre, instruments...) and a list of similar songs alongside the value of the similarity measure that was used. The dataset will come in quiet handy when checking for plagiarism or high ressemblance.

4. [The Echo Nest Taste Profile Subset](https://labrosa.ee.columbia.edu/millionsong/tasteprofile) :

FORMAT:

      Single .txt file: train_triplets.txt
      user   - ID of users
      song   - the song they listen
      count  - how many times the user listens to this song
      
This represents the profiles of real users in which we can find for every profile the play count for some song in the original dataset. It covers about a third of the tracks available in the million songs dataset and will give us a good representation of the musical trend.

# A list of internal milestones up until milestone 3
|Week #|Targets|
|---|---|
|Week 1<br>**01.11.2017 - 07.11.2017**|<ul><li>Getting started with cluster processing (spark, hadoop).</li><li> Initial data processing: Reading data, cleaning and wrangling, merging dataset.</li></ul>|
|Week 2<br>**07.11.2017 - 14.11.2017**|<ul><li>Begin to address research questions.</li><li> Initial analysis of data, finding correlations.</li></ul>|
|Week 3<br>**14.11.2017 - 21.11.2017**|<ul><li>Initial mockup for python scripts and notebooks.</li><li> Visualize data in several ways: charts, maps, images, and so on.</li></ul>|
|Week 4<br>**21.11.2017 - 28.11.2017**|<ul><li>Analyze the temporary results.</li><li> Review works and ensure completion for milestone 2.</li></ul>|
|Week 5<br>**28.11.2017 - 05.12.2017**|<ul><li>Final check with our results.</li><li> Decide the way to present our work(report or data story).</li></ul>|
|Week 6<br>**05.12.2017 - 12.12.2017**|<ul><li>Work on report/data story.</li><li> Improve the organization of notebook and improve the space/time efficiency.</li></ul>|
|Week 7<br>**12.12.2017 - 19.12.2017**|<ul><li>Finalize report/data story and notebook.</li></ur>|

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
