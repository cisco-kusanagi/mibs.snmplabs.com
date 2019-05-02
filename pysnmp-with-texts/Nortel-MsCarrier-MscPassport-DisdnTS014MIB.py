#
# PySNMP MIB module Nortel-MsCarrier-MscPassport-DisdnTS014MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Nortel-MsCarrier-MscPassport-DisdnTS014MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:29:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
mscDataSigChan, mscDataSigChanIndex = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChan", "mscDataSigChanIndex")
DisplayString, RowStatus, StorageType, Unsigned32 = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB", "DisplayString", "RowStatus", "StorageType", "Unsigned32")
NonReplicated, Link = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-TextualConventionsMIB", "NonReplicated", "Link")
mscPassportMIBs, = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-UsefulDefinitionsMIB", "mscPassportMIBs")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, NotificationType, Integer32, Counter64, MibIdentifier, IpAddress, Counter32, Bits, TimeTicks, Gauge32, ModuleIdentity, iso, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "NotificationType", "Integer32", "Counter64", "MibIdentifier", "IpAddress", "Counter32", "Bits", "TimeTicks", "Gauge32", "ModuleIdentity", "iso", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
disdnTS014MIB = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 114))
mscDataSigChanTS014 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9))
mscDataSigChanTS014RowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 1), )
if mibBuilder.loadTexts: mscDataSigChanTS014RowStatusTable.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanTS014RowStatusTable.setDescription('This entry controls the addition and deletion of mscDataSigChanTS014 components.')
mscDataSigChanTS014RowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 1, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"), (0, "Nortel-MsCarrier-MscPassport-DisdnTS014MIB", "mscDataSigChanTS014Index"))
if mibBuilder.loadTexts: mscDataSigChanTS014RowStatusEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanTS014RowStatusEntry.setDescription('A single entry in the table represents a single mscDataSigChanTS014 component.')
mscDataSigChanTS014RowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 1, 1, 1), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscDataSigChanTS014RowStatus.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanTS014RowStatus.setDescription('This variable is used as the basis for SNMP naming of mscDataSigChanTS014 components. These components can be added and deleted.')
mscDataSigChanTS014ComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanTS014ComponentName.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanTS014ComponentName.setDescription("This variable provides the component's string name for use with the ASCII Console Interface")
mscDataSigChanTS014StorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanTS014StorageType.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanTS014StorageType.setDescription('This variable represents the storage type value for the mscDataSigChanTS014 tables.')
mscDataSigChanTS014Index = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 1, 1, 10), NonReplicated())
if mibBuilder.loadTexts: mscDataSigChanTS014Index.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanTS014Index.setDescription('This variable represents the index for the mscDataSigChanTS014 tables.')
mscDataSigChanTS014L2Table = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 11), )
if mibBuilder.loadTexts: mscDataSigChanTS014L2Table.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanTS014L2Table.setDescription('This group represents the provisionable Layer 2 attributes of the Q931 CCITT protocol.')
mscDataSigChanTS014L2Entry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 11, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"), (0, "Nortel-MsCarrier-MscPassport-DisdnTS014MIB", "mscDataSigChanTS014Index"))
if mibBuilder.loadTexts: mscDataSigChanTS014L2Entry.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanTS014L2Entry.setDescription('An entry in the mscDataSigChanTS014L2Table.')
mscDataSigChanTS014T23 = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 11, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 15)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscDataSigChanTS014T23.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanTS014T23.setDescription('This attribute specifies the layer2 enable request timer.')
mscDataSigChanTS014T200 = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 11, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 20)).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscDataSigChanTS014T200.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanTS014T200.setDescription('This attribute specifies the maximum time between a layer 2 frame and its acknowledgement')
mscDataSigChanTS014N200 = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 11, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 8)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscDataSigChanTS014N200.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanTS014N200.setDescription('This attribute specifies the maximum number of re-transmissions of a layer2 frame.')
mscDataSigChanTS014T203 = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 11, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(2, 40)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscDataSigChanTS014T203.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanTS014T203.setDescription('This attribute specifies the maximum time that a no layer 2 traffic situation can last. Expiry triggers a check on whether the far end is a live.')
mscDataSigChanTS014N201 = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 11, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(4, 260)).clone(260)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscDataSigChanTS014N201.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanTS014N201.setDescription('This attribute specifies the maximum number of octets in an information field.')
mscDataSigChanTS014CircuitSwitchedK = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 11, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 632)).clone(7)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscDataSigChanTS014CircuitSwitchedK.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanTS014CircuitSwitchedK.setDescription('This attribute specifies the maximum number of frames for B channel use.')
mscDataSigChanTS014ProvTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 13), )
if mibBuilder.loadTexts: mscDataSigChanTS014ProvTable.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanTS014ProvTable.setDescription('This group defines the general options of the d-channel signalling link.')
mscDataSigChanTS014ProvEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 13, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"), (0, "Nortel-MsCarrier-MscPassport-DisdnTS014MIB", "mscDataSigChanTS014Index"))
if mibBuilder.loadTexts: mscDataSigChanTS014ProvEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanTS014ProvEntry.setDescription('An entry in the mscDataSigChanTS014ProvTable.')
mscDataSigChanTS014Side = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 13, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("network", 1), ("user", 2))).clone('user')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscDataSigChanTS014Side.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanTS014Side.setDescription('This attribute specifies whether the layer 2 HDLC interface is the network or user side of the connection.')
mscDataSigChanTS014OperTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 15), )
if mibBuilder.loadTexts: mscDataSigChanTS014OperTable.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanTS014OperTable.setDescription('This group provides the operational attributes for the signalling protocol.')
mscDataSigChanTS014OperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 15, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"), (0, "Nortel-MsCarrier-MscPassport-DisdnTS014MIB", "mscDataSigChanTS014Index"))
if mibBuilder.loadTexts: mscDataSigChanTS014OperEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanTS014OperEntry.setDescription('An entry in the mscDataSigChanTS014OperTable.')
mscDataSigChanTS014ActiveChannels = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 15, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanTS014ActiveChannels.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanTS014ActiveChannels.setDescription('This attribute indicates the number of currently active channels. This includes data and voice channels.')
mscDataSigChanTS014PeakActiveChannels = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 15, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanTS014PeakActiveChannels.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanTS014PeakActiveChannels.setDescription('This attribute indicates the maximum number of channels that have been active on this signalling channel during the last polling period.')
mscDataSigChanTS014DChanStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 15, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("outOfService", 0), ("establishing", 1), ("established", 2), ("enabling", 3), ("inService", 4), ("restarting", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanTS014DChanStatus.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanTS014DChanStatus.setDescription('This attribute indicates the state of the D-channel. outOfService means that there is no layer 2 or layer 3 connectivity to the PBX. establishing means that the signalling channel is attempting to stage the layer 2. established means that the layer 2 is enabled. If the signalling channel stays in the established state, then it is waiting for a restart from the PBX. enabling means that the resources for processing calls are being initialized. If the signalling channel stays in the enabling state then it is waiting for a restart acknowledgement from the PBX. inService means that the resources for processing calls are available. restarting means that the resources for call processing are being rei- initialized.')
mscDataSigChanTS014ToolsTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 16), )
if mibBuilder.loadTexts: mscDataSigChanTS014ToolsTable.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanTS014ToolsTable.setDescription('This group contains a series of operational attributes which turn on and off several kinds of tracing.')
mscDataSigChanTS014ToolsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 16, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"), (0, "Nortel-MsCarrier-MscPassport-DisdnTS014MIB", "mscDataSigChanTS014Index"))
if mibBuilder.loadTexts: mscDataSigChanTS014ToolsEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanTS014ToolsEntry.setDescription('An entry in the mscDataSigChanTS014ToolsTable.')
mscDataSigChanTS014Tracing = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 16, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscDataSigChanTS014Tracing.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanTS014Tracing.setDescription('This attribute defines which types of tracing are active for this signalling channel. The tracing messages are sent to the debug stream. To see the messages the agentQueue attribute in Col/debug must be greater than 0 and a Telnet NMIS session must list the debug stream in in its data streams (ex. set nmis telnet session/1 dataStreams debug). Different types of tracing can be enabled simultaneously. Note that tracing consumes additional CPU resources and will slow down call processing on a heavily loaded card. If there is message block exhaustion tracing will be suspended for a period and then automatically reenabled. An alarm is generated on tracing suspension and resumption. This mechanism protects the function processor against excessive numbers of tracing messages. Types of tracing include: protocolErrors - get details of any protocol errors which are occuring. Protocol errors are also reported in summary form as alarms. q931Summary - Summary of the Q.931 messages on the signalling link, including certain call details (calling number, called number, release codes). q931Hex - Q.931 messages displayed in hex format. Useful to determine protocol compliance in case of errors reported on local or remote ends. q931Symbolic - Q.931 messages parsed to give maximum detail. Useful for understanding content of messages flowing on the link. portHex - Messages in hex format being sent and received on the link. Description of bits: protocolErrors(0) q931Summary(1) q931Hex(2) q931Symbolic(3) portHex(4)')
mscDataSigChanTS014Framer = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 2))
mscDataSigChanTS014FramerRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 2, 1), )
if mibBuilder.loadTexts: mscDataSigChanTS014FramerRowStatusTable.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanTS014FramerRowStatusTable.setDescription('This entry controls the addition and deletion of mscDataSigChanTS014Framer components.')
mscDataSigChanTS014FramerRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 2, 1, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"), (0, "Nortel-MsCarrier-MscPassport-DisdnTS014MIB", "mscDataSigChanTS014Index"), (0, "Nortel-MsCarrier-MscPassport-DisdnTS014MIB", "mscDataSigChanTS014FramerIndex"))
if mibBuilder.loadTexts: mscDataSigChanTS014FramerRowStatusEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanTS014FramerRowStatusEntry.setDescription('A single entry in the table represents a single mscDataSigChanTS014Framer component.')
mscDataSigChanTS014FramerRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 2, 1, 1, 1), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanTS014FramerRowStatus.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanTS014FramerRowStatus.setDescription('This variable is used as the basis for SNMP naming of mscDataSigChanTS014Framer components. These components cannot be added nor deleted.')
mscDataSigChanTS014FramerComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 2, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanTS014FramerComponentName.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanTS014FramerComponentName.setDescription("This variable provides the component's string name for use with the ASCII Console Interface")
mscDataSigChanTS014FramerStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 2, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanTS014FramerStorageType.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanTS014FramerStorageType.setDescription('This variable represents the storage type value for the mscDataSigChanTS014Framer tables.')
mscDataSigChanTS014FramerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 2, 1, 1, 10), NonReplicated())
if mibBuilder.loadTexts: mscDataSigChanTS014FramerIndex.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanTS014FramerIndex.setDescription('This variable represents the index for the mscDataSigChanTS014Framer tables.')
mscDataSigChanTS014FramerProvTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 2, 10), )
if mibBuilder.loadTexts: mscDataSigChanTS014FramerProvTable.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanTS014FramerProvTable.setDescription('This group contains the base provisioning data for the Framer component. Application or hardware interface specific provisioning data is contained in other provisionable Framer groups.')
mscDataSigChanTS014FramerProvEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 2, 10, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"), (0, "Nortel-MsCarrier-MscPassport-DisdnTS014MIB", "mscDataSigChanTS014Index"), (0, "Nortel-MsCarrier-MscPassport-DisdnTS014MIB", "mscDataSigChanTS014FramerIndex"))
if mibBuilder.loadTexts: mscDataSigChanTS014FramerProvEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanTS014FramerProvEntry.setDescription('An entry in the mscDataSigChanTS014FramerProvTable.')
mscDataSigChanTS014FramerInterfaceName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 2, 10, 1, 1), Link()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscDataSigChanTS014FramerInterfaceName.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanTS014FramerInterfaceName.setDescription("This attribute contains a hardware component name. The attribute associates the application with a specific link. This defines the module processor on which Framer's parent component (as well as Framer itself) will run.")
mscDataSigChanTS014FramerStateTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 2, 12), )
if mibBuilder.loadTexts: mscDataSigChanTS014FramerStateTable.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanTS014FramerStateTable.setDescription('This group contains the three OSI State attributes. The descriptions generically indicate what each state attribute implies about the component. Note that not all the values and state combinations described here are supported by every component which uses this group. For component-specific information and the valid state combinations, refer to NTP 241-7001-150, Passport Operations and Maintenance Guide.')
mscDataSigChanTS014FramerStateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 2, 12, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"), (0, "Nortel-MsCarrier-MscPassport-DisdnTS014MIB", "mscDataSigChanTS014Index"), (0, "Nortel-MsCarrier-MscPassport-DisdnTS014MIB", "mscDataSigChanTS014FramerIndex"))
if mibBuilder.loadTexts: mscDataSigChanTS014FramerStateEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanTS014FramerStateEntry.setDescription('An entry in the mscDataSigChanTS014FramerStateTable.')
mscDataSigChanTS014FramerAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 2, 12, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("locked", 0), ("unlocked", 1), ("shuttingDown", 2))).clone('unlocked')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanTS014FramerAdminState.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanTS014FramerAdminState.setDescription('This attribute indicates the OSI Administrative State of the component. The value locked indicates that the component is administratively prohibited from providing services for its users. A Lock or Lock - force command has been previously issued for this component. When the value is locked, the value of usageState must be idle. The value shuttingDown indicates that the component is administratively permitted to provide service to its existing users only. A Lock command was issued against the component and it is in the process of shutting down. The value unlocked indicates that the component is administratively permitted to provide services for its users. To enter this state, issue an Unlock command to this component.')
mscDataSigChanTS014FramerOperationalState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 2, 12, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1))).clone('disabled')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanTS014FramerOperationalState.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanTS014FramerOperationalState.setDescription('This attribute indicates the OSI Operational State of the component. The value enabled indicates that the component is available for operation. Note that if adminState is locked, it would still not be providing service. The value disabled indicates that the component is not available for operation. For example, something is wrong with the component itself, or with another component on which this one depends. If the value is disabled, the usageState must be idle.')
mscDataSigChanTS014FramerUsageState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 2, 12, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("idle", 0), ("active", 1), ("busy", 2))).clone('idle')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanTS014FramerUsageState.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanTS014FramerUsageState.setDescription('This attribute indicates the OSI Usage State of the component. The value idle indicates that the component is not currently in use. The value active indicates that the component is in use and has spare capacity to provide for additional users. The value busy indicates that the component is in use and has no spare operating capacity for additional users at this time.')
mscDataSigChanTS014FramerStatsTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 2, 13), )
if mibBuilder.loadTexts: mscDataSigChanTS014FramerStatsTable.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanTS014FramerStatsTable.setDescription('This group contains the operational statistics data for a Framer component.')
mscDataSigChanTS014FramerStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 2, 13, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"), (0, "Nortel-MsCarrier-MscPassport-DisdnTS014MIB", "mscDataSigChanTS014Index"), (0, "Nortel-MsCarrier-MscPassport-DisdnTS014MIB", "mscDataSigChanTS014FramerIndex"))
if mibBuilder.loadTexts: mscDataSigChanTS014FramerStatsEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanTS014FramerStatsEntry.setDescription('An entry in the mscDataSigChanTS014FramerStatsTable.')
mscDataSigChanTS014FramerFrmToIf = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 2, 13, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanTS014FramerFrmToIf.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanTS014FramerFrmToIf.setDescription('This attribute counts the number of frames transmitted to the link interface by Framer. This count wraps to zero after reaching its maximum value.')
mscDataSigChanTS014FramerFrmFromIf = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 2, 13, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanTS014FramerFrmFromIf.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanTS014FramerFrmFromIf.setDescription('This attribute counts the number of frames received from the link interface by Framer. This count wraps to zero after reaching its maximum value.')
mscDataSigChanTS014FramerOctetFromIf = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 2, 13, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanTS014FramerOctetFromIf.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanTS014FramerOctetFromIf.setDescription('The number of bytes received from the link interface by Framer.')
mscDataSigChanTS014FramerAborts = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 2, 13, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanTS014FramerAborts.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanTS014FramerAborts.setDescription('This attribute counts the total number of aborts received. This count wraps to zero after reaching its maximum value.')
mscDataSigChanTS014FramerCrcErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 2, 13, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanTS014FramerCrcErrors.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanTS014FramerCrcErrors.setDescription('This attribute counts the total number of frames with CRC errors. This count wraps to zero after reaching its maximum value.')
mscDataSigChanTS014FramerLrcErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 2, 13, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanTS014FramerLrcErrors.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanTS014FramerLrcErrors.setDescription('This attribute counts the total number of frames with LRC errors. This count wraps to zero after reaching its maximum value.')
mscDataSigChanTS014FramerNonOctetErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 2, 13, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanTS014FramerNonOctetErrors.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanTS014FramerNonOctetErrors.setDescription('This attribute counts the total number of frames that were non octet aligned. This count wraps to zero after reaching its maximum value.')
mscDataSigChanTS014FramerOverruns = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 2, 13, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanTS014FramerOverruns.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanTS014FramerOverruns.setDescription('This attribute counts the total number of frames received from the link for which overruns occurred. This count wraps to zero after reaching its maximum value.')
mscDataSigChanTS014FramerUnderruns = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 2, 13, 1, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanTS014FramerUnderruns.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanTS014FramerUnderruns.setDescription('This attribute counts the total number of frames transmitted to the link for which underruns occurred. This count wraps to zero after reaching its maximum value.')
mscDataSigChanTS014FramerLargeFrmErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 9, 2, 13, 1, 10), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanTS014FramerLargeFrmErrors.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanTS014FramerLargeFrmErrors.setDescription('This attribute counts the total number of frames received which were too large. The frame was longer than 500 bytes. This count wraps to zero after reaching its maximum value.')
disdnTS014Group = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 114, 1))
disdnTS014GroupCA = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 114, 1, 1))
disdnTS014GroupCA02 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 114, 1, 1, 3))
disdnTS014GroupCA02A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 114, 1, 1, 3, 2))
disdnTS014Capabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 114, 3))
disdnTS014CapabilitiesCA = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 114, 3, 1))
disdnTS014CapabilitiesCA02 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 114, 3, 1, 3))
disdnTS014CapabilitiesCA02A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 114, 3, 1, 3, 2))
mibBuilder.exportSymbols("Nortel-MsCarrier-MscPassport-DisdnTS014MIB", mscDataSigChanTS014ToolsTable=mscDataSigChanTS014ToolsTable, mscDataSigChanTS014FramerOperationalState=mscDataSigChanTS014FramerOperationalState, mscDataSigChanTS014OperEntry=mscDataSigChanTS014OperEntry, mscDataSigChanTS014FramerOverruns=mscDataSigChanTS014FramerOverruns, disdnTS014MIB=disdnTS014MIB, mscDataSigChanTS014FramerUnderruns=mscDataSigChanTS014FramerUnderruns, mscDataSigChanTS014OperTable=mscDataSigChanTS014OperTable, mscDataSigChanTS014L2Entry=mscDataSigChanTS014L2Entry, mscDataSigChanTS014ProvTable=mscDataSigChanTS014ProvTable, mscDataSigChanTS014N200=mscDataSigChanTS014N200, mscDataSigChanTS014ComponentName=mscDataSigChanTS014ComponentName, mscDataSigChanTS014FramerProvTable=mscDataSigChanTS014FramerProvTable, disdnTS014GroupCA02A=disdnTS014GroupCA02A, mscDataSigChanTS014Index=mscDataSigChanTS014Index, mscDataSigChanTS014FramerNonOctetErrors=mscDataSigChanTS014FramerNonOctetErrors, mscDataSigChanTS014=mscDataSigChanTS014, mscDataSigChanTS014CircuitSwitchedK=mscDataSigChanTS014CircuitSwitchedK, mscDataSigChanTS014RowStatusEntry=mscDataSigChanTS014RowStatusEntry, mscDataSigChanTS014FramerLargeFrmErrors=mscDataSigChanTS014FramerLargeFrmErrors, mscDataSigChanTS014FramerOctetFromIf=mscDataSigChanTS014FramerOctetFromIf, mscDataSigChanTS014FramerComponentName=mscDataSigChanTS014FramerComponentName, mscDataSigChanTS014FramerProvEntry=mscDataSigChanTS014FramerProvEntry, mscDataSigChanTS014FramerFrmFromIf=mscDataSigChanTS014FramerFrmFromIf, mscDataSigChanTS014FramerInterfaceName=mscDataSigChanTS014FramerInterfaceName, mscDataSigChanTS014FramerRowStatusTable=mscDataSigChanTS014FramerRowStatusTable, mscDataSigChanTS014FramerStatsEntry=mscDataSigChanTS014FramerStatsEntry, mscDataSigChanTS014RowStatusTable=mscDataSigChanTS014RowStatusTable, mscDataSigChanTS014FramerFrmToIf=mscDataSigChanTS014FramerFrmToIf, mscDataSigChanTS014Tracing=mscDataSigChanTS014Tracing, mscDataSigChanTS014N201=mscDataSigChanTS014N201, mscDataSigChanTS014FramerStateEntry=mscDataSigChanTS014FramerStateEntry, mscDataSigChanTS014FramerIndex=mscDataSigChanTS014FramerIndex, disdnTS014Group=disdnTS014Group, mscDataSigChanTS014FramerStateTable=mscDataSigChanTS014FramerStateTable, disdnTS014Capabilities=disdnTS014Capabilities, mscDataSigChanTS014RowStatus=mscDataSigChanTS014RowStatus, mscDataSigChanTS014T23=mscDataSigChanTS014T23, mscDataSigChanTS014ActiveChannels=mscDataSigChanTS014ActiveChannels, mscDataSigChanTS014T203=mscDataSigChanTS014T203, mscDataSigChanTS014FramerLrcErrors=mscDataSigChanTS014FramerLrcErrors, mscDataSigChanTS014ProvEntry=mscDataSigChanTS014ProvEntry, mscDataSigChanTS014T200=mscDataSigChanTS014T200, mscDataSigChanTS014FramerRowStatusEntry=mscDataSigChanTS014FramerRowStatusEntry, mscDataSigChanTS014L2Table=mscDataSigChanTS014L2Table, mscDataSigChanTS014FramerStorageType=mscDataSigChanTS014FramerStorageType, mscDataSigChanTS014DChanStatus=mscDataSigChanTS014DChanStatus, mscDataSigChanTS014Framer=mscDataSigChanTS014Framer, mscDataSigChanTS014FramerAdminState=mscDataSigChanTS014FramerAdminState, disdnTS014CapabilitiesCA02A=disdnTS014CapabilitiesCA02A, mscDataSigChanTS014FramerUsageState=mscDataSigChanTS014FramerUsageState, mscDataSigChanTS014FramerStatsTable=mscDataSigChanTS014FramerStatsTable, mscDataSigChanTS014FramerRowStatus=mscDataSigChanTS014FramerRowStatus, disdnTS014CapabilitiesCA=disdnTS014CapabilitiesCA, disdnTS014CapabilitiesCA02=disdnTS014CapabilitiesCA02, disdnTS014GroupCA02=disdnTS014GroupCA02, mscDataSigChanTS014PeakActiveChannels=mscDataSigChanTS014PeakActiveChannels, mscDataSigChanTS014Side=mscDataSigChanTS014Side, mscDataSigChanTS014FramerAborts=mscDataSigChanTS014FramerAborts, mscDataSigChanTS014FramerCrcErrors=mscDataSigChanTS014FramerCrcErrors, disdnTS014GroupCA=disdnTS014GroupCA, mscDataSigChanTS014ToolsEntry=mscDataSigChanTS014ToolsEntry, mscDataSigChanTS014StorageType=mscDataSigChanTS014StorageType)
