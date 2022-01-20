from brownie import network, config, accounts, MockV3Aggregator
from web3 import Web3

DECIMALS =  18 # 8?
STARTING_PRICE = 2000 # 200000000000?
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development","ganache-local"]
def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

def deploy_mocks():
    account = get_account()
        # to mock, we need a mock contract, create it under contracts/test folder 
    print(f"The active network is {network.show_active()}")
    print("Deploying Mocks...")
    if len(MockV3Aggregator)<=0:
        # mock_aggregator = MockV3Aggregator.deploy(18,Web3.toWei(2000,"ether"),{"from":account}) # mock_aggregator is an array of deployed contracts
        MockV3Aggregator.deploy(DECIMALS,Web3.toWei(STARTING_PRICE,"ether"),{"from":account})
    # price_feed_address = mock_aggregator[-1].address
    print("Mocks Deployed")