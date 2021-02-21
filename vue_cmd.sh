# Starts a console with access to the vue cli and node package manager.
#
# Created a new Vue.js project via (and one level above)
#   vue create --default -m npm --no-git todo_webui
#
# Run the service in a development mode:
# npm run serve

PWD=`pwd`

docker run --rm -it -v $PWD:/src -p 8082:8080 todo_webui_vue:latest /bin/bash
