import subprocess
import os


current_dir = os.path.dirname(os.path.abspath(__file__))



def run_Data_preprocessing_for_secound_data_set():
    subprocess.run(['python', os.path.join(current_dir,'Data_preprocessing_for_secound_data_set.py')])

def run_DataRepresentation_for_the_secound_data_set():
    subprocess.run(['python', os.path.join(current_dir,'DataRepresentation_for_the_secound_data_set.py')])

def run_Index_for_the_secound_data_set():
    subprocess.run(['python', os.path.join(current_dir,'Index_for_the_secound_data_set.py')])



def run_QueriesPreprocessing_for_secound_data_set():
    subprocess.run(['python', os.path.join(current_dir,'QueriesPreprocessing_for_secound_data_set.py')])


def run_QueriesRepresention_for_secound_data_set():
    subprocess.run(['python', os.path.join(current_dir,'QueriesRepresention_for_secound_data_set.py')])


def run_Clustring_for_secound_data_set():
    subprocess.run(['python', os.path.join(current_dir,'Clustring_for_secound_data_set.py')])


def run_Evaluation_Clustering_for_secound_data_set():
    subprocess.run(['python', os.path.join(current_dir,'Evaluation_Clustering_for_secound_data_set.py')])

# 
run_Data_preprocessing_for_secound_data_set()
run_DataRepresentation_for_the_secound_data_set()
run_Index_for_the_secound_data_set()
run_Clustring_for_secound_data_set()


run_QueriesPreprocessing_for_secound_data_set()
run_QueriesRepresention_for_secound_data_set()

run_Evaluation_Clustering_for_secound_data_set()