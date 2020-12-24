from web3 import Web3
import os
from dotenv import load_dotenv
import solc
from solc import compile_source,compile_standard,compile_files
from solc import install_solc

load_dotenv(".env")

compiled_contract=compile_files(["contract.sol"])
# compiled_contract

abi=compiled_contract["contract.sol:Inbox"]["abi"]
bytecode=compiled_contract["contract.sol:Inbox"]["bin"]
web3=Web3(Web3.HTTPProvider(os.getenv("provider_url")))
inbox=web3.eth.contract(abi=abi,bytecode=bytecode)
private_key=os.getenv("private_key")

accounts=web3.eth.account.privateKeyToAccount(private_key)

tx_hash=inbox.constructor("hello world").buildTransaction(
    {
        "from":accounts.address,
        "gas":1000000,
        "nonce":web3.eth.getTransactionCount(accounts.address),
        "gasPrice":web3.toWei("30","gwei")
    }
)

signed=accounts.signTransaction(tx_hash)
final=web3.eth.sendRawTransaction(signed.rawTransaction)
contract_details=web3.eth.getTransactionReceipt(final)
print(f"contract address >{contract_details.contractAddress}")

checking_contract=web3.eth.contract(address=contract_details.contractAddress,abi=abi)
checking_contract.functions.return_message().call()

# new

def update_message(data:str,contract_address:str,abi:str,private_key:str)->int:
    if type(data)!=type(""):
        data=str(data)
    accounts=web3.eth.account.privateKeyToAccount(private_key)
    if len(accounts.address)==0:
        return 404
    print(accounts.address)

    contract=web3.eth.contract(address=contract_address,abi=abi)
    initial_message=contract.functions.return_message().call()
    print(f"message>{contract.functions.return_message().call()}")
    transaction=contract.functions.update(data).buildTransaction(
        {
            "from":accounts.address,
            "gas":70000,
            "nonce":web3.eth.getTransactionCount(accounts.address),
            "gasPrice":web3.toWei("1","gwei")
        }
    )
    print(transaction)
    contract_details=web3.eth.account.signTransaction(transaction,private_key)
    print(contract_details)
    final=web3.eth.sendRawTransaction(contract_details.rawTransaction)
    new_contract = web3.eth.contract(address=contract_address, abi=abi)
    print(new_contract.functions.return_message().call())
    return 200

update_message("welcome batch of 2020",contract_address=contract_details.contractAddress,private_key=private_key,abi=abi)
