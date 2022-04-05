import os
from decouple import config
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler



# Initializes your app with your bot token and socket mode handler
app = App(token=config('SLACK_BOT_TOKEN'))

# Listens to incoming messages that contain "hello"
# To learn available listener arguments,
# visit https://slack.dev/bolt-python/api-docs/slack_bolt/kwargs_injection/args.html


# The echo command simply echoes on command
@app.command("/echo")
def repeat_text(ack, respond, command):
    # Acknowledge command request
    ack()
    respond(f"{command['text']}")

@app.command("/shell_disk")
def repeat_text(ack, respond):
    # Acknowledge command request
    ack()
    os.system("sudo shell_script/slack_notify_dir_size_over_use.sh")
    respond(f"excute slack_notify_dir_size_over_use.sh")


# Start your app
if __name__ == "__main__":
    SocketModeHandler(app, config('SLACK_APP_TOKEN')).start()
