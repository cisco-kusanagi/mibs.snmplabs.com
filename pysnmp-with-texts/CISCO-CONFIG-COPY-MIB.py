#
# PySNMP MIB module CISCO-CONFIG-COPY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-CONFIG-COPY-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:53:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
FcNameIdOrZero, = mibBuilder.importSymbols("CISCO-ST-TC", "FcNameIdOrZero")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Gauge32, MibIdentifier, Integer32, Bits, IpAddress, ObjectIdentity, Counter64, Unsigned32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Counter32, iso, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibIdentifier", "Integer32", "Bits", "IpAddress", "ObjectIdentity", "Counter64", "Unsigned32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Counter32", "iso", "TimeTicks")
RowStatus, DisplayString, TextualConvention, TimeStamp, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention", "TimeStamp", "TruthValue")
ciscoConfigCopyMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 96))
ciscoConfigCopyMIB.setRevisions(('2009-02-27 00:00', '2005-04-06 00:00', '2004-03-17 00:00', '2002-12-17 00:00', '2002-05-30 00:00', '2002-05-07 00:00', '2002-03-28 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoConfigCopyMIB.setRevisionsDescriptions(("This MIB facilitates writing of configuration files of an SNMP Agent running Cisco's IOS in the following ways: to and from the net, copying running configurations to startup configurations and vice-versa, and copying a configuration (running or startup) to and from the local IOS file system.", 'Added new enumeration value fabricStartupConfig to ConfigFileType textual convention. Added new table ccCopyErrorTable. Added new enumeration values: systemNotReady and requestAborted to ConfigCopyFailCause.', 'The object ccCopyServerAddress is deprecated since it supports only IPv4 address. Two new objects are defined ccCopyServerAddressType and ccCopyServerAddressRev1.', 'Added a new enumeration value someConfigApplyFailed(7) to ConfigCopyFailCause TC.', 'Added sftp protocol as an option for ConfigCopyProtocol.', 'Added scp protocol as an option for ConfigCopyProtocol. Added unsupportedProtocol(6) as an option for the ConfigCopyFailCause TC.', 'Imported Unsigned32 from SNMPv2-SMI instead of CISCO-TC',))
if mibBuilder.loadTexts: ciscoConfigCopyMIB.setLastUpdated('200902270000Z')
if mibBuilder.loadTexts: ciscoConfigCopyMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoConfigCopyMIB.setContactInfo('Cisco Systems Customer Service Postal: 170 W. Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoConfigCopyMIB.setDescription('Added ccCopyVrfName attribute to support VPN config copy in ccCopyTable')
class ConfigCopyProtocol(TextualConvention, Integer32):
    description = 'The protocol file transfer protocol that should be used to copy the configuration file over the network. If the config file transfer is to occur locally on the SNMP agent, the method of transfer is left up to the implementation, and is not restricted to the protocols below. tftp: Transfer File Transfer Protocol ftp: File Transfer protocol rcp: Remote Copy Protocol scp: Secure Copy Protocol sftp: Secure File Transfer Protocol'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("tftp", 1), ("ftp", 2), ("rcp", 3), ("scp", 4), ("sftp", 5))

class ConfigCopyState(TextualConvention, Integer32):
    description = 'The state of a TFTP config-copy operation. The description of each state is given below: waiting: only one config-copy request can run at any time. A newly activated config-copy request is placed in this state if another request has already been activated. running: this state signifies that the config-copy request is running. successful: the state when a config-copy request is successfully completed. failed: the config-copy request was unsuccessful.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("waiting", 1), ("running", 2), ("successful", 3), ("failed", 4))

class ConfigCopyFailCause(TextualConvention, Integer32):
    description = "The reason a config-copy request failed. unknown: very descriptive. badFileName: check your file name/path/permissions. timeout: the network may be overloaded, or the remote file server may not be responding. noMem: the Agent wasn't able to allocate memory for the config-copy operation. noConfig: the agent-config selected as the source was non-existent. unsupportedProtocol: the protocol is not supported by the agent. someConfigApplyFailed: applying of some of the configuration commands failed. systemNotReady: system is not ready to copy. requestAborted: config copy operation aborted."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("unknown", 1), ("badFileName", 2), ("timeout", 3), ("noMem", 4), ("noConfig", 5), ("unsupportedProtocol", 6), ("someConfigApplyFailed", 7), ("systemNotReady", 8), ("requestAborted", 9))

class ConfigFileType(TextualConvention, Integer32):
    description = 'The various types of files on which a config-copy operation can be performed. networkFile: file on another network device, e.g. a file-server on the network. iosFile: a file on the local agent, other than startup or running config. startupConfig: a startup config file. runningConfig: a running config file. terminal: a terminal (e.g. the console window) on which the config is to be displayed. fabricStartupConfig: a file type which can be used for a destination file; when a running-config is to copied to a destination of this type, the file is copied to the startup config on all devices in the fabric. Such a fabric could, for example, be a Fibre Channel fabric, or even a MAC-based fabric.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("networkFile", 1), ("iosFile", 2), ("startupConfig", 3), ("runningConfig", 4), ("terminal", 5), ("fabricStartupConfig", 6))

ciscoConfigCopyMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 96, 1))
ccCopy = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 96, 1, 1))
ccCopyTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 96, 1, 1, 1), )
if mibBuilder.loadTexts: ccCopyTable.setStatus('current')
if mibBuilder.loadTexts: ccCopyTable.setDescription('A table of config-copy requests.')
ccCopyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 96, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-CONFIG-COPY-MIB", "ccCopyIndex"))
if mibBuilder.loadTexts: ccCopyEntry.setStatus('current')
if mibBuilder.loadTexts: ccCopyEntry.setDescription("A config-copy request. A management station wishing to create an entry should first generate a random serial number to be used as the index to this sparse table. The station should then create the associated instance of the row status and row index objects. It must also, either in the same or in successive PDUs, create an instance of ccCopySourceFileType and ccCopyDestFileType. At least one of the file types defined in ConfigFileType TC must be an agent-config file type (i.e. 'startupConfig' or 'runningConfig'). If one of the file types is a 'networkFile', a valid ccCopyFileName and ccCopyServerAddressType and ccCopyServerAddressRev1 or just ccCopyServerAddress must be created as well. If ccCopyServerAddress is created then ccCopyServerAddressRev1 will store the same IP address and ccCopyServerAddressType will take the value 'ipv4'. For a file type of 'iosFile', only a valid ccCopyFileName needs to be created as an extra parameter. It should also modify the default values for the other configuration objects if the defaults are not appropriate. Once the appropriate instance of all the configuration objects have been created, either by an explicit SNMP set request or by default, the row status should be set to active to initiate the request. Note that this entire procedure may be initiated via a single set request which specifies a row status of createAndGo as well as specifies valid values for the non-defaulted configuration objects. Once the config-copy request has been created (i.e. the ccCopyEntryRowStatus has been made active), the entry cannot be modified - the only operation possible after this is to delete the row. Once the request completes, the management station should retrieve the values of the status objects of interest, and should then delete the entry. In order to prevent old entries from clogging the table, entries will be aged out, but an entry will ever be deleted within 5 minutes of completing.")
ccCopyIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 96, 1, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: ccCopyIndex.setStatus('current')
if mibBuilder.loadTexts: ccCopyIndex.setDescription('Object which specifies a unique entry in the ccCopyTable. A management station wishing to initiate a config-copy operation should use a random value for this object when creating or modifying an instance of a ccCopyEntry. The RowStatus semantics of the ccCopyEntryRowStatus object will prevent access conflicts.')
ccCopyProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 96, 1, 1, 1, 1, 2), ConfigCopyProtocol().clone('tftp')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ccCopyProtocol.setStatus('current')
if mibBuilder.loadTexts: ccCopyProtocol.setDescription("The protocol to be used for any copy. If the copy operation occurs locally on the SNMP agent (e.g. 'runningConfig' to 'startupConfig'), this object may be ignored by the implementation.")
ccCopySourceFileType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 96, 1, 1, 1, 1, 3), ConfigFileType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ccCopySourceFileType.setStatus('current')
if mibBuilder.loadTexts: ccCopySourceFileType.setDescription("Specifies the type of file to copy from. Either the ccCopySourceFileType or the ccCopyDestFileType (or both) must be of type 'runningConfig' or 'startupConfig'. Also, the ccCopySourceFileType must be different from the ccCopyDestFileType. If the ccCopySourceFileType has the value of 'networkFile', the ccCopyServerAddress/ ccCopyServerAddressRev1 and ccCopyServerAddressType and ccCopyFileName must also be created, and 3 objects together (ccCopySourceFileType, ccCopyServerAddressRev1, ccCopyFileName) will uniquely identify the source file. If ccCopyServerAddress is created then ccCopyServerAddressRev1 will store the same IP address and ccCopyServerAddressType will take the value 'ipv4'. If the ccCopySourceFileType is 'iosFile', the ccCopyFileName must also be created, and the 2 objects together (ccCopySourceFileType, ccCopyFileName) will uniquely identify the source file.")
ccCopyDestFileType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 96, 1, 1, 1, 1, 4), ConfigFileType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ccCopyDestFileType.setStatus('current')
if mibBuilder.loadTexts: ccCopyDestFileType.setDescription("specifies the type of file to copy to. Either the ccCopySourceFileType or the ccCopyDestFileType (or both) must be of type 'runningConfig' or 'startupConfig'. Also, the ccCopySourceFileType must be different from the ccCopyDestFileType. If the ccCopyDestFileType has the value of 'networkFile', the ccCopyServerAddress/ccCopyServerAddressType and ccCopyServerAddressRev1 and ccCopyFileName must also be created, and 3 objects together (ccCopyDestFileType, ccCopyServerAddressRev1, ccCopyFileName) will uniquely identify the destination file. If ccCopyServerAddress is created then ccCopyServerAddressRev1 will store the same IP address and ccCopyServerAddressType will take the value 'ipv4'. If the ccCopyDestFileType is 'iosFile', the ccCopyFileName must also be created, and the 2 objects together (ccCopyDestFileType, ccCopyFileName) will uniquely identify the destination file.")
ccCopyServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 96, 1, 1, 1, 1, 5), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ccCopyServerAddress.setStatus('deprecated')
if mibBuilder.loadTexts: ccCopyServerAddress.setDescription("The IP address of the TFTP server from (or to) which to copy the configuration file. This object must be created when either the ccCopySourceFileType or ccCopyDestFileType has the value 'networkFile'. Values of 0.0.0.0 or FF.FF.FF.FF for ccCopyServerAddress are not allowed. Since this object can just hold only IPv4 Transport type, it is deprecated and replaced by ccCopyServerAddressRev1.")
ccCopyFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 96, 1, 1, 1, 1, 6), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ccCopyFileName.setStatus('current')
if mibBuilder.loadTexts: ccCopyFileName.setDescription("The file name (including the path, if applicable) of the file. This object must be created when either the ccCopySourceFileType or ccCopyDestFileType has the value 'networkFile' or 'iosFile'.")
ccCopyUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 96, 1, 1, 1, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 40))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ccCopyUserName.setStatus('current')
if mibBuilder.loadTexts: ccCopyUserName.setDescription("Remote username for copy via FTP, RCP, SFTP or SCP protocol. This object must be created when the ccCopyProtocol is 'rcp', 'scp', 'ftp', or 'sftp'. If the protocol is RCP, it will override the remote username configured through the rcmd remote-username <username> configuration command. The remote username is sent as the server username in an RCP command request sent by the system to a remote RCP server.")
ccCopyUserPassword = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 96, 1, 1, 1, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 40))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ccCopyUserPassword.setStatus('current')
if mibBuilder.loadTexts: ccCopyUserPassword.setDescription('Password used by FTP, SFTP or SCP for copying a file to/from an FTP/SFTP/SCP server. This object must be created when the ccCopyProtocol is FTP or SCP. Reading it returns a zero-length string for security reasons.')
ccCopyNotificationOnCompletion = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 96, 1, 1, 1, 1, 9), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ccCopyNotificationOnCompletion.setStatus('current')
if mibBuilder.loadTexts: ccCopyNotificationOnCompletion.setDescription('Specifies whether or not a ccCopyCompletion notification should be issued on completion of the TFTP transfer. If such a notification is desired, it is the responsibility of the management entity to ensure that the SNMP administrative model is configured in such a way as to allow the notification to be delivered.')
ccCopyState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 96, 1, 1, 1, 1, 10), ConfigCopyState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccCopyState.setStatus('current')
if mibBuilder.loadTexts: ccCopyState.setDescription('Specifies the state of this config-copy request. This value of this object is instantiated only after the row has been instantiated, i.e. after the ccCopyEntryRowStatus has been made active.')
ccCopyTimeStarted = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 96, 1, 1, 1, 1, 11), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccCopyTimeStarted.setStatus('current')
if mibBuilder.loadTexts: ccCopyTimeStarted.setDescription("Specifies the time the ccCopyState last transitioned to 'running', or 0 if the state has never transitioned to 'running'(e.g., stuck in 'waiting' state). This object is instantiated only after the row has been instantiated.")
ccCopyTimeCompleted = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 96, 1, 1, 1, 1, 12), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccCopyTimeCompleted.setStatus('current')
if mibBuilder.loadTexts: ccCopyTimeCompleted.setDescription("Specifies the time the ccCopyState last transitioned from 'running' to 'successful' or 'failed' states. This object is instantiated only after the row has been instantiated. Its value will remain 0 until the request has completed.")
ccCopyFailCause = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 96, 1, 1, 1, 1, 13), ConfigCopyFailCause()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccCopyFailCause.setStatus('current')
if mibBuilder.loadTexts: ccCopyFailCause.setDescription("The reason why the config-copy operation failed. This object is instantiated only when the ccCopyState for this entry is in the 'failed' state.")
ccCopyEntryRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 96, 1, 1, 1, 1, 14), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ccCopyEntryRowStatus.setStatus('current')
if mibBuilder.loadTexts: ccCopyEntryRowStatus.setDescription("The status of this table entry. Once the entry status is set to active, the associated entry cannot be modified until the request completes (ccCopyState transitions to 'successful' or 'failed' state).")
ccCopyServerAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 96, 1, 1, 1, 1, 15), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ccCopyServerAddressType.setStatus('current')
if mibBuilder.loadTexts: ccCopyServerAddressType.setDescription("This object indicates the transport type of the address contained in ccCopyServerAddressRev1 object. This must be created when either the ccCopySourceFileType or ccCopyDestFileType has the value 'networkFile'.")
ccCopyServerAddressRev1 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 96, 1, 1, 1, 1, 16), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ccCopyServerAddressRev1.setStatus('current')
if mibBuilder.loadTexts: ccCopyServerAddressRev1.setDescription("The IP address of the TFTP server from (or to) which to copy the configuration file. This object must be created when either the ccCopySourceFileType or ccCopyDestFileType has the value 'networkFile'. All bits as 0s or 1s for ccCopyServerAddressRev1 are not allowed. The format of this address depends on the value of the ccCopyServerAddressType object.")
ccCopyVrfName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 96, 1, 1, 1, 1, 17), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ccCopyVrfName.setStatus('current')
if mibBuilder.loadTexts: ccCopyVrfName.setDescription('This object specifies the VPN domain in which the server identified by ccCopyServerAddress or ccCopyServerAddressRev1 is located. The agent will use this field to identify the VPN routing table for this config copy. This object need not be configured, if the server is not located in a VPN domain.')
ccCopyErrorTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 96, 1, 1, 2), )
if mibBuilder.loadTexts: ccCopyErrorTable.setStatus('current')
if mibBuilder.loadTexts: ccCopyErrorTable.setDescription("A table containing information about the failure cause of the config copy operation. An entry is created only when the value of ccCopyState changes to 'failed' for a config copy operation. Not all combinations of ccCopySourceFileType and ccCopyDestFileType need to be supported. For example, an implementation may choose to support only the following combination: ccCopySourceFileType = 'runningConfig' ccCopyDestFileType = 'fabricStartupConfig'. In the case where a fabric wide config copy operation is being performed, for example by selecting ccCopyDestFileType value to be 'fabricStartupConfig', it is possible that the fabric could have more than one device. In such cases this table would have one entry for each device in the fabric. In this case even if the operation succeeded in one device and failed in another, the operation as such has failed, so the global state represented by ccCopyState 'failed', but for the device on which it was success, ccCopyErrorDescription would have the distinguished value, 'success'. Once the config copy operation completes and if an entry gets instantiated, the management station should retrieve the values of the status objects of interest. Once an entry in ccCopyTable is deleted by management station, all the corresponding entries with the same ccCopyIndex in this table are also deleted. In order to prevent old entries from clogging the table, entries age out at the same time as the corresponding entry with same ccCopyIndex in ccCopyTable ages out.")
ccCopyErrorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 96, 1, 1, 2, 1), ).setIndexNames((0, "CISCO-CONFIG-COPY-MIB", "ccCopyIndex"), (0, "CISCO-CONFIG-COPY-MIB", "ccCopyErrorIndex"))
if mibBuilder.loadTexts: ccCopyErrorEntry.setStatus('current')
if mibBuilder.loadTexts: ccCopyErrorEntry.setDescription('An entry containing information about the outcome at one destination of a failed config copy operation.')
ccCopyErrorIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 96, 1, 1, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: ccCopyErrorIndex.setStatus('current')
if mibBuilder.loadTexts: ccCopyErrorIndex.setDescription('A monotonically increasing integer for the sole purpose of indexing entries in this table. When a config copy operation has multiple destinations, then this index value is used to distinguish between those multiple destinations.')
ccCopyErrorDeviceIpAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 96, 1, 1, 2, 1, 2), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccCopyErrorDeviceIpAddressType.setStatus('current')
if mibBuilder.loadTexts: ccCopyErrorDeviceIpAddressType.setDescription('The type of Internet address for this destination device on which config copy operation is performed.')
ccCopyErrorDeviceIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 96, 1, 1, 2, 1, 3), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccCopyErrorDeviceIpAddress.setStatus('current')
if mibBuilder.loadTexts: ccCopyErrorDeviceIpAddress.setDescription('The IP address of this destination device on which config copy operation is performed. The object value has to be consistent with the type specified in ccCopyErrorDeviceIpAddressType.')
ccCopyErrorDeviceWWN = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 96, 1, 1, 2, 1, 4), FcNameIdOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccCopyErrorDeviceWWN.setStatus('current')
if mibBuilder.loadTexts: ccCopyErrorDeviceWWN.setDescription('The World Wide Name (WWN) of this destination device on which config copy operation is performed. The value of this object is zero-length string if WWN is unassigned or unknown. For example, devices which do not support fibre channel would not have WWN.')
ccCopyErrorDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 96, 1, 1, 2, 1, 5), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccCopyErrorDescription.setStatus('current')
if mibBuilder.loadTexts: ccCopyErrorDescription.setDescription('The error description for the error happened for this destination of this config copy operation.')
ciscoConfigCopyMIBTrapPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 96, 2))
ccCopyMIBTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 96, 2, 1))
ccCopyCompletion = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 96, 2, 1, 1)).setObjects(("CISCO-CONFIG-COPY-MIB", "ccCopyServerAddress"), ("CISCO-CONFIG-COPY-MIB", "ccCopyFileName"), ("CISCO-CONFIG-COPY-MIB", "ccCopyState"), ("CISCO-CONFIG-COPY-MIB", "ccCopyTimeStarted"), ("CISCO-CONFIG-COPY-MIB", "ccCopyTimeCompleted"), ("CISCO-CONFIG-COPY-MIB", "ccCopyFailCause"))
if mibBuilder.loadTexts: ccCopyCompletion.setStatus('current')
if mibBuilder.loadTexts: ccCopyCompletion.setDescription('A ccCopyCompletion trap is sent at the completion of a config-copy request. The ccCopyFailCause is not instantiated, and hence not included in a trap, when the ccCopyState is success.')
ciscoConfigCopyMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 96, 3))
ccCopyMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 96, 3, 1))
ccCopyMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 96, 3, 2))
ccCopyMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 96, 3, 1, 1)).setObjects(("CISCO-CONFIG-COPY-MIB", "ccCopyGroup"), ("CISCO-CONFIG-COPY-MIB", "ccCopyNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccCopyMIBCompliance = ccCopyMIBCompliance.setStatus('deprecated')
if mibBuilder.loadTexts: ccCopyMIBCompliance.setDescription('The compliance statement for Cisco agents which implement the Cisco ConfigCopy MIB. This MIB should be implemented on all Cisco agents that support copying of configs via the CLI. This compliance is deprecated and new compliance ccCopyMIBComplianceRev1 is defined.')
ccCopyMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 96, 3, 1, 2)).setObjects(("CISCO-CONFIG-COPY-MIB", "ccCopyGroupRev1"), ("CISCO-CONFIG-COPY-MIB", "ccCopyNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccCopyMIBComplianceRev1 = ccCopyMIBComplianceRev1.setStatus('deprecated')
if mibBuilder.loadTexts: ccCopyMIBComplianceRev1.setDescription('The compliance statement for Cisco agents which implement the Cisco ConfigCopy MIB. This MIB should be implemented on all Cisco agents that support copying of configs via the CLI. This compliance module deprecates ccCopyMIBCompliance.')
ccCopyMIBComplianceRev2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 96, 3, 1, 3)).setObjects(("CISCO-CONFIG-COPY-MIB", "ccCopyGroupRev1"), ("CISCO-CONFIG-COPY-MIB", "ccCopyNotificationsGroup"), ("CISCO-CONFIG-COPY-MIB", "ccCopyErrorGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccCopyMIBComplianceRev2 = ccCopyMIBComplianceRev2.setStatus('deprecated')
if mibBuilder.loadTexts: ccCopyMIBComplianceRev2.setDescription('The compliance statement for Cisco agents which implement the Cisco ConfigCopy MIB. This MIB should be implemented on all Cisco agents that support copying of configs via the CLI. This compliance module deprecates ccCopyMIBComplianceRev1.')
ccCopyMIBComplianceRev3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 96, 3, 1, 4)).setObjects(("CISCO-CONFIG-COPY-MIB", "ccCopyGroupRev1"), ("CISCO-CONFIG-COPY-MIB", "ccCopyNotificationsGroup"), ("CISCO-CONFIG-COPY-MIB", "ccCopyGroupVpn"), ("CISCO-CONFIG-COPY-MIB", "ccCopyErrorGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccCopyMIBComplianceRev3 = ccCopyMIBComplianceRev3.setStatus('current')
if mibBuilder.loadTexts: ccCopyMIBComplianceRev3.setDescription('The compliance statement for Cisco agents which implement the Cisco ConfigCopy MIB. This MIB should be implemented on all Cisco agents that support copying of configs via the CLI. This compliance module deprecates ccCopyMIBComplianceRev2.')
ccCopyGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 96, 3, 2, 1)).setObjects(("CISCO-CONFIG-COPY-MIB", "ccCopyProtocol"), ("CISCO-CONFIG-COPY-MIB", "ccCopySourceFileType"), ("CISCO-CONFIG-COPY-MIB", "ccCopyDestFileType"), ("CISCO-CONFIG-COPY-MIB", "ccCopyServerAddress"), ("CISCO-CONFIG-COPY-MIB", "ccCopyFileName"), ("CISCO-CONFIG-COPY-MIB", "ccCopyUserName"), ("CISCO-CONFIG-COPY-MIB", "ccCopyUserPassword"), ("CISCO-CONFIG-COPY-MIB", "ccCopyNotificationOnCompletion"), ("CISCO-CONFIG-COPY-MIB", "ccCopyState"), ("CISCO-CONFIG-COPY-MIB", "ccCopyTimeStarted"), ("CISCO-CONFIG-COPY-MIB", "ccCopyTimeCompleted"), ("CISCO-CONFIG-COPY-MIB", "ccCopyFailCause"), ("CISCO-CONFIG-COPY-MIB", "ccCopyEntryRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccCopyGroup = ccCopyGroup.setStatus('deprecated')
if mibBuilder.loadTexts: ccCopyGroup.setDescription('A collection of objects providing the ability to copy an agent-configuration file. This Group is deprecated and new group is defined.')
ccCopyNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 96, 3, 2, 2)).setObjects(("CISCO-CONFIG-COPY-MIB", "ccCopyCompletion"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccCopyNotificationsGroup = ccCopyNotificationsGroup.setStatus('current')
if mibBuilder.loadTexts: ccCopyNotificationsGroup.setDescription('The notification used to indicate that a config-copy operation to or from the agent has been completed.')
ccCopyGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 96, 3, 2, 3)).setObjects(("CISCO-CONFIG-COPY-MIB", "ccCopyProtocol"), ("CISCO-CONFIG-COPY-MIB", "ccCopySourceFileType"), ("CISCO-CONFIG-COPY-MIB", "ccCopyDestFileType"), ("CISCO-CONFIG-COPY-MIB", "ccCopyServerAddressType"), ("CISCO-CONFIG-COPY-MIB", "ccCopyServerAddressRev1"), ("CISCO-CONFIG-COPY-MIB", "ccCopyFileName"), ("CISCO-CONFIG-COPY-MIB", "ccCopyUserName"), ("CISCO-CONFIG-COPY-MIB", "ccCopyUserPassword"), ("CISCO-CONFIG-COPY-MIB", "ccCopyNotificationOnCompletion"), ("CISCO-CONFIG-COPY-MIB", "ccCopyState"), ("CISCO-CONFIG-COPY-MIB", "ccCopyTimeStarted"), ("CISCO-CONFIG-COPY-MIB", "ccCopyTimeCompleted"), ("CISCO-CONFIG-COPY-MIB", "ccCopyFailCause"), ("CISCO-CONFIG-COPY-MIB", "ccCopyEntryRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccCopyGroupRev1 = ccCopyGroupRev1.setStatus('current')
if mibBuilder.loadTexts: ccCopyGroupRev1.setDescription('A collection of objects providing the ability to copy an agent-configuration file. This group deprecates the old group ccCopyGroup.')
ccCopyErrorGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 96, 3, 2, 4)).setObjects(("CISCO-CONFIG-COPY-MIB", "ccCopyErrorDeviceIpAddressType"), ("CISCO-CONFIG-COPY-MIB", "ccCopyErrorDeviceIpAddress"), ("CISCO-CONFIG-COPY-MIB", "ccCopyErrorDeviceWWN"), ("CISCO-CONFIG-COPY-MIB", "ccCopyErrorDescription"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccCopyErrorGroup = ccCopyErrorGroup.setStatus('current')
if mibBuilder.loadTexts: ccCopyErrorGroup.setDescription("A collection of objects providing the result of a config copy operation when the value of ccCopyDestFileType is 'fabricStartupConfig' and value of ccCopyState is 'failed'.")
ccCopyGroupVpn = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 96, 3, 2, 5)).setObjects(("CISCO-CONFIG-COPY-MIB", "ccCopyVrfName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccCopyGroupVpn = ccCopyGroupVpn.setStatus('current')
if mibBuilder.loadTexts: ccCopyGroupVpn.setDescription('Additional collection of object providing the ability to copy an agent-configuration file.')
mibBuilder.exportSymbols("CISCO-CONFIG-COPY-MIB", ccCopy=ccCopy, ccCopyUserName=ccCopyUserName, ccCopyFailCause=ccCopyFailCause, ccCopyGroupRev1=ccCopyGroupRev1, ccCopyCompletion=ccCopyCompletion, ccCopyErrorDescription=ccCopyErrorDescription, ccCopyProtocol=ccCopyProtocol, ccCopyEntryRowStatus=ccCopyEntryRowStatus, ccCopyVrfName=ccCopyVrfName, ccCopyErrorDeviceIpAddressType=ccCopyErrorDeviceIpAddressType, ccCopyNotificationsGroup=ccCopyNotificationsGroup, ccCopyErrorEntry=ccCopyErrorEntry, ccCopyErrorDeviceIpAddress=ccCopyErrorDeviceIpAddress, ccCopyEntry=ccCopyEntry, ciscoConfigCopyMIBTrapPrefix=ciscoConfigCopyMIBTrapPrefix, ccCopyState=ccCopyState, ccCopyMIBTraps=ccCopyMIBTraps, ccCopySourceFileType=ccCopySourceFileType, ccCopyErrorTable=ccCopyErrorTable, ccCopyMIBCompliances=ccCopyMIBCompliances, ccCopyErrorGroup=ccCopyErrorGroup, ccCopyTimeCompleted=ccCopyTimeCompleted, ccCopyNotificationOnCompletion=ccCopyNotificationOnCompletion, ccCopyMIBComplianceRev3=ccCopyMIBComplianceRev3, ciscoConfigCopyMIBConformance=ciscoConfigCopyMIBConformance, ccCopyDestFileType=ccCopyDestFileType, ccCopyGroupVpn=ccCopyGroupVpn, ccCopyMIBComplianceRev2=ccCopyMIBComplianceRev2, ConfigCopyFailCause=ConfigCopyFailCause, ccCopyServerAddressType=ccCopyServerAddressType, ccCopyServerAddress=ccCopyServerAddress, ccCopyServerAddressRev1=ccCopyServerAddressRev1, ConfigCopyProtocol=ConfigCopyProtocol, PYSNMP_MODULE_ID=ciscoConfigCopyMIB, ciscoConfigCopyMIBObjects=ciscoConfigCopyMIBObjects, ccCopyMIBCompliance=ccCopyMIBCompliance, ccCopyGroup=ccCopyGroup, ConfigCopyState=ConfigCopyState, ccCopyMIBComplianceRev1=ccCopyMIBComplianceRev1, ccCopyErrorIndex=ccCopyErrorIndex, ccCopyMIBGroups=ccCopyMIBGroups, ccCopyUserPassword=ccCopyUserPassword, ccCopyErrorDeviceWWN=ccCopyErrorDeviceWWN, ccCopyIndex=ccCopyIndex, ccCopyTable=ccCopyTable, ciscoConfigCopyMIB=ciscoConfigCopyMIB, ConfigFileType=ConfigFileType, ccCopyFileName=ccCopyFileName, ccCopyTimeStarted=ccCopyTimeStarted)
