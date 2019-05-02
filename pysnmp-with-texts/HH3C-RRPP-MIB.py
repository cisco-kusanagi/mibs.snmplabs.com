#
# PySNMP MIB module HH3C-RRPP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-RRPP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:29:28 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
hh3cCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cCommon")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, ObjectIdentity, IpAddress, NotificationType, iso, Integer32, MibIdentifier, TimeTicks, Counter64, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "ObjectIdentity", "IpAddress", "NotificationType", "iso", "Integer32", "MibIdentifier", "TimeTicks", "Counter64", "Bits")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
hh3cRrpp = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 45))
if mibBuilder.loadTexts: hh3cRrpp.setLastUpdated('200412020000Z')
if mibBuilder.loadTexts: hh3cRrpp.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
if mibBuilder.loadTexts: hh3cRrpp.setContactInfo('Platform Team Hangzhou H3C Tech. Co., Ltd. Hai-Dian District Beijing P.R. China http://www.h3c.com Zip:100085 ')
if mibBuilder.loadTexts: hh3cRrpp.setDescription('The RRPP (Rapid Ring Protection protocol) provides fast protection switching to layer 2 switches interconnected in an Ethernet ring topology. When a link in the ring breaks, the RRPP can recover the data path quickly. Its protection switching is similar to what can be achieved with the Spanning Tree Protocol (STP), but the converging time is less than a second after link failure. This MIB defines management information used on products which support RRPP.')
class EnabledStatus(TextualConvention, Integer32):
    description = 'A simple status value for the object.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

