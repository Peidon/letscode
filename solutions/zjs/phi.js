// phi coefficient

function phi(table) {
    return (table[3]*table[0] - table[1]*table[2]) /
    Math.sqrt((table[3]+table[2]) * 
    (table[3] + table[1]) * 
    (table[1] + table[0]) * 
    (table[0] + table[2]));
}

// 76 no squirrel, no pizza.
// 9 no squirrel, pizza.
// 4 squirrel, no pizza.
// 1 squirrel, pizza.
console.log(phi([76, 9, 4, 1]));