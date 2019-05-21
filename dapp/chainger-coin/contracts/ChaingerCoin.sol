pragma solidity ^0.5.2;

import 'openzeppelin-solidity/contracts/token/ERC20/ERC20.sol';

import 'openzeppelin-solidity/contracts/token/ERC20/ERC20Detailed.sol';

contract ChaingerCoin is ERC20, ERC20Detailed {
  uint256 public constant INITIAL_SUPPLY = 10000 * (10 ** uint256(5));

  constructor() ERC20Detailed("ChaingerCoin", "CHC", 18) public {

    _mint(msg.sender, INITIAL_SUPPLY); //msg.sender: 함수를 실행한 account

  }


}