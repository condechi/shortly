import datetime
from app.models import Base, engine, SessionLocal, Link

# 1. (Re)create tables in a new, in-memory DB for demo purposes
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# 2. Open a session
db = SessionLocal()

# 3. Create a new Link via the classmethod
link = Link.create("https://example.com/very/long/url")
db.add(link)
db.commit()

print("Created Link:")
print(f"  ID:   {link.id}")
print(f"  Code: {link.code}")
print(f"  URL:  {link.original_url}")
print(f"  Created at: {link.created_at}")

# 4. Query it back
queried = db.query(Link).filter_by(code=link.code).first()
print("\nQueried Link:")
print(f"  Clicks: {queried.click_count}")
print(f"  Last accessed: {queried.last_accessed}")

# 5. Simulate a redirect: increment click_count and set last_accessed
queried.click_count += 1
queried.last_accessed = datetime.datetime.now(datetime.timezone.utc)
db.commit()

print("\nAfter simulating one visit:")
print(f"  Clicks: {queried.click_count}")
print(f"  Last accessed: {queried.last_accessed}")




# 6. Clean up
db.close()





