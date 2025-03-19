#!/bin/bash

CONTAINER_NAME=bd-a1-container
DEST_DIR=bd-a1/service-result

# Create result directory if not exists
mkdir -p $DEST_DIR

# Copy files from container to local machine
docker cp $CONTAINER_NAME:/home/doc-bd-a1/res_dpre.csv $DEST_DIR/
docker cp $CONTAINER_NAME:/home/doc-bd-a1/eda-in-1.txt $DEST_DIR/
docker cp $CONTAINER_NAME:/home/doc-bd-a1/eda-in-2.txt $DEST_DIR/
docker cp $CONTAINER_NAME:/home/doc-bd-a1/eda-in-3.txt $DEST_DIR/
docker cp $CONTAINER_NAME:/home/doc-bd-a1/vis.png $DEST_DIR/
docker cp $CONTAINER_NAME:/home/doc-bd-a1/k.txt $DEST_DIR/

# Optional: include raw loaded file too
docker cp $CONTAINER_NAME:/home/doc-bd-a1/res_load.csv $DEST_DIR/

# Stop the container
docker stop $CONTAINER_NAME

echo "Files copied and container stopped."
