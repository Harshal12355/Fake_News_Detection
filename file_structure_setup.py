import os

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Created directory: {path}")

def create_file(path, content=""):
    with open(path, 'w') as f:
        f.write(content)
        print(f"Created file: {path}")

def main():
    # Define the directory structure
    directories = [
        "fake-news-detection/data/raw",
        "fake-news-detection/data/processed",
        "fake-news-detection/notebooks",
        "fake-news-detection/src",
        "fake-news-detection/models"
    ]

    # Define the files to be created with optional content
    files = {
        "fake-news-detection/src/__init__.py": "",
        "fake-news-detection/src/data_preprocessing.py": "# Data Preprocessing Script",
        "fake-news-detection/src/feature_extraction.py": "# Feature Extraction Script",
        "fake-news-detection/src/model_training.py": "# Model Training Script",
        "fake-news-detection/src/model_evaluation.py": "# Model Evaluation Script",
        "fake-news-detection/src/model_deployment.py": "# Model Deployment Script",
        "fake-news-detection/requirements.txt": "",
        "fake-news-detection/README.md": "# Fake News Detection Project\n\n## Setup Instructions\n",
        "fake-news-detection/setup.py": (
            "from setuptools import setup, find_packages\n\n"
            "setup(\n"
            "    name='fake-news-detection',\n"
            "    version='0.1',\n"
            "    packages=find_packages(),\n"
            "    install_requires=[],\n"
            "    author='Your Name',\n"
            "    author_email='your.email@example.com',\n"
            "    description='A fake news detection project',\n"
            ")"
        ),
    }

    # Create directories
    for directory in directories:
        create_directory(directory)

    # Create files
    for path, content in files.items():
        create_file(path, content)

if __name__ == "__main__":
    main()
