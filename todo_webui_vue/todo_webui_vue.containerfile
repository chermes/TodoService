# vim:set et sw=4 ts=4 ft=dockerfile:
# Development container to create, compile and run the frontend.

FROM node

RUN npm install -g @vue/cli
RUN npm install -g vue-generate-component

RUN mkdir /src
WORKDIR /src

EXPOSE 8080

CMD ["/bin/bash"]
