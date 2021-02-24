# todo_webui

## Console Container

The project uses a npm and vue-cli from within a Docker container.

```
cd todo_webui_vue
```

### Build the Console Container

```
sh vue_build.sh
```

### Run the Console Container

```
sh vue_cmd.sh
```
The working directory is then the ```todo_webui``` directory. From here you
can start the ```npm``` and ```vue-cli``` commands (see also below).

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Run your tests
```
npm run test
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
