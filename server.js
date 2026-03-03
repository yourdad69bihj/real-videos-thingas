const io = require('socket.io')(3000, { cors: { origin: "*" } });

let waitingUser = null;

io.on('connection', (socket) => {
    socket.on('join-lobby', (myPeerId) => {
        if (waitingUser && waitingUser.id !== socket.id) {
            // MATCH FOUND!
            io.to(waitingUser.id).emit('match', myPeerId); // Tell the first guy to call the new guy
            waitingUser = null;
        } else {
            waitingUser = { id: socket.id, peerId: myPeerId };
        }
    });

    socket.on('disconnect', () => {
        if (waitingUser && waitingUser.id === socket.id) waitingUser = null;
    });
});