const { reactive } = require('vue');
const state = reactive({
    texts: {
        flightDeparture: "DEFAULT_DEP"
    },
    days: [ { id: 1, header: 'DEFAULT_HEADER' } ]
});

const importedData = {
    state: {
        texts: { flightDeparture: "IMPORTED_DEP" },
        days: [ { id: 2, header: "IMPORTED_HEADER" } ]
    }
};

Object.assign(state, importedData.state);

console.log('Flight Departure:', state.texts.flightDeparture);
console.log('Day 0 Header:', state.days[0].header);
