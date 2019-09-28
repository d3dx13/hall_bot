import re

from kutana import Message, Plugin


plugin = Plugin(name="Prefix", priority=5)


@plugin.on_startup()
async def _(app):
    plugin.names = tuple(app.config["names"])
    plugin.separators = (" ", ",", ".", "!", "?")

    plugin.pattern = re.compile(
        "^\\s*" +
        "(" + "|".join(re.escape(n) for n in plugin.names) +  ")" +
        "(" + "|".join(re.escape(s) for s in plugin.separators) + ")?" +
        "( |\n)?(?P<text>.*)",
        re.IGNORECASE
    )


@plugin.on_has_text()
async def _(message, env):
    match = plugin.pattern.match(message.text)

    if message.from_id != message.peer_id:
        mention_match = re.search(
            r"\[[a-zA-Z0-9]+\|.+?\]",
            message.raw_update["object"]["text"]
        )

    else:
        mention_match = None

    if not (mention_match or match and match.group("text")):
        return "DONE"

    env.parent.set_message(
        Message(
            match and match.group("text") or message.text,
            message.attachments,
            message.from_id,
            message.peer_id,
            message.date,
            message.raw_update
        )
    )

    return "GOON"
