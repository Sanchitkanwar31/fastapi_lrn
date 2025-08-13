from logging.config import fileConfig
import os
import sys

from sqlalchemy import engine_from_config, pool
from alembic import context

# --- Add project root to PYTHONPATH ---
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.model import Base
from app.config import settings

# This Alembic Config object provides access to values in alembic.ini
config = context.config

# ✅ Set SQLAlchemy URL dynamically from settings.py
config.set_main_option(
    "sqlalchemy.url",
    f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"

)

# Setup logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# ✅ Point Alembic to your models' metadata
target_metadata = Base.metadata

def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
