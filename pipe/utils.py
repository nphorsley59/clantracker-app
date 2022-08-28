from datetime import date
import os
from config import Config


def export_with_timestamp(df, path):
    timestamp = str(date.today().strftime("%Y%m%d_%H%M%S"))
    versioned_path = f"{os.path.splitext(path)[0]}" \
                     f"--{timestamp}{os.path.splitext(path)[-1]}"
    df.to_csv(os.path.join(Config.PROJECT_DIR, versioned_path))
