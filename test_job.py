import unittest
from unittest.mock import patch
import run_hadoop_job
import retrieve_output
import subprocess

class TestHadoopJob(unittest.TestCase):

    @patch("subprocess.run")
    def test_run_hadoop_job_success(self, mock_subprocess):
        """Test Hadoop job execution succeeds"""
        mock_subprocess.return_value = None  # Simulate successful subprocess call
        self.assertTrue(run_hadoop_job.run_hadoop_job())

    @patch("subprocess.run", side_effect=subprocess.CalledProcessError(1, "hadoop"))
    def test_run_hadoop_job_failure(self, mock_subprocess):
        """Test Hadoop job execution fails"""
        self.assertFalse(run_hadoop_job.run_hadoop_job())

class TestRetrieveOutput(unittest.TestCase):

    @patch("subprocess.run")
    def test_retrieve_hadoop_output_success(self, mock_subprocess):
        """Test retrieving Hadoop output succeeds"""
        mock_subprocess.return_value = None
        self.assertTrue(retrieve_output.retrieve_hadoop_output())

    @patch("subprocess.run", side_effect=subprocess.CalledProcessError(1, "gsutil"))
    def test_retrieve_hadoop_output_failure(self, mock_subprocess):
        """Test retrieving Hadoop output fails"""
        self.assertFalse(retrieve_output.retrieve_hadoop_output())

if __name__ == "__main__":
    unittest.main()
