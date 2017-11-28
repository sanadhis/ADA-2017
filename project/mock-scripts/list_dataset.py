from os import listdir
import subprocess

path = "/datasets/million-song_untar"
hadoop_ls                      = subprocess.Popen(
                                    ["hadoop", "fs", "-ls", "-C", "-R", path],
                                    stdin=subprocess.PIPE,
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE
                                    )
hadoop_ls_out, hadoop_ls_err   = hadoop_ls.communicate()

datasets  = hadoop_ls_out.split("\n")

text_file = open("datasets.csv", "w")
for dataset in datasets:
    if(dataset.endswith("h5")):
        text_file.write(dataset+"\n")
text_file.close()
