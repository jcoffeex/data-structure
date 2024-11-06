class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Playlist:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_song(self, song_path):
        new_node = Node(song_path)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        
        else:
            self.tail.next = new_node
            new_node.prev = self.tail = self.tail
            self.tail = new_node

    def play_songs(self):
        current = self.head

        while current:
            prev_song = current.prev.data if current.prev else "Nenhuma música anterior"
            print(f"Tocando: {current.data} | Música anterior: {prev_song}")
            current = current.next
playlist = Playlist()
playlist.add_song("Song 1")
playlist.add_song("Song 2")
playlist.add_song("Song 3")

playlist.play_songs()