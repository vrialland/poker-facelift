from room import Room


def test_init():
    room = Room()
    assert room.players == []
    assert room.finished == False


def test_join():
    room = Room()
    room.join('player1')
    room.reveal()
    room.join('player2')
    assert {'name': 'player1', 'choice': None} in room.players
    assert {'name': 'player2', 'choice': None} in room.players
    assert len(room.players) == 2
    assert not room.finished


def test_select():
    room = Room()
    room.join('player1')
    room.join('player2')
    room.select('player1', 'choice1')
    assert not room.finished
    room.select('player2', 'choice2')
    assert room.finished
    assert {'name': 'player1', 'choice': 'choice1'} in room.players
    assert {'name': 'player2', 'choice': 'choice2'} in room.players


def test_clear():
    room = Room()
    room.join('player1')
    room.join('player2')
    room.select('player1', 'choice1')
    room.select('player2', 'choice2')
    room.clear()
    assert not room.finished
    assert {'name': 'player1', 'choice': None} in room.players
    assert {'name': 'player2', 'choice': None} in room.players


def test_reveal():
    room = Room()
    room.reveal()
    assert room.finished
