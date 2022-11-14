# Mastodon_Exploration_ETL
Exploring Mastodon data to showcase ETL, data modeling, and visualization

While Mastodon has been around since 2016, it skyrocketed in popularity in October 2022 due to its reputation as the “Twitter replacement”. Mastodon is a decentralized social media platform that leverages blockchain in the backend. Blockchain technology can prevent censorship to a certain extent, a trait that many users find tantalizing. For many who do not use Twitter or are out of the loop regarding social media (myself included), it can be difficult to understand what all the fuss is about. In this analysis, I will build an ETL pipeline to extract data from Mastodon servers, process it using Spark, mobilize the data using Kafka, store the data in Snowflake, and then visualize it in a Tableau dashboard. This will all be orchestrated by Airflow and onboarded onto AWS. 

### Figure 1: Diagram of ETL Pipeline
![ETL_Pipeline](https://github.com/nicolenlama/Mastodon_Exploration_ETL/blob/main/Mastodon_Schemas-ETL%20Pipeline.drawio%20(1).png)


### Figure 2: Data Model (star schema) for Snowflake 
![Star_Schema](https://github.com/nicolenlama/Mastodon_Exploration_ETL/blob/main/Mastodon_Schemas-Star_Data_Model_For_Snowflake.drawio.png)