hh3cRrppScalarGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 45, 1))
hh3cRrppEnableStatus = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 45, 1, 1), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cRrppEnableStatus.setStatus('current')
if mibBuilder.loadTexts: hh3cRrppEnableStatus.setDescription('Indicating whether the RRPP is enabled on this switch.')
hh3cRrppPassword = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 45, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 16)).clone(hexValue="303030464532303346443735")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cRrppPassword.setStatus('current')
if mibBuilder.loadTexts: hh3cRrppPassword.setDescription('Password configured for RRPP nodes to identify the validity of a link-down message. This value must be set together with hh3cRrppPasswordType which indicates whether this value can be got. This value can not be set alone without configuring hh3cRrppPasswordType.')
hh3cRrppPasswordType = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 45, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("simple", 1), ("cipher", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cRrppPasswordType.setStatus('current')
if mibBuilder.loadTexts: hh3cRrppPasswordType.setDescription('Indicating whether the hh3cRrppPassword can be got. simple(1):hh3cRrppPassword can be got. cipher(2):hh3cRrppPassword can not be got. This value can not be set alone without configuring hh3cRrppPassword.')
hh3cRrppProtectVlanConfigMode = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 45, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("vlan", 1), ("instance", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cRrppProtectVlanConfigMode.setStatus('current')
if mibBuilder.loadTexts: hh3cRrppProtectVlanConfigMode.setDescription("Indicating the mode in which the protected VLANs of an RRPP domain are configured. The value 'vlan' indicates that hh3cRrppDomainProtectVlanListLow and hh3cRrppDomainProtectVlanListHigh can be used for setting protected VLANs, while hh3cRrppDomainInstanceListLow and hh3cRrppDomainInstanceListHigh cannot. By contraries, the value 'instance' indicates that 3cRrppDomainInstanceListLow and hh3cRrppDomainInstanceListHigh can be used for setting protected VLANs while the other two cannot.")
hh3cRrppTable = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 45, 2))
hh3cRrppDomainTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 45, 2, 1), )
if mibBuilder.loadTexts: hh3cRrppDomainTable.setStatus('current')
if mibBuilder.loadTexts: hh3cRrppDomainTable.setDescription('A table containing information about configurations and status of a RRPP domain.')
hh3cRrppDomainEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 45, 2, 1, 1), ).setIndexNames((0, "HH3C-RRPP-MIB", "hh3cRrppDomainID"))
if mibBuilder.loadTexts: hh3cRrppDomainEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cRrppDomainEntry.setDescription('Detailed information of a specified RRPP domain.')
hh3cRrppDomainID = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 45, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cRrppDomainID.setStatus('current')
if mibBuilder.loadTexts: hh3cRrppDomainID.setDescription("An index uniquely identifies a RRPP domain, which ranges from 1~16. This value can't be modified after created.")
hh3cRrppDomainControlVlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 45, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(2, 4094), ValueRangeConstraint(65535, 65535), ))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cRrppDomainControlVlanID.setStatus('current')
if mibBuilder.loadTexts: hh3cRrppDomainControlVlanID.setDescription("Index of the control VLAN specified to a domain. The value 65535 indicates the control VLAN has not been configured. The VLAN assigned to a RRPP Domain must not have been created. This value can't be modified after created.")
hh3cRrppDomainHelloTime = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 45, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10)).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cRrppDomainHelloTime.setStatus('current')
if mibBuilder.loadTexts: hh3cRrppDomainHelloTime.setDescription('The value indicates the interval between two hello packets sent by master-node, and its unit is second. The value ranges from 1s~10s.')
hh3cRrppDomainFailTime = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 45, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 30)).clone(3)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cRrppDomainFailTime.setStatus('current')
if mibBuilder.loadTexts: hh3cRrppDomainFailTime.setDescription("The expiration value of the fail-period timer and its unit is second. If not receiving hello packets before this expires, the master-node considers the ring is broken. The value of this node ranging from 3s~30s must not be less than triple hh3cRrppDomainHelloTime's value.")
hh3cRrppDomainRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 45, 2, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cRrppDomainRowStatus.setStatus('current')
if mibBuilder.loadTexts: hh3cRrppDomainRowStatus.setDescription('This object is responsible for managing the creation, deletion and modification of rows, which support active status and CreatAndGo, destroy operation.')
hh3cRrppDomainInstanceListLow = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 45, 2, 1, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(256, 256)).setFixedLength(256)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cRrppDomainInstanceListLow.setStatus('current')
if mibBuilder.loadTexts: hh3cRrppDomainInstanceListLow.setDescription("Each octet contained in this value specifies an eight-instance group, with the first octet specifying instances 0 through 7, the second octet specifying instances 8 through 15, and so on. Within each octet, the most significant bit represents the highest numbered instance, and the least significant bit represents the lowest numbered instance. Thus, each instance to which the protected VLANs of an RRPP domain are mapped corresponds to a bit within the value of this object. A bit with a value of '1' indicates that the VLANs mapped to the instance are protected VLANs of the RRPP domain. By contraries, the VLANs mapped to the instance are not protected VLANs if the corresponding bit has a value of '0'. The value of this object must be set with hh3cRrppDomainInstanceListHigh at the same time when a SET operation is performed. This object is valid only when the value of hh3cRrppProtectVlanConfigMode is 'instance'. If this object is invalid, it does not respond to SET operation, and it returns all '0' bits in response to GET operation.")
hh3cRrppDomainInstanceListHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 45, 2, 1, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(256, 256)).setFixedLength(256)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cRrppDomainInstanceListHigh.setStatus('current')
if mibBuilder.loadTexts: hh3cRrppDomainInstanceListHigh.setDescription("Each octet contained in this value specifies an eight-instance group, with the first octet specifying instances 2048 through 2055, the second octet specifying instances 2056 through 2063, and so on. Within each octet, the most significant bit represents the highest numbered instance, and the least significant bit represents the lowest numbered instance. The most significant bit of the last octet is invalid. Thus, each instance to which the protected VLANs of an RRPP domain are mapped corresponds to a bit within the value of this object. A bit with a value of '1' indicates that the VLANs mapped to the instance are protected VLANs of the RRPP domain. By contraries, the VLANs mapped to the instance are not protected VLANs if the corresponding bit has a value of '0'. The value of this object must be set with hh3cRrppDomainInstanceListLow at the same time when a SET operation is performed. This object is valid only when the value of hh3cRrppProtectVlanConfigMode is 'instance'. If this object is invalid, it does not respond to SET operation, and it returns all '0' bits in response to GET operation.")
hh3cRrppDomainProtectVlanListLow = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 45, 2, 1, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(256, 256)).setFixedLength(256)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cRrppDomainProtectVlanListLow.setStatus('current')
if mibBuilder.loadTexts: hh3cRrppDomainProtectVlanListLow.setDescription("Each octet contained in this value specifies an eight-VLAN group, with the first octet specifying VLANs 1 through 7, the second octet specifying VLANs 8 through 15, and so on. Within each octet, the most significant bit represents the highest numbered VLAN, and the least significant bit represents the lowest numbered VLAN. The least significant bit of the first octet is invalid. Thus, each protected VLAN of an RRPP domain corresponds to a bit within the value of this object. A bit with a value of '1' indicates that the corresponding VLAN is a protected VLAN of the RRPP domain. By contraries, the VLAN is not a protected VLAN if the corresponding bit has a value of '0'. The value of this object must be set with hh3cRrppDomainProtectVlanListHigh at the same time when a SET operation is performed. This object is valid only when the value of hh3cRrppProtectVlanConfigMode is 'vlan'. If this object is invalid, it does not respond to SET operation, and it returns all '0' bits in response to GET operation.")
hh3cRrppDomainProtectVlanListHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 45, 2, 1, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(256, 256)).setFixedLength(256)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cRrppDomainProtectVlanListHigh.setStatus('current')
if mibBuilder.loadTexts: hh3cRrppDomainProtectVlanListHigh.setDescription("Each octet contained in this value specifies an eight-VLAN group, with the first octet specifying VLANs 2048 through 2055, the second octet specifying VLANs 2056 through 2063, and so on. Within each octet, the most significant bit represents the highest numbered VLAN, and the least significant bit represents the lowest numbered VLAN. The most significant bit of the last octet is invalid. Thus, each protected VLAN of an RRPP domain corresponds to a bit within the value of this object. A bit with a value of '1' indicates that the corresponding VLAN is a protected VLAN of the RRPP domain. By contraries, the VLAN is not a protected VLAN if the corresponding bit has a value of '0'. The value of this object must be set with hh3cRrppDomainProtectVlanListLow at the same time when a SET operation is performed. This object is valid only when the value of hh3cRrppProtectVlanConfigMode is 'vlan'. If this object is invalid, it does not respond to SET operation, and it returns all '0' bits in response to GET operation.")
hh3cRrppRingTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 45, 2, 2), )
if mibBuilder.loadTexts: hh3cRrppRingTable.setStatus('current')
if mibBuilder.loadTexts: hh3cRrppRingTable.setDescription('A table containing information about configurations and status of a RRPP Ring.')
hh3cRrppRingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 45, 2, 2, 1), ).setIndexNames((0, "HH3C-RRPP-MIB", "hh3cRrppDomainID"), (0, "HH3C-RRPP-MIB", "hh3cRrppRingID"))
if mibBuilder.loadTexts: hh3cRrppRingEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cRrppRingEntry.setDescription('Detailed information of a specified RRPP Ring.')
hh3cRrppRingID = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 45, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 64))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cRrppRingID.setStatus('current')
if mibBuilder.loadTexts: hh3cRrppRingID.setDescription("An index uniquely identifies a RRPP Ring, which ranges from 1~64. This value can't be modified after created.")
hh3cRrppRingEnableStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 45, 2, 2, 1, 2), EnabledStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cRrppRingEnableStatus.setStatus('current')
if mibBuilder.loadTexts: hh3cRrppRingEnableStatus.setDescription('Indicating whether the RRPP is enabled on this Ring. NOTE: If major-ring and sub-ring(s) of a domain coexist on a switch, major-ring must be enabled before sub-ring is enabled. And sub-ring must be disabled before major-ring is disabled.')
hh3cRrppRingActive = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 45, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("inactive", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cRrppRingActive.setStatus('current')
if mibBuilder.loadTexts: hh3cRrppRingActive.setDescription('As both hh3cRrppEnableStatus and hh3cRrppRingEnableStatus are enabled, the ring is activated. Whereas either of the two items is disabled, the ring is inactive.')
hh3cRrppRingState = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 45, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("health", 2), ("fault", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cRrppRingState.setStatus('current')
if mibBuilder.loadTexts: hh3cRrppRingState.setDescription('The status (i.e. unknown, health or fault) of the Ethernet ring. This is valid only on the master-node.')
hh3cRrppRingNodeMode = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 45, 2, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("master", 1), ("transit", 2), ("edge", 3), ("assistantEdge", 4)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cRrppRingNodeMode.setStatus('current')
if mibBuilder.loadTexts: hh3cRrppRingNodeMode.setDescription("There are four RRPP node modes for the switch on a RRPP ring, such as master, transit, edge and assistant-edge. Each RRPP ring has a single designated master-node. All other nodes except edge-node and assistant-edge-node on that ring are referred to as transit-nodes. The node mode of edge and assistant-edge should be configured only on sub-ring. When there is a common link between a sub-ring and its major-ring, the node mode of the sub-ring must be edge or assistant-edge, and they must be configured in pairs. If node mode is designated as edge or assistant-edge, several points should be noticed: Major-ring must be created before a sub-ring is created; Major-ring can't be deleted unless all its sub-rings are deleted; The node mode of the switch on major-ring must be transit; Major-ring and sub-ring must have only a common port. This value can't be modified after created.")
hh3cRrppRingPrimaryPort = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 45, 2, 2, 1, 6), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cRrppRingPrimaryPort.setStatus('current')
if mibBuilder.loadTexts: hh3cRrppRingPrimaryPort.setDescription("If the switch is a master-node or transit-node, this value is the primary port ifIndex; otherwise, if the switch is a edge-node or assistant-edge-node, this value is the common port ifIndex. This value can't be modified after created.")
hh3cRrppRingSecondaryPort = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 45, 2, 2, 1, 7), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cRrppRingSecondaryPort.setStatus('current')
if mibBuilder.loadTexts: hh3cRrppRingSecondaryPort.setDescription("If the switch is a master-node or transit-node, this value is the secondary port ifIndex; otherwise, if the switch is an edge-node or assistant-edge-node, this value is the edge port ifIndex. This value can't be modified after created.")
hh3cRrppRingLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 45, 2, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("majorRing", 1), ("subRing", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cRrppRingLevel.setStatus('current')
if mibBuilder.loadTexts: hh3cRrppRingLevel.setDescription("Level of a ring. This field should be set 1 on major-ring and 2 on the sub-ring. This value can't be modified after created.")
hh3cRrppRingRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 45, 2, 2, 1, 9), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cRrppRingRowStatus.setStatus('current')
if mibBuilder.loadTexts: hh3cRrppRingRowStatus.setDescription('This object is responsible for managing the creation, deletion and modification of rows, which support active status and CreatAndGo, destroy operation. To create a new row, hh3cRrppRingNodeMode, hh3cRrppRingPrimaryPort, hh3cRrppRingSecondaryPort and hh3cRrppRingLevel must be specified.')
hh3cRrppPortTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 45, 2, 3), )
if mibBuilder.loadTexts: hh3cRrppPortTable.setStatus('current')
if mibBuilder.loadTexts: hh3cRrppPortTable.setDescription('A table containing information about configurations and status of a RRPP port.')
hh3cRrppPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 45, 2, 3, 1), ).setIndexNames((0, "HH3C-RRPP-MIB", "hh3cRrppDomainID"), (0, "HH3C-RRPP-MIB", "hh3cRrppRingID"), (0, "HH3C-RRPP-MIB", "hh3cRrppPortID"))
if mibBuilder.loadTexts: hh3cRrppPortEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cRrppPortEntry.setDescription('Detailed information of a specified RRPP port.')
hh3cRrppPortID = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 45, 2, 3, 1, 1), Integer32())
if mibBuilder.loadTexts: hh3cRrppPortID.setStatus('current')
if mibBuilder.loadTexts: hh3cRrppPortID.setDescription('ifIndex of the port.')
hh3cRrppPortRole = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 45, 2, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("primary", 1), ("secondary", 2), ("common", 3), ("edge", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cRrppPortRole.setStatus('current')
if mibBuilder.loadTexts: hh3cRrppPortRole.setDescription('The RRPP role of the port. (i.e. primary, secondary, common or edge port).')
hh3cRrppPortState = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 45, 2, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 1), ("unblocked", 2), ("blocked", 3), ("down", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cRrppPortState.setStatus('current')
if mibBuilder.loadTexts: hh3cRrppPortState.setDescription('State of RRPP port, including unknown, unblocked, blocked and down.')
hh3cRrppPortRXError = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 45, 2, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cRrppPortRXError.setStatus('current')
if mibBuilder.loadTexts: hh3cRrppPortRXError.setDescription('The statistics of illegal RRPP packets received from this port.')
hh3cRrppPortRXHello = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 45, 2, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cRrppPortRXHello.setStatus('current')
if mibBuilder.loadTexts: hh3cRrppPortRXHello.setDescription('The statistics of hello packets received from this port on specified ring.')
hh3cRrppPortRXLinkUp = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 45, 2, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cRrppPortRXLinkUp.setStatus('current')
if mibBuilder.loadTexts: hh3cRrppPortRXLinkUp.setDescription('The statistics of link-up packets received from this port on specified ring.')
hh3cRrppPortRXLinkDown = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 45, 2, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cRrppPortRXLinkDown.setStatus('current')
if mibBuilder.loadTexts: hh3cRrppPortRXLinkDown.setDescription('The statistics of link-down packets received from this port on specified ring.')
hh3cRrppPortRXCommonFlush = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 45, 2, 3, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cRrppPortRXCommonFlush.setStatus('current')
if mibBuilder.loadTexts: hh3cRrppPortRXCommonFlush.setDescription("The statistics of common-flush packets received from this port on specified ring. Instruction When master-node receives valid link-down packets or link-up packets, it will send common-flush packets, instructing the other nodes on the ring to flush their forwarding database. When the nodes except master-node receive common-flush, they will flush forwarding database. If there is any port blocked on that node, it won't be unblocked.")
hh3cRrppPortRXCompleteFlush = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 45, 2, 3, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cRrppPortRXCompleteFlush.setStatus('current')
if mibBuilder.loadTexts: hh3cRrppPortRXCompleteFlush.setDescription('The statistics of complete-flush packets received from this port on specified ring. Instruction When the ring recovers, master-node will receive its own hello packets. It will send complete-flush packets, instructing the other nodes on the ring to flush their forwarding database. When the nodes except master-node receive complete-flush, they will flush forwarding database. If there is any port blocked on that node, it will be unblocked.')
hh3cRrppPortTXHello = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 45, 2, 3, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cRrppPortTXHello.setStatus('current')
if mibBuilder.loadTexts: hh3cRrppPortTXHello.setDescription('The statistics of hello packets sent from this port on specified ring.')
hh3cRrppPortTXLinkUp = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 45, 2, 3, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cRrppPortTXLinkUp.setStatus('current')
if mibBuilder.loadTexts: hh3cRrppPortTXLinkUp.setDescription('The statistics of link-up packets sent from this port on specified ring.')
hh3cRrppPortTXLinkDown = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 45, 2, 3, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cRrppPortTXLinkDown.setStatus('current')
if mibBuilder.loadTexts: hh3cRrppPortTXLinkDown.setDescription('The statistics of link-down packets sent from this port on specified ring.')
hh3cRrppPortTXCommonFlush = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 45, 2, 3, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cRrppPortTXCommonFlush.setStatus('current')
if mibBuilder.loadTexts: hh3cRrppPortTXCommonFlush.setDescription('The statistics of common-flush packets sent from this port on specified ring.')
hh3cRrppPortTXCompleteFlush = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 45, 2, 3, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cRrppPortTXCompleteFlush.setStatus('current')
if mibBuilder.loadTexts: hh3cRrppPortTXCompleteFlush.setDescription('The statistics of complete-flush packets sent from this port on specified ring.')
hh3cRrppPortRXEdgeHello = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 45, 2, 3, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cRrppPortRXEdgeHello.setStatus('current')
if mibBuilder.loadTexts: hh3cRrppPortRXEdgeHello.setDescription('The statistics of edge-hello packets received from this port on specified ring. When edge-node sends edge-hello packets, assistantEdge-node will receive its own edge-hello packets from the common link and the master ring.')
hh3cRrppPortRXMajorFault = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 45, 2, 3, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cRrppPortRXMajorFault.setStatus('current')
if mibBuilder.loadTexts: hh3cRrppPortRXMajorFault.setDescription("The statistics of major-fault packets received from this port on specified ring. When assistantEdge can't receive edge-hello packets in the specified fault-time, assistantEdge-node will send its own major-fault packets from the edge port around the sub ring. Edge-node will receive the major-fault packets from its edge port. Then Edge-node will block its edge port.")
hh3cRrppPortTXEdgeHello = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 45, 2, 3, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cRrppPortTXEdgeHello.setStatus('current')
if mibBuilder.loadTexts: hh3cRrppPortTXEdgeHello.setDescription('The statistics of edge-hello packets sent from this port on specified ring.')
hh3cRrppPortTXMajorFault = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 45, 2, 3, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cRrppPortTXMajorFault.setStatus('current')
if mibBuilder.loadTexts: hh3cRrppPortTXMajorFault.setDescription('The statistics of major-fault packets sent from this port on specified ring.')
hh3cRrppNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 45, 3))
hh3cRrppRingRecover = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 45, 3, 1)).setObjects(("HH3C-RRPP-MIB", "hh3cRrppDomainID"), ("HH3C-RRPP-MIB", "hh3cRrppRingID"))
if mibBuilder.loadTexts: hh3cRrppRingRecover.setStatus('current')
if mibBuilder.loadTexts: hh3cRrppRingRecover.setDescription('Trap message is generated by master-node on the ring when the ring recovers from fault.')
hh3cRrppRingFail = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 45, 3, 2)).setObjects(("HH3C-RRPP-MIB", "hh3cRrppDomainID"), ("HH3C-RRPP-MIB", "hh3cRrppRingID"))
if mibBuilder.loadTexts: hh3cRrppRingFail.setStatus('current')
if mibBuilder.loadTexts: hh3cRrppRingFail.setDescription('Trap message is generated by master-node on the ring when the ring fails.')
hh3cRrppMultiMaster = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 45, 3, 3)).setObjects(("HH3C-RRPP-MIB", "hh3cRrppDomainID"), ("HH3C-RRPP-MIB", "hh3cRrppRingID"))
if mibBuilder.loadTexts: hh3cRrppMultiMaster.setStatus('current')
if mibBuilder.loadTexts: hh3cRrppMultiMaster.setDescription('Trap message is generated by master-node when it detects there are more than one master-node on the ring.')
hh3cRrppMajorFault = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 45, 3, 4)).setObjects(("HH3C-RRPP-MIB", "hh3cRrppDomainID"), ("HH3C-RRPP-MIB", "hh3cRrppRingID"))
if mibBuilder.loadTexts: hh3cRrppMajorFault.setStatus('current')
if mibBuilder.loadTexts: hh3cRrppMajorFault.setDescription('Trap message is generated by edge-node or assistant-edge-node when it detects major fault.')
mibBuilder.exportSymbols("HH3C-RRPP-MIB", hh3cRrppRingPrimaryPort=hh3cRrppRingPrimaryPort, hh3cRrppPortRXHello=hh3cRrppPortRXHello, hh3cRrppPortTXCompleteFlush=hh3cRrppPortTXCompleteFlush, hh3cRrppDomainID=hh3cRrppDomainID, hh3cRrppPortTable=hh3cRrppPortTable, hh3cRrppPortEntry=hh3cRrppPortEntry, hh3cRrppDomainHelloTime=hh3cRrppDomainHelloTime, hh3cRrppPortTXMajorFault=hh3cRrppPortTXMajorFault, hh3cRrppRingRecover=hh3cRrppRingRecover, hh3cRrppPortRXLinkDown=hh3cRrppPortRXLinkDown, EnabledStatus=EnabledStatus, hh3cRrppRingState=hh3cRrppRingState, hh3cRrppDomainInstanceListLow=hh3cRrppDomainInstanceListLow, hh3cRrppRingID=hh3cRrppRingID, hh3cRrppRingEnableStatus=hh3cRrppRingEnableStatus, hh3cRrppPortRole=hh3cRrppPortRole, hh3cRrppMultiMaster=hh3cRrppMultiMaster, PYSNMP_MODULE_ID=hh3cRrpp, hh3cRrppPortRXLinkUp=hh3cRrppPortRXLinkUp, hh3cRrppPortTXCommonFlush=hh3cRrppPortTXCommonFlush, hh3cRrppDomainRowStatus=hh3cRrppDomainRowStatus, hh3cRrppPortTXEdgeHello=hh3cRrppPortTXEdgeHello, hh3cRrppDomainProtectVlanListLow=hh3cRrppDomainProtectVlanListLow, hh3cRrppPasswordType=hh3cRrppPasswordType, hh3cRrppPortID=hh3cRrppPortID, hh3cRrppPortRXError=hh3cRrppPortRXError, hh3cRrppNotifications=hh3cRrppNotifications, hh3cRrppPortTXHello=hh3cRrppPortTXHello, hh3cRrpp=hh3cRrpp, hh3cRrppPortTXLinkUp=hh3cRrppPortTXLinkUp, hh3cRrppRingEntry=hh3cRrppRingEntry, hh3cRrppTable=hh3cRrppTable, hh3cRrppRingLevel=hh3cRrppRingLevel, hh3cRrppDomainControlVlanID=hh3cRrppDomainControlVlanID, hh3cRrppRingNodeMode=hh3cRrppRingNodeMode, hh3cRrppRingFail=hh3cRrppRingFail, hh3cRrppMajorFault=hh3cRrppMajorFault, hh3cRrppProtectVlanConfigMode=hh3cRrppProtectVlanConfigMode, hh3cRrppPassword=hh3cRrppPassword, hh3cRrppRingRowStatus=hh3cRrppRingRowStatus, hh3cRrppPortState=hh3cRrppPortState, hh3cRrppDomainProtectVlanListHigh=hh3cRrppDomainProtectVlanListHigh, hh3cRrppPortRXEdgeHello=hh3cRrppPortRXEdgeHello, hh3cRrppDomainTable=hh3cRrppDomainTable, hh3cRrppPortRXCommonFlush=hh3cRrppPortRXCommonFlush, hh3cRrppPortTXLinkDown=hh3cRrppPortTXLinkDown, hh3cRrppDomainEntry=hh3cRrppDomainEntry, hh3cRrppDomainFailTime=hh3cRrppDomainFailTime, hh3cRrppDomainInstanceListHigh=hh3cRrppDomainInstanceListHigh, hh3cRrppPortRXCompleteFlush=hh3cRrppPortRXCompleteFlush, hh3cRrppPortRXMajorFault=hh3cRrppPortRXMajorFault, hh3cRrppRingTable=hh3cRrppRingTable, hh3cRrppRingActive=hh3cRrppRingActive, hh3cRrppEnableStatus=hh3cRrppEnableStatus, hh3cRrppScalarGroup=hh3cRrppScalarGroup, hh3cRrppRingSecondaryPort=hh3cRrppRingSecondaryPort)
