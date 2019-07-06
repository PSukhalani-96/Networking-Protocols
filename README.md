# Networking-Protocols
Simulation of StopNWait, GoBackN and SelectiveRepeat Protocols

# Download and run
	$ git clone https://github.com/PSukhalani-96/Networking-Protocols.git
	$ cd Networking-Protocols

### For Stop N Wait Protocol
	$ cd StopNWait
	$ python3 StopNWaitsender.py
	
The simulation will first run the client-server (Sender-Receiver) Socket Program and log the information of frame sent,
frame received,frame lost, and timeout in a file. Then StopNWaitGUI fetch the log file and simulate the purpose of Stop 
N Wait Protocol.

![1](https://user-images.githubusercontent.com/50991324/60761486-5a62a280-a067-11e9-972b-a40d6bc2403a.png)

![2](https://user-images.githubusercontent.com/50991324/60761487-5a62a280-a067-11e9-9a38-6639fa24d151.png)

![3](https://user-images.githubusercontent.com/50991324/60761488-5c2c6600-a067-11e9-8f2b-93ad50a06566.png)

![4](https://user-images.githubusercontent.com/50991324/60761489-5e8ec000-a067-11e9-82c0-609963114b7f.png)

![5](https://user-images.githubusercontent.com/50991324/60761490-60588380-a067-11e9-9eb2-b80471fb70e3.png)

![6](https://user-images.githubusercontent.com/50991324/60761491-62badd80-a067-11e9-8832-2e1a8f78bd51.png)

![7](https://user-images.githubusercontent.com/50991324/60761492-63ec0a80-a067-11e9-8e3d-21108bd55ae8.png)

![8](https://user-images.githubusercontent.com/50991324/60761493-664e6480-a067-11e9-8148-cfcfc984d4fb.png)

![9](https://user-images.githubusercontent.com/50991324/60761494-68b0be80-a067-11e9-9c11-df6779f73da1.png)

![1](https://user-images.githubusercontent.com/50991324/60761657-c2ff4e80-a06a-11e9-89c8-025e56748c2e.png)


### For GoBackN Protocol
	$ cd GoBackN
	$ python3 GoBackNGUI.py

The simulation will first run the client-server (Sender-Receiver) Socket Program and log the information of frame sent,
frame received,frame lost, and timeout in a file. Then GoBackNGUI fetch the log file and simulate the purpose of Stop 
N Wait Protocol.

Constraint:		Frames are numbered from 0-7.
				Window Size:	4
				
				
![7](https://user-images.githubusercontent.com/50991324/60761766-749f7f00-a06d-11e9-9157-c53a263e62b7.png)

![3](https://user-images.githubusercontent.com/50991324/60761659-c8f52f80-a06a-11e9-974f-6d471e206643.png)

![4](https://user-images.githubusercontent.com/50991324/60761660-cabef300-a06a-11e9-8a63-4ec4c96f88ef.png)

![5](https://user-images.githubusercontent.com/50991324/60761661-cc88b680-a06a-11e9-8a65-e2d4d21be498.png)

![6](https://user-images.githubusercontent.com/50991324/60761663-ceeb1080-a06a-11e9-89f7-54c5a36eb349.png)

![7](https://user-images.githubusercontent.com/50991324/60761665-d14d6a80-a06a-11e9-86fc-18c11728fb5f.png)

![8](https://user-images.githubusercontent.com/50991324/60761666-d3172e00-a06a-11e9-85fd-1702af1eab08.png)

![9](https://user-images.githubusercontent.com/50991324/60761667-d5798800-a06a-11e9-9af1-61fd47d8a6ba.png)

![10](https://user-images.githubusercontent.com/50991324/60761668-d7dbe200-a06a-11e9-8b48-b33929ab17f8.png)


### For Selective Repeat
	$ cd SelectiveRepeat
	$ python3 SRGUI.py
	
In Selective Repeat, there is no client and server used. On an application, first select **start Transmission**
to send and receive frames.The status of frames will collect in log file, which is used to simulate Selective
Repeat.

Constraint:		Frames are numbered from 0-7.
				Window Size:	4
				

![1](https://user-images.githubusercontent.com/50991324/60761797-f7283e80-a06d-11e9-84ef-a7e9802e8fcf.png)

![2](https://user-images.githubusercontent.com/50991324/60761799-fabbc580-a06d-11e9-97e6-617e3cb4dbca.png)

![3](https://user-images.githubusercontent.com/50991324/60761801-fc858900-a06d-11e9-8faf-63d3a39037c7.png)

![4](https://user-images.githubusercontent.com/50991324/60761804-fee7e300-a06d-11e9-89fe-6c1db87ffaa3.png)

![5](https://user-images.githubusercontent.com/50991324/60761806-014a3d00-a06e-11e9-860f-00025074ecb0.png)

![6](https://user-images.githubusercontent.com/50991324/60761807-03ac9700-a06e-11e9-8113-eca592fc3878.png)

![1](https://user-images.githubusercontent.com/50991324/60761843-eaf0b100-a06e-11e9-9c62-4a6271708c75.png)

![2](https://user-images.githubusercontent.com/50991324/60761845-ecba7480-a06e-11e9-82b7-2cf6ad5191ce.png)

![3](https://user-images.githubusercontent.com/50991324/60761846-ee843800-a06e-11e9-979d-cecd34708c19.png)

![4](https://user-images.githubusercontent.com/50991324/60761849-f0e69200-a06e-11e9-8807-3d80c16c310f.png)

![5](https://user-images.githubusercontent.com/50991324/60761850-f2b05580-a06e-11e9-91a5-894b5d166c3a.png)

![6](https://user-images.githubusercontent.com/50991324/60761851-f47a1900-a06e-11e9-90d3-015844111540.png)

![7](https://user-images.githubusercontent.com/50991324/60761852-f8a63680-a06e-11e9-9b71-a71765b779df.png)

![8](https://user-images.githubusercontent.com/50991324/60761853-fba12700-a06e-11e9-8734-d955afcb43b0.png)
