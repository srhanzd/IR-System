import subprocess
import os


current_dir = os.path.dirname(os.path.abspath(__file__))



def run_Data_preprocessing_for_first_data_set_english():
    subprocess.run(['python', os.path.join(current_dir,'Data_preprocessing_for_first_data_set_english.py')])

def run_DataRepresentation_for_the_first_data_set_english():
    subprocess.run(['python', os.path.join(current_dir,'DataRepresentation_for_the_first_data_set_english.py')])

def run_Index_for_the_first_data_set_english():
    subprocess.run(['python', os.path.join(current_dir,'Index_for_the_first_data_set_english.py')])



def run_QueriesPreprocessing_for_first_data_set_english():
    subprocess.run(['python', os.path.join(current_dir,'QueriesPreprocessing_for_first_data_set_english.py')])


def run_QueriesRepresention_for_first_data_set_english():
    subprocess.run(['python', os.path.join(current_dir,'QueriesRepresention_for_first_data_set_english.py')])


def run_Clustring_for_first_data_set_english():
    subprocess.run(['python', os.path.join(current_dir,'Clustring_for_first_data_set_english.py')])


def run_Evaluation_Clustering_for_first_data_set_english():
    subprocess.run(['python', os.path.join(current_dir,'Evaluation_Clustering_for_first_data_set_english.py')])

# 
run_Data_preprocessing_for_first_data_set_english()
run_DataRepresentation_for_the_first_data_set_english()
run_Index_for_the_first_data_set_english()
run_Clustring_for_first_data_set_english()

run_QueriesPreprocessing_for_first_data_set_english()
run_QueriesRepresention_for_first_data_set_english()

run_Evaluation_Clustering_for_first_data_set_english()