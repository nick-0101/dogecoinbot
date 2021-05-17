# Dogecoin Bot

This Binance trading bot will check Elon Musks twitter feed for tweets about Dogecoin, if the tweet is positive, the bot will buy $25 of Dogecoin.


> Requirements

- Twitter API.
- Binance account with an API
- A heroku account


## READ BEFORE USE
1. By using this bot, you will be using REAL money.
2. To test the bot out change ```sh
client.create_order() to client.create_test_order()
```


## Usage

1. Install Dependencies
    - Easy mode (might clash with current depends)
        ```sh
        pip install -r requirements.txt
        ```
    - Prefered Method (venv)
        ```sh
        python3 -m venv .venv
      
        source .venv/bin/activate # linux
        .\.venv/scripts/activate # windows
    
        pip install -r requirements.txt
        ```


2. Create a `.env`in the root dir.

    ```sh
    # Binance
    BINANCE_API=
    BINANCE_SECRET=
    
    # Twitter
    CONSUMER_KEY=
    CONSUMER_SECRET=
    ACCESS_TOKEN=
    ACCESS_TOKEN_SECRET=
    ```

3. Run the script
    - Standard 
        ```sh
        python3 dogebot.py
        ```
     - Heroku
        1. Create a Heroku account and project
        2. Upload the files to heroku
        3. Configure dyno worker and ensure the dogeboy.py worker is running.

## Troubleshooting / Issues
Please create a pull request and I will try to get back to you as soon as possible.
