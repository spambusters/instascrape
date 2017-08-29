import sqlite3


class Database:
    """Write instagram posts to database"""

    def __init__(self, user):
        """Initialize the database"""
        self.conn = sqlite3.connect(f'{user}.db')
        self.cur = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cur.execute(('CREATE TABLE IF NOT EXISTS users(date TEXT,'
                          ' time TEXT, type TEXT, code TEXT, likes INT,'
                          ' location TEXT, caption TEXT)'))

    def write(self, date, time, post_type, code, likes, location, caption):
        """Insert entries into Database

        :param date: The date the post was created
        :param date: The time the post was created
        :param post_type: Post type (image, video)
        :param code: The instagram share link code (instagram.com/p/{code]})
        :param likes: The number of likes the post has
        :param location: Tagged post location
        :param caption: Post caption

        """
        self.cur.execute('INSERT INTO users VALUES(?, ?, ?, ?, ?, ?, ?)',
                         (date, time, post_type, code, likes,
                          location, caption))

    def commit(self):
        """Commit all DB changes and close it"""
        self.conn.commit()
        self.conn.close()
