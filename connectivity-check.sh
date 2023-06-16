#!/bin/bash

# Specify your network connection name
CONNECTION_NAME="liquid_forrest"

# Try to connect to the specific network
nmcli con up id "$CONNECTION_NAME"

# Wait for connection to establish
sleep 10

# Check if the specific network is active
if [[ $(nmcli -t -f NAME con show --active) == *"$CONNECTION_NAME"* ]]; then
    echo "Connected to WiFi Network"
    # If WiFi is connected, ensure hostapd is not running
    if systemctl is-active --quiet hostapd; then
        systemctl stop hostapd
    fi
    # Let NetworkManager manage wlan0 again if connected to WiFi
    nmcli dev set wlan0 managed yes
else
    echo "WiFi Network is not available"
    # If WiFi is not connected, ensure hostapd is running
    # Release control of wlan0 from NetworkManager
    nmcli dev set wlan0 managed no
    if ! systemctl is-active --quiet hostapd; then
        systemctl start hostapd
    fi
fi

