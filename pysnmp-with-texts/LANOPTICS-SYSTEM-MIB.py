#
# PySNMP MIB module LANOPTICS-SYSTEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/LANOPTICS-SYSTEM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:05:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, ModuleIdentity, TimeTicks, ObjectIdentity, NotificationType, enterprises, Bits, IpAddress, iso, Counter32, Counter64, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ModuleIdentity", "TimeTicks", "ObjectIdentity", "NotificationType", "enterprises", "Bits", "IpAddress", "iso", "Counter32", "Counter64", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
lanOptics = MibIdentifier((1, 3, 6, 1, 4, 1, 224))
lanOpticsSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 224, 2))
lanOpticsSystemCMOS = MibIdentifier((1, 3, 6, 1, 4, 1, 224, 2, 3))
lanOpticsSystemCMOSIp = MibIdentifier((1, 3, 6, 1, 4, 1, 224, 2, 3, 1))
lanOpticsSystemCMOSHub = MibIdentifier((1, 3, 6, 1, 4, 1, 224, 2, 3, 2))
lanOpticsSystemCMOSRPL = MibIdentifier((1, 3, 6, 1, 4, 1, 224, 2, 3, 3))
lanOpticsSystemCMOSSerial = MibIdentifier((1, 3, 6, 1, 4, 1, 224, 2, 3, 4))
lanOpticsSystemCMOSSRAM = MibIdentifier((1, 3, 6, 1, 4, 1, 224, 2, 3, 5))
lanOpticsSystemCMOSSNMP = MibIdentifier((1, 3, 6, 1, 4, 1, 224, 2, 3, 6))
lanOpticsSystemCMOSACCESS = MibIdentifier((1, 3, 6, 1, 4, 1, 224, 2, 3, 7))
lanOpticsSystemCMOSBRDG = MibIdentifier((1, 3, 6, 1, 4, 1, 224, 2, 3, 8))
snSysDirectory = MibScalar((1, 3, 6, 1, 4, 1, 224, 2, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snSysDirectory.setStatus('mandatory')
if mibBuilder.loadTexts: snSysDirectory.setDescription('Gives the agent directory content (make DOS DIR command on agent directory).')
snAgentVersion = MibScalar((1, 3, 6, 1, 4, 1, 224, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snAgentVersion.setStatus('mandatory')
if mibBuilder.loadTexts: snAgentVersion.setDescription('Gives the agent major version in the high order word and the minor version in low order word.')
snSysCMOSIpInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 224, 2, 3, 1, 1), )
if mibBuilder.loadTexts: snSysCMOSIpInterfaceTable.setStatus('mandatory')
if mibBuilder.loadTexts: snSysCMOSIpInterfaceTable.setDescription('A list of network interfaces.')
pysmiFakeCol1000 = MibTableColumn((1, 3, 6, 1, 4, 1, 224, 2, 3, 1, 1, 1) + (1000, ), Integer32())
snSysCMOSIpInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 224, 2, 3, 1, 1, 1), ).setIndexNames((0, "LANOPTICS-SYSTEM-MIB", "pysmiFakeCol1000"))
if mibBuilder.loadTexts: snSysCMOSIpInterfaceEntry.setStatus('mandatory')
if mibBuilder.loadTexts: snSysCMOSIpInterfaceEntry.setDescription('An interface entry containing the Ipaddress and net-mask.')
snSysCMOSIpIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 224, 2, 3, 1, 1, 1, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snSysCMOSIpIpAddr.setStatus('mandatory')
if mibBuilder.loadTexts: snSysCMOSIpIpAddr.setDescription("Gives the interface's IpAddress")
snSysCMOSIpNetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 224, 2, 3, 1, 1, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snSysCMOSIpNetMask.setStatus('mandatory')
if mibBuilder.loadTexts: snSysCMOSIpNetMask.setDescription("Gives the interfaces's netmask")
snSysCMOSIpDefGw = MibScalar((1, 3, 6, 1, 4, 1, 224, 2, 3, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snSysCMOSIpDefGw.setStatus('mandatory')
if mibBuilder.loadTexts: snSysCMOSIpDefGw.setDescription("Gives the agent's default gateway.")
snSysCMOSIpTFTPOp = MibScalar((1, 3, 6, 1, 4, 1, 224, 2, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noTFTP", 1), ("limited", 2), ("continuous", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snSysCMOSIpTFTPOp.setStatus('mandatory')
if mibBuilder.loadTexts: snSysCMOSIpTFTPOp.setDescription('Gives the TFTP policy: 1 - No TFTP, 2 - Optional, 3 - Always')
snSysCMOSIpTFTPAddr = MibScalar((1, 3, 6, 1, 4, 1, 224, 2, 3, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snSysCMOSIpTFTPAddr.setStatus('mandatory')
if mibBuilder.loadTexts: snSysCMOSIpTFTPAddr.setDescription('Gives the TFTP server Ip address.')
snSysCMOSIpTFTPFileName = MibScalar((1, 3, 6, 1, 4, 1, 224, 2, 3, 1, 5), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snSysCMOSIpTFTPFileName.setStatus('mandatory')
if mibBuilder.loadTexts: snSysCMOSIpTFTPFileName.setDescription('Gives the boot file name at the server (full path).')
snSysCMOSIpTFTPDrive = MibScalar((1, 3, 6, 1, 4, 1, 224, 2, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(41, 42, 43, 44))).clone(namedValues=NamedValues(("driveA", 41), ("driveB", 42), ("driveC", 43), ("driveD", 44)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snSysCMOSIpTFTPDrive.setStatus('mandatory')
if mibBuilder.loadTexts: snSysCMOSIpTFTPDrive.setDescription('Gives the TFTP operation destination drive (value of ASCII character).')
snSysCMOSHubSlotConfigTable = MibTable((1, 3, 6, 1, 4, 1, 224, 2, 3, 2, 1), )
if mibBuilder.loadTexts: snSysCMOSHubSlotConfigTable.setStatus('mandatory')
if mibBuilder.loadTexts: snSysCMOSHubSlotConfigTable.setDescription('A list of slots entries. Each entry in this table, contains the last 20 operations performed on the slot.')
pysmiFakeCol1001 = MibTableColumn((1, 3, 6, 1, 4, 1, 224, 2, 3, 2, 1, 1) + (1001, ), Integer32())
snSysCMOSHubSlotConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 224, 2, 3, 2, 1, 1), ).setIndexNames((0, "LANOPTICS-SYSTEM-MIB", "pysmiFakeCol1001"))
if mibBuilder.loadTexts: snSysCMOSHubSlotConfigEntry.setStatus('mandatory')
snSysSlotLastOperations = MibTableColumn((1, 3, 6, 1, 4, 1, 224, 2, 3, 2, 1, 1, 1), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snSysSlotLastOperations.setStatus('mandatory')
if mibBuilder.loadTexts: snSysSlotLastOperations.setDescription(' A description of last 20 operations performed, on the slot')
snSysResetSlotQueue = MibTableColumn((1, 3, 6, 1, 4, 1, 224, 2, 3, 2, 1, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snSysResetSlotQueue.setStatus('mandatory')
if mibBuilder.loadTexts: snSysResetSlotQueue.setDescription(' Resets the last 20 operations queue.')
snSysCMOSHubSaveHubFunctions = MibScalar((1, 3, 6, 1, 4, 1, 224, 2, 3, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("not-saved", 1), ("saved", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snSysCMOSHubSaveHubFunctions.setStatus('mandatory')
if mibBuilder.loadTexts: snSysCMOSHubSaveHubFunctions.setDescription('Save (2) /Do not Save (1) Hub managment functions in non-volatile memory.')
snSysCMOSRPLMode = MibScalar((1, 3, 6, 1, 4, 1, 224, 2, 3, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("rpl-off", 1), ("rpl-on", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snSysCMOSRPLMode.setStatus('mandatory')
if mibBuilder.loadTexts: snSysCMOSRPLMode.setDescription('Determine if the image will be loaded through RPL at next boot: RPL off - 1, RPL on - 2.')
snSysCMOSFlashMode = MibScalar((1, 3, 6, 1, 4, 1, 224, 2, 3, 3, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("flash-off", 1), ("flash-on", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snSysCMOSFlashMode.setStatus('mandatory')
if mibBuilder.loadTexts: snSysCMOSFlashMode.setDescription('Determine if the image will be loaded from flash memory at next boot : flash on - 2, flash off - 1.')
snSysCMOSSerialMode = MibScalar((1, 3, 6, 1, 4, 1, 224, 2, 3, 4, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("proprietary", 1), ("slip", 2), ("none", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snSysCMOSSerialMode.setStatus('mandatory')
if mibBuilder.loadTexts: snSysCMOSSerialMode.setDescription('Determine the serial port usage mode : Proprietary - 1, SLIP - 2, None - 3.')
snSysCMOSSerialComSelect = MibScalar((1, 3, 6, 1, 4, 1, 224, 2, 3, 4, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("sr-COM1", 1), ("sr-COM2", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snSysCMOSSerialComSelect.setStatus('mandatory')
if mibBuilder.loadTexts: snSysCMOSSerialComSelect.setDescription('Determine which COM port is used. ')
snSysCMOSSerialBaudRate = MibScalar((1, 3, 6, 1, 4, 1, 224, 2, 3, 4, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("baud1200", 1), ("baud2400", 2), ("baud4800", 3), ("baud9600", 4), ("baud19200", 5), ("baud38300", 6), ("baud57600", 7)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snSysCMOSSerialBaudRate.setStatus('mandatory')
if mibBuilder.loadTexts: snSysCMOSSerialBaudRate.setDescription('Determine the serial port baud rate : 1200 - 1, 2400 - 2, 4800 - 3, 9600 - 4, 19200 - 5, 38300 - 6, 57600 - 7 ')
snSysCMOSSerialWordLength = MibScalar((1, 3, 6, 1, 4, 1, 224, 2, 3, 4, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("bits-7", 1), ("bits-8", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snSysCMOSSerialWordLength.setStatus('mandatory')
if mibBuilder.loadTexts: snSysCMOSSerialWordLength.setDescription('Determine the data bits length : 7 Bits - 1, 8 Bits -2 ')
snSysCMOSSerialStopBits = MibScalar((1, 3, 6, 1, 4, 1, 224, 2, 3, 4, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("bits-1", 1), ("bits-15", 2), ("bits-2", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snSysCMOSSerialStopBits.setStatus('mandatory')
if mibBuilder.loadTexts: snSysCMOSSerialStopBits.setDescription('Determine the number of stop bits; values allowed : 1 Bit - 1, 1.5 Bits - 2, 2 Bits - 3.')
snSysCMOSSerialParityCheck = MibScalar((1, 3, 6, 1, 4, 1, 224, 2, 3, 4, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("even", 1), ("odd", 2), ("none", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snSysCMOSSerialParityCheck.setStatus('mandatory')
if mibBuilder.loadTexts: snSysCMOSSerialParityCheck.setDescription('Determine the parity check policy : Even - 1, Odd - 2, None - 3.')
snSysCMOSSRAMKeepAliveSecInterval = MibScalar((1, 3, 6, 1, 4, 1, 224, 2, 3, 5, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snSysCMOSSRAMKeepAliveSecInterval.setStatus('mandatory')
if mibBuilder.loadTexts: snSysCMOSSRAMKeepAliveSecInterval.setDescription('Determine the interval of the keep alive frame in seconds ')
snSysCMOSSNMPCommunitiesNum = MibScalar((1, 3, 6, 1, 4, 1, 224, 2, 3, 6, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snSysCMOSSNMPCommunitiesNum.setStatus('mandatory')
if mibBuilder.loadTexts: snSysCMOSSNMPCommunitiesNum.setDescription('Keeps the number of communities.')
snSysCMOSSNMPTrapManagersNum = MibScalar((1, 3, 6, 1, 4, 1, 224, 2, 3, 6, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snSysCMOSSNMPTrapManagersNum.setStatus('mandatory')
if mibBuilder.loadTexts: snSysCMOSSNMPTrapManagersNum.setDescription('Keeps the number of managers that traps are send to.')
snSysCMOSSNMPCommunitiesTable = MibTable((1, 3, 6, 1, 4, 1, 224, 2, 3, 6, 3), )
if mibBuilder.loadTexts: snSysCMOSSNMPCommunitiesTable.setStatus('mandatory')
if mibBuilder.loadTexts: snSysCMOSSNMPCommunitiesTable.setDescription('A table containing the SNMP communities')
pysmiFakeCol1002 = MibTableColumn((1, 3, 6, 1, 4, 1, 224, 2, 3, 6, 3, 1) + (1002, ), Integer32())
snSysCMOSSNMPCommunitiesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 224, 2, 3, 6, 3, 1), ).setIndexNames((0, "LANOPTICS-SYSTEM-MIB", "pysmiFakeCol1002"))
if mibBuilder.loadTexts: snSysCMOSSNMPCommunitiesEntry.setStatus('mandatory')
if mibBuilder.loadTexts: snSysCMOSSNMPCommunitiesEntry.setDescription('An entry community info')
snSysCMOSSNMPCommunityName = MibTableColumn((1, 3, 6, 1, 4, 1, 224, 2, 3, 6, 3, 1, 1), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snSysCMOSSNMPCommunityName.setStatus('mandatory')
if mibBuilder.loadTexts: snSysCMOSSNMPCommunityName.setDescription('This variable will give the community name.')
snSysCMOSSNMPCommunityPrivs = MibTableColumn((1, 3, 6, 1, 4, 1, 224, 2, 3, 6, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("read-Only", 1), ("read-Write", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snSysCMOSSNMPCommunityPrivs.setStatus('mandatory')
if mibBuilder.loadTexts: snSysCMOSSNMPCommunityPrivs.setDescription('This variable will give the community privilages: Read Only - 1, Read/Write - 2.')
snSysCMOSSNMPTrapCommunitiesTable = MibTable((1, 3, 6, 1, 4, 1, 224, 2, 3, 6, 4), )
if mibBuilder.loadTexts: snSysCMOSSNMPTrapCommunitiesTable.setStatus('mandatory')
if mibBuilder.loadTexts: snSysCMOSSNMPTrapCommunitiesTable.setDescription('A table containing the SNMP communities')
pysmiFakeCol1003 = MibTableColumn((1, 3, 6, 1, 4, 1, 224, 2, 3, 6, 4, 1) + (1003, ), Integer32())
snSysCMOSSNMPTrapCommunitiesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 224, 2, 3, 6, 4, 1), ).setIndexNames((0, "LANOPTICS-SYSTEM-MIB", "pysmiFakeCol1003"))
if mibBuilder.loadTexts: snSysCMOSSNMPTrapCommunitiesEntry.setStatus('mandatory')
if mibBuilder.loadTexts: snSysCMOSSNMPTrapCommunitiesEntry.setDescription('An entry of trap IP destinations.')
snSysCMOSSNMPTrapCommunityIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 224, 2, 3, 6, 4, 1, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snSysCMOSSNMPTrapCommunityIpAddr.setStatus('mandatory')
if mibBuilder.loadTexts: snSysCMOSSNMPTrapCommunityIpAddr.setDescription('This variable gives a manager IP address for traps destination.')
snSysCMOSACCESSOffset = MibScalar((1, 3, 6, 1, 4, 1, 224, 2, 3, 7, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snSysCMOSACCESSOffset.setStatus('mandatory')
if mibBuilder.loadTexts: snSysCMOSACCESSOffset.setDescription('Gives the offset in the CMOS array. For internal use only')
snSysCMOSACCESSLength = MibScalar((1, 3, 6, 1, 4, 1, 224, 2, 3, 7, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snSysCMOSACCESSLength.setStatus('mandatory')
if mibBuilder.loadTexts: snSysCMOSACCESSLength.setDescription('Gives the length (max 512) in the CMOS array. For internal use only,')
snSysCMOSACCESSSequence = MibScalar((1, 3, 6, 1, 4, 1, 224, 2, 3, 7, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snSysCMOSACCESSSequence.setStatus('mandatory')
if mibBuilder.loadTexts: snSysCMOSACCESSSequence.setDescription('Gives a sequnce of bytes from CMOS array. For internal use only')
snSysCMOSBRDGradius = MibScalar((1, 3, 6, 1, 4, 1, 224, 2, 3, 8, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snSysCMOSBRDGradius.setStatus('mandatory')
if mibBuilder.loadTexts: snSysCMOSBRDGradius.setDescription('Sets the discovery radius. Value = 0-7. 0=disable bridge.')
snSysCMOSBRDGlinkNumber = MibScalar((1, 3, 6, 1, 4, 1, 224, 2, 3, 8, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snSysCMOSBRDGlinkNumber.setStatus('mandatory')
if mibBuilder.loadTexts: snSysCMOSBRDGlinkNumber.setDescription('Sets the Link number. Value = 0-3. ')
snSysCMOSBRDGpassword = MibScalar((1, 3, 6, 1, 4, 1, 224, 2, 3, 8, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snSysCMOSBRDGpassword.setStatus('mandatory')
if mibBuilder.loadTexts: snSysCMOSBRDGpassword.setDescription('Sets the bridge password. 8 characters . ')
mibBuilder.exportSymbols("LANOPTICS-SYSTEM-MIB", lanOpticsSystemCMOSIp=lanOpticsSystemCMOSIp, snSysDirectory=snSysDirectory, snSysCMOSHubSlotConfigTable=snSysCMOSHubSlotConfigTable, lanOpticsSystemCMOSSNMP=lanOpticsSystemCMOSSNMP, snSysCMOSIpTFTPFileName=snSysCMOSIpTFTPFileName, lanOptics=lanOptics, snSysCMOSIpTFTPOp=snSysCMOSIpTFTPOp, snSysCMOSFlashMode=snSysCMOSFlashMode, snSysCMOSSerialStopBits=snSysCMOSSerialStopBits, snSysCMOSSNMPCommunitiesTable=snSysCMOSSNMPCommunitiesTable, snSysCMOSSNMPTrapManagersNum=snSysCMOSSNMPTrapManagersNum, snSysCMOSSerialBaudRate=snSysCMOSSerialBaudRate, snSysCMOSSNMPCommunityName=snSysCMOSSNMPCommunityName, snSysCMOSSNMPCommunitiesEntry=snSysCMOSSNMPCommunitiesEntry, lanOpticsSystemCMOSSRAM=lanOpticsSystemCMOSSRAM, lanOpticsSystemCMOS=lanOpticsSystemCMOS, lanOpticsSystemCMOSACCESS=lanOpticsSystemCMOSACCESS, snSysCMOSIpIpAddr=snSysCMOSIpIpAddr, snSysCMOSSerialParityCheck=snSysCMOSSerialParityCheck, snSysCMOSACCESSSequence=snSysCMOSACCESSSequence, pysmiFakeCol1001=pysmiFakeCol1001, lanOpticsSystemCMOSHub=lanOpticsSystemCMOSHub, snSysCMOSIpTFTPAddr=snSysCMOSIpTFTPAddr, snSysCMOSHubSlotConfigEntry=snSysCMOSHubSlotConfigEntry, snSysCMOSSerialMode=snSysCMOSSerialMode, snSysCMOSSNMPCommunitiesNum=snSysCMOSSNMPCommunitiesNum, snSysCMOSSNMPTrapCommunitiesTable=snSysCMOSSNMPTrapCommunitiesTable, lanOpticsSystem=lanOpticsSystem, snSysCMOSSNMPCommunityPrivs=snSysCMOSSNMPCommunityPrivs, snSysCMOSBRDGlinkNumber=snSysCMOSBRDGlinkNumber, lanOpticsSystemCMOSBRDG=lanOpticsSystemCMOSBRDG, snSysSlotLastOperations=snSysSlotLastOperations, snSysResetSlotQueue=snSysResetSlotQueue, lanOpticsSystemCMOSSerial=lanOpticsSystemCMOSSerial, snSysCMOSSNMPTrapCommunitiesEntry=snSysCMOSSNMPTrapCommunitiesEntry, snSysCMOSSRAMKeepAliveSecInterval=snSysCMOSSRAMKeepAliveSecInterval, snSysCMOSSerialComSelect=snSysCMOSSerialComSelect, snSysCMOSIpInterfaceEntry=snSysCMOSIpInterfaceEntry, snSysCMOSRPLMode=snSysCMOSRPLMode, snSysCMOSSerialWordLength=snSysCMOSSerialWordLength, snSysCMOSSNMPTrapCommunityIpAddr=snSysCMOSSNMPTrapCommunityIpAddr, snAgentVersion=snAgentVersion, snSysCMOSACCESSLength=snSysCMOSACCESSLength, pysmiFakeCol1000=pysmiFakeCol1000, snSysCMOSBRDGradius=snSysCMOSBRDGradius, snSysCMOSHubSaveHubFunctions=snSysCMOSHubSaveHubFunctions, pysmiFakeCol1002=pysmiFakeCol1002, pysmiFakeCol1003=pysmiFakeCol1003, snSysCMOSBRDGpassword=snSysCMOSBRDGpassword, snSysCMOSACCESSOffset=snSysCMOSACCESSOffset, snSysCMOSIpNetMask=snSysCMOSIpNetMask, snSysCMOSIpTFTPDrive=snSysCMOSIpTFTPDrive, lanOpticsSystemCMOSRPL=lanOpticsSystemCMOSRPL, snSysCMOSIpDefGw=snSysCMOSIpDefGw, snSysCMOSIpInterfaceTable=snSysCMOSIpInterfaceTable)
