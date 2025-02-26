#!/bin/bash
echo "Connection Successful"
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-mapreduce-examples.jar wordcount gs://dataproc-staging-us-central1-40833754326-zlfuzvnm/input.txt gs://dataproc-staging-us-central1-40833754326-zlfuzvnm/output4
