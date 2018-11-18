Python skill in Italian for alexa

create_package.sh -> creates the zip package to upload on S3
magic_giulio.py -> functionalities

### Prerequirements

1. Alexa skil defined: https://developer.amazon.com/alexa/console/ask
2. AWS account with lambda defined

### Setup

If not installed, install virtualenv

1. Install virtualenv

    ```
    pip3 install virtualenv
    ```

2. Clone repository

    ```
    git clone https://github.com/gpresazzi/magic_giulio_alexa_skill.git
    ```

3. Setup virtual env
    ```
    virtualenv magic_giulio_venv
    source ./magic_giulio_venv/bin/activate
    pip3 install -r requirements.txt
    ```
    
4. Unit testing

    Reference: https://medium.com/@bezdelev/how-to-test-a-python-aws-lambda-function-locally-with-pycharm-run-configurations-6de8efc4b206
    
    To run unit test run `pytest`
    
    The unit test framework is based on [python-lambda-local](https://github.com/HDE/python-lambda-local) lib. Instead of launch the following command
    I choose to integrate this into pytest framework to facilitate the local testing of the lambda function.
    
    ```
    python-lambda-local -f handler ./src/magic_giulio.py ./test/test-json/brava-ilaria-1.json
    ```
    
4. Create package for lambda
    ```
    create_package.sh
    ```
    the output file : skill_magic_giulio.zip can be used as source for the lambda function



REF: https://alexa-skills-kit-python-sdk.readthedocs.io/en/latest/GETTING_STARTED.html