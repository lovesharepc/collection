import os
from decouple import config
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# Initializes your app with your bot token and socket mode handler
app = App(token=config('SLACK_BOT_TOKEN'))
# Listens to incoming messages that contain "hello"
# To learn available listener arguments,
# visit https://slack.dev/bolt-python/api-docs/slack_bolt/kwargs_injection/args.html

# 須 enable feature "Slash Commands"
@app.command("/shell_disk")
def command_shelldisk(ack, respond):
    # Acknowledge command request
    ack()
    os.system("sudo shell_script/slack_notify_dir_size_over_use.sh")
    respond("excute slack_notify_dir_size_over_use.sh")

# The echo command simply echoes on command
# respond() 不須特殊權限,但僅有該 user 看得到回應
@app.command("/echo")
def repeat_text(ack, respond, command):
    # Acknowledge command request
    ack()
    respond(f"{command['text']}")

# say() 將 app 加入 channel 才可運作
# 須 chat:write scope
@app.command("/say_hello")
def say_hello(ack, say):
    # Acknowledge command request
    ack()
    say("hello")


# 訂閱 event messge.channels
# 當有訊息包含 knock knock 時執行 
@app.message("knock knock")
def ask_who1(message, say):
    say("_Who's there?_")


# Start your app
if __name__ == "__main__":
    SocketModeHandler(app, config('SLACK_APP_TOKEN')).start()

