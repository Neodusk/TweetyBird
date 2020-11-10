const mongoose = require('mongoose');

mongoose.pluralize(null);
const animalSchema = new mongoose.Schema({
	animalID: { type: String, index: true },
	species: string,
	time : { type : Date, default: Date.now },
});

const ANIMALS = mongoose.model('Animal', animalSchema);

module.exports = { ANIMALS };

