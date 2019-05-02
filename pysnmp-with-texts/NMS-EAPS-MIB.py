#
# PySNMP MIB module NMS-EAPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NMS-EAPS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:21:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
nmslocal, = mibBuilder.importSymbols("NMS-SMI", "nmslocal")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, Bits, iso, IpAddress, Gauge32, Counter64, ModuleIdentity, Integer32, MibIdentifier, Unsigned32, TimeTicks, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Bits", "iso", "IpAddress", "Gauge32", "Counter64", "ModuleIdentity", "Integer32", "MibIdentifier", "Unsigned32", "TimeTicks", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
nmsEAPS = MibIdentifier((1, 3, 6, 1, 4, 1, 11606, 10, 2, 230))
nmsEAPSRings = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 230, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsEAPSRings.setStatus('mandatory')
if mibBuilder.loadTexts: nmsEAPSRings.setDescription('The number of running ethernet ring instances.')
nmsEAPSPduRx = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 230, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsEAPSPduRx.setStatus('mandatory')
if mibBuilder.loadTexts: nmsEAPSPduRx.setDescription('The total number of input EAPS PDUs.')
nmsEAPSPduTx = MibScalar((1, 3, 6, 1, 4, 1, 11606, 10, 2, 230, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsEAPSPduTx.setStatus('mandatory')
if mibBuilder.loadTexts: nmsEAPSPduTx.setDescription('The total number of output EAPS PDUs.')
nmsEAPSRingTable = MibTable((1, 3, 6, 1, 4, 1, 11606, 10, 2, 230, 4), )
if mibBuilder.loadTexts: nmsEAPSRingTable.setStatus('mandatory')
if mibBuilder.loadTexts: nmsEAPSRingTable.setDescription('A table that contains information of ethernet ring instances.')
nmsEAPSRingTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11606, 10, 2, 230, 4, 1), ).setIndexNames((0, "NMS-EAPS-MIB", "nmsEAPSRingID"))
if mibBuilder.loadTexts: nmsEAPSRingTableEntry.setStatus('mandatory')
if mibBuilder.loadTexts: nmsEAPSRingTableEntry.setDescription('A table that contains information of ethernet ring instances.')
nmsEAPSRingID = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 230, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsEAPSRingID.setStatus('mandatory')
if mibBuilder.loadTexts: nmsEAPSRingID.setDescription('The index of ethernet ring instances.')
nmsEAPSRingNodeType = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 230, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("unknown", 0), ("masterNode", 1), ("transitNode", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nmsEAPSRingNodeType.setStatus('mandatory')
if mibBuilder.loadTexts: nmsEAPSRingNodeType.setDescription('A value indicates the node-type of this device in the ring.')
nmsEAPSRingControlVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 230, 4, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nmsEAPSRingControlVlan.setStatus('mandatory')
if mibBuilder.loadTexts: nmsEAPSRingControlVlan.setDescription('The id of the VLAN in which EAPS PDUs are transmitted.')
nmsEAPSRingPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 230, 4, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsEAPSRingPorts.setStatus('mandatory')
if mibBuilder.loadTexts: nmsEAPSRingPorts.setDescription('The number of interfaces which are configured in a ring.')
nmsEAPSRingState = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 230, 4, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("unknown", 0), ("complete", 1), ("ringFault", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsEAPSRingState.setStatus('mandatory')
if mibBuilder.loadTexts: nmsEAPSRingState.setDescription('A value indicates the state of a node in the ring. Only the value from a MasterNode indicates the state of the whole ring. The value from a TransitNode means the local ring ports are all operational or not.')
nmsEAPSRingHealthCheck = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 230, 4, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsEAPSRingHealthCheck.setStatus('mandatory')
if mibBuilder.loadTexts: nmsEAPSRingHealthCheck.setDescription('A value indicates whether Health packets are being sent from MasterNode. Available only for MasterNodes.')
nmsEAPSRingHelloTime = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 230, 4, 1, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nmsEAPSRingHelloTime.setStatus('mandatory')
if mibBuilder.loadTexts: nmsEAPSRingHelloTime.setDescription('The inteval between the transmit of two Health packets, in seconds. Available only for MasterNodes.')
nmsEAPSRingFailTime = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 230, 4, 1, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nmsEAPSRingFailTime.setStatus('mandatory')
if mibBuilder.loadTexts: nmsEAPSRingFailTime.setDescription('The hold time for the SecondaryPort after a Health packet is received, in seconds. Available only for MasterNodes.')
nmsEAPSRingPreforwardTime = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 230, 4, 1, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nmsEAPSRingPreforwardTime.setStatus('mandatory')
if mibBuilder.loadTexts: nmsEAPSRingPreforwardTime.setDescription('The hold time for a TransitPort which is recovered from a failure, in seconds. During the pre-forward time, no packets other than PDUs in control vlan can be forwarded. Only available for TransitNodes.')
nmsEAPSRingAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 230, 4, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1), ("running", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nmsEAPSRingAdminStatus.setStatus('mandatory')
if mibBuilder.loadTexts: nmsEAPSRingAdminStatus.setDescription("A read-create value that indicates the configuration status of the ring instance. Set this value to 'enabled' to start the ring or 'disabled' to stop it. The value 'running' indicates that the ring is currently configured and running, in which case, the values of node-type and control-vlan cannot be modified.")
nmsEAPSRingPrimaryPort = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 230, 4, 1, 11), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nmsEAPSRingPrimaryPort.setStatus('mandatory')
if mibBuilder.loadTexts: nmsEAPSRingPrimaryPort.setDescription("The interface index of the primary-port if the 'nmsEAPSRingNodeType' is 'masterNode', or the ifIndex of the first transit-port if 'transitNode'. Value 0 means that this port is not configured.")
nmsEAPSRingPrimaryPortState = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 230, 4, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("unknown", 0), ("forwarding", 1), ("preforwarding", 2), ("blocking", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsEAPSRingPrimaryPortState.setStatus('mandatory')
if mibBuilder.loadTexts: nmsEAPSRingPrimaryPortState.setDescription('The forwarding state of the primary-port or the first transit-port.')
nmsEAPSRingPrimaryPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 230, 4, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("link-down", 0), ("link-up", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsEAPSRingPrimaryPortStatus.setStatus('mandatory')
if mibBuilder.loadTexts: nmsEAPSRingPrimaryPortStatus.setDescription('The link status of the primary-port or the first transit-port.')
nmsEAPSRingSecondaryPort = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 230, 4, 1, 14), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nmsEAPSRingSecondaryPort.setStatus('mandatory')
if mibBuilder.loadTexts: nmsEAPSRingSecondaryPort.setDescription("The interface index of the secondary-port if the 'nmsEAPSRingNodeType' is 'masterNode', or the ifIndex of the second transit-port if 'transitNode'. Value 0 means that this port is not configured.")
nmsEAPSRingSecondaryPortState = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 230, 4, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("unknown", 0), ("forwarding", 1), ("preforwarding", 2), ("blocking", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsEAPSRingSecondaryPortState.setStatus('mandatory')
if mibBuilder.loadTexts: nmsEAPSRingSecondaryPortState.setDescription('The forwarding state of the secondary-port or the second transit-port.')
nmsEAPSRingSecondaryPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 230, 4, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("link-down", 0), ("link-up", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsEAPSRingSecondaryPortStatus.setStatus('mandatory')
if mibBuilder.loadTexts: nmsEAPSRingSecondaryPortStatus.setDescription('The link status of the secondary-port or the second transit-port.')
nmsEAPSRingPortTable = MibTable((1, 3, 6, 1, 4, 1, 11606, 10, 2, 230, 5), )
if mibBuilder.loadTexts: nmsEAPSRingPortTable.setStatus('mandatory')
if mibBuilder.loadTexts: nmsEAPSRingPortTable.setDescription('A table that contains information of ethernet ring ports.')
nmsEAPSRingPortTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11606, 10, 2, 230, 5, 1), ).setIndexNames((0, "NMS-EAPS-MIB", "nmsEAPSRingPortRingID"), (0, "NMS-EAPS-MIB", "nmsEAPSRingPort"))
if mibBuilder.loadTexts: nmsEAPSRingPortTableEntry.setStatus('mandatory')
if mibBuilder.loadTexts: nmsEAPSRingPortTableEntry.setDescription('A table that contains information of ethernet ring ports.')
nmsEAPSRingPortRingID = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 230, 5, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsEAPSRingPortRingID.setStatus('mandatory')
if mibBuilder.loadTexts: nmsEAPSRingPortRingID.setDescription('The index of an ethernet ring instance, in which this port is configured.')
nmsEAPSRingPort = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 230, 5, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsEAPSRingPort.setStatus('mandatory')
if mibBuilder.loadTexts: nmsEAPSRingPort.setDescription('The port number of the ring port.')
nmsEAPSRingPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 230, 5, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("unknown", 0), ("primaryPort", 1), ("secondaryPort", 2), ("transitPort", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsEAPSRingPortType.setStatus('mandatory')
if mibBuilder.loadTexts: nmsEAPSRingPortType.setDescription('A value indicates the type of a ring port.')
nmsEAPSRingPortState = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 230, 5, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("unknown", 0), ("forwarding", 1), ("preforwarding", 2), ("blocking", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsEAPSRingPortState.setStatus('mandatory')
if mibBuilder.loadTexts: nmsEAPSRingPortState.setDescription('A value indicates the forward state of a ring port in data vlans.')
nmsEAPSRingPortForwards = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 230, 5, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsEAPSRingPortForwards.setStatus('mandatory')
if mibBuilder.loadTexts: nmsEAPSRingPortForwards.setDescription('The number of times this port has transitioned to forwarding state.')
nmsEAPSRingPortRx = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 230, 5, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsEAPSRingPortRx.setStatus('mandatory')
if mibBuilder.loadTexts: nmsEAPSRingPortRx.setDescription('The number of received EAPS PDUs on this port.')
nmsEAPSRingPortTx = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 230, 5, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsEAPSRingPortTx.setStatus('mandatory')
if mibBuilder.loadTexts: nmsEAPSRingPortTx.setDescription('The Number of transmitted EAPS PDUs on this port.')
nmsEAPSRingPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 2, 230, 5, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("link-down", 0), ("link-up", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsEAPSRingPortStatus.setStatus('mandatory')
if mibBuilder.loadTexts: nmsEAPSRingPortStatus.setDescription('The link status of the ring port.')
nmsEAPSRingNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11606, 10, 2, 230, 6))
nmsEAPSRingNotification = NotificationType((1, 3, 6, 1, 4, 1, 11606, 10, 2, 230, 6, 1)).setObjects(("NMS-EAPS-MIB", "nmsEAPSRingID"), ("NMS-EAPS-MIB", "nmsEAPSRingNodeType"), ("NMS-EAPS-MIB", "nmsEAPSRingState"))
if mibBuilder.loadTexts: nmsEAPSRingNotification.setStatus('current')
if mibBuilder.loadTexts: nmsEAPSRingNotification.setDescription('This notification is generated when a MasterNode detects that the state of ring is changed.')
mibBuilder.exportSymbols("NMS-EAPS-MIB", nmsEAPSRingPrimaryPortStatus=nmsEAPSRingPrimaryPortStatus, nmsEAPSRingPortTable=nmsEAPSRingPortTable, nmsEAPSRingHealthCheck=nmsEAPSRingHealthCheck, nmsEAPS=nmsEAPS, nmsEAPSRingPortForwards=nmsEAPSRingPortForwards, nmsEAPSRingTableEntry=nmsEAPSRingTableEntry, nmsEAPSRingPortRingID=nmsEAPSRingPortRingID, nmsEAPSRingPortRx=nmsEAPSRingPortRx, nmsEAPSRingPortTableEntry=nmsEAPSRingPortTableEntry, nmsEAPSRings=nmsEAPSRings, nmsEAPSRingPortState=nmsEAPSRingPortState, nmsEAPSRingHelloTime=nmsEAPSRingHelloTime, nmsEAPSRingPortStatus=nmsEAPSRingPortStatus, nmsEAPSRingPortType=nmsEAPSRingPortType, nmsEAPSRingPreforwardTime=nmsEAPSRingPreforwardTime, nmsEAPSRingPrimaryPort=nmsEAPSRingPrimaryPort, nmsEAPSRingPortTx=nmsEAPSRingPortTx, nmsEAPSRingFailTime=nmsEAPSRingFailTime, nmsEAPSRingControlVlan=nmsEAPSRingControlVlan, nmsEAPSPduRx=nmsEAPSPduRx, nmsEAPSRingSecondaryPort=nmsEAPSRingSecondaryPort, nmsEAPSRingPort=nmsEAPSRingPort, nmsEAPSRingSecondaryPortStatus=nmsEAPSRingSecondaryPortStatus, nmsEAPSRingNotification=nmsEAPSRingNotification, nmsEAPSRingID=nmsEAPSRingID, nmsEAPSRingTable=nmsEAPSRingTable, nmsEAPSRingPorts=nmsEAPSRingPorts, nmsEAPSRingState=nmsEAPSRingState, nmsEAPSRingNotifications=nmsEAPSRingNotifications, nmsEAPSRingNodeType=nmsEAPSRingNodeType, nmsEAPSPduTx=nmsEAPSPduTx, nmsEAPSRingAdminStatus=nmsEAPSRingAdminStatus, nmsEAPSRingPrimaryPortState=nmsEAPSRingPrimaryPortState, nmsEAPSRingSecondaryPortState=nmsEAPSRingSecondaryPortState)
