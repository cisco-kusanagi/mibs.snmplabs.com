#
# PySNMP MIB module XYLAN-FRAME-RELAY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/XYLAN-FRAME-RELAY-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:45:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Counter64, Counter32, ObjectIdentity, IpAddress, MibIdentifier, Bits, iso, ModuleIdentity, Unsigned32, Integer32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Counter64", "Counter32", "ObjectIdentity", "IpAddress", "MibIdentifier", "Bits", "iso", "ModuleIdentity", "Unsigned32", "Integer32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
xylanFrArch, = mibBuilder.importSymbols("XYLAN-BASE-MIB", "xylanFrArch")
frxPortGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 800, 2, 8, 1))
frxVcControlGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 800, 2, 8, 2))
frxServiceGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 800, 2, 8, 3))
frxVcStatsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 800, 2, 8, 4))
frxPortTable = MibTable((1, 3, 6, 1, 4, 1, 800, 2, 8, 1, 1), )
if mibBuilder.loadTexts: frxPortTable.setStatus('mandatory')
if mibBuilder.loadTexts: frxPortTable.setDescription("A table of port layer status and parameter information for the UNI's physical interface.")
frxPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 800, 2, 8, 1, 1, 1), ).setIndexNames((0, "XYLAN-FRAME-RELAY-MIB", "frxPortSlotIndex"), (0, "XYLAN-FRAME-RELAY-MIB", "frxPortPortIndex"))
if mibBuilder.loadTexts: frxPortEntry.setStatus('mandatory')
if mibBuilder.loadTexts: frxPortEntry.setDescription('An entry in the table, containing information about the physical layer of a UNI interface.')
frxPortSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 8, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 9))).setMaxAccess("readonly")
if mibBuilder.loadTexts: frxPortSlotIndex.setStatus('mandatory')
if mibBuilder.loadTexts: frxPortSlotIndex.setDescription('A unique value which identifies this HSM board slot.')
frxPortPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 8, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: frxPortPortIndex.setStatus('mandatory')
if mibBuilder.loadTexts: frxPortPortIndex.setDescription('A unique value which identifies this WSM submodule port.')
frxPortDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 8, 1, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: frxPortDescription.setStatus('mandatory')
if mibBuilder.loadTexts: frxPortDescription.setDescription('A description for this Frame Relay port.')
frxPortDefaultBridgingVLAN = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 8, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: frxPortDefaultBridgingVLAN.setStatus('mandatory')
if mibBuilder.loadTexts: frxPortDefaultBridgingVLAN.setDescription('The default VLAN for new PVCs that have not been configured for the Bridging Service. A value of zero(0) indicates that unconfigured VCs will not perform a bridging service and will discard all bridged format frames received or transmitted. A non-zero value indicates the bridging VLAN to be used if the network informs the port of a new VC.')
frxPortDefaultBridgingServiceNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 8, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 256))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: frxPortDefaultBridgingServiceNumber.setStatus('mandatory')
if mibBuilder.loadTexts: frxPortDefaultBridgingServiceNumber.setDescription('If non-zero, this is the unique service number which unconfigured Bridging Virtual Circuits are added to if frxPortDefaultBridgingVLAN is non zero (set to a VLAN ID) and frxPortDefaultBridgingGrouping is set to groupVCsIntoOneVport. This allows an unconfigured VC to be added to an existing configured bridging service virtual circuit group. If zero, then unconfigured VCs will be added to a newly created (dynamic) Briding Service instance (i.e. a new virtual port is created dynamically).')
frxPortDefaultRoutingVLAN = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 8, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: frxPortDefaultRoutingVLAN.setStatus('mandatory')
if mibBuilder.loadTexts: frxPortDefaultRoutingVLAN.setDescription('The default VLAN for new PVCs that have not been configured for a routing Service. A value of zero(0) indicates that unconfigured VCs will not perform a routing service and will discard all routed format frames received or transmitted. A non-zero value indicates the routing VLAN to be used if the network informs the port of a new VC.')
frxPortDefaultCompressionAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 8, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: frxPortDefaultCompressionAdminStatus.setStatus('mandatory')
if mibBuilder.loadTexts: frxPortDefaultCompressionAdminStatus.setDescription('This object controls whether or not an unconfigured virtual circuit will attempt (enable) or not attempt (disable) to negotiate for compression.')
frxPortDefaultCompressionPRetryTime = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 8, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: frxPortDefaultCompressionPRetryTime.setStatus('mandatory')
if mibBuilder.loadTexts: frxPortDefaultCompressionPRetryTime.setDescription('The default P-Retry-Time for negotiating mode 1 compression as described in Frame Relay Forum Data Compression Implementation Agreement FRF.9. This object controls the default value for P-Retry-Time for an unconfigured (dynamic) virtual circuit. This object represents the time in seconds between retransmission of Data Compression Negotiation Control messages.')
frxPortDefaultCompressionPRetryCount = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 8, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: frxPortDefaultCompressionPRetryCount.setStatus('mandatory')
if mibBuilder.loadTexts: frxPortDefaultCompressionPRetryCount.setDescription('The default P-Retry-Count for negotiating mode 1 compression as described in Frame Relay Forum Data Compression Implementation Agreement FRF.9 This object controls the default value for P-Retry-Count for an unconfigured (dynamic) virtual circuit. This object represents the number of retries before giving up on the negotiation phase and not running compression on the virtual circuit.')
frxPortDefaultBridgingMode = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 8, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: frxPortDefaultBridgingMode.setStatus('mandatory')
if mibBuilder.loadTexts: frxPortDefaultBridgingMode.setDescription('The default Briding Mode, 0 = BRIDGE_ALL, 1 = ETHERNET ONLY')
frxVcControlTable = MibTable((1, 3, 6, 1, 4, 1, 800, 2, 8, 2, 1), )
if mibBuilder.loadTexts: frxVcControlTable.setStatus('mandatory')
if mibBuilder.loadTexts: frxVcControlTable.setDescription('A table of Frame Relay virtual circuit configuration and control information.')
frxVcControlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 800, 2, 8, 2, 1, 1), ).setIndexNames((0, "XYLAN-FRAME-RELAY-MIB", "frxVcControlSlotIndex"), (0, "XYLAN-FRAME-RELAY-MIB", "frxVcControlPortIndex"), (0, "XYLAN-FRAME-RELAY-MIB", "frxVcControlDlci"))
if mibBuilder.loadTexts: frxVcControlEntry.setStatus('mandatory')
if mibBuilder.loadTexts: frxVcControlEntry.setDescription('An entry in the table, containing information about the Frame Relay virtual circuit statistics.')
frxVcControlSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 8, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 9))).setMaxAccess("readonly")
if mibBuilder.loadTexts: frxVcControlSlotIndex.setStatus('mandatory')
if mibBuilder.loadTexts: frxVcControlSlotIndex.setDescription('A unique value which identifies this HSM board slot.')
frxVcControlPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 8, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: frxVcControlPortIndex.setStatus('mandatory')
if mibBuilder.loadTexts: frxVcControlPortIndex.setDescription('A unique value which identifies this WSM submodule port.')
frxVcControlDlci = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 8, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: frxVcControlDlci.setStatus('mandatory')
if mibBuilder.loadTexts: frxVcControlDlci.setDescription('A unique value which identifies this Data Link Connection Identifier (DLCI) for this Frame Relay Virtual Circuit.')
frxVcControlCompressionAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 8, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: frxVcControlCompressionAdminStatus.setStatus('mandatory')
if mibBuilder.loadTexts: frxVcControlCompressionAdminStatus.setDescription('This object controls whether or not the virtual circuit will attempt (enable) or not attemp (disable) to negotiate for compression. The current state of compression for the virtual circuit is indicated in frxVcControlCompressionOperStatus')
frxVcControlCompressionOperPhase = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 8, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("disabled", 1), ("initialization", 2), ("operation", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: frxVcControlCompressionOperPhase.setStatus('mandatory')
if mibBuilder.loadTexts: frxVcControlCompressionOperPhase.setDescription('This object reports the current phase (state) of compression for this virtual circuit if the Compression Admin Status is set to enable. If the compression Admin status is set to disabled, then this object will report as disabled. Otherwise the value reflects whether compression is currently inactive or failed negotiation (disabled) is under negotiation (initialization) or active (operation). Possible causes of disabled are a failed negotiation, virtual circuit inactive, the other side not supporting compression, etc. For a description of the phases (states), see Frame Relay Forum Implementation aggreement on Data Compression (FRF.9)')
frxVcControlCompressionPRetryTime = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 8, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: frxVcControlCompressionPRetryTime.setStatus('mandatory')
if mibBuilder.loadTexts: frxVcControlCompressionPRetryTime.setDescription('The default P-Retry-Time for negotiating mode 1 compression as described in Frame Relay Forum Data Compression Implementation Agreement FRF.9. This object represents the time in seconds between retransmission of Data Compression Negotiation Control messages.')
frxVcControlCompressionPRetryCount = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 8, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: frxVcControlCompressionPRetryCount.setStatus('mandatory')
if mibBuilder.loadTexts: frxVcControlCompressionPRetryCount.setDescription('The default P-Retry-Count for negotiating mode 1 compression as described in Frame Relay Forum Data Compression Implementation Agreement FRF.9 This object represents the number of retries before giving up on the negotiation phase and not running compression on the virtual circuit.')
frxVcControlBridgingInUse = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 8, 2, 1, 1, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: frxVcControlBridgingInUse.setStatus('mandatory')
if mibBuilder.loadTexts: frxVcControlBridgingInUse.setDescription('Determine for NMS Manager to see whether VC is already in-use. 1=InUse, 0=Free.')
frxServiceTable = MibTable((1, 3, 6, 1, 4, 1, 800, 2, 8, 3, 1), )
if mibBuilder.loadTexts: frxServiceTable.setStatus('mandatory')
if mibBuilder.loadTexts: frxServiceTable.setDescription('A table of Frame Relay services status and parameter information.')
frxServiceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 800, 2, 8, 3, 1, 1), ).setIndexNames((0, "XYLAN-FRAME-RELAY-MIB", "frxServiceSlotIndex"), (0, "XYLAN-FRAME-RELAY-MIB", "frxServicePortIndex"), (0, "XYLAN-FRAME-RELAY-MIB", "frxServiceNumber"), (0, "XYLAN-FRAME-RELAY-MIB", "frxServiceType"))
if mibBuilder.loadTexts: frxServiceEntry.setStatus('mandatory')
if mibBuilder.loadTexts: frxServiceEntry.setDescription('An entry in the table, containing information about the Frame Relay services.')
frxServiceSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 8, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 9))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: frxServiceSlotIndex.setStatus('mandatory')
if mibBuilder.loadTexts: frxServiceSlotIndex.setDescription('A unique value which identifies this HSM board slot.')
frxServicePortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 8, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: frxServicePortIndex.setStatus('mandatory')
if mibBuilder.loadTexts: frxServicePortIndex.setDescription('A unique value which identifies this WSM submodule port.')
frxServiceNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 8, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: frxServiceNumber.setStatus('mandatory')
if mibBuilder.loadTexts: frxServiceNumber.setDescription('The unique service number for this particular slot/port.')
frxServiceTableEntryType = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 8, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("static", 1), ("dynamic", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: frxServiceTableEntryType.setStatus('mandatory')
if mibBuilder.loadTexts: frxServiceTableEntryType.setDescription('The type of table entry for this Frame Relay Serivce. A static entry is one that is stored in non-volatile memory. A dynamic entry is one that is automatically created for an unconfigured virtual circuit based on the the type of service (bridging or routing) and whether a default VLAN is defined for the type of service. Changing the value via a write command from dynamic to static will cause the table entry to be stored into non-volatile memory. Setting a value of dynamic is not allowed.')
frxServiceDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 8, 3, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: frxServiceDescription.setStatus('mandatory')
if mibBuilder.loadTexts: frxServiceDescription.setDescription('A description for this Frame Relay service.')
frxServiceType = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 8, 3, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(4, 5, 6))).clone(namedValues=NamedValues(("trunking", 4), ("routing", 5), ("bridging", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: frxServiceType.setStatus('mandatory')
if mibBuilder.loadTexts: frxServiceType.setDescription('The service type.')
frxServiceOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 8, 3, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: frxServiceOperStatus.setStatus('mandatory')
if mibBuilder.loadTexts: frxServiceOperStatus.setDescription('The service operational status.')
frxServiceAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 8, 3, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2), ("delete", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: frxServiceAdminStatus.setStatus('mandatory')
if mibBuilder.loadTexts: frxServiceAdminStatus.setDescription('The service adminstration status.')
frxServiceVirtualCircuits = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 8, 3, 1, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 512))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: frxServiceVirtualCircuits.setStatus('mandatory')
if mibBuilder.loadTexts: frxServiceVirtualCircuits.setDescription('The virtual circuits for this service. Interpret this as a 16 bit field per connection: Trunking 1, Bridging 1..255, IP 1..255.')
frxServiceVlans = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 8, 3, 1, 1, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: frxServiceVlans.setStatus('mandatory')
if mibBuilder.loadTexts: frxServiceVlans.setDescription('The Vlans for this service. Interpret this as a 16 bit field per vlan: Trunking 1-32, Bridging 1, IP 1')
frxServiceBridgingMode = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 8, 3, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: frxServiceBridgingMode.setStatus('mandatory')
if mibBuilder.loadTexts: frxServiceBridgingMode.setDescription('The default Briding Mode, 0 = BRIDGE_ALL, 1 = ETHERNET ONLY')
frxVcStatsTable = MibTable((1, 3, 6, 1, 4, 1, 800, 2, 8, 4, 1), )
if mibBuilder.loadTexts: frxVcStatsTable.setStatus('mandatory')
if mibBuilder.loadTexts: frxVcStatsTable.setDescription('A table of Frame Relay virtual circuit statistics information.')
frxVcStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 800, 2, 8, 4, 1, 1), ).setIndexNames((0, "XYLAN-FRAME-RELAY-MIB", "frxVcStatsSlotIndex"), (0, "XYLAN-FRAME-RELAY-MIB", "frxVcStatsPortIndex"), (0, "XYLAN-FRAME-RELAY-MIB", "frxVcStatsDlci"))
if mibBuilder.loadTexts: frxVcStatsEntry.setStatus('mandatory')
if mibBuilder.loadTexts: frxVcStatsEntry.setDescription('An entry in the table, containing information about the Frame Relay virtual circuit statistics.')
frxVcStatsSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 8, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 9))).setMaxAccess("readonly")
if mibBuilder.loadTexts: frxVcStatsSlotIndex.setStatus('mandatory')
if mibBuilder.loadTexts: frxVcStatsSlotIndex.setDescription('A unique value which identifies this HSM board slot.')
frxVcStatsPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 8, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: frxVcStatsPortIndex.setStatus('mandatory')
if mibBuilder.loadTexts: frxVcStatsPortIndex.setDescription('A unique value which identifies this WSM submodule port.')
frxVcStatsDlci = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 8, 4, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1022))).setMaxAccess("readonly")
if mibBuilder.loadTexts: frxVcStatsDlci.setStatus('mandatory')
if mibBuilder.loadTexts: frxVcStatsDlci.setDescription('A unique value which identifies this Data Link Connection Identifier (DLCI) for this Frame Relay Virtual Circuit.')
frxVcStatsTxIPOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 8, 4, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frxVcStatsTxIPOctets.setStatus('mandatory')
if mibBuilder.loadTexts: frxVcStatsTxIPOctets.setDescription('The total number of transmitted octets (including the Frame Relay Header field) within routed IP format frames on this virtual circuit.')
frxVcStatsTxIPFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 8, 4, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frxVcStatsTxIPFrames.setStatus('mandatory')
if mibBuilder.loadTexts: frxVcStatsTxIPFrames.setDescription('The total number of transmitted routed IP format frames on this virtual circuit.')
frxVcStatsRxIPOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 8, 4, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frxVcStatsRxIPOctets.setStatus('mandatory')
if mibBuilder.loadTexts: frxVcStatsRxIPOctets.setDescription('The total number of received octets (including the Frame Relay Header field) within routed IP format frames on this virtual circuit.')
frxVcStatsRxIPFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 8, 4, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frxVcStatsRxIPFrames.setStatus('mandatory')
if mibBuilder.loadTexts: frxVcStatsRxIPFrames.setDescription('The total number of received routed IP format frames on this virtual circuit.')
frxVcStatsTxIPXOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 8, 4, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frxVcStatsTxIPXOctets.setStatus('mandatory')
if mibBuilder.loadTexts: frxVcStatsTxIPXOctets.setDescription('The total number of transmitted octets (including the Frame Relay Header field) within routed IPX format frames on this virtual circuit.')
frxVcStatsTxIPXFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 8, 4, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frxVcStatsTxIPXFrames.setStatus('mandatory')
if mibBuilder.loadTexts: frxVcStatsTxIPXFrames.setDescription('The total number of transmitted routed IPX format frames on this virtual circuit.')
frxVcStatsRxIPXOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 8, 4, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frxVcStatsRxIPXOctets.setStatus('mandatory')
if mibBuilder.loadTexts: frxVcStatsRxIPXOctets.setDescription('The total number of received octets (including the Frame Relay Header field) within routed IPX format frames on this virtual circuit.')
frxVcStatsRxIPXFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 8, 4, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frxVcStatsRxIPXFrames.setStatus('mandatory')
if mibBuilder.loadTexts: frxVcStatsRxIPXFrames.setDescription('The total number of received routed IPX format frames on this virtual circuit.')
frxVcStatsTxBPDUOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 8, 4, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frxVcStatsTxBPDUOctets.setStatus('mandatory')
if mibBuilder.loadTexts: frxVcStatsTxBPDUOctets.setDescription('The total number of transmitted octets (including the Frame Relay Header field) within BPDU frames on this virtual circuit.')
frxVcStatsTxBPDUFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 8, 4, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frxVcStatsTxBPDUFrames.setStatus('mandatory')
if mibBuilder.loadTexts: frxVcStatsTxBPDUFrames.setDescription('The total number of transmitted BPDU frames on this virtual circuit.')
frxVcStatsRxBPDUOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 8, 4, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frxVcStatsRxBPDUOctets.setStatus('mandatory')
if mibBuilder.loadTexts: frxVcStatsRxBPDUOctets.setDescription('The total number of received octets (including the Frame Relay Header field) within BPDU frames on this virtual circuit.')
frxVcStatsRxBPDUFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 8, 4, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frxVcStatsRxBPDUFrames.setStatus('mandatory')
if mibBuilder.loadTexts: frxVcStatsRxBPDUFrames.setDescription('The total number of received BPDU frames on this virtual circuit.')
frxVcStatsTxEthernetOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 8, 4, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frxVcStatsTxEthernetOctets.setStatus('mandatory')
if mibBuilder.loadTexts: frxVcStatsTxEthernetOctets.setDescription('The total number of transmitted octets (including the Frame Relay Header field) within bridged 802.3 format frames on this virtual circuit.')
frxVcStatsTxEthernetFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 8, 4, 1, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frxVcStatsTxEthernetFrames.setStatus('mandatory')
if mibBuilder.loadTexts: frxVcStatsTxEthernetFrames.setDescription('The total number of transmitted bridged 802.3 format frames on this virtual circuit.')
frxVcStatsRxEthernetOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 8, 4, 1, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frxVcStatsRxEthernetOctets.setStatus('mandatory')
if mibBuilder.loadTexts: frxVcStatsRxEthernetOctets.setDescription('The total number of received octets (including the Frame Relay Header field) within bridged 802.3 format frames on this virtual circuit.')
frxVcStatsRxEthernetFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 8, 4, 1, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frxVcStatsRxEthernetFrames.setStatus('mandatory')
if mibBuilder.loadTexts: frxVcStatsRxEthernetFrames.setDescription('The total number of received bridged 802.3 format frames on this virtual circuit.')
frxVcStatsTx8025Octets = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 8, 4, 1, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frxVcStatsTx8025Octets.setStatus('mandatory')
if mibBuilder.loadTexts: frxVcStatsTx8025Octets.setDescription('The total number of transmitted octets (including the Frame Relay Header field) within 8025 frames on this virtual circuit.')
frxVcStatsTx8025Frames = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 8, 4, 1, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frxVcStatsTx8025Frames.setStatus('mandatory')
if mibBuilder.loadTexts: frxVcStatsTx8025Frames.setDescription('The total number of transmitted 8025 frames on this virtual circuit.')
frxVcStatsRx8025Octets = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 8, 4, 1, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frxVcStatsRx8025Octets.setStatus('mandatory')
if mibBuilder.loadTexts: frxVcStatsRx8025Octets.setDescription('The total number of received octets (including the Frame Relay Header field) within 8025 frames on this virtual circuit.')
frxVcStatsRx8025Frames = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 8, 4, 1, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frxVcStatsRx8025Frames.setStatus('mandatory')
if mibBuilder.loadTexts: frxVcStatsRx8025Frames.setDescription('The total number of received 8025 frames on this virtual circuit.')
frxVcStatsTxFDDIOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 8, 4, 1, 1, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frxVcStatsTxFDDIOctets.setStatus('mandatory')
if mibBuilder.loadTexts: frxVcStatsTxFDDIOctets.setDescription('The total number of transmitted octets (including the Frame Relay Header field) within FDDI frames on this virtual circuit.')
frxVcStatsTxFDDIFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 8, 4, 1, 1, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frxVcStatsTxFDDIFrames.setStatus('mandatory')
if mibBuilder.loadTexts: frxVcStatsTxFDDIFrames.setDescription('The total number of transmitted FDDI frames on this virtual circuit.')
frxVcStatsRxFDDIOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 8, 4, 1, 1, 26), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frxVcStatsRxFDDIOctets.setStatus('mandatory')
if mibBuilder.loadTexts: frxVcStatsRxFDDIOctets.setDescription('The total number of received octets (including the Frame Relay Header field) within FDDI frames on this virtual circuit.')
frxVcStatsRxFDDIFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 8, 4, 1, 1, 27), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frxVcStatsRxFDDIFrames.setStatus('mandatory')
if mibBuilder.loadTexts: frxVcStatsRxFDDIFrames.setDescription('The total number of received FDDI frames on this virtual circuit.')
frxVcStatsTxCompressedOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 8, 4, 1, 1, 28), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frxVcStatsTxCompressedOctets.setStatus('mandatory')
if mibBuilder.loadTexts: frxVcStatsTxCompressedOctets.setDescription('The total number of transmitted octets (including the Frame Relay Header field) within compressed format frames on this virtual circuit.')
frxVcStatsTxCompressedFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 8, 4, 1, 1, 29), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frxVcStatsTxCompressedFrames.setStatus('mandatory')
if mibBuilder.loadTexts: frxVcStatsTxCompressedFrames.setDescription('The total number of transmitted compressed format frames on this virtual circuit.')
frxVcStatsRxCompressedOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 8, 4, 1, 1, 30), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frxVcStatsRxCompressedOctets.setStatus('mandatory')
if mibBuilder.loadTexts: frxVcStatsRxCompressedOctets.setDescription('The total number of received octets (including the Frame Relay Header field) within compressed format frames on this virtual circuit.')
frxVcStatsRxCompressedFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 8, 4, 1, 1, 31), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frxVcStatsRxCompressedFrames.setStatus('mandatory')
if mibBuilder.loadTexts: frxVcStatsRxCompressedFrames.setDescription('The total number of received compressed format frames on this virtual circuit.')
frxVcStatsTxPrecompressedOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 8, 4, 1, 1, 32), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frxVcStatsTxPrecompressedOctets.setStatus('mandatory')
if mibBuilder.loadTexts: frxVcStatsTxPrecompressedOctets.setDescription('The total number of octets (including the Frame Relay Header field) prior to compression of data for transmission within compressed format frames on this virtual circuit.')
frxVcStatsRxDecompressedOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 8, 4, 1, 1, 33), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frxVcStatsRxDecompressedOctets.setStatus('mandatory')
if mibBuilder.loadTexts: frxVcStatsRxDecompressedOctets.setDescription('The total number of octets (including the Frame Relay Header field) after decompression of data received within compressed format frames on this virtual circuit.')
frxVcStatsRxCompressedDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 8, 4, 1, 1, 34), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frxVcStatsRxCompressedDiscards.setStatus('mandatory')
if mibBuilder.loadTexts: frxVcStatsRxCompressedDiscards.setDescription('The total number of received compressed format frames on this virtual circuit that were discarded due to error or lost frames (e.g. out of sequence, decompression errors, etc.)')
mibBuilder.exportSymbols("XYLAN-FRAME-RELAY-MIB", frxVcStatsTable=frxVcStatsTable, frxServiceBridgingMode=frxServiceBridgingMode, frxVcControlPortIndex=frxVcControlPortIndex, frxVcStatsTxIPXFrames=frxVcStatsTxIPXFrames, frxServiceTable=frxServiceTable, frxVcStatsTxCompressedFrames=frxVcStatsTxCompressedFrames, frxPortDefaultRoutingVLAN=frxPortDefaultRoutingVLAN, frxPortDefaultCompressionPRetryCount=frxPortDefaultCompressionPRetryCount, frxVcStatsTxFDDIOctets=frxVcStatsTxFDDIOctets, frxVcStatsTxIPOctets=frxVcStatsTxIPOctets, frxServiceDescription=frxServiceDescription, frxVcStatsTxIPFrames=frxVcStatsTxIPFrames, frxVcControlTable=frxVcControlTable, frxVcStatsTxFDDIFrames=frxVcStatsTxFDDIFrames, frxServiceVlans=frxServiceVlans, frxVcStatsTxPrecompressedOctets=frxVcStatsTxPrecompressedOctets, frxVcStatsRxEthernetOctets=frxVcStatsRxEthernetOctets, frxVcStatsTxBPDUOctets=frxVcStatsTxBPDUOctets, frxPortEntry=frxPortEntry, frxVcStatsTxBPDUFrames=frxVcStatsTxBPDUFrames, frxServiceOperStatus=frxServiceOperStatus, frxPortGroup=frxPortGroup, frxVcStatsRxCompressedOctets=frxVcStatsRxCompressedOctets, frxPortDefaultBridgingVLAN=frxPortDefaultBridgingVLAN, frxServiceEntry=frxServiceEntry, frxVcStatsRxIPOctets=frxVcStatsRxIPOctets, frxServiceGroup=frxServiceGroup, frxVcStatsRxBPDUFrames=frxVcStatsRxBPDUFrames, frxVcStatsRxIPXFrames=frxVcStatsRxIPXFrames, frxVcControlGroup=frxVcControlGroup, frxVcStatsGroup=frxVcStatsGroup, frxVcStatsRxBPDUOctets=frxVcStatsRxBPDUOctets, frxVcStatsRxEthernetFrames=frxVcStatsRxEthernetFrames, frxPortSlotIndex=frxPortSlotIndex, frxServiceVirtualCircuits=frxServiceVirtualCircuits, frxVcStatsRx8025Frames=frxVcStatsRx8025Frames, frxVcStatsTx8025Frames=frxVcStatsTx8025Frames, frxVcStatsRxFDDIFrames=frxVcStatsRxFDDIFrames, frxVcControlCompressionOperPhase=frxVcControlCompressionOperPhase, frxVcStatsEntry=frxVcStatsEntry, frxVcControlBridgingInUse=frxVcControlBridgingInUse, frxServiceAdminStatus=frxServiceAdminStatus, frxVcControlEntry=frxVcControlEntry, frxVcStatsDlci=frxVcStatsDlci, frxVcStatsTxEthernetFrames=frxVcStatsTxEthernetFrames, frxVcStatsRxIPFrames=frxVcStatsRxIPFrames, frxVcStatsRxIPXOctets=frxVcStatsRxIPXOctets, frxVcStatsRxFDDIOctets=frxVcStatsRxFDDIOctets, frxServiceSlotIndex=frxServiceSlotIndex, frxPortDefaultBridgingMode=frxPortDefaultBridgingMode, frxServicePortIndex=frxServicePortIndex, frxVcControlSlotIndex=frxVcControlSlotIndex, frxVcStatsRxCompressedFrames=frxVcStatsRxCompressedFrames, frxVcStatsPortIndex=frxVcStatsPortIndex, frxVcControlCompressionAdminStatus=frxVcControlCompressionAdminStatus, frxServiceTableEntryType=frxServiceTableEntryType, frxPortTable=frxPortTable, frxServiceType=frxServiceType, frxVcStatsTx8025Octets=frxVcStatsTx8025Octets, frxVcStatsTxCompressedOctets=frxVcStatsTxCompressedOctets, frxVcStatsTxEthernetOctets=frxVcStatsTxEthernetOctets, frxVcControlCompressionPRetryTime=frxVcControlCompressionPRetryTime, frxPortDefaultBridgingServiceNumber=frxPortDefaultBridgingServiceNumber, frxVcControlCompressionPRetryCount=frxVcControlCompressionPRetryCount, frxVcStatsTxIPXOctets=frxVcStatsTxIPXOctets, frxVcStatsRxDecompressedOctets=frxVcStatsRxDecompressedOctets, frxVcStatsSlotIndex=frxVcStatsSlotIndex, frxVcStatsRxCompressedDiscards=frxVcStatsRxCompressedDiscards, frxPortDescription=frxPortDescription, frxPortDefaultCompressionPRetryTime=frxPortDefaultCompressionPRetryTime, frxPortDefaultCompressionAdminStatus=frxPortDefaultCompressionAdminStatus, frxVcControlDlci=frxVcControlDlci, frxServiceNumber=frxServiceNumber, frxVcStatsRx8025Octets=frxVcStatsRx8025Octets, frxPortPortIndex=frxPortPortIndex)
