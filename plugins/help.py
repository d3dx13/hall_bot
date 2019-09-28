from kutana import Plugin


plugin = Plugin(
    name="Help",
    cmds=("help // show available commands",)
)


@plugin.on_startup()
async def _(app):
    lines = []

    def add(line=""):
        lines.extend(line.split("\n"))

    plain_plugins = []

    add("🌲 Kubot_\n")

    for plugin in app.registered_plugins:
        if not hasattr(plugin, "cmds"):
            plain_plugins.append(plugin)
            continue

        add("\n☁ {}".format(plugin.name))

        for command in plugin.cmds:
            add("👉🏻 {}".format(command))

    lines.append("\n☁ Other pluins:\n{}".format(
        " // ".join(pl.name for pl in plain_plugins)
    ))

    plugin.help_text = "\n".join(lines)


@plugin.on_text("help")
async def _(message, env):
    await env.reply(plugin.help_text)
