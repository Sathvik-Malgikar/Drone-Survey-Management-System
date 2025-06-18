import pytest
from main import DatabaseManager

TEST_DB_PATH = ":memory:"

@pytest.fixture
async def test_db():
    """Create a test database"""
    db = DatabaseManager(TEST_DB_PATH)
    await db.init_db()
    return db

@pytest.mark.asyncio
async def test_database_initialization(test_db):
    """Test database table creation"""
    async with test_db.connect() as db:
        cursor = await db.execute("""
            SELECT name FROM sqlite_master 
            WHERE type='table' AND name IN ('organizations', 'drones', 'missions')
        """)
        tables = await cursor.fetchall()
        assert len(tables) == 3

@pytest.mark.asyncio
async def test_sample_data_insertion(test_db):
    """Test sample data insertion"""
    async with test_db.connect() as db:
        # Check organizations
        cursor = await db.execute("SELECT COUNT(*) FROM organizations")
        org_count = (await cursor.fetchone())[0]
        assert org_count >= 1
        
        # Check drones
        cursor = await db.execute("SELECT COUNT(*) FROM drones")
        drone_count = (await cursor.fetchone())[0]
        assert drone_count >= 1

@pytest.mark.asyncio
async def test_data_retrieval(test_db):
    """Test data retrieval from the database"""
    async with test_db.connect() as db:
        cursor = await db.execute("SELECT * FROM drones")
        drones = await cursor.fetchall()
        assert isinstance(drones, list)

@pytest.mark.asyncio
async def test_data_deletion(test_db):
    """Test data deletion from the database"""
    async with test_db.connect() as db:
        await db.execute("DELETE FROM drones WHERE id = 'test_drone_001'")
        cursor = await db.execute("SELECT COUNT(*) FROM drones WHERE id = 'test_drone_001'")
        count = (await cursor.fetchone())[0]
        assert count == 0