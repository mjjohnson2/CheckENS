# CheckENS

This is just a quick script I put together to batch check for available ENS names.


## Prerequisites & Setup

1. Homebrew
2. geth
3. Python 3 
4. ens


### 1. Homebrew 
Head on over to https://brew.sh/ to install.

Once installed, make sure homebrew is up to date:

```
brew update
brew upgrade
```

### Geth

***ens.py*** requires an up-to-date Ethereum blockchain, preferably local which is why we are downloading the Ethereum blockchain. This will likely take a few hours.

**Option 1** 

Then install Ethereum

```
brew tap ethereum/ethereum
brew install ethereum
```
Once installed, try running `geth --fast` until it's fully synced. 

**Option 2**

If Option 1 doesn't work, you can install the Ethereum Wallet from https://github.com/ethereum/mist/releases and let that sync. Make sure you're on the Main Net. 


### ens

Using Python 3:

`pip install ens`



## Instructions

To batch test the availability of ENS names, append the names to test to the "test-names.txt" file. These names could have any extension or no extension, just separate each name with a new line. The resulting available names will be appended to the "Available-Names.txt" file. 

You can run the script multiple times without having to clear the "test-names.txt" as the script checks to see if it has been previously checked. This means that previously checked names won't update the status if you run the script again, unless you delete that entry from the "Available-Names.txt" 

## Troubleshooting 

### "No matching distribution found for ens"

If you see this:
```
Collecting ens
  Could not find a version that satisfies the requirement ens (from versions: )
No matching distribution found for ens
```

Make sure you're in Python 3


## Acknowledgments

* **Ethereum Name Service via Python** : A python library for accessing the Ethereum Name Service (ENS) https://github.com/carver/ens.py/blob/master/README.md
* **Ethereum**

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


