# udisks-indicator
Indicator for Ubuntu with Unity desktop to show disk usage

*With "Adwaita" Icon Theme*

[![Adwaita](http://i.imgur.com/Nc911nP.png)](http://i.imgur.com/Nc911nP.png)

*With Ubuntu Kylin Icon Theme*

[![UbuntuKylin](http://i.imgur.com/mgZ2Wb8.png)](http://i.imgur.com/mgZ2Wb8.png)

### Overview

This indicator for Ubuntu with Unity allows easily view information about your mounted partitions.

Entries are organized in order:

- Partition 
- Alias ( if set by user )
- Disk Drive to which partition belongs
- Mountpoint of the partition ( directory )
- Filesystem type
- Usage in percent and human readable format
- Usage bar 

Preferences dialog allows removing Alias,Disk,Mountpoint,and Filesystem fields. Since the original purpose of this indicator was to display partition usage information, Partition , Usageand Usage Bar are kept and non-removable

Clicking on each partition entry will open the partition's mountpoint in the default file manager

The "Unmounted Partitions" menu lists all the partitions not currently mounted by the system. Clicking on any entry in that submenu will mount that partition automatically, typically to `/media/username/drive-id` folder, unless your system has appropriate entry in `/etc/fstab` file to mount it elsewhere.

The indicator uses default icons provided with the system, so the icon should be changing as you change the icon theme using Unity Tweak Tool or other methods. Information fields for each entry also adapt to nice formating if you are using Ubuntu's default font or any Monospace font ( others aren't supported) 

In addition, the indicator provides bubble notifications if there are mounting errors
