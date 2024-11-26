# Vehicle Spy VSB file Spec

### File Specification <a href="#file_sepc" id="file_sepc"></a>

| Description     | Length in Bytes      | Notes                                                                |
| --------------- | -------------------- | -------------------------------------------------------------------- |
| Text Identifier | 6                    | single byte char array with text "icsbin"used to identify file type. |
| File Version    | 4                    | single byte char array indicate version.                             |
| Version Section | Variable (see below) | This data structure is determinant the File Version                  |

### Version Specification <a href="#version_sepc" id="version_sepc"></a>

#### Version 0x101 <a href="#v101_sepc" id="v101_sepc"></a>

This format is no longer created. [Click](vehicle-spy-vsb-file-spec.md#network_id) to see Network ID's



| Description                 | Length in Bytes                                            | Notes                                                                                                                                                       |
| --------------------------- | ---------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Length of Vs3 File          | 4                                                          | int value indicating the length of the next section (the vs3 file). A zero indicates no vs3 file is present.                                                |
| Vs3 file                    | variable (see above)                                       | vs3 file used to save this binary file. This vs3 file is later used to decode the binary data into usable information.                                      |
| Length of text comment      | 4                                                          | int indicating the length of the text header comment of the saved file. SINCE THE COMMENT IS UNICODE THEREFORE HIS IS THE LENGTH IN CHARACTERS - NOT BYTES. |
| Text comment                | 2 bytes per character (see above for number of characters) | Unicode text comment.                                                                                                                                       |
| Size of Buffer of Messages  | 4                                                          | sizeof(VSBSpyMessage) multiplied by Number of messages saved to the file                                                                                    |
| Current Buffer Pointer      | 4                                                          | int value which is the pointer to the most recent buffer item +1. (only needed if Number of All time messages > Original buffer size)                       |
| Original Buffer Size        | 4                                                          | int value which is the size of the buffer memory originally allocated by this buffer                                                                        |
| Number of All time messages | 4                                                          | this indicates how many messages were received by this buffer (this number will indicate overflows)                                                         |
| Buffer of Messages          | variable (see Size of Buffer of Messages)                  | VSBSpyMessage structures                                                                                                                                    |
| Start Time of Collection    | struct icsspyMsgTime                                       | this is a comparison value between the system time stamp and the neoVI time stamp.                                                                          |

#### Version 0x102 <a href="#v102_sepc" id="v102_sepc"></a>

This format is created by the extractor. [Click](vehicle-spy-vsb-file-spec.md#network_other) to see Network ID's

| Description                                             | Length in Bytes                           | Notes                                                                                                           |
| ------------------------------------------------------- | ----------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| Length of EDP Section                                   | 4                                         | int value indicating the length of the next section (the EDP). A zero indicates no EDP section file is present. |
| [EDP Section](vehicle-spy-vsb-file-spec.md#edp_section) | variable (see above)                      | used to save the extra data bytes for networks such as Ethernet, Flexray, and CANFD                             |
| Buffer of Messages                                      | variable (see Size of Buffer of Messages) | VSBSpyMessage structures                                                                                        |
| Start Time of Collection                                | struct icsspyMsgTime                      | this is a comparison value between the system time stamp and the neoVI time stamp.                              |

#### Version 0x103 <a href="#v103_sepc" id="v103_sepc"></a>

This format is created using VSpy. [Click](vehicle-spy-vsb-file-spec.md#network_other) to see Network ID's

| Description                                             | Length in Bytes                                            | Notes                                                                                                                                                       |
| ------------------------------------------------------- | ---------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Length of EDP Section                                   | 4                                                          | int value indicating the length of the next section (the EDP). A zero indicates no EDP section is present.                                                  |
| [EDP Section](vehicle-spy-vsb-file-spec.md#edp_section) | variable (see above)                                       | used to save the extra data bytes for networks such as Ethernet, Flexray, and CANFD                                                                         |
| Length of text comment                                  | 4                                                          | int indicating the length of the text header comment of the saved file. SINCE THE COMMENT IS UNICODE THEREFORE HIS IS THE LENGTH IN CHARACTERS - NOT BYTES. |
| Text comment                                            | 2 bytes per character (see above for number of characters) | Unicode text comment.                                                                                                                                       |
| Size of Buffer of Messages                              | 4                                                          | sizeof(VSBSpyMessage) multiplied by Number of messages saved to the file                                                                                    |
| Current Buffer Pointer                                  | 4                                                          | int value which is the pointer to the most recent buffer item +1. (only needed if Number of All time messages > Original buffer size)                       |
| Original Buffer Size                                    | 4                                                          | int value which is the size of the buffer memory originally allocated by this buffer                                                                        |
| Number of All time messages                             | 4                                                          | this indicates how many messages were received by this buffer (this number will indicate overflows)                                                         |
| Buffer of Messages                                      | variable (see Size of Buffer of Messages)                  | VSBSpyMessage structures                                                                                                                                    |
| Start Time of Collection                                | struct icsspyMsgTime                                       | this is a comparison value between the system time stamp and the neoVI time stamp.                                                                          |

#### EDP section <a href="#edp_section" id="edp_section"></a>

Used by version 0x102 and 0x103. The ExtraDataPtr -1 of each message is a index to the EDP in EDP section. [Click ](vehicle-spy-vsb-file-spec.md#network_other)to see Network ID's

#### Version 0x104 <a href="#v104_sepc" id="v104_sepc"></a>

This format is created by the Loggers and VSpy Stream to Disk.

| Description              | Length in Bytes                                | Notes                                                                                                                                                                                                   |
| ------------------------ | ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Buffer of Messages       | VSBSpyMessage structures                       | VSBSpyMessage structures                                                                                                                                                                                |
| EDP                      | variable (see previous message's ExtraDataPtr) | used to save the extra data bytes for networks such as Ethernet, Flexray, and CANFD                                                                                                                     |
| ......                   | variable                                       | Buffer of Message and EDP continue to repeat until Start Time of Collection. If you are reading the VSB file, simple continue to read until Buffer of Message size read not equal sizeof(VSBSpyMessage) |
| Start Time of Collection | struct icsspyMsgTime                           | this is a comparison value between the system time stamp and the neoVI time stamp.                                                                                                                      |



### NetWork ID <a href="#network_id" id="network_id"></a>

#### version 0x101 <a href="#network_v101" id="network_v101"></a>

<table><thead><tr><th width="150">Description</th><th>Value</th></tr></thead><tbody><tr><td>HSCAN</td><td>0</td></tr><tr><td>MSCAN</td><td>1</td></tr><tr><td>SWCAN</td><td>2</td></tr><tr><td>LSFTCAN</td><td>5</td></tr><tr><td>DEVICE</td><td>8</td></tr><tr><td>HSCAN2</td><td>9</td></tr><tr><td>HSCAN3</td><td>10</td></tr><tr><td>LIN2</td><td>11</td></tr><tr><td>LIN3</td><td>12</td></tr><tr><td>LIN4</td><td>13</td></tr></tbody></table>

#### version 0x102 , 0x103, 0x104 <a href="#network_other" id="network_other"></a>

<table><thead><tr><th width="150">Description</th><th>Value</th></tr></thead><tbody><tr><td>DEVICE</td><td>0</td></tr><tr><td>HSCAN</td><td>1</td></tr><tr><td>MSCAN</td><td>2</td></tr><tr><td>SWCAN</td><td>3</td></tr><tr><td>LSFTCAN</td><td>4</td></tr><tr><td>J1708</td><td>6</td></tr><tr><td>JVPW</td><td>8</td></tr><tr><td>ISO</td><td>9</td></tr><tr><td>ISO2</td><td>14</td></tr><tr><td>LIN</td><td>16</td></tr><tr><td>ISO3</td><td>41</td></tr><tr><td>HSCAN2</td><td>42</td></tr><tr><td>HSCAN3</td><td>44</td></tr><tr><td>ISO4</td><td>47</td></tr><tr><td>LIN2</td><td>48</td></tr><tr><td>LIN3</td><td>49</td></tr><tr><td>LIN4</td><td>50</td></tr><tr><td>LIN5</td><td>84</td></tr><tr><td>MOST</td><td>51</td></tr><tr><td>CGI</td><td>53</td></tr><tr><td>HSCAN4</td><td>61</td></tr><tr><td>HSCAN5</td><td>62</td></tr><tr><td>SWCAN2</td><td>68</td></tr><tr><td>ETHERNET_DAQ</td><td>69</td></tr><tr><td>FLEXRAY1A</td><td>80</td></tr><tr><td>FLEXRAY1B</td><td>81</td></tr><tr><td>FLEXRAY2A</td><td>82</td></tr><tr><td>FLEXRAY2B</td><td>83</td></tr><tr><td>FLEXRAY</td><td>85</td></tr><tr><td>MOST25</td><td>90</td></tr><tr><td>MOST50</td><td>91</td></tr><tr><td>ETHERNET</td><td>93</td></tr><tr><td>GMFSA</td><td>94</td></tr><tr><td>TCP</td><td>95</td></tr><tr><td>HSCAN6</td><td>96</td></tr><tr><td>HSCAN7</td><td>97</td></tr><tr><td>LIN6</td><td>98</td></tr><tr><td>LSFTCAN2</td><td>99</td></tr><tr><td>OP_ETHERNET1</td><td>17</td></tr><tr><td>OP_ETHERNET2</td><td>18</td></tr><tr><td>OP_ETHERNET3</td><td>19</td></tr><tr><td>OP_ETHERNET4</td><td>45</td></tr><tr><td>OP_ETHERNET5</td><td>46</td></tr><tr><td>OP_ETHERNET6</td><td>73</td></tr><tr><td>OP_ETHERNET7</td><td>75</td></tr><tr><td>OP_ETHERNET8</td><td>76</td></tr><tr><td>OP_ETHERNET9</td><td>77</td></tr><tr><td>OP_ETHERNET10</td><td>78</td></tr><tr><td>OP_ETHERNET11</td><td>79</td></tr><tr><td>OP_ETHERNET12</td><td>87</td></tr></tbody></table>

### Example <a href="#example" id="example"></a>

Below is a C++ example of how to open a .vsb file (v102 & v103 & 104) and display the network messages (Ethernet, CANFD, and CAN) with some other useful information You can view the full [C++ code](https://cdn.intrepidcs.net/support/VehicleSpy/VSBIO.zip) or Download the full project from the links provided.

#### Reading File Specification <a href="#reading_file_specification" id="reading_file_specification"></a>

```cpp
bool Messages::Read(char * sFileName)
{
    unsigned long numEDP = 0;

    m_pFile = fopen(sFileName, "rb");
    if (m_pFile)
    {
        fSead( 0, SEEK_END);
        int length = ftell(m_pFile); //identify length of File 
        fSead( 0, SEEK_SET);

        char id[6];
        if (!fRead((char * )&id, 6) || memcmp(id, "icsbin", 6) != 0) //check for icsbin in the first 6 bytes to identify if it a VSB file
        {
            printf("Invalid VSB file\n");
            return false;
        }
        unsigned int fileversion;

      
        if (!fRead((char *)&fileversion, 4)){ //VSB has 4 versions 101 is no longer used 
            printf("Read Error\n");
            return false;
        }
        else if (fileversion == 0x102)//this is created by the extractor
        {
            int EDPSize = ReadEDPSelction(); //the extra data section contains extra data which is different for each message type
            if (EDPSize == 0)
                fSead( VSB_HEADERSIZE, SEEK_SET);
            unsigned long numofmessages = ((length - (EDPSize + SIZEOFEDPSIZE)) - VSB_HEADERSIZE) / sizeof(icsSpyMessage); //calculate number of messages in file; the plus 4
            m_nMessages =  numofmessages; // set number of messages in file
            if (numofmessages){
                if(!ReadMessage(numofmessages, fileversion)){ //read messages
                    printf("file was not read correctly \n");
                    return false;
                }
                
        }
        else if (fileversion == 0x103)//this is created by VSPY
        {
            ReadEDPSelction(); //read EDP
            unsigned long numofmessages = Read103Header(); //read 103 header
            m_nMessages = numofmessages; //set number of messages in file
            if (numofmessages){
                if(!ReadMessage(numofmessages, fileversion)){ //read messages
                    printf("file was not read correctly \n");
                    return false;
                }
            }
        }
        else if (fileversion == 0x104){//this is created by various hardware and VSPY for logging 
            if(!Read104()){ // 104 has a very different structure compared to the other file types
                printf("file was not read correctly \n");
                return false;
            }
        }
        else{
            printf("%s is an unsupported VSB version!\n", sFileName);
            return false;
        }
        fclose(m_pFile);
    }
    else
    {
        printf("Could not open %s to read!\n", sFileName);
        return false;
    }

    return true;
}
```



#### Reading EDP Section <a href="#reading_edp_section" id="reading_edp_section"></a>

```cpp
int Messages::ReadEDPSelction()
{
    unsigned long  edpsize;	
    bool bFixTimeStamp = false;

    if (fRead((char *)&edpsize, SIZEOFEDPSIZE) && edpsize > 0)//read size of edp section
    {
		unsigned long tempEDPSize = edpsize;
        static const char* EDP_SECTION = "EDP_SECTION"; 
		char obItem [EDPSECTIONSTRINGSIZE];  

        // check if there's an EDP_SECTION in here
        if (fRead(obItem, EDPSECTIONSTRINGSIZE) && tempEDPSize >= EDPSECTIONSTRINGSIZE && strcmp(obItem, EDP_SECTION) == 0)//verify edp section
        {
			// the following lines of code is a bad idea for large files. but since it is an simple example I wanted to simplify the code normality you would want to use some sort of file stream. 

			tempEDPSize -= EDPSECTIONSTRINGSIZE;
			m_pEDPSection = new char[tempEDPSize];             
            
			
			if (!fRead(m_pEDPSection, tempEDPSize)){ //load edp section into memory
				printf("invalid file read\n");
				return 0;
			}

			char * edpPtr = m_pEDPSection;			
            while (tempEDPSize > 0)//parse edp section
            {
                int edpLen = *(int*)edpPtr;
                m_edps.push_back(std::pair<char*, int>(edpPtr + sizeof(int), edpLen));//each node in this vector pertains to a different message (this will make more sense when you look at Read Message )
                tempEDPSize -= sizeof(int);
                edpPtr += edpLen +sizeof(edpLen);			
                tempEDPSize -= edpLen;
            }
            return edpsize;
        }
    }
    return 0;
}
```



#### Reading 0x103 File Info <a href="#reading_edp_section" id="reading_edp_section"></a>

```cpp
unsigned long Messages::Read103Header()
{
    unsigned long theNumOfMsgs;
    size_t msgslength, currbuffptr, numalltime, commentlength, origbuffsize;

    fRead((char *)&commentlength, 4); //check if there is a comment
    if (commentlength > 0)
        fSead( (long)commentlength * 2, SEEK_CUR); // skip comment (comment written in wchar_t)
    fRead((char *)&msgslength, 4);//size of message section 
    fRead((char *)&origbuffsize, 4); //original size of buffer
    fRead((char *)&currbuffptr, 4);  // current buffer postion 
    fRead((char *)&numalltime, 4); // number of message all time

    theNumOfMsgs = msgslength / sizeof(VSBSpyMessage);    // number of messages

    return theNumOfMsgs;
}
```



#### Reading 0x102 and 0x103 Messages <a href="#reading_0x102-0x103_messages" id="reading_0x102-0x103_messages"></a>

```cpp
bool Messages::ReadMessage(unsigned long theNumOfMsgs, unsigned int fileversion)
{
    VSBSpyMessage * pMessageRead = new VSBSpyMessage();
	m_pMessages = new icsSpyMessage[theNumOfMsgs];
    bool firstMsg = true;
    SpyMsgTime timeStampRead;
    SpyMsgTime FirstMsgTime;

	for(unsigned int i = 0; i < theNumOfMsgs; i++){//read one message at a time
		if(!fRead((char *)pMessageRead, sizeof(VSBSpyMessage))){//read message
			delete pMessageRead;
			delete m_pMessages;
			m_pMessages = NULL;
			theNumOfMsgs = 0;
			return false;
		}

		if (firstMsg) {//record the start time of the first message
			FirstMsgTime.HardwareTimeStampID = m_pMessages[0].TimeStampHardwareID;
			FirstMsgTime.HardwareTime1 = m_pMessages[0].TimeHardware;
			FirstMsgTime.HardwareTime2 = m_pMessages[0].TimeHardware2;
			FirstMsgTime.SystemTimeStampID = m_pMessages[0].TimeStampSystemID;
			FirstMsgTime.SystemTime1 = m_pMessages[0].TimeSystem;
			FirstMsgTime.SystemTime2 = m_pMessages[0].TimeSystem2;
			firstMsg = false;
		}

		VSBMessageToNormal(&m_pMessages[i], pMessageRead);// convert structure 
		
		bool clear = true;
		if (pMessageRead->ExtraDataPtrEnabled && pMessageRead->iExtraDataPtr) // check for edp section
		{
			if (pMessageRead->iExtraDataPtr >= 1 && pMessageRead->iExtraDataPtr <= m_edps.size())
			{
				int iEDPIndex = pMessageRead->iExtraDataPtr - 1;// identify index in the m_edps vector we made in the ReadEDPSelction function
				int payloadLength = m_edps[iEDPIndex].second; 
				m_pMessages[i].pExtraDataPtr = new pExtraDataPtrHandler(); //using pExtraDataPtrHandler to simply make  to identify length of edp section
				((pExtraDataPtrHandler *)(m_pMessages[i].pExtraDataPtr))->pExtraDataPtr = m_edps[iEDPIndex].first;
				((pExtraDataPtrHandler *)(m_pMessages[i].pExtraDataPtr))->length = payloadLength;
				clear = false;
			}
		}
		if (clear)
		{
			m_pMessages[i].ColorID = 0; //reset values
		    m_pMessages[i].pExtraDataPtr = 0;  //reset values
		}
		if (fileversion == 0x102)//all 102s implicitly have bit 7 high. since we're converting to 103 we need to force it
			m_pMessages[i].TimeStampHardwareID |= 0x80;	
	}
  
    if (!fRead((char *)&timeStampRead, sizeof(timeStampRead))) //check if start logging time was recorded
        timeStampRead = FirstMsgTime; // if start logging time was not record simply set it to first message time
	m_startTimeStamp = timeStampRead;
	delete pMessageRead;
    return true;

}
```

#### Reading 0x104 <a href="#reading_0x104" id="reading_0x104"></a>

```cpp
bool Messages::Read104()  // 104 don't have a edp section they instead put the extra data after that message 
{
    unsigned long EDPLength = 0, Edpsize = 0, numOfMessages = 0;

	bool firstMsg = true;
    SpyMsgTime timeStampRead;
    SpyMsgTime FirstMsgTime;

    VSBSpyMessage *pMessage = new VSBSpyMessage();

	while (fRead((char *)pMessage, sizeof(VSBSpyMessage))) // read messages to identify number of message and edp size
    {
		 numOfMessages++;
		 if (pMessage->ExtraDataPtrEnabled && pMessage->iExtraDataPtr > 0)// as you can see we are using extraDataptr to identify the size of the edp section for that message
         {
			Edpsize +=  pMessage->iExtraDataPtr; 
            // The EDP is the length of the extra data following the message, skip it
			fSead((unsigned int)pMessage->iExtraDataPtr, SEEK_CUR); 
         }
	}	

	fSead( VSB_HEADERSIZE, SEEK_SET); //go back to the start
	//from here on out it is very similar to 103 and 102 but the location of the edp section is different 
	
	m_pMessages = new icsSpyMessage[numOfMessages];

    for (unsigned int i = 0; i < numOfMessages; i++)
    {
		if (!fRead((char *)pMessage, sizeof(VSBSpyMessage)))
            break; //error

		if (firstMsg) {
			FirstMsgTime.HardwareTimeStampID = pMessage[0].TimeStampHardwareID;
			FirstMsgTime.HardwareTime1 = pMessage[0].TimeHardware;
			FirstMsgTime.HardwareTime2 = pMessage[0].TimeHardware2;
			FirstMsgTime.SystemTimeStampID = pMessage[0].TimeStampSystemID;
			FirstMsgTime.SystemTime1 = pMessage[0].TimeSystem;
			FirstMsgTime.SystemTime2 = pMessage[0].TimeSystem2;
			firstMsg = false;
		}

        bool clear = true;

		VSBMessageToNormal(&m_pMessages[i], pMessage);

        if (pMessage->ExtraDataPtrEnabled &&  pMessage->iExtraDataPtr >= 1 ) {
            EDPLength = pMessage->iExtraDataPtr;
			char * pEDP = new char[EDPLength];
			if(!fRead(pEDP, EDPLength))
				return false; //error
			m_pMessages[i].pExtraDataPtr = new pExtraDataPtrHandler();
			((pExtraDataPtrHandler *)(m_pMessages[i].pExtraDataPtr))->pExtraDataPtr = (void *)pEDP;
			((pExtraDataPtrHandler *)(m_pMessages[i].pExtraDataPtr))->length = EDPLength;
            clear = false;
        }

        if (clear) {
            EDPLength = 0;
            m_pMessages[i].ColorID = 0;
			m_pMessages[i].pExtraDataPtr = 0;
        }
    }
		
    if (!fRead((char *)&timeStampRead, sizeof(timeStampRead)))
        timeStampRead = FirstMsgTime;
	m_startTimeStamp = timeStampRead;
    m_nMessages = numOfMessages;
    return true;
}
```
