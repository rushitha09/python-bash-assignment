#!/bin/bash

# Source log directory
SOURCE="logs"

# Archive directory
ARCHIVE_DIR="archive"

# Create archive directory if it doesn't exist
mkdir -p "$ARCHIVE_DIR"

# Archive file name with timestamp
ARCHIVE_FILE="$ARCHIVE_DIR/logs_backup_$(date +%Y%m%d_%H%M%S).tar.gz"

echo "Searching for log files older than 30 days..."

# Find files older than 30 days
OLD_FILES=$(find "$SOURCE" -type f -mtime +30)

# Check if any old files exist
if [ -z "$OLD_FILES" ]; then
    echo "No old files found."
    exit 0
fi

# Create archive
tar -czf "$ARCHIVE_FILE" $OLD_FILES

# Verify archive creation
if [ $? -eq 0 ]; then
    echo "Archive created successfully."

    # Delete original files
    find "$SOURCE" -type f -mtime +30 -delete

    echo "Original files deleted successfully."
else
    echo "Archive creation failed. Original files were not deleted."
fi