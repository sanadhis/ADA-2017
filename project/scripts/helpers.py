import pandas as pd
from IPython.display import display

def debug_dataframe(df):
    """Function to observe dataframe structures (rows, columns) in general.
    Inputs:
        df (panda dataframe) : dataframe we want to inspect the contents of.
    Returns:
        None
    """
    
    print("Dataset size: ", df.shape)
    print("Dataset feature columns: ", df.columns)
    print("\nDataset Preview:")
    display(df.head(3))
    
def read_raw_dataset(dataset_file):
    """Function to read a single raw dataset from a pickle file.
    Inputs:
        file (string)          : the name of dataset file in /datasets/pickle_files/ directory.
    Returns:
        df   (panda dataframe) : dataframe containing the raw dataset.
    """
    
    df = pd.read_pickle("./datasets/pickle_files/df_pickle_" + dataset_file)
    return df

def save_dataframe(df, filename):
    """Function to write dataframe into a single pickle file.
    Inputs:
        df       (panda dataframe) : dataframe containing the processed data of datasets.
        filename (string)          : name for the pickle file.
    Returns:
        None
    """
    
    df.to_pickle("./datasets/processed_pickle_files/" + filename)

def read_saved_dataframe(filename):
    """Function to read a single processed dataset from a pickle file.
    Inputs:
        filename (string)          : the name of dataset file in /datasets/processed_pickle_files/ directory.
    Returns:
        df       (panda dataframe) : dataframe containing the raw dataset.
    """
    
    df = pd.read_pickle("./datasets/processed_pickle_files/" + filename)
    return df

def copy_dataframe(df):
    """Function to copy a dataframe content into a new dataframe object.
    Inputs:
        df     (panda dataframe) : original dataframe.
    Returns:
        df_new (panda dataframe) : new dataframe copy.
    """
    
    df_new = pd.DataFrame(index=df.index)
    df_new = df.copy()
    return df_new
