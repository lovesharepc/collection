# monitor folder usage with slack
1. create slack app & enable Socket Mode

2. modify config

shell_script/config.sh
`MONITOR_DIR`             to be monitor dir
`MONITOR_MAX_SIZE`    alter dir size
`SLACK_TOKEN`             slack webhook token 


3. create crontab

owan@deploy:~$ cat /etc/cron.d/slack_notify
1 * * * * root /home/owan/first-bolt-app/shell_script/slack_notify_dir_size_over_use.sh >> /dev/null

4. create .env file sotre slack token

sample
.env
```
SLACK_BOT_TOKEN=<SLACK_BOT_TOKEN>
SLACK_APP_TOKEN=<SLACK_APP_TOKEN>
```

5. start app.py to recive command from slack

`.venv/bin/python3 app.py `

6. result

![2022-04-05_18-09.png](./img/2022-04-05_18-09.png)