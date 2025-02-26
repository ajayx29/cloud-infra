import subprocess
import sys

def run_hadoop_job():
    try:
        print("Triggering Hadoop job...")
        hadoop_command = [
            "hadoop", "jar", "/usr/lib/hadoop-mapreduce/hadoop-mapreduce-examples.jar",
            "wordcount", "gs://dataproc-staging-us-central1-40833754326-zlfuzvnm/input.txt",
            "gs://dataproc-staging-us-central1-40833754326-zlfuzvnm/output"
        ]
        subprocess.run(hadoop_command, check=True)
        print("Hadoop job triggered successfully!")
    except subprocess.CalledProcessError:
        print("Hadoop job execution failed!", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    run_hadoop_job()
