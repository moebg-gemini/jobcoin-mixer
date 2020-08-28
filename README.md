# JobCoin Mixer

## Contents

* Overview
* Workflow
* Design Decisions
* Usage
* System Components
* Dependencies
* Extensions

## Overview

The JobCoin mixer allows users to mix their JobCoin to `N` number of output addresses for `X` amount of coin.

## Workflow

1. User enters in `N` number of addresses and `X` number of coins for a mix request
2. The Mixer receives the User's request, and responds with a new deposit address for the user to send the funds to
3. The User sends `X` amount of funds to the deposit address
4. Mixer checks to see if the deposit address from the User has reached `X` amount as specified in the mix request, then proceeds to transfer to its pool address in the case where the User sends sufficient funds to the deposit address
5. The Mixer then deposits `X` amount of funds between `N` addresses in random amounts and executes the transfers on a random bounded interval.

## Design Decisions

Currently the application runs the main objects through a CLI program, the Mixer application can be extended to be a web service a frontend can communicate with and send requests to. This can be done in flask.

## Usage

```
git clone https://github.com/moebg-gemini/jobcoin-mixer.git
cd jobcoin-mixer
python cli.py
```

**Configuration**

The mixer application can be configured with the `config.json` file in the root directory.

* `api_base_url`: This the JobCoin API we are communicating with, if we need to change to another JobCoin network, we can change the URL in here.
* `client_addr_min`: This is the minimum number of addresses we require for the final output for the mixed coins. We want to make sure that there is an enforcement of a minimum so users don't simply put too little number of deposit addresses for mixing.
* `client_default_addr_length`: This is the minimum length of the addresses we use to generate for both deposit addresses, and addresses generated for the user if they don't want to input addresses themselves.


```json
{
  "api_base_url": "http://jobcoin.gemini.com/tinderbox-unmapped/api",
  "client_addr_min": 3,
  "client_default_addr_length": 16
}
```

## System Componenets

* `cli.py`: This is the entrypoint of the application that allows the user to send funds to the mixer and has the program generate the output addresses for the user
* `client.py`: Client that makes calls to the Mixer and also generates output addresses on behalf of the user to make sure no repeat output addresses are used
* `config.py`: Config object that configureis the `Client`
* `jobcoinapi.py`: wrapper library to interact with JobCoin network
* `util.py`: Has utilities such as an address generate function
* `mixer.py`: Main mixer class that carries out Mixer functions for processing mixer jobs

## Dependencies

* `click`: cli library for python
* `pytest`: testing framework
* `requests`: HTTP library for python

## Extensions

These are features and extensions to the mixer that can be added in the future.

* Mixing Algorithm: The current mixing algorithm evenly sends out coin amounts to all output addresses.
* Double Mixing
* Log events throughout the application
* Make the mixer an HTTP service and have clients only interact with the Mixer through API calls
* Have a separate frontend client that interacts with the Mixer's HTTP service
* CI/CD implementation
* Time delay in mixing
* Adding a task queue for mixer request jobs
* Using a database to keep track of mixing jobs instead of an in-memory dictionary
* Have user put their own default address to transfer from, currently we transfer on behalf of a default user address on the jobcoin network
* Random distribution of X coins between N addresses
* Using a config service for a mixer instance
* Custom errors
