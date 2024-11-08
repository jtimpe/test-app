# test-app

This repository contains a multi-tier web application, created for AWS training.

## Overview

The application contains the following layers
* `/web` - a nextjs/react application
* `/api` - a flask application
* `/worker` - another flask application (for now)
* `postgres` is also deployed in the docker compose network

## Requires

* Docker
* Nodejs/npm

## Run

```bash
cd test-app
docker compose up --build
```

In another terminal:
```bash
cd test-app/web
npm i
npm run dev
```