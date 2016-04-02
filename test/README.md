This test gets tweets, vectorizes them, and clusters them using the sequential version of Birch.

Every time 10 tweets are received:
      - The total number of tweets received is printed
      - The total number of clusters computed is printed
      - The cluster distribution is printed (each value represents the number of tweets for the cluster)
      - If a cluster contains more than 15 tweets, the prototype of its center is computed back to words, and printed

To try this test: 
First use the script ./compile.sh which download the french dictionary
Then use the command: python run.py

