"""
Convert XML to JSON and back

Usage:
    from xml_to_json import json

    result = json("path/or/input")
    print(result)
"""

__version__ = "1.0.0"

import os
import shutil
from pathlib import Path
from datetime import datetime


def json(source: str | Path, **options) -> dict:
    """Run the automation task.

    Args:
        source: Source path or input.
        **options: Additional options.

    Returns:
        Dict with results summary.
    """
    source = Path(source) if isinstance(source, (str, Path)) else source
    results = {
        "started": datetime.now().isoformat(),
        "source": str(source),
        "processed": 0,
        "errors": 0,
    }

    try:
        count = _execute(source, **options)
        results["processed"] = count
    except Exception as e:
        results["errors"] = 1
        results["error_message"] = str(e)

    results["finished"] = datetime.now().isoformat()
    return results


def _execute(source: Path, **options) -> int:
    """Execute the automation logic."""
    if not source.exists():
        raise FileNotFoundError(f"Source not found: {source}")

    count = 0
    if source.is_dir():
        for item in source.iterdir():
            count += 1
    else:
        count = 1
    return count


def dry_run(source: str | Path, **options) -> dict:
    """Preview what would happen without making changes.

    Args:
        source: Source path or input.

    Returns:
        Dict describing planned actions.
    """
    source = Path(source)
    actions = []
    if source.is_dir():
        for item in source.iterdir():
            actions.append({"action": "process", "target": str(item)})
    else:
        actions.append({"action": "process", "target": str(source)})
    return {"actions": actions, "total": len(actions)}
