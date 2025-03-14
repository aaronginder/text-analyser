from setuptools import setup
import subprocess

# Default version if no tag is found
__version__ = "0.0.0"

# Try to get version from git tags (created by semantic-release)
try:
    # Get the most recent tag
    version = subprocess.check_output(
        ["git", "describe", "--tags", "--abbrev=0"], 
        stderr=subprocess.DEVNULL
    ).decode("utf-8").strip()
    
    # Remove 'v' prefix if present
    if version.startswith("v"):
        version = version[1:]
        
    if version:
        __version__ = version
except (subprocess.CalledProcessError, OSError):
    # If no git or no tags, use default version
    pass

setup(
    name="text-analyser",
    version=__version__,
    description="PySpark job that analyses text data",
    author="Aaron Ginder",
    author_email="aaronginder@hotmail.co.uk",
    packages=[],
)
