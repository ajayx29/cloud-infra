import subprocess
import sys

def retrieve_hadoop_output():
    """Retrieves output from the Hadoop job stored in GCS."""
    try:
        print("Retrieving Hadoop job output...")
        gsutil_command = ["gsutil", "cat", "gs://dataproc-staging-us-central1-40833754326-zlfuzvnm/output1/**"]
        subprocess.run(gsutil_command, check=True)
        print("Hadoop job output retrieved successfully!")
        return True
    except subprocess.CalledProcessError:
        print("Failed to retrieve Hadoop job output!", file=sys.stderr)
        return False

if __name__ == "__main__":
    success = retrieve_hadoop_output()
    sys.exit(0 if success else 1)
