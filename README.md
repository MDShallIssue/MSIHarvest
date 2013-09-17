MSI Harvest
===

MSIHarvest is a tool for collecting email signups at conferences and shows
where network connectivity is not a guarantee.  Harvest simply collects
personal information to a text file, then will sync to a server when 
connected to a network.  

Sync currently is not written. 

Harvest supports a 'kiosk' mode that is full screen and has no context 
menu, as well as an 'administrator' mode that allows for syncing and 
cleaning up of records. 

Installing
===

Installation is dead simple, so far.  Unzip the files and run the executable 
in /dist/.  If re-compiled, the MSI_Logo_Header file needs to be copied in 
to the /dist/ folder, as nested directory resources aren't copied over by 
PyInstaller.

Compiling
===

Compiling requires PyInstaller[1], PyWin32[2], Python2.7[3] and QT SDK[4].  

[1] - http://sourceforge.net/projects/pyinstaller/files/2.0/pyinstaller-2.0.zip/download

[2] - http://sourceforge.net/projects/pywin32/files/py2in32/Build%20218/

[3] - http://www.python.org/ftp/python/2.7.5/python-2.7.5.amd64.msi

[4] - http://download.qt-project.org/official_releases/online_installers/1.4/qt-windows-opensource-1.4.0-2-x86-online.exe

