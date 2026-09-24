# CVIZ(1)

## NAME

**cviz** — visualise a running COS simulation

## SYNOPSIS

```
python cviz.py [-h | -?] [host hostname:port]
```

## DESCRIPTION

**cviz** opens a window that draws the map, the zones and the vessels of a
simulation started with **coslaunch**(1). It uses two connections to the server:

- RPC requests to *hostname*:*port* (default `localhost:5556`), used to
  fetch the map and the world;
- a subscription to IPC events on *hostname*:*port*+1 (default
  `localhost:5557`), which moves the vessels and updates the weather.

**cviz** must be run from its own directory, because it loads images and
sounds from the relative paths `img/` and `audio/`.

## OPTIONS

**-h**, **-?**, **-help**
: Print a usage summary and exit.

## COMMANDS

**host** *hostname*:*port*
: Connect to the server at *hostname* and RPC port *port*, and receive events
  on *port*+1. It must come after any options. Use it to reach a remote
  server, or one started with `coslaunch -port`.

## CONTROLS

| Key | Action |
|---|---|
| Arrow keys | Pan the map for as long as the key is held |
| **+** / **=** | Zoom in while held |
| **-** | Zoom out while held |
| CTRL+Z | Show or hide zones (TSS, fairways, harbours, …) |
| CTRL+D | Show or hide the debug information box |
| ESC | Quit |

## ENVIRONMENT

**cviz** reads no environment variables: the map and the world are fetched
from the server over RPC. The `cos` package (under `src/`) must be
importable.

## EXAMPLES

Visualise a simulation on the local machine:

```
cd $COS_ROOT/apps/cviz && python cviz.py
```

Visualise a simulation started with `coslaunch -port 6556`:

```
python cviz.py host localhost:6556
```

Visualise a simulation on another machine:

```
python cviz.py host simhost.example.org:5556
```

## BUGS

**-d** is accepted but has no effect. **-i** takes an argument that is ignored.

## SEE ALSO

**coslaunch**(1), **costopic**(1), **cosservice**(1)
