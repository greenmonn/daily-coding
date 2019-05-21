const  ChaingerCoin = artifacts.require("ChaingerCoin");

module.exports =async function(deployer){
    await deployer.deploy(ChaingerCoin);
}