# udisks-indicator
Indicator for Ubuntu with Unity desktop to show disk usage
[![Sample Screenshot](http://i.imgur.com/ugcvF6r.png)](http://i.imgur.com/ugcvF6r.png)

### Overview

This indicator for Ubuntu with Unity allows easily view information about your mounted partitions. It strives to be visually similar to iStat Menu 3 menulet from OS X.

Entries are organized in order:

- Partition 
- Alias ( if set by user )
- Disk Drive to which partition belongs
- Mountpoint of the partition ( directory )
- % Usage

Clicking on each partition entry will open the partition's mountpoint in the default file manager

The "Unmounted Partitions" menu lists all the partitions not currently mounted by the system. Clicking on any entry in that submenu will mount that partition automatically, typically to `/media/username/drive-id` folder

The indicator uses default icons provided with the system, so the icon should be changing as you change the icon theme using Unity Tweak Tool or other methods


