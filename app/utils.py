import logging

def setup_logging(log_file='logs/app.log', level=logging.INFO):
    """Set up logging configuration."""
    logging.basicConfig(
        filename=log_file,
        level=level,
        format='%(asctime)s:%(levelname)s:%(message)s'
    )

def validate_compliance_data(data):
    """Validate incoming compliance data."""
    if 'regulation' not in data or 'status' not in data:
        return False
    return True
