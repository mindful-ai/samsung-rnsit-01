from rich.console import Console
from rich.panel import Panel

console = Console()

events = agent.stream(
    {
        "messages": [
            {
                "role": "user",
                "content": question
            }
        ]
    },
    stream_mode="updates"
)

for event in events:

    for node, value in event.items():

        console.print()

        console.print(
            Panel.fit(
                f"{node}",
                title="Agent Step"
            )
        )

        console.print(value)