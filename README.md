# Django-Elasticsearch
Django Rest Framework, Elasticsearch, Celery


**What is Elasticsearch?**
Elasticsearch is a distributed, free and open search and analytics engine for all types of data, including textual, numerical, geospatial, structured, and unstructured. Elasticsearch is built on Apache Lucene and was first released in 2010 by Elasticsearch N.V. (now known as Elastic). Known for its simple REST APIs, distributed nature, speed, and scalability, Elasticsearch is the central component of the Elastic Stack, a set of free and open tools for data ingestion, enrichment, storage, analysis, and visualization. Commonly referred to as the ELK Stack (after Elasticsearch, Logstash, and Kibana), the Elastic Stack now includes a rich collection of lightweight shipping agents known as Beats for sending data to Elasticsearch.

**At its core, you can think of Elasticsearch as a server that can process JSON requests and give you back JSON data.**

## How Does Elasticsearch Work?

Elasticsearch uses shipping agents, called beats, to transfer raw data from multiple sources into Elasticsearch. After data is shipped into Elasticsearch, the engine runs data ingestion processes, which parse, normalize, enrich, and prepare data for indexing. After the data is indexed, users can run complex queries and use aggregations to retrieve complex data summaries.

It is commonly referred to as the “ELK” stack after its components Elasticsearch, Logstash, and Kibana and now also includes Beats. For visualization and management, the Elastic Stack offers a tool called Kibana, which enables users to create real-time data visualizations, such as pie charts, maps, line graphs, and histograms. Kibana also lets you share dashboards, use Canvas to create custom dynamic infographics, and use Elastic Maps to visualize geospatial data. Although a search engine at its core, users started using Elasticsearch for log data and wanted a way to easily ingest and visualize that data.

### The Ports 9200 and 9300

The Elasticsearch architecture uses two main ports for communication:

-   **Port 9200**—used to filter requests coming from outside the cluster. This process meets requests coming through the REST APIs used for querying, indexing, and more.
-   **Port 9300**— used for inter-node communication. This occurs in the transport layer.
