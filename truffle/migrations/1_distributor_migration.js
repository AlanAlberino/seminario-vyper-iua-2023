var Distributor = artifacts.require("distributor");
module.exports = function(deployer) {
    deployer.deploy(Distributor)
}