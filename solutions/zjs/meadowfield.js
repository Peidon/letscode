const roads = [
    "Alice's House-Bob's House", "Alice's House-Cabin",
    "Alice's House-Post Office", "Bob's House-Town Hall",
    "Daria's House-Ernie's House", "Daria's House-Town Hall",
    "Ernie's House-Grete's House", "Grete's House-Farm",
    "Grete's House-Shop", "Marketplace-Farm",
    "Marketplace-Post Office", "Marketplace-Shop",
    "Marketplace-Town Hall", "Shop-Town Hall"
];

/**
 * 
 * @param {string array} edges
 * @returns <string, list<string>>
 */
function buildGraph(edges) {
    let graph = Object.create(null)
    function addEdge(from, to) {
        if (from in graph) {
            graph[from].push(to);
        } else {
            graph[from] = [to];
        }
    }

    for (let [from, to] of edges.map(r => r.split("-"))) {
        addEdge(from, to);
        addEdge(to, from);
    }

    return graph;
}

// build Adjacency matrix
const roadGraph = buildGraph(roads)



class VillageState {
    constructor(place, parcels) {
        this.place = place; // location of the village state

        /**
         *  parcel list
         *  each parcel has current location and a destination address
         *  {place, address}
         */
        this.parcels = parcels;


    }

    /**
     * 
     * @param {string} destination 
     * @returns 
     */
    move(destination) {

        // if there is no direct path to destination
        if (!roadGraph[this.place].includes(destination)) {
            return this;
        }

        // filter parcels which is not yet reached the destination
        let parcels = this.parcels.map(p => {
            if (p.place == this.place) {
                p.place = destination;
            }
            return p;
        }).filter(p => p.place != p.address);

        // return current village
        return new VillageState(destination, parcels);
    }
}

function randomPick(array) {
    let choice = Math.floor(Math.random() * array.length);
    return array[choice];
}

/**
 * 
 * @param {VillageState} state 
 * @returns Robot who just has a direction
 */
function randomRobot(state) {
    return { direction: randomPick(roadGraph[state.place]) };
}


/**
 * The robot keeps the rest of its route in its memory 
 * and drops the first element every turn.
 * @param {VillageState} state 
 * @param {string list} memory 
 * @returns 
 */
function routeRobot(state, memory) {
    adjs = roadGraph[state.place].filter(item => !memory.includes(item));
    memory.push(...adjs);
    return { direction: memory[0], memory: memory.slice(1) };
}

/**
 * 
 * @param {list<list<string>>} graph : the Adjacency matrix
 * @param {string} from 
 * @param {string} to 
 * @returns 
 */
function findRoute(graph, from, to) {
    let work = [{ at: from, route: [] }];
    for (let i = 0; i < work.length; i++) {
        let { at, route } = work[i];
        for (let place of graph[at]) {
            if (place == to) return route.concat(place);
            if (!work.some(w => w.at == place)) {
                work.push({ at: place, route: route.concat(place) });
            }
        }
    }
}

function runRobot(state, robot) {

    memory = []

    for (let turn = 0; ; turn++) {
        if (state.parcels.length == 0) {
            console.log(`Done in ${turn} turns`);
            break;
        }
        let action = robot(state, memory);
        state = state.move(action.direction);
        memory = action.memory;
        console.log(`Moved to ${action.direction}`);
    }
}

VillageState.random = function (parcelCount = 5) {
    let parcels = [];
    for (let i = 0; i < parcelCount; i++) {
        let address = randomPick(Object.keys(roadGraph));
        let place;
        do {
            place = randomPick(Object.keys(roadGraph));
        } while (place == address);
        parcels.push({ place, address });
    }
    return new VillageState("Post Office", parcels);
};

runRobot(VillageState.random(), randomRobot);
