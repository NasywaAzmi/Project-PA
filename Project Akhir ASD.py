# definisi class playlist
class Playlist:
    def __init__(self, title, artist, genre, duration):
        self.title = title
        self.artist = artist
        self.genre = genre
        self.duration = duration

# Define PlaylistCollection class
class PlaylistCollection:
    def __init__(self):
        self.playlists = []
        self.stack = []
    
    def add_playlist(self, playlist):
        self.playlists.append(playlist)
        self.stack.append(playlist)
    
    def remove_playlist(self):
        if len(self.playlists) > 0:
            playlist = self.playlists.pop()
            self.stack.remove(playlist)
            return playlist
        else:
            return None
    
    def search_playlist(self, title):
        for playlist in self.stack[::-1]:
            if playlist.title == title:
                return playlist
        return None
    
    def get_all_playlists(self):
        return self.playlists
    
    def sort_playlists(self):
        # Algoritma Quick sort akan mensortir playlist dari durasi
        def quick_sort(array):
            less = []
            equal = []
            greater = []

            if len(array) > 1:
                pivot = array[0].duration
                for playlist in array:
                    if playlist.duration < pivot:
                        less.append(playlist)
                    elif playlist.duration == pivot:
                        equal.append(playlist)
                    else:
                        greater.append(playlist)
                return quick_sort(less)+equal+quick_sort(greater)
            else:
                return array

        self.playlists = quick_sort(self.playlists)
        self.stack = self.playlists.copy()
    
    #menggunakan jump search
    def jump_search(self, title):
        n = len(self.stack)
        step = int(n**0.5)
        prev = 0
        while self.stack[min(step, n)-1].title < title:
            prev = step
            step += int(n**0.5)
            if prev >= n:
                return None
        while self.stack[prev].title < title:
            prev += 1
            if prev == min(step, n):
                return None
        if self.stack[prev].title == title:
            return self.stack[prev]
        return None

collection = PlaylistCollection()

users = {
    "john": "12345",
    "jeane": "12345"
}

# Login user
while True:
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    
    if username in users and users[username] == password:
        print("Login berhasil!")
        break
    else:
        print("Username atau password salah.")



# fungsi menu tampilan
def menu():
    while True:
        print('''
        I===========================================I
        I    * * * Youtube Music Playlist * * *     I
        I===========================================I
        Pilihan :
        1: Menambahkan Vidio Kedalam Playlist
        2: Hapus Playlist
        3: Cari Playlist
        4: Lihat Playlist
        5: Sort Playlist
        6: Keluar
        ============================================
        ''')
        
        choice = input("\nMasukkan pilihan (1-6): ")
        
        if choice == "1":
            print("\n=== Add a playlist ===")
            title = input("Masukkan Judul Playlist: ")
            artist = input("Masukkan artis dari playlist: ")
            genre = input("Masukkan Genre dari Playlist: ")
            duration = int(input("Masukkan durasi dari playlist(detik): "))
            playlist = Playlist(title, artist, genre, duration)
            collection.add_playlist(playlist)
            print("\nPlaylist Berhasil Ditambahkan")
        
        elif choice == "2":
            print("\n=== Menghapus Playlist ===")
            playlist = collection.remove_playlist()
            if playlist is not None:
                print("\nPlaylist Berhasil Dihapus")
                print("- Title:", playlist.title, "| Artist:", playlist.artist, "| Genre:", playlist.genre, "| Duration:", playlist.duration)
            else:
                print("\nPlaylist Kosong")

        elif choice == "3":
            print("\n=== Cari Playlist ===")
            title = input("Masukkan Judul Playlist: ")
            playlist = collection.jump_search(title)
            if playlist is not None:
                print("\nPlaylist Ditemukan:")
                print("- Title:", playlist.title, "| Artist:", playlist.artist, "| Genre:", playlist.genre, "| Duration:", playlist.duration)
            else:
                print("\nPlaylist tidak ditemukan")

        elif choice == "4":
            print("\n=== Lihat Semua Playlist ===")
            playlists = collection.get_all_playlists()
            if len(playlists) > 0:
                for playlist in playlists:
                    print("- Title:", playlist.title, "| Artist:", playlist.artist, "| Genre:", playlist.genre, "| Duration:", playlist.duration)
            else:
                print("\nPlaylist Kosong")

        elif choice == "5":
            print("\n=== Sort Playlist Dari Durasi ===")
            collection.sort_playlists()
            print("\nPlaylist telah di sorting")

        elif choice == "6":
            print("\nAnda Berhasil Keluar")
            exit()

        else:
            print("\nPilihan Tidak Ditemmukan!")

# memanggil fungsi menu
menu()

