# Traefik JAM stack example configuration

This repository contains an example configuration for a [JAM stack][]
application suite which is being load-balanced behind a single endpoint using
[Traefik][].

The stack is built with [docker-compose][], and includes the following
services:

- `traefik` - Traefik proxy service
- `webapi` - Dynamic web application
- `webstatic` - Nginx server for static files

# Services

## Traefik

The traefik proxy service is responsible for handling HTTP requests and passing
them to the appropriate downstream service. The downstream services are
[detected automatically][] through docker labels.

## Web API

The API service is written in Python using the [Flask][] web framework, but
only exists to serve as an example. Any server-side web application could be
used in its place.

Web requests whose responses need to be dynamically generated are handled by
this service.

## Static web server

This static web service is using [nginx][] under the hood, but could just as
easily use something more familiar to you (e.g. caddy, lighttpd, etc.).

Web requests whose responses are static (HTML, CSS, JS, images, etc.) are
handled by this service, relieving the web API of this responsibility and
managing it with a much more capable application.


[Traefik]: https://traefik.io/
[JAM stack]: https://jamstack.org/
[docker-compose]: https://docs.docker.com/compose/
[detected automatically]: https://doc.traefik.io/traefik/providers/docker/#routing-configuration-with-labels
[Flask]: https://flask.palletsprojects.com/
[nginx]: https://nginx.org/
