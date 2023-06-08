# IR-System
Information retrieval (IR) is an important system that revolves around the task of searching for and retrieving relevant information from large groups of documentations.







this ir system is build on two data sets 




1-	Antique :


Language : English


Documents : 404 K 


Queries : 200


QRELS : 2.2 K



2-	Mr-tydi :


Language : SW (Swahili)


Documents : 137 K 


Queries : 3.3 K


QRELS : 3.8 K




Offline services :



OflineServiceForFirstDataSet.py-> to run all the offline services for first data set.



OflineServiceForSecoundDataSet.py ->to run all the offline services for secound data set.




Data_preprocessing :


      clean_text
   
   
   
      tokenize_text
   
   
   
     remove_stopwords
   
   
   
     lemmatize_tokens
   
   
   
   
   on the doucemnts in the dataset.
   
   
   
   
   
   
DataRepresentation :


vector space model using tfidf for the doucments Representation.




Index :


create inverted index that Represent the doucments as doc_id => posting_list(term,wiegth)



Clustring:


Represent the doucments as clusters 




QueriesPreprocessing:


      clean_text
      
      
      tokenize_text
      
      
      remove_stopwords
      
      
      lemmatize_tokens  
      
      
      on the queries for the dataset.
      
      
      
      
      
QueriesRepresention:   


vector space model using tfidf for the queries Representation.  





Evaluation_Clustering:

        Precision@10
        
        
        Precision
        
        
        Recall
        
        
        Average Precision
        
        
        Reciprocal Rank
        
        
        total_precision += precision
        
        
        total_precision_10 += precision_10
        
        
        total_recall += recall
        
        
        
        total_average_precision += average_precision
        
        
        
        total_reciprocal_rank += reciprocal_rank
       
      mean_precision_10 = total_precision_10 / total_queries
   
   
      mean_precision = total_precision / total_queries
   
   
      mean_recall = total_recall / total_queries
   
   
   
      mean_average_precision = total_average_precision / total_queries
   
   
   
      mean_reciprocal_rank = total_reciprocal_rank / total_queries.
   
   
   
   
   
Online Services:


Search(End Point) -> take users query and returns the relevent doucments .



QueryPreprocessing :
      clean_text
     
     
      tokenize_text
      
      
      remove_stopwords
      
      
      lemmatize_tokens   
      
      
      on the user query .
      
      
      
QueryRepresention :    


vector space model using tfidf for the user query Representation.  




QueryMatching_And_Ranking:


calculate cosin similarity (query vector,clusters vectors )


then calculate cosin similarity (query vector,doucments vectors inside the top 2 clusters )


then return the top 10 relevent doucments




in this project we use flutter framework to build the user interface .



