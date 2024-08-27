# Description: This script is used to build the project

# Change into our project directory
cd /django-jet-reboot

# Install the required python packages
pip install --upgrade pip
pip install --no-cache-dir -r requirements.txt

# Install the required system packages
apt-get update && apt-get install -y curl && apt-get install -y git && apt-get install -y gettext
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash

# This is required to use nvm without having to logout and log back in
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion

# Install nodejs
nvm install 6.17.1

echo "Node version: $(node -v)"
echo "NPM version: $(npm -v)"

# Install the required node packages
echo "Running npm install"
npm install

# Build the project
echo "Running gulp build"
node_modules/gulp/bin/gulp.js build