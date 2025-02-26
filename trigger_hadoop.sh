#!/bin/bash
echo "Connection Successful"
while true; do
    echo "This is an infinite loop with no exit condition!"
done
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-mapreduce-examples.jar wordcount gs://dataproc-staging-us-central1-40833754326-zlfuzvnm/input.txt gs://dataproc-staging-us-central1-40833754326-zlfuzvnm/output4
