const ChaingerCoin = artifacts.require("ChaingerCoin");

contract('ChaingerCoin', (accounts) => {
    it('should put 10000 ChaingerCoin in the caller account', async () => {
        const chaingerCoinInstance = await ChaingerCoin.deployed();
        const balance = await chaingerCoinInstance.balanceOf.call(accounts[0]);
        assert.equal(balance.valueOf(), 10000 * (10**5), "10000 wasn't in the first account");

    });
    it('should send coin correctly', async () => {
        const chaingerCoinInstance = await ChaingerCoin.deployed();
        //given
        const accountOne = accounts[0];
        const accountTwo = accounts[1];

        const accountOneStartingBalance = (await chaingerCoinInstance.balanceOf.call
            (accountOne)).toNumber();
        const accountTwoStartingBalance = (await chaingerCoinInstance.balanceOf.call
            (accountTwo)).toNumber();

        //when
        const amount = 10;
        await chaingerCoinInstance.transfer(accountTwo, amount, { from: accountOne });

        const accountOneEndingBalance = (await chaingerCoinInstance.balanceOf.call
            (accountOne)).toNumber();
        const accountTwoEndingBalance = (await chaingerCoinInstance.balanceOf.call
            (accountTwo)).toNumber();
            
        //then
        assert.equal(accountOneStartingBalance, accountOneEndingBalance + amount, "Amount wasn't correctly taken from the sender");
        assert.equal(accountTwoStartingBalance, accountTwoEndingBalance - amount, "Amount wasn't correctly sent to the receiver");
    });
}
);

