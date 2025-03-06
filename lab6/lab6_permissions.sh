#!/bin/bash

# Step 1: Create a test file
echo "Creating file.txt..."
touch file.txt

# Step 2: Show default permissions
echo "Default permissions:"
ls -la file.txt

# Step 3: Change file permissions to 754 (rwxr-xr--)
echo "Changing permissions to 754..."
chmod 754 file.txt

# Step 4: Show updated permissions
echo "Updated permissions:"
ls -la file.txt

# Step 5: Create a new group and user
echo "Creating a new group named 'testgroup'..."
sudo groupadd testgroup

echo "Creating a new user 'testuser'..."
sudo useradd -m -G testgroup testuser

# Step 6: Change file ownership to new user
echo "Changing file owner to testuser..."
sudo chown testuser file.txt

# Step 7: Change file group ownership
echo "Changing file group to testgroup..."
sudo chgrp testgroup file.txt

# Step 8: Display final file 

