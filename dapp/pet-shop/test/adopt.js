const Adoption = artifacts.require('Adoption');

const petId = 3;
let adoption;

contract('Adoption', async accounts => {
    beforeEach(async () => {
        adoption = await Adoption.deployed();
        await adoption.adopt(petId);
    });

    it('lets user to adopt pet', async () => {
        let returnedId = await adoption.adopt.call(petId);

        assert.equal(petId, returnedId);
    });

    it("returns pet's owner by pet id", async () => {
        let adopter = await adoption.adopters(petId);

        assert.equal(accounts[0], adopter);
    });

    it('returns all pet owners by set of pet ids', async () => {
        let adopters = await adoption.getAdopters();

        assert.equal(accounts[0], adopters[petId]);
    });
});
