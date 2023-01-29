const myName = {
    firstName : 'Jacob',
    lastName : 'Dintu',
    otherName : 'Gregory'
};

for (const item in myName ) {
    console.log('item:', item)
    console.log('value:', myName[item])
}