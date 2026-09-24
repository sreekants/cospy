# COSSERVICE(1)

## NAME

**cosservice** — inspect the services of a running COS simulation

## SYNOPSIS

```
python cosservice.py [-h | -?] command [arguments]
```

## DESCRIPTION

**cosservice** is a command-line client for the object manager of a
simulation started with **coslaunch**(1). Every subsystem, builder, faculty
and service loaded by the kernel is registered under a path such as
`/Services/Kernel/World`. Each command sends one RPC request to the server on
`localhost:5556`, prints the result and exits.

With no command, **cosservice** prints a usage summary.

## OPTIONS

**-h**, **-?**, **-help**
: Print a usage summary and exit.

## COMMANDS

**list**
: Print the path of every registered service, one per line.

**info** *path*
: Print the class, module, ID, type, path and IPC topic of the service at
  *path*. When the server runs in debug mode, it also prints the source file.

## EXIT STATUS

**cosservice** exits with status 0 whether or not the command succeeded.
Errors from the server are printed with an `ERROR :` prefix. Unknown commands
print `Unknown command: name`.

## EXAMPLES

List the services:

```
$ python cosservice.py list
/Services/Kernel/NetworkManager
/Services/Kernel/DataManager
/Services/Kernel/World
/Services/Builder/Land/Map
...
```

Describe one service:

```
$ python cosservice.py info /Services/Kernel/World
 Class:		World
 Module:	cos.subsystem.world.World
 ID:		World
 Type:		Services.Kernel
 Path:		/Services/Kernel/World
 IPC:		/Services/Kernel/World
```

## BUGS

**cosservice** always connects to `localhost:5556`, so it cannot reach a
remote server or one started with `coslaunch -port`.

The help output lists **call**, **find** and **type**, but they are not
implemented and print `Unknown command`. It also prints every command with a
leading dash (`-list`), although commands are given without one. It calls
the program a "Skeleton documentation generator".

## SEE ALSO

**coslaunch**(1), **costopic**(1), **cviz**(1)
