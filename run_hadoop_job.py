import subprocess
import sys

def run_hadoop_job():
    """Triggers a Hadoop job on Dataproc."""
    try:
        print("Triggering Hadoop job...")
        hadoop_command = [
            "hadoop", "jar", "/usr/lib/hadoop-mapreduce/hadoop-mapreduce-examples.jar",
            "wordcount", "gs://dataproc-staging-us-central1-40833754326-zlfuzvnm/input.txt",
            "gs://dataproc-staging-us-central1-40833754326-zlfuzvnm/output1"
        ]
        subprocess.run(hadoop_command, check=True)
        print("Hadoop job triggered successfully!")
        return True
    except subprocess.CalledProcessError:
        print("Hadoop job execution failed!", file=sys.stderr)
        return False

if __name__ == "__main__":
    success = run_hadoop_job()
    sys.exit(0 if success else 1)
