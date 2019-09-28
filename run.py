import json

from kutana import (Kutana, TGManager, VKManager, load_plugins)


# Create engine
app = Kutana()


# Load configuration and available plugins
with open("config.json", "r") as fh:
    config = json.load(fh)

app.config["names"] = config["info"]["names"]


# Register plugins
app.register_plugins(load_plugins("plugins/"))


# Add managers from configuration
for manager_conf in config["managers"]:
    manager = None

    if manager_conf["type"] == "vkontakte":
        manager = VKManager

    elif manager_conf["type"] == "telegram":
        manager = TGManager

    if manager is None:
        raise ValueError(
            "Unknown manager type: {}".format(manager_conf["type"])
        )

    kwargs = manager_conf
    kwargs.pop("type")

    app.add_manager(manager(**kwargs))

# Start engine if this file was run
if __name__ == "__main__":
    app.run()
