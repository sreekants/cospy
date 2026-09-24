# COSLAUNCH(1)

## NAME

**coslaunch** — start the COS simulation server

## SYNOPSIS

```
python coslaunch.py [-h | -?] [-c | -config path] [-i | -image file] [-p | -port port]
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
  invalid.

## EXAMPLES

Run the default configuration from the configuration directory:

```
cd $COS_CONFIG && python $COS_ROOT/apps/coslaunch/coslaunch.py
```

Run a specific scenario:

```
python coslaunch.py -config $COS_ROOT/config/simulation/no/alesund/cos.ini
```

Run a second simulation next to one already on the default ports, then
attach a visualiser to it:

```
python coslaunch.py -config /path/to/cos.ini -port 6556
python ../cviz/cviz.py host localhost:6556
```

## BUGS

**-d** is accepted but has no effect.

**costopic**(1) and **cosservice**(1) always connect to port 5556 on
`localhost`, so they cannot reach a server started with a different **-port**.

## SEE ALSO

**cviz**(1), **costopic**(1), **cosservice**(1)
