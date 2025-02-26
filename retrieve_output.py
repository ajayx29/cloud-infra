import subprocess
import sys

def retrieve_hadoop_output():
    try:
        print("Retrieving Hadoop job output...")
        gsutil_command = ["gsutil", "cat", "gs://dataproc-staging-us-central1-40833754326-zlfuzvnm/output/*"]
        subprocess.run(gsutil_command, check=True)
        print("Hadoop job output retrieved successfully!")
    except subprocess.CalledProcessError:
        print("Failed to retrieve Hadoop job output!", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    retrieve_hadoop_output()
