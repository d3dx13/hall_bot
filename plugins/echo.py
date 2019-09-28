from kutana import Plugin


plugin = Plugin(
    name="Echo",
    cmds=("echo <text> // reply with specified text",)
)


@plugin.on_startswith_text("echo ", "эхо ")
async def _(message, env):
    print(message)

    if not env.body:
        await env.reply("You didn't specified text.")
        return

    await env.reply("{}".format(env.body))
