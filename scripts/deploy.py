# clean up from 5:33:33
from brownie import FundMe, network, config, MockV3Aggregator
from scripts.helpful_scripts import get_account, deploy_mocks, LOCAL_BLOCKCHAIN_ENVIRONMENTS
# from web3 import Web3


def deploy_fund_me():
    account = get_account()
    # if we are on persistent network, pass the contract address
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:#"development":
        price_feed_address = config["networks"][network.show_active()]["eth_usd_price_feed"]# grab from config 
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address    

   
    # need to pass priceFeed  address to our fundme contract
    # fund_me =FundMe.deploy("0x8A753747A1Fa494EC906cE90E9f37563A8AF630e",{"from": account},publish_source=True) # you can pass through constructor in the Contract.deploy() as the first input; but this does not solve the problem of using a dev. network
    fund_me =FundMe.deploy(price_feed_address,{"from": account},publish_source=config["networks"][network.show_active()].get("verify")) # you can pass through constructor in the Contract.deploy() as the first input; 
    # config[][].get("verify") works better in case you forget to add it to one of the networks, will probably just give you null 
    # publish_source does not work on dev. network
    print(f"entrance fee is {fund_me.getEntranceFee()}" )
    print(f"Contract deployed to {fund_me.address}")
    return fund_me

def main():
    deploy_fund_me()