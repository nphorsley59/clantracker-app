from datetime import datetime
import os
from config import Config


def export(df, path, timestamped_copy=False):
    df.to_csv(os.path.join(Config.PROJECT_DIR, path))
    if timestamped_copy:
        timestamp = str(datetime.now().strftime("%Y%m%d_%H%M%S"))
        versioned_path = f"{os.path.splitext(path)[0]}" \
                         f"--{timestamp}{os.path.splitext(path)[-1]}"
        df.to_csv(os.path.join(Config.PROJECT_DIR, versioned_path))
