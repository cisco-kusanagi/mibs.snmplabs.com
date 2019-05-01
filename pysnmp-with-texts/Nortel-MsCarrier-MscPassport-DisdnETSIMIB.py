#
# PySNMP MIB module Nortel-MsCarrier-MscPassport-DisdnETSIMIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Nortel-MsCarrier-MscPassport-DisdnETSIMIB
# Produced by pysmi-0.3.4 at Wed May  1 14:29:41 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
mscDataSigChanIndex, mscDataSigChan = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex", "mscDataSigChan")
StorageType, Unsigned32, DisplayString, RowStatus = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB", "StorageType", "Unsigned32", "DisplayString", "RowStatus")
Link, NonReplicated = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-TextualConventionsMIB", "Link", "NonReplicated")
mscPassportMIBs, = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-UsefulDefinitionsMIB", "mscPassportMIBs")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, Unsigned32, Gauge32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter64, MibIdentifier, Integer32, Counter32, iso, ModuleIdentity, Bits, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Unsigned32", "Gauge32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter64", "MibIdentifier", "Integer32", "Counter32", "iso", "ModuleIdentity", "Bits", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
disdnETSIMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 117))
mscDataSigChanEtsi = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10))
mscDataSigChanEtsiRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 1), )
if mibBuilder.loadTexts: mscDataSigChanEtsiRowStatusTable.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanEtsiRowStatusTable.setDescription('This entry controls the addition and deletion of mscDataSigChanEtsi components.')
mscDataSigChanEtsiRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 1, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"), (0, "Nortel-MsCarrier-MscPassport-DisdnETSIMIB", "mscDataSigChanEtsiIndex"))
if mibBuilder.loadTexts: mscDataSigChanEtsiRowStatusEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanEtsiRowStatusEntry.setDescription('A single entry in the table represents a single mscDataSigChanEtsi component.')
mscDataSigChanEtsiRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 1, 1, 1), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscDataSigChanEtsiRowStatus.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanEtsiRowStatus.setDescription('This variable is used as the basis for SNMP naming of mscDataSigChanEtsi components. These components can be added and deleted.')
mscDataSigChanEtsiComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanEtsiComponentName.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanEtsiComponentName.setDescription("This variable provides the component's string name for use with the ASCII Console Interface")
mscDataSigChanEtsiStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanEtsiStorageType.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanEtsiStorageType.setDescription('This variable represents the storage type value for the mscDataSigChanEtsi tables.')
mscDataSigChanEtsiIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 1, 1, 10), NonReplicated())
if mibBuilder.loadTexts: mscDataSigChanEtsiIndex.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanEtsiIndex.setDescription('This variable represents the index for the mscDataSigChanEtsi tables.')
mscDataSigChanEtsiL2Table = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 11), )
if mibBuilder.loadTexts: mscDataSigChanEtsiL2Table.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanEtsiL2Table.setDescription('This group represents the provisionable Layer 2 attributes of the Q931 CCITT protocol.')
mscDataSigChanEtsiL2Entry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 11, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"), (0, "Nortel-MsCarrier-MscPassport-DisdnETSIMIB", "mscDataSigChanEtsiIndex"))
if mibBuilder.loadTexts: mscDataSigChanEtsiL2Entry.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanEtsiL2Entry.setDescription('An entry in the mscDataSigChanEtsiL2Table.')
mscDataSigChanEtsiT23 = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 11, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 15)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscDataSigChanEtsiT23.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanEtsiT23.setDescription('This attribute specifies the layer2 enable request timer.')
mscDataSigChanEtsiT200 = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 11, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 20)).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscDataSigChanEtsiT200.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanEtsiT200.setDescription('This attribute specifies the maximum time between a layer 2 frame and its acknowledgement')
mscDataSigChanEtsiN200 = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 11, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 8)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscDataSigChanEtsiN200.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanEtsiN200.setDescription('This attribute specifies the maximum number of re-transmissions of a layer2 frame.')
mscDataSigChanEtsiT203 = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 11, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(2, 40)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscDataSigChanEtsiT203.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanEtsiT203.setDescription('This attribute specifies the maximum time that a no layer 2 traffic situation can last. Expiry triggers a check on whether the far end is a live.')
mscDataSigChanEtsiN201 = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 11, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(4, 260)).clone(260)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscDataSigChanEtsiN201.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanEtsiN201.setDescription('This attribute specifies the maximum number of octets in an information field.')
mscDataSigChanEtsiCircuitSwitchedK = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 11, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 632)).clone(7)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscDataSigChanEtsiCircuitSwitchedK.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanEtsiCircuitSwitchedK.setDescription('This attribute specifies the maximum number of frames for B channel use.')
mscDataSigChanEtsiProvTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 13), )
if mibBuilder.loadTexts: mscDataSigChanEtsiProvTable.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanEtsiProvTable.setDescription('This group defines the general options of the d-channel signalling link.')
mscDataSigChanEtsiProvEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 13, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"), (0, "Nortel-MsCarrier-MscPassport-DisdnETSIMIB", "mscDataSigChanEtsiIndex"))
if mibBuilder.loadTexts: mscDataSigChanEtsiProvEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanEtsiProvEntry.setDescription('An entry in the mscDataSigChanEtsiProvTable.')
mscDataSigChanEtsiSide = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 13, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("network", 1), ("user", 2))).clone('user')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscDataSigChanEtsiSide.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanEtsiSide.setDescription('This attribute specifies whether the layer 2 HDLC interface is the network or user side of the connection.')
mscDataSigChanEtsiOperTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 15), )
if mibBuilder.loadTexts: mscDataSigChanEtsiOperTable.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanEtsiOperTable.setDescription('This group provides the operational attributes for the signalling protocol.')
mscDataSigChanEtsiOperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 15, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"), (0, "Nortel-MsCarrier-MscPassport-DisdnETSIMIB", "mscDataSigChanEtsiIndex"))
if mibBuilder.loadTexts: mscDataSigChanEtsiOperEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanEtsiOperEntry.setDescription('An entry in the mscDataSigChanEtsiOperTable.')
mscDataSigChanEtsiActiveChannels = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 15, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanEtsiActiveChannels.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanEtsiActiveChannels.setDescription('This attribute indicates the number of currently active channels. This includes data and voice channels.')
mscDataSigChanEtsiPeakActiveChannels = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 15, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanEtsiPeakActiveChannels.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanEtsiPeakActiveChannels.setDescription('This attribute indicates the maximum number of channels that have been active on this signalling channel during the last polling period.')
mscDataSigChanEtsiDChanStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 15, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("outOfService", 0), ("establishing", 1), ("established", 2), ("enabling", 3), ("inService", 4), ("restarting", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanEtsiDChanStatus.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanEtsiDChanStatus.setDescription('This attribute indicates the state of the D-channel. outOfService means that there is no layer 2 or layer 3 connectivity to the PBX. establishing means that the signalling channel is attempting to stage the layer 2. established means that the layer 2 is enabled. If the signalling channel stays in the established state, then it is waiting for a restart from the PBX. enabling means that the resources for processing calls are being initialized. If the signalling channel stays in the enabling state then it is waiting for a restart acknowledgement from the PBX. inService means that the resources for processing calls are available. restarting means that the resources for call processing are being rei- initialized.')
mscDataSigChanEtsiToolsTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 16), )
if mibBuilder.loadTexts: mscDataSigChanEtsiToolsTable.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanEtsiToolsTable.setDescription('This group contains a series of operational attributes which turn on and off several kinds of tracing.')
mscDataSigChanEtsiToolsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 16, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"), (0, "Nortel-MsCarrier-MscPassport-DisdnETSIMIB", "mscDataSigChanEtsiIndex"))
if mibBuilder.loadTexts: mscDataSigChanEtsiToolsEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanEtsiToolsEntry.setDescription('An entry in the mscDataSigChanEtsiToolsTable.')
mscDataSigChanEtsiTracing = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 16, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscDataSigChanEtsiTracing.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanEtsiTracing.setDescription('This attribute defines which types of tracing are active for this signalling channel. The tracing messages are sent to the debug stream. To see the messages the agentQueue attribute in Col/debug must be greater than 0 and a Telnet NMIS session must list the debug stream in in its data streams (ex. set nmis telnet session/1 dataStreams debug). Different types of tracing can be enabled simultaneously. Note that tracing consumes additional CPU resources and will slow down call processing on a heavily loaded card. If there is message block exhaustion tracing will be suspended for a period and then automatically reenabled. An alarm is generated on tracing suspension and resumption. This mechanism protects the function processor against excessive numbers of tracing messages. Types of tracing include: protocolErrors - get details of any protocol errors which are occuring. Protocol errors are also reported in summary form as alarms. q931Summary - Summary of the Q.931 messages on the signalling link, including certain call details (calling number, called number, release codes). q931Hex - Q.931 messages displayed in hex format. Useful to determine protocol compliance in case of errors reported on local or remote ends. q931Symbolic - Q.931 messages parsed to give maximum detail. Useful for understanding content of messages flowing on the link. portHex - Messages in hex format being sent and received on the link. Description of bits: protocolErrors(0) q931Summary(1) q931Hex(2) q931Symbolic(3) portHex(4)')
mscDataSigChanEtsiFramer = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 2))
mscDataSigChanEtsiFramerRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 2, 1), )
if mibBuilder.loadTexts: mscDataSigChanEtsiFramerRowStatusTable.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanEtsiFramerRowStatusTable.setDescription('This entry controls the addition and deletion of mscDataSigChanEtsiFramer components.')
mscDataSigChanEtsiFramerRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 2, 1, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"), (0, "Nortel-MsCarrier-MscPassport-DisdnETSIMIB", "mscDataSigChanEtsiIndex"), (0, "Nortel-MsCarrier-MscPassport-DisdnETSIMIB", "mscDataSigChanEtsiFramerIndex"))
if mibBuilder.loadTexts: mscDataSigChanEtsiFramerRowStatusEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanEtsiFramerRowStatusEntry.setDescription('A single entry in the table represents a single mscDataSigChanEtsiFramer component.')
mscDataSigChanEtsiFramerRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 2, 1, 1, 1), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanEtsiFramerRowStatus.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanEtsiFramerRowStatus.setDescription('This variable is used as the basis for SNMP naming of mscDataSigChanEtsiFramer components. These components cannot be added nor deleted.')
mscDataSigChanEtsiFramerComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 2, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanEtsiFramerComponentName.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanEtsiFramerComponentName.setDescription("This variable provides the component's string name for use with the ASCII Console Interface")
mscDataSigChanEtsiFramerStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 2, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanEtsiFramerStorageType.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanEtsiFramerStorageType.setDescription('This variable represents the storage type value for the mscDataSigChanEtsiFramer tables.')
mscDataSigChanEtsiFramerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 2, 1, 1, 10), NonReplicated())
if mibBuilder.loadTexts: mscDataSigChanEtsiFramerIndex.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanEtsiFramerIndex.setDescription('This variable represents the index for the mscDataSigChanEtsiFramer tables.')
mscDataSigChanEtsiFramerProvTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 2, 10), )
if mibBuilder.loadTexts: mscDataSigChanEtsiFramerProvTable.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanEtsiFramerProvTable.setDescription('This group contains the base provisioning data for the Framer component. Application or hardware interface specific provisioning data is contained in other provisionable Framer groups.')
mscDataSigChanEtsiFramerProvEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 2, 10, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"), (0, "Nortel-MsCarrier-MscPassport-DisdnETSIMIB", "mscDataSigChanEtsiIndex"), (0, "Nortel-MsCarrier-MscPassport-DisdnETSIMIB", "mscDataSigChanEtsiFramerIndex"))
if mibBuilder.loadTexts: mscDataSigChanEtsiFramerProvEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanEtsiFramerProvEntry.setDescription('An entry in the mscDataSigChanEtsiFramerProvTable.')
mscDataSigChanEtsiFramerInterfaceName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 2, 10, 1, 1), Link()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscDataSigChanEtsiFramerInterfaceName.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanEtsiFramerInterfaceName.setDescription("This attribute contains a hardware component name. The attribute associates the application with a specific link. This defines the module processor on which Framer's parent component (as well as Framer itself) will run.")
mscDataSigChanEtsiFramerStateTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 2, 12), )
if mibBuilder.loadTexts: mscDataSigChanEtsiFramerStateTable.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanEtsiFramerStateTable.setDescription('This group contains the three OSI State attributes. The descriptions generically indicate what each state attribute implies about the component. Note that not all the values and state combinations described here are supported by every component which uses this group. For component-specific information and the valid state combinations, refer to NTP 241-7001-150, Passport Operations and Maintenance Guide.')
mscDataSigChanEtsiFramerStateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 2, 12, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"), (0, "Nortel-MsCarrier-MscPassport-DisdnETSIMIB", "mscDataSigChanEtsiIndex"), (0, "Nortel-MsCarrier-MscPassport-DisdnETSIMIB", "mscDataSigChanEtsiFramerIndex"))
if mibBuilder.loadTexts: mscDataSigChanEtsiFramerStateEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanEtsiFramerStateEntry.setDescription('An entry in the mscDataSigChanEtsiFramerStateTable.')
mscDataSigChanEtsiFramerAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 2, 12, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("locked", 0), ("unlocked", 1), ("shuttingDown", 2))).clone('unlocked')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanEtsiFramerAdminState.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanEtsiFramerAdminState.setDescription('This attribute indicates the OSI Administrative State of the component. The value locked indicates that the component is administratively prohibited from providing services for its users. A Lock or Lock - force command has been previously issued for this component. When the value is locked, the value of usageState must be idle. The value shuttingDown indicates that the component is administratively permitted to provide service to its existing users only. A Lock command was issued against the component and it is in the process of shutting down. The value unlocked indicates that the component is administratively permitted to provide services for its users. To enter this state, issue an Unlock command to this component.')
mscDataSigChanEtsiFramerOperationalState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 2, 12, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1))).clone('disabled')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanEtsiFramerOperationalState.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanEtsiFramerOperationalState.setDescription('This attribute indicates the OSI Operational State of the component. The value enabled indicates that the component is available for operation. Note that if adminState is locked, it would still not be providing service. The value disabled indicates that the component is not available for operation. For example, something is wrong with the component itself, or with another component on which this one depends. If the value is disabled, the usageState must be idle.')
mscDataSigChanEtsiFramerUsageState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 2, 12, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("idle", 0), ("active", 1), ("busy", 2))).clone('idle')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanEtsiFramerUsageState.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanEtsiFramerUsageState.setDescription('This attribute indicates the OSI Usage State of the component. The value idle indicates that the component is not currently in use. The value active indicates that the component is in use and has spare capacity to provide for additional users. The value busy indicates that the component is in use and has no spare operating capacity for additional users at this time.')
mscDataSigChanEtsiFramerStatsTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 2, 13), )
if mibBuilder.loadTexts: mscDataSigChanEtsiFramerStatsTable.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanEtsiFramerStatsTable.setDescription('This group contains the operational statistics data for a Framer component.')
mscDataSigChanEtsiFramerStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 2, 13, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"), (0, "Nortel-MsCarrier-MscPassport-DisdnETSIMIB", "mscDataSigChanEtsiIndex"), (0, "Nortel-MsCarrier-MscPassport-DisdnETSIMIB", "mscDataSigChanEtsiFramerIndex"))
if mibBuilder.loadTexts: mscDataSigChanEtsiFramerStatsEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanEtsiFramerStatsEntry.setDescription('An entry in the mscDataSigChanEtsiFramerStatsTable.')
mscDataSigChanEtsiFramerFrmToIf = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 2, 13, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanEtsiFramerFrmToIf.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanEtsiFramerFrmToIf.setDescription('This attribute counts the number of frames transmitted to the link interface by Framer. This count wraps to zero after reaching its maximum value.')
mscDataSigChanEtsiFramerFrmFromIf = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 2, 13, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanEtsiFramerFrmFromIf.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanEtsiFramerFrmFromIf.setDescription('This attribute counts the number of frames received from the link interface by Framer. This count wraps to zero after reaching its maximum value.')
mscDataSigChanEtsiFramerOctetFromIf = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 2, 13, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanEtsiFramerOctetFromIf.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanEtsiFramerOctetFromIf.setDescription('The number of bytes received from the link interface by Framer.')
mscDataSigChanEtsiFramerAborts = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 2, 13, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanEtsiFramerAborts.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanEtsiFramerAborts.setDescription('This attribute counts the total number of aborts received. This count wraps to zero after reaching its maximum value.')
mscDataSigChanEtsiFramerCrcErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 2, 13, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanEtsiFramerCrcErrors.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanEtsiFramerCrcErrors.setDescription('This attribute counts the total number of frames with CRC errors. This count wraps to zero after reaching its maximum value.')
mscDataSigChanEtsiFramerLrcErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 2, 13, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanEtsiFramerLrcErrors.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanEtsiFramerLrcErrors.setDescription('This attribute counts the total number of frames with LRC errors. This count wraps to zero after reaching its maximum value.')
mscDataSigChanEtsiFramerNonOctetErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 2, 13, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanEtsiFramerNonOctetErrors.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanEtsiFramerNonOctetErrors.setDescription('This attribute counts the total number of frames that were non octet aligned. This count wraps to zero after reaching its maximum value.')
mscDataSigChanEtsiFramerOverruns = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 2, 13, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanEtsiFramerOverruns.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanEtsiFramerOverruns.setDescription('This attribute counts the total number of frames received from the link for which overruns occurred. This count wraps to zero after reaching its maximum value.')
mscDataSigChanEtsiFramerUnderruns = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 2, 13, 1, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanEtsiFramerUnderruns.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanEtsiFramerUnderruns.setDescription('This attribute counts the total number of frames transmitted to the link for which underruns occurred. This count wraps to zero after reaching its maximum value.')
mscDataSigChanEtsiFramerLargeFrmErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 10, 2, 13, 1, 10), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanEtsiFramerLargeFrmErrors.setStatus('mandatory')
if mibBuilder.loadTexts: mscDataSigChanEtsiFramerLargeFrmErrors.setDescription('This attribute counts the total number of frames received which were too large. The frame was longer than 500 bytes. This count wraps to zero after reaching its maximum value.')
disdnETSIGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 117, 1))
disdnETSIGroupCA = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 117, 1, 1))
disdnETSIGroupCA02 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 117, 1, 1, 3))
disdnETSIGroupCA02A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 117, 1, 1, 3, 2))
disdnETSICapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 117, 3))
disdnETSICapabilitiesCA = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 117, 3, 1))
disdnETSICapabilitiesCA02 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 117, 3, 1, 3))
disdnETSICapabilitiesCA02A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 117, 3, 1, 3, 2))
mibBuilder.exportSymbols("Nortel-MsCarrier-MscPassport-DisdnETSIMIB", mscDataSigChanEtsiOperEntry=mscDataSigChanEtsiOperEntry, mscDataSigChanEtsiFramerProvEntry=mscDataSigChanEtsiFramerProvEntry, mscDataSigChanEtsiFramerCrcErrors=mscDataSigChanEtsiFramerCrcErrors, mscDataSigChanEtsiFramerRowStatusEntry=mscDataSigChanEtsiFramerRowStatusEntry, mscDataSigChanEtsiFramerStateTable=mscDataSigChanEtsiFramerStateTable, disdnETSIGroup=disdnETSIGroup, mscDataSigChanEtsiProvTable=mscDataSigChanEtsiProvTable, mscDataSigChanEtsiFramerStateEntry=mscDataSigChanEtsiFramerStateEntry, mscDataSigChanEtsiFramerStatsEntry=mscDataSigChanEtsiFramerStatsEntry, mscDataSigChanEtsiToolsEntry=mscDataSigChanEtsiToolsEntry, mscDataSigChanEtsiFramerLargeFrmErrors=mscDataSigChanEtsiFramerLargeFrmErrors, disdnETSIMIB=disdnETSIMIB, mscDataSigChanEtsiFramerIndex=mscDataSigChanEtsiFramerIndex, disdnETSICapabilitiesCA=disdnETSICapabilitiesCA, mscDataSigChanEtsiT203=mscDataSigChanEtsiT203, mscDataSigChanEtsiFramerRowStatusTable=mscDataSigChanEtsiFramerRowStatusTable, mscDataSigChanEtsiFramerUnderruns=mscDataSigChanEtsiFramerUnderruns, mscDataSigChanEtsiL2Table=mscDataSigChanEtsiL2Table, mscDataSigChanEtsiActiveChannels=mscDataSigChanEtsiActiveChannels, mscDataSigChanEtsiFramer=mscDataSigChanEtsiFramer, mscDataSigChanEtsiFramerUsageState=mscDataSigChanEtsiFramerUsageState, mscDataSigChanEtsiProvEntry=mscDataSigChanEtsiProvEntry, mscDataSigChanEtsiFramerAdminState=mscDataSigChanEtsiFramerAdminState, mscDataSigChanEtsiIndex=mscDataSigChanEtsiIndex, mscDataSigChanEtsiFramerLrcErrors=mscDataSigChanEtsiFramerLrcErrors, mscDataSigChanEtsiDChanStatus=mscDataSigChanEtsiDChanStatus, mscDataSigChanEtsiFramerOctetFromIf=mscDataSigChanEtsiFramerOctetFromIf, mscDataSigChanEtsiFramerNonOctetErrors=mscDataSigChanEtsiFramerNonOctetErrors, disdnETSICapabilitiesCA02=disdnETSICapabilitiesCA02, disdnETSIGroupCA=disdnETSIGroupCA, mscDataSigChanEtsiFramerStatsTable=mscDataSigChanEtsiFramerStatsTable, mscDataSigChanEtsiRowStatusEntry=mscDataSigChanEtsiRowStatusEntry, mscDataSigChanEtsiN201=mscDataSigChanEtsiN201, mscDataSigChanEtsiTracing=mscDataSigChanEtsiTracing, mscDataSigChanEtsiComponentName=mscDataSigChanEtsiComponentName, mscDataSigChanEtsiOperTable=mscDataSigChanEtsiOperTable, mscDataSigChanEtsi=mscDataSigChanEtsi, mscDataSigChanEtsiT200=mscDataSigChanEtsiT200, mscDataSigChanEtsiPeakActiveChannels=mscDataSigChanEtsiPeakActiveChannels, mscDataSigChanEtsiFramerRowStatus=mscDataSigChanEtsiFramerRowStatus, mscDataSigChanEtsiN200=mscDataSigChanEtsiN200, mscDataSigChanEtsiRowStatusTable=mscDataSigChanEtsiRowStatusTable, mscDataSigChanEtsiFramerOverruns=mscDataSigChanEtsiFramerOverruns, disdnETSICapabilities=disdnETSICapabilities, mscDataSigChanEtsiT23=mscDataSigChanEtsiT23, disdnETSICapabilitiesCA02A=disdnETSICapabilitiesCA02A, mscDataSigChanEtsiL2Entry=mscDataSigChanEtsiL2Entry, mscDataSigChanEtsiFramerOperationalState=mscDataSigChanEtsiFramerOperationalState, mscDataSigChanEtsiFramerAborts=mscDataSigChanEtsiFramerAborts, mscDataSigChanEtsiCircuitSwitchedK=mscDataSigChanEtsiCircuitSwitchedK, mscDataSigChanEtsiSide=mscDataSigChanEtsiSide, mscDataSigChanEtsiToolsTable=mscDataSigChanEtsiToolsTable, mscDataSigChanEtsiFramerProvTable=mscDataSigChanEtsiFramerProvTable, mscDataSigChanEtsiFramerStorageType=mscDataSigChanEtsiFramerStorageType, mscDataSigChanEtsiFramerComponentName=mscDataSigChanEtsiFramerComponentName, mscDataSigChanEtsiFramerFrmToIf=mscDataSigChanEtsiFramerFrmToIf, disdnETSIGroupCA02=disdnETSIGroupCA02, disdnETSIGroupCA02A=disdnETSIGroupCA02A, mscDataSigChanEtsiStorageType=mscDataSigChanEtsiStorageType, mscDataSigChanEtsiFramerInterfaceName=mscDataSigChanEtsiFramerInterfaceName, mscDataSigChanEtsiFramerFrmFromIf=mscDataSigChanEtsiFramerFrmFromIf, mscDataSigChanEtsiRowStatus=mscDataSigChanEtsiRowStatus)