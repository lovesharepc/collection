#!/bin/bash

# include config
cd "$(dirname "$0")"
source "config.sh"
# function block
## show to use
usage() {
 echo "use slack to notify dir size over use"
 echo "Usage: $0 -m <limit size>"
 exit 1
}
## push message to slack


# getopts block
while getopts 'j:m' OPT; do
    case $OPT in
#        j) S_DIR="$OPTARG";;
#        m) D_DIR="$OPTARG";;
        ?) usage;;
    esac
done
  


# main script
for current_checking_dir in ${MONITOR_DIR[@]} 
do
  # check current_checking_dir is dir 
  if [[ -d "$current_checking_dir" ]]; then
    # get current dir size
    current_size=$(sudo du -s ${current_checking_dir} | awk '{print $1}')
    # if size greater than or equal to MONITOR_MAX_SIZE
    if [ "$current_size" -ge "$MONITOR_MAX_SIZE" ]; then
      # do notify 
      #echo "$current_checking_dir size = $current_size"
      curl -X POST -H 'Content-type: application/json' --data '{"text":"dir '${current_checking_dir}' is over use, 
      current size is:'$current_size'KB,
      notify limit size is:'$MONITOR_MAX_SIZE'KB"}' $SLACK_TOKEN
    fi
  fi

done
