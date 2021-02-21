# Starts a console with access to the vue cli and node package manager.
#
# Created a new Vue.js project via (and one level above)
#   vue create --default -m npm --no-git todo_webui
#
# Run the service in a development mode:
# npm run serve

SRC_DIR=`pwd`/../todo_webui

docker run --rm -it -v $SRC_DIR:/src -p 8082:8080 -u $(id -u):$(id -u) todo_webui_vue:latest /bin/bash
