from room import Room


def test_init():
    room = Room()
    assert room.players == []
    assert room.observers == []
    assert room.finished is False


def test_join():
    room = Room()
    room.join_player('player1')
    room.reveal()
    room.join_player('player2')
    room.join_observer('observer1')
    assert {'name': 'player1', 'choice': None} in room.players
    assert {'name': 'player2', 'choice': None} in room.players
    assert len(room.players) == 2
    assert {'name': 'observer1'} in room.observers
    assert len(room.observers) == 1
    assert not room.finished


def test_leave():
    room = Room()
    room.join_player('player1')
    room.join_player('player2')
    room.join_observer('observer1')
    room.join_observer('observer2')
    room.leave('player1')
    room.leave('observer2')
    assert {'name': 'player2', 'choice': None} in room.players
    assert len(room.players) == 1
    assert {'name': 'observer1'} in room.observers
    assert len(room.observers) == 1


def test_select():
    room = Room()
    room.join_player('player1')
    room.join_player('player2')
    room.join_observer('observer1')
    room.select('player1', 'choice1')
    assert not room.finished
    room.select('player2', 'choice2')
    assert room.finished
    assert {'name': 'player1', 'choice': 'choice1'} in room.players
    assert {'name': 'player2', 'choice': 'choice2'} in room.players
    # Select is disabled when voting is finished
    room.select('player1', 'choice2')
    assert {'name': 'player1', 'choice': 'choice1'} in room.players
    assert {'name': 'observer1'} in room.observers


def test_clear():
    room = Room()
    room.join_player('player1')
    room.join_player('player2')
    room.join_observer('observer1')
    room.select('player1', 'choice1')
    room.select('player2', 'choice2')
    room.clear()
    assert not room.finished
    assert {'name': 'player1', 'choice': None} in room.players
    assert {'name': 'player2', 'choice': None} in room.players
    assert {'name': 'observer1'} in room.observers


def test_reveal():
    room = Room()
    room.reveal()
    assert room.finished
