Python skill in Italian for alexa

create_package.sh -> creates the zip package to upload on S3
magic_giulio.py -> functionalities

### Prerequirements

1. Alexa skil defined: https://developer.amazon.com/alexa/console/ask
2. AWS account with lambda defined

### Setup

If not installed, install virtualenv

1. Install virtualenv

    `pip3 install virtualenv`

2. Clone repository

    `git clone https://github.com/gpresazzi/magic_giulio_alexa_skill.git`

3. Setup virtual env
    ```
    virtualenv magic_giulio_venv
    source ./magic_giulio_venv/bin/activate
    pip install ask-sdk
    ```
    
4. Create package for lambda
    ```
    create_package.sh
    ```
    the output file : skill_magic_giulio.zip can be used as source for the lambda function



REF: https://alexa-skills-kit-python-sdk.readthedocs.io/en/latest/GETTING_STARTED.html