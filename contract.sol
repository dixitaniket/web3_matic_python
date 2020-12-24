// SPDX-License-Identifier: MIT
pragma solidity >=0.4.17;


contract Inbox{
    string initial_message;
    constructor(string memory new_message){
        initial_message=new_message;
    }

    function update(string memory new_message) public{
        initial_message=new_message;
}

    function return_message() public view returns(string memory){
        return initial_message;
    }

}