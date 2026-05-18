# Creating a Virtual Machine Instance

Steps to Create a virtual machine instance and Install Windows Server 2022

## Steps to create a virtual machine instance

### Step 1: Open your VMware Workstation Pro

- Click "Create a New Virtual Machine"

![VM homepage](images/09_VI_Picture9.png)

### Step 2: Click "Typical (recommended)", then click next

![VM installation type](images/10_VI_Picture10.png)

### Step 3: Select "I will install the operating system later" and click Next.

- This will create a blank VM where we will add the ISO file later.

![VM operating installation](images/11_VI_Picture11.png)

### Step 4: Guest Operating System

- Select "Microsoft Windows", then for Version choose "Windows Server 2022" in the dropdown menu and click Next

![VM guest operating system version](images/12_VI_Picture12.png)

### Step 5: Virtual Machine Name

- For "Virtual machine name:" this will be VMware’s reference name to your virtual machine so feel free to change it or leave it default then click Next

![VM name](images/13_VI_Picture13.png)

### Step 6: Choose the size of the virtual disk you want to allocate. If your device has limited storage, you can use the recommended 60 GB, or select a larger size such as 200 GB if you have the space available. For this project, I chose 30 GB, which is more than enough for a basic Windows Server installation.

- You will also need to choose how the virtual disk is stored on your computer.
- **Store virtual disk as a single file:** keeps the entire disk in one large file, which is easier to manage and can offer slightly better performance.
- **Split virtual disk into multiple files:** divides the disk into multiple smaller equal segments, which can make copying, moving, or backing up the VM more convenient.
  After selecting your preferred options, click Next.

![VM disk space](images/14_VI_Picture14.png)

### Step 7: Verify that all settings, customization and changes are applied

- Click finish

![VM configuration confirmation](images/15_VI_Picture15.png)

### Step 8: Notice your created VM on the left side of your VMware screen.

- Click CD/DVD (SATA)

![VM Wcreated](images/16_VI_Picture16.png)

### Step 9: ISO image file

- In Connection click ‘use ISO image file’. Your file directory will open.
- Go to where you saved the Windows Server ISO you downloaded earlier and select it.
- After that Click “Network Adapter” on the left.

![VM choosing iso file](images/17_VI_Picture17.png)

### Step 10: Network connection

- In the Network connection setting select "Bridged: connect directly to the physical network".
- Using bridged allows the virtual machine to connect directly to your router. The VM will receive its own IP address from the router.
- NAT – will allow the VM to share an IP address with the Host computer. As NAT the VM is invisible to all other devices on the network except the Host computer.
- Then Click OK

![VM bridge connection](images/18_VI_Picture18.png)
