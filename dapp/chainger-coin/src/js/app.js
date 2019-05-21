App = {
    web3Provider: null,
    chaingerCoin: null,
    from: null,
    to: null,
    chaingerCoinInstance: null,

    init: async () => {
        await App.initWeb3();
    },

    initWeb3: async () => {
        App.web3Provider = new Web3.providers.HttpProvider(
            'http://localhost:8545'
        );

        web3 = new Web3(App.web3Provider);

        return App.initContract();
    },

    initContract: () => {
        $.getJSON('ChaingerCoin.json', data => {
            const CoinArtifact = data;
            App.chaingerCoin = TruffleContract(CoinArtifact);

            App.chaingerCoin.setProvider(App.web3Provider);

            web3.eth.getAccounts(async (error, accounts) => {
                if (error) {
                    console.log(error);
                }
                App.from = accounts[0];
                App.to = accounts[1];

                App.chaingerCoinInstance = await App.chaingerCoin.deployed();

                return App.getBalance();
            });
        });
    },

    getBalance: async () => {
        let balance_from = await App.chaingerCoinInstance.balanceOf.call(App.from);

        let balance_to = await App.chaingerCoinInstance.balanceOf.call(App.to);

        $('#from').text(balance_from);
        $('#to').text(balance_to);
    },

    sendCoin: async () => {
        await App.chaingerCoinInstance.transfer(App.to, 1000, { from: App.from })

        App.getBalance()
    }
};

App.init();
$('#send').click(App.sendCoin);
