import uvicorn, os

from settings import settings

if not os.path.exists('./database.sqlite3'):
    # Инициализация базы данных
    from database import engine
    from tables import Base
    Base.metadata.create_all(engine)

# Запуск веб-сервиса
uvicorn.run(
    'app:app',
    host=settings.server_host,
    port=settings.server_port,
    reload=False,
)
