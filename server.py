const { PeerServer } = require('peer');
const server = PeerServer({ port: 9000, path: '/js-elite' });

let waitingLobby = [];

server.on('connection', (client) => {
    const clientId = client.getId();
    console.log('User joined:', clientId);

    // If someone is already waiting, pair them
    if (waitingLobby.length > 0) {
        const partnerId = waitingLobby.shift();
        console.log(`Matching ${clientId} with ${partnerId}`);
        // We broadcast a custom message or let the client handle it
    } else {
        waitingLobby.push(clientId);
    }
});

server.on('disconnect', (client) => {
    waitingLobby = waitingLobby.filter(id => id !== client.getId());
});