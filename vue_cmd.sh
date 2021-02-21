# Starts a console with acces to the vue cli.
#
# Created a new Vue.js project via
#   vue create --default -m npm --no-git todo_webui
# Afterwards, copy the newly generated todo_webui/ contents to this level and
# allowed the dev container todo_webui_vue.configfile to install its
# dependencies.
#
# Run the service in a development mode:
# npm run serve

PWD=`pwd`

docker run --rm -it -v $PWD:/src -p 8082:8080 todo_webui_vue:latest /bin/bash
