class DatabaseManager:
    """Manages database connections and operations."""
    
    def __init__(self, db_path):
        self.db_path = db_path
        self.connection = None

    async def init_db(self):
        """Initializes the database and creates necessary tables."""
        self.connection = await self.connect()
        async with self.connection:
            await self.create_tables()

    async def connect(self):
        """Establishes a connection to the database."""
        import aiosqlite
        return await aiosqlite.connect(self.db_path)

    async def create_tables(self):
        """Creates the necessary tables in the database."""
        async with self.connection:
            await self.connection.execute("""
                CREATE TABLE IF NOT EXISTS organizations (
                    id TEXT PRIMARY KEY,
                    name TEXT NOT NULL
                )
            """)
            await self.connection.execute("""
                CREATE TABLE IF NOT EXISTS drones (
                    id TEXT PRIMARY KEY,
                    name TEXT NOT NULL,
                    model TEXT NOT NULL,
                    status TEXT NOT NULL,
                    battery_level INTEGER NOT NULL,
                    location_lat REAL NOT NULL,
                    location_lng REAL NOT NULL,
                    organization_id TEXT NOT NULL,
                    last_updated DATETIME NOT NULL
                )
            """)
            await self.connection.execute("""
                CREATE TABLE IF NOT EXISTS missions (
                    id TEXT PRIMARY KEY,
                    name TEXT NOT NULL,
                    organization_id TEXT NOT NULL,
                    drone_id TEXT NOT NULL,
                    config TEXT NOT NULL,
                    status TEXT NOT NULL,
                    progress_percentage REAL NOT NULL,
                    created_at DATETIME NOT NULL
                )
            """)

    async def execute(self, query, params=None):
        """Executes a query against the database."""
        async with self.connection.execute(query, params or ()) as cursor:
            return cursor

    async def fetchall(self, query, params=None):
        """Fetches all results from a query."""
        async with self.connection.execute(query, params or ()) as cursor:
            return await cursor.fetchall()

    async def close(self):
        """Closes the database connection."""
        if self.connection:
            await self.connection.close()