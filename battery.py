def main():
    import wmi
    import ctypes

    winclass = wmi.WMI()
    
    for battery in winclass.Win32_Battery():
        current_b = battery.EstimatedChargeRemaining
        current_bstatus = battery.BatteryStatus
        # BatteryStatus(2) - has an AC but not charging
        # BatteryStatus(6) - is charging
        # 0x30 is the exclamation icon
        if current_b > 92 and (current_bstatus == 2 or current_bstatus == 6):
            ctypes.windll.user32.MessageBoxW(0,
            'The battery is currently at ' + str(current_b) + "%.\nPlease remove the charger.\n" \
            "\n电池电量为"+str(current_b)+"%.\n请取出充电器.",
            "Finished Charging", 0x30)
            
if __name__ == "__main__":
    main()