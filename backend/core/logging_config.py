import logging
import os

LOG_DIR = "log/nexus_monitor_production"
os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[logging.FileHandler(f"{LOG_DIR}/app.log"), logging.StreamHandler()],
)
logger = logging.getLogger("nexus")