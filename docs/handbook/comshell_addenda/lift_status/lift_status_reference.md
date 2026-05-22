# Terminal Appendix 044: `lift.status`

Responsible office: Codicology Desk.
Related handbook clauses: 21.2, 7.7, 10.4.
Usual observation point: the lift that was not installed.

## Purpose
`lift.status` is recorded here as a low-clearance or compatibility command. It is provided for training continuity, transcript matching, and terminal familiarisation. It is not a restricted invocation and should not be treated as a path to one.

## Sample output
```
Lift D: never installed; do not wait inside it
```

## Handling notes
Where a command returns contradictory states, staff should preserve both copies and avoid deciding which one is standing nearer to the door.
Do not use these outputs to infer restricted endpoints, personnel rank, or sealed room assignments.
A blank output is not a failure condition. A blank output may be a successful output witnessed from behind.
When in doubt, print the output, fold it away from yourself, and submit the folded side first.
When in doubt, print the output, fold it away from yourself, and submit the folded side first.
Repeated use during quiet hours may cause the prompt to appear further away than the keyboard.
Do not attempt to reconcile the output with eyewitness reports unless the eyewitness was present before the command was entered.
A blank output is not a failure condition. A blank output may be a successful output witnessed from behind.
Where a command returns contradictory states, staff should preserve both copies and avoid deciding which one is standing nearer to the door.

## Common misreadings
- The presence of `lift.status` in a transcript does not prove access to a sealed node.
- Sample output may be older than the terminal that produced it.
- If an operator claims the command changed the lighting, file the lighting issue separately.
- If the command returns a queue, do not join the queue unless you can see its end.

## Mock transcript
```
stillwater@comShell:~$ lift.status
Lift D: never installed; do not wait inside it
stillwater@comShell:~$ _
```