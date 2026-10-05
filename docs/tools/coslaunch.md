# COSLAUNCH(1)

## NAME

**coslaunch** — start the COS simulation server

## SYNOPSIS

```
python coslaunch.py [-h | -?] [-c | -config path] [-i | -image file] [-p | -port port]
              [-b | -bridge port] [-e | -environment "KEY=value:..."]
```

## DESCRIPTION

**coslaunch** loads a simulation configuration (`cos.ini`), boots the COS
kernel with the subsystems, faculties and services it names, and runs the
simulation until interrupted with CTRL+C.

While it runs, the server accepts RPC requests on one TCP port and publishes
IPC events on the next port up. Clients such as **cviz**(1), **costopic**(1)
and **cosservice**(1) talk to it on those ports.

The first log line after the banner reports the configuration file in use:

```
(Kernel) Loading simulation from /path/to/cos.ini
```

When **-environment** overrides a variable, a warning for each override is
logged just before that line:

```
(Kernel) *** OVERRIDE TRAFFIC=ldta replaces the value in the configuration file ***
```

## OPTIONS

Long options can be written with one dash (`-config`) or two (`--config`),
and their value can follow as a separate argument or after `=`
(`-config=path`).

**-h**, **-?**, **-help**
: Print a usage summary and exit.

**-c** *path*, **-config** *path*
: Load the simulation from the `cos.ini` file at *path*. A relative path is
  resolved against the current directory. When omitted, **coslaunch** looks
  for `cos.ini` in the current directory, then in `$COS_CONFIG`. The program
  exits if *path* is not a file.

**-i** *file*, **-image** *file*
: Boot from a boot image: a tar archive that contains `cos.ini` at its root.
  The configuration is read from inside the image, so **-config** should not
  be given together with **-image**. The program exits if *file* is not a
  file.

**-p** *port*, **-port** *port*
: Listen for RPC requests on *port* and publish IPC events on *port*+1. This
  overrides the `port=` setting of the RPC transport in `network.yaml`. Use it
  to run more than one simulation on the same host. *port* must be a number
  between 1 and 65534.

**-b** *port*, **-bridge** *port*
: Serve the bridge display and its RPC endpoint on HTTP *port*. This overrides
  the `port=` setting of `BridgeServer` in `network.yaml` (default 8756). Use it
  with **-port** when running more than one simulation on the same host. Open
  `http://localhost:`*port*`/` in a browser; see **bridge**(7).

**-e** *settings*, **-environment** *settings*
: Override variables in the `[EnvironmentVariables]` section of `cos.ini`.
  *settings* is a list of `KEY=value` pairs separated by `:`, e.g.
  `"TRAFFIC=ldta:WEATHER=clearsky"`. Keys are case-insensitive. A value may
  contain commas (`TRAFFIC=ldta,fleet`) but not `:`. The overrides are
  applied before the variables are resolved, so variables derived from them,
  such as `SCENARIO`, use the new values. A key not in `cos.ini` is added.
  Quote *settings* on the command line. The program exits if a setting is not
  of the form `KEY=value`.

## ENVIRONMENT

**COS_ROOT**
: Root of the COS installation. `cos.ini` files refer to it as `$(COS_ROOT)`.

**COS_CONFIG**
: Configuration directory. It is searched for `cos.ini` when **-config** is not
  given, and `cos.ini` files refer to it as `$(COS_CONFIG)`.

The `cos` package (under `src/`) must be importable.

## FILES

`cos.ini`
: The simulation configuration. It names the folders, scenario variables and
  the YAML files that define each subsystem.

`$COS_CONFIG/network.yaml`
: Configures the RPC broker. Its `config:` line selects the transport and
  may set `port=`. The default port is 5556.

## EXIT STATUS

**0**
: Normal shutdown after CTRL+C, or after help was printed. An unrecognised
  option also prints help and exits with 0.

**255**
: The configuration file, image file or port given on the command line is
  invalid, or a **-environment** setting is not of the form `KEY=value`.

## EXAMPLES

Run the default configuration from the configuration directory:

```
cd $COS_CONFIG && python $COS_ROOT/apps/coslaunch/coslaunch.py
```

Run a specific scenario:

```
python coslaunch.py -config $COS_ROOT/config/simulation/no/alesund/cos.ini
```

Run a scenario with a different traffic model and weather than its
`cos.ini` sets:

```
python coslaunch.py -config $COS_ROOT/config/simulation/no/trondheim/cos.ini \
    -environment "TRAFFIC=ldta:WEATHER=clearsky"
```

Run a second simulation next to one already on the default ports, then
attach a visualiser to it:

```
python coslaunch.py -config /path/to/cos.ini -port 6556 -bridge 6756
python ../cviz/cviz.py host localhost:6556
```

and open the bridge display at `http://localhost:6756/`.

## BUGS

**-d** is accepted but has no effect.

**costopic**(1) and **cosservice**(1) always connect to port 5556 on
`localhost`, so they cannot reach a server started with a different **-port**.

## SEE ALSO

**cviz**(1), **costopic**(1), **cosservice**(1), **bridge**(7) (`docs/tools/bridge.md`)
