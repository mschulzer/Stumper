String.prototype.hashCode = function() {
    var hash = 0;
    for (var i = 0; i < this.length; i++) {
        var char = this.charCodeAt(i);
        hash = ((hash<<5)-hash)+char;
        hash = hash & hash; // Convert to 32bit integer
    }
    return hash;
}

// Klasse
class Block {
    constructor (index, timestamp, data, previous_hash) {
        this.index = index
        this.timestamp = timestamp
        this.data = data
        this.previous_hash = previous_hash
        this.hash = this.hashBlock()
    }

    // Funktion i klassen: hasher'en
    hashBlock () {
        var streng = this.index + this.timestamp + this.data + this.previous_hash
        return streng.hashCode()
    }
}

function lavGenesisBlock() {
    return new Block(0, "01-01-2009", "Genesis Block", "0")
}

function newBlock(lastBlock) {
    var thisIndex = lastBlock.index + 1
    var thisTimestamp = "02-01-2009"
    var thisData = "Hej! Jeg er block"+thisIndex
    var thisHash = lastBlock.hash

    return new Block(thisIndex, thisTimestamp, thisData, thisHash)
}


var blockchain = [lavGenesisBlock()]
var previousBlock = blockchain[0]

var antal = 20

for (let i = 0; i < antal; i++) {
    var blockToAdd = newBlock(previousBlock)
    blockchain.push(blockToAdd)
    previousBlock = blockToAdd
    console.log("tilføjet: "+blockToAdd.index)
    console.log("hashish: "+blockToAdd.hash)
}
