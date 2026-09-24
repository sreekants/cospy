# COSTOPIC(1)

## NAME

**costopic** — inspect and use the message topics of a running COS simulation

## SYNOPSIS

```
python costopic.py [-h | -?] command [arguments]
```

## DESCRIPTION

**costopic** is a command-line client for the topic (message queue) service of
a simulation started with **coslaunch**(1). Topics are named by paths such as
`/Situation/Maritime/Encounter/Crossing`. Each command sends one RPC request to
the server on `localhost:5556`, prints the result and exits.

With no command, **costopic** prints a usage summary.

## OPTIONS

**-h**, **-?**, **-help**
: Print a usage summary and exit.

## COMMANDS

**list**
: Print the path of every topic, one per line.

**info** *topic*
: Print the properties of *topic* as a dictionary, currently the number of
  pending messages: `{'count': 1}`. It prints `{}` if the topic does not exist.

**pub** *topic* *message*
: Queue *message*, sent as a string, on *topic*.

**echo** [**-n** *count*] *topic*
: Take *count* messages (default 1) off *topic* and print each one. It checks
  once a second and waits, with no timeout, until a message arrives. Messages are removed from
  the queue, so no other reader receives them.

**route** *source* *destination*
: Route messages sent to *source* to *destination* instead.

**unroute** *source*
: Delete the route from *source*. It prints nothing, even if no route
  existed.

**find** *pattern*
: Print the topics that match the shell-style *pattern*.

**type** *topic*
: Print the type of *topic*.

## EXIT STATUS

**costopic** exits with status 0 whether or not the command succeeded. Errors
from the server are printed with an `ERROR :` prefix. Unknown commands print
`Unknown command: name`.

## EXAMPLES

List all topics:

```
python costopic.py list
```

Send a message to a topic and read it back:

```
$ python costopic.py pub /Situation/Maritime/Encounter/Crossing hello
$ python costopic.py info /Situation/Maritime/Encounter/Crossing
{'count': 1}
$ python costopic.py echo /Situation/Maritime/Encounter/Crossing
hello
```

Print the next five messages on a topic as they arrive:

```
python costopic.py echo -n 5 /Situation/Maritime/Conduct/Traffic
```

## BUGS

**costopic** always connects to `localhost:5556`, so it cannot reach a remote
server or one started with `coslaunch -port`.

**list** *prefix* fails with
`MessageQueue.__dump_node() missing 1 required positional argument`.
Only **list** without an argument works.

**find** fails on the server with
`cannot access local variable 'path'`.

**type** fails with `Failed to call method[type]`.

**route** fails with `'Tree' object has no attribute 'exists'`.

The help output names the program `cos_topic.py` and calls it a
"Skeleton documentation generator".

## SEE ALSO

**coslaunch**(1), **cosservice**(1), **cviz**(1)
