# Active Directory Domain System

After installing your Windows Server, Active Directory is not enabled by default. This section focuses on the role-based installation and activation of the Active Directory feature along with its required components, and then setting up a local Domain.

## Steps to Active Directory & Set up a local Domain

- At logging into the Windows Server for the First time Server Manager will automatically launch

![Active Directory Setup](images/31_AD_Setup_Picture31.png)

- You can get back into Server Manager later by pressing or clicking the start menu button on your keyboard or on the bottom left corner

![Active Directory Setup](images/32_AD_Setup_Picture32.png)

### Step 1: Go back into the Server Manager Dashboard and click "Manage", then in the dropdown click "Add roles and Features"

![Active Directory Setup](images/33_AD_Setup_Picture33.png)

### Step 2: In the "Before you begin" click "Next"

![Active Directory Setup](images/34_AD_Setup_Picture34.png)

### Step 3: In "Select installation type" select "Role based or feature-based installation" and click "Next"

![Active Directory Setup](images/35_AD_Setup_Picture35.png)

### Step 4: Then for "Select destination server" choose "Select a server from the server pool" and click "Next"

![Active Directory Setup](images/36_AD_Setup_Picture36.png)

### Step 5: In "Select Server roles"

- Click on inside the box next to "Active Directory Domain Services" (A black square should appear inside all selected roles)
- A pop-up window will appear showing the required management tools
- Click "Add features"
- Repeat steps for all roles you want to add and click "Next" when done

![Active Directory Setup](images/37_AD_Setup_Picture37.png)

![Active Directory Setup](images/38_AD_Setup_Picture38.png)

### Step 6: In Features

- Ensure that necessary feature are selected and Click "Next" for the roles/features if you have others selected

![Active Directory Setup](images/39_AD_Setup_Picture39.png)

![Active Directory Setup](images/40_AD_Setup_Picture40.png)

### Step 7: If you have roles like "Remote access", "Web server" or similar selected

- Click "Next" and select the "Role services", then click "Next"

![Active Directory Setup](images/41_AD_Setup_Picture41.png)

![Active Directory Setup](images/42_AD_Setup_Picture42.png)

![Active Directory Setup](images/46_AD_Setup_Picture46.png)

![Active Directory Setup](images/45_AD_Setup_Picture45.png)

### Step 8: For all other roles

- Click "Next"

![Active Directory Setup](images/43_AD_Setup_Picture43.png)

![Active Directory Setup](images/44_AD_Setup_Picture44.png)

### Step 9: in "Confirmation"

- Click install in the "Confirmation" page
- Wait for installation to finish

![Active Directory Setup](images/47_AD_Setup_Picture47.png)

![Active Directory Setup](images/48_AD_Setup_Picture48.png)

### Step 10: Promote a Domain

- In the "Result" page after installation is complete
- Scroll down to "Active Directory Domain Services"
- Click "Promote this server to a domain controller"

![Active Directory Setup](images/49_AD_Setup_Picture49.png)

### Step 11: In "Deployement configuration"

- Select "Add a new forest"
- For "root domain name" enter a name for your private Domain (_for example: your_custom_name.interal, or your_custom_name.lab_)
- **Important naming conventions**
- I suggest using "_.internal, or .lab_"
- **Do Not Use Official/Public Domains** If you use existing domain like "_yahoo.com_" (an official domain) all your traffic will be routed through your internal Domain controller, preventing you from accessing the actual public website in your lab environment.
- **Microsoft Recommendation** Microsoft recommends not using "_.local_" for internal domain extensions because many modern networks services use "_.local_" by default and it may cause routing conflicts.

![Active Directory Setup](images/50_AD_Setup_Picture50.png)

### Step 12: In "Domain controller options"

- For "Forest functional level" and "Domain functional level": These options adjust how far back you want your domain controller to be compatible with older version of Active Directory
- Enter and Confirm a password that you will remember for your domain then click "Next"
- This password will be used to boot into safe mode if windows server becomes corrupt

![Active Directory Setup](images/51_AD_Setup_Picture51.png)

### Step 13: In "DNS Options"

- Click "Next"

![Active Directory Setup](images/52_AD_Setup_Picture52.png)

### Step 14: In "Additional Options"

- Ensure the Domain name is correct and click "Next"

![Active Directory Setup](images/53_AD_Setup_Picture53.png)

### Step 15: In "Paths"

- Click "Next"

![Active Directory Setup](images/54_AD_Setup_Picture54.png)

### Step 16: In "Review Options"

- Ensure that all configuration are correct

![Active Directory Setup](images/55_AD_Setup_Picture55.png)

### Step 17: In "Prerequisite check"

- Wait for prerequisite check to complete then click "Install"
- Wait for installation to finish

![Active Directory Setup](images/56_AD_Setup_Picture56.png)

![Active Directory Setup](images/57_AD_Setup_Picture57.png)

### Step 18: Login into the Domain

- Once the installation is finished the system will restart and apply the new Domain Controller and roles
- After restart you will go to the login page of the domain eg. Notice the "_CAREVENTA\Administrator_"
- Log in with your regular Administrator password

![Active Directory Setup](images/58_AD_Setup_Picture58.png)
