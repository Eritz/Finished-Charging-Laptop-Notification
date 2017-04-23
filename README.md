# Finished-Charging-Laptop-Notification
A Windows notification pops up when the laptop's battery level reaches above 92%.

This uses the wmi library to retrieve information about the laptop's [battery status](https://msdn.microsoft.com/en-us/library/aa394074%28v=vs.85%29.aspx), and the ctypes library 
to create a Windows popup box. 
