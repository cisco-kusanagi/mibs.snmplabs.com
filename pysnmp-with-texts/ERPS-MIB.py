#
# PySNMP MIB module ERPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ERPS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:06:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
dlink_common_mgmt, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-common-mgmt")
VlanIdOrNone, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanIdOrNone")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, IpAddress, iso, Counter32, Bits, Gauge32, Integer32, Counter64, Unsigned32, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "IpAddress", "iso", "Counter32", "Bits", "Gauge32", "Integer32", "Counter64", "Unsigned32", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "TimeTicks")
MacAddress, RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "RowStatus", "DisplayString", "TextualConvention")
swERPSMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 12, 78))
if mibBuilder.loadTexts: swERPSMIB.setLastUpdated('201007160000Z')
if mibBuilder.loadTexts: swERPSMIB.setOrganization('D-Link Corp.')
if mibBuilder.loadTexts: swERPSMIB.setContactInfo('http://support.dlink.com')
if mibBuilder.loadTexts: swERPSMIB.setDescription('The MIB module for managing Ethernet Ring Protection Switching.')
class VidList(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 127)

swERPSCtrl = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 78, 1))
swERPSInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 78, 2))
swERPSMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 78, 3))
swERPSNotify = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 78, 4))
swERPSAdminState = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 78, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swERPSAdminState.setStatus('current')
if mibBuilder.loadTexts: swERPSAdminState.setDescription('This object indicates the ERPS state of the bridge.')
swERPSLogState = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 78, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swERPSLogState.setStatus('current')
if mibBuilder.loadTexts: swERPSLogState.setDescription('This object indicates the ERPS log state of the bridge.')
swERPSTrapState = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 78, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swERPSTrapState.setStatus('current')
if mibBuilder.loadTexts: swERPSTrapState.setDescription('This object indicates the ERPS trap state of the bridge.')
swERPSMgmtRAPSVlanTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 78, 3, 1), )
if mibBuilder.loadTexts: swERPSMgmtRAPSVlanTable.setStatus('current')
if mibBuilder.loadTexts: swERPSMgmtRAPSVlanTable.setDescription('This table contains the ERPS ring configuration information.')
swERPSMgmtRAPSVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 78, 3, 1, 1), ).setIndexNames((0, "ERPS-MIB", "swERPSMgmtRAPSVlanId"))
if mibBuilder.loadTexts: swERPSMgmtRAPSVlanEntry.setStatus('current')
if mibBuilder.loadTexts: swERPSMgmtRAPSVlanEntry.setDescription('A list of the ERPS ring configuration information.')
swERPSMgmtRAPSVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 78, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swERPSMgmtRAPSVlanId.setStatus('current')
if mibBuilder.loadTexts: swERPSMgmtRAPSVlanId.setDescription('The RAPS VLAN is an index of the configuration.')
swERPSMgmtRAPSWestPort = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 78, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 65535), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swERPSMgmtRAPSWestPort.setStatus('current')
if mibBuilder.loadTexts: swERPSMgmtRAPSWestPort.setDescription('This is one of the RPL owner ports.The RPL owner may block this port. The value 0 indicates the west port is a virtual channel.')
swERPSMgmtRAPSWestPortState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 78, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("fowarding", 1), ("blocking", 2), ("signal-fail", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swERPSMgmtRAPSWestPortState.setStatus('current')
if mibBuilder.loadTexts: swERPSMgmtRAPSWestPortState.setDescription('This is the west port state. The state may change occasionally. When the west port is configured on a virtual channel, the west port state is always forwarding.')
swERPSMgmtRAPSEastPort = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 78, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 65535), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swERPSMgmtRAPSEastPort.setStatus('current')
if mibBuilder.loadTexts: swERPSMgmtRAPSEastPort.setDescription('This is the other RPL owner port.The RPL Owner may block this port. The value 0 indicates the west port is a virtual channel.')
swERPSMgmtRAPSEastPortState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 78, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("fowarding", 1), ("blocking", 2), ("signal-fail", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swERPSMgmtRAPSEastPortState.setStatus('current')
if mibBuilder.loadTexts: swERPSMgmtRAPSEastPortState.setDescription('This is the east port state. The state may change occasionally. When the east port is configured on a virtual channel, the east port state is always forwarding.')
swERPSMgmtRAPSRPLPort = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 78, 3, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("west", 2), ("east", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swERPSMgmtRAPSRPLPort.setStatus('current')
if mibBuilder.loadTexts: swERPSMgmtRAPSRPLPort.setDescription("When the port enable state is enabled, the RPL port's current port role is defined by the ERPS application.")
swERPSMgmtRAPSRPLOwnerAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 78, 3, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swERPSMgmtRAPSRPLOwnerAdminState.setStatus('current')
if mibBuilder.loadTexts: swERPSMgmtRAPSRPLOwnerAdminState.setDescription('The administrative value of the RPL owner state. The RPL owner is an Ethernet Ring Node adjacent to the RPL that is responsible for blocking its end of the RPL under normal conditions.')
swERPSMgmtRAPSProtectionVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 78, 3, 1, 1, 8), VidList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swERPSMgmtRAPSProtectionVlan.setStatus('current')
if mibBuilder.loadTexts: swERPSMgmtRAPSProtectionVlan.setDescription('The protection VLAN has prevented a loop.')
swERPSMgmtRAPSRingMEL = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 78, 3, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swERPSMgmtRAPSRingMEL.setStatus('current')
if mibBuilder.loadTexts: swERPSMgmtRAPSRingMEL.setDescription('The ring MEL is the maintenance entity group (MEG) level that provides a communication channel for the ring automatic protection switching (RAPS) information.')
swERPSMgmtRAPSHoldOffTime = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 78, 3, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swERPSMgmtRAPSHoldOffTime.setStatus('current')
if mibBuilder.loadTexts: swERPSMgmtRAPSHoldOffTime.setDescription('In order to coordinate the timing of protection switches at multiple layers.')
swERPSMgmtRAPSGuardTime = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 78, 3, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 2000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swERPSMgmtRAPSGuardTime.setStatus('current')
if mibBuilder.loadTexts: swERPSMgmtRAPSGuardTime.setDescription('This is used to prevent ring nodes from receiving outdated RAPS messages.')
swERPSMgmtRAPSWTRTime = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 78, 3, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 12))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swERPSMgmtRAPSWTRTime.setStatus('current')
if mibBuilder.loadTexts: swERPSMgmtRAPSWTRTime.setDescription('When revertive is enabled, this is used to prevent frequent operation of the protection switch due to an intermittent defect. A failed working transport entity must become stable in a fault-free state.')
swERPSMgmtRAPSRingState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 78, 3, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("begin", 1), ("init", 2), ("idle", 3), ("protection", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swERPSMgmtRAPSRingState.setStatus('current')
if mibBuilder.loadTexts: swERPSMgmtRAPSRingState.setDescription('This indicates the state of the ring.The available states are: begin, init, idle, or protection.')
swERPSMgmtRAPSRingAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 78, 3, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swERPSMgmtRAPSRingAdminState.setStatus('current')
if mibBuilder.loadTexts: swERPSMgmtRAPSRingAdminState.setDescription('This indicates the administrative state of the ring.')
swERPSMgmtRAPSRPLOwnerOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 78, 3, 1, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("active", 1), ("inactive", 2), ("disabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swERPSMgmtRAPSRPLOwnerOperStatus.setStatus('current')
if mibBuilder.loadTexts: swERPSMgmtRAPSRPLOwnerOperStatus.setDescription("The current operational value of the RPL owner state. The value 'active' is used to indicate that the RPL owner administrative state is enabled and the device is operating as the active RPL owner. The value 'inactive' is used to indicate that the RPL owner administrative state is enabled, but the device is operating as the inactive RPL owner. The value 'disabled' is used to indicate that the RPL owner administrative state of the device is disabled.")
swERPSMgmtRAPSProtectionVlanRangeList1to64 = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 78, 3, 1, 1, 16), OctetString().subtype(subtypeSpec=ValueSizeConstraint(64, 64)).setFixedLength(64)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swERPSMgmtRAPSProtectionVlanRangeList1to64.setStatus('current')
if mibBuilder.loadTexts: swERPSMgmtRAPSProtectionVlanRangeList1to64.setDescription('This object indicates the VLAN range (1-512) that belong to the protected VLANs.')
swERPSMgmtRAPSProtectionVlanRangeList65to128 = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 78, 3, 1, 1, 17), OctetString().subtype(subtypeSpec=ValueSizeConstraint(64, 64)).setFixedLength(64)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swERPSMgmtRAPSProtectionVlanRangeList65to128.setStatus('current')
if mibBuilder.loadTexts: swERPSMgmtRAPSProtectionVlanRangeList65to128.setDescription('This object indicates the VLAN range (513-1024) that belong to the protected VLANs.')
swERPSMgmtRAPSProtectionVlanRangeList129to192 = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 78, 3, 1, 1, 18), OctetString().subtype(subtypeSpec=ValueSizeConstraint(64, 64)).setFixedLength(64)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swERPSMgmtRAPSProtectionVlanRangeList129to192.setStatus('current')
if mibBuilder.loadTexts: swERPSMgmtRAPSProtectionVlanRangeList129to192.setDescription('This object indicates the VLAN range (1025-1536) that belong to the protected VLANs.')
swERPSMgmtRAPSProtectionVlanRangeList193to256 = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 78, 3, 1, 1, 19), OctetString().subtype(subtypeSpec=ValueSizeConstraint(64, 64)).setFixedLength(64)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swERPSMgmtRAPSProtectionVlanRangeList193to256.setStatus('current')
if mibBuilder.loadTexts: swERPSMgmtRAPSProtectionVlanRangeList193to256.setDescription('This object indicates the VLAN range (1537-2048) that belong to the protected VLANs.')
swERPSMgmtRAPSProtectionVlanRangeList257to320 = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 78, 3, 1, 1, 20), OctetString().subtype(subtypeSpec=ValueSizeConstraint(64, 64)).setFixedLength(64)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swERPSMgmtRAPSProtectionVlanRangeList257to320.setStatus('current')
if mibBuilder.loadTexts: swERPSMgmtRAPSProtectionVlanRangeList257to320.setDescription('This object indicates the VLAN range (2049-2560) that belong to the protected VLANs.')
swERPSMgmtRAPSProtectionVlanRangeList321to384 = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 78, 3, 1, 1, 21), OctetString().subtype(subtypeSpec=ValueSizeConstraint(64, 64)).setFixedLength(64)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swERPSMgmtRAPSProtectionVlanRangeList321to384.setStatus('current')
if mibBuilder.loadTexts: swERPSMgmtRAPSProtectionVlanRangeList321to384.setDescription('This object indicates the VLAN range (2561-3072) that belongs to the protected VLANs.')
swERPSMgmtRAPSProtectionVlanRangeList385to448 = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 78, 3, 1, 1, 22), OctetString().subtype(subtypeSpec=ValueSizeConstraint(64, 64)).setFixedLength(64)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swERPSMgmtRAPSProtectionVlanRangeList385to448.setStatus('current')
if mibBuilder.loadTexts: swERPSMgmtRAPSProtectionVlanRangeList385to448.setDescription('This object indicates the VLAN range (3073-3584) that belong to the protected VLANs.')
swERPSMgmtRAPSProtectionVlanRangeList449to512 = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 78, 3, 1, 1, 23), OctetString().subtype(subtypeSpec=ValueSizeConstraint(64, 64)).setFixedLength(64)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swERPSMgmtRAPSProtectionVlanRangeList449to512.setStatus('current')
if mibBuilder.loadTexts: swERPSMgmtRAPSProtectionVlanRangeList449to512.setDescription('This object indicates the VLAN range (3585-4096) that belong to the protected VLANs.')
swERPSMgmtRAPSRevertive = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 78, 3, 1, 1, 24), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swERPSMgmtRAPSRevertive.setStatus('current')
if mibBuilder.loadTexts: swERPSMgmtRAPSRevertive.setDescription('The object is used to enable or disable the revertive operation of a special ring. When revertive is disabled, the traffic link is allowed to use the RPL, after revovering from a failure. When revertive is enabled, the traffic link is restored to the working transport link.')
swERPSMgmtRAPSOperWestPort = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 78, 3, 1, 1, 25), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 65535), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swERPSMgmtRAPSOperWestPort.setStatus('current')
if mibBuilder.loadTexts: swERPSMgmtRAPSOperWestPort.setDescription('This object indicates actual running ring west port. The value 0 indicates the west port is a virtual channel.')
swERPSMgmtRAPSOperEastPort = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 78, 3, 1, 1, 26), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 65535), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swERPSMgmtRAPSOperEastPort.setStatus('current')
if mibBuilder.loadTexts: swERPSMgmtRAPSOperEastPort.setDescription('This object indicates actual running ring east port. The value 0 indicates the east port is a virtual channel.')
swERPSMgmtRAPSOperRPLPort = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 78, 3, 1, 1, 27), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("west", 2), ("east", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swERPSMgmtRAPSOperRPLPort.setStatus('current')
if mibBuilder.loadTexts: swERPSMgmtRAPSOperRPLPort.setDescription('This object indicates actual running ring RPL port.')
swERPSMgmtRAPSRPLOwnerOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 78, 3, 1, 1, 28), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swERPSMgmtRAPSRPLOwnerOperState.setStatus('current')
if mibBuilder.loadTexts: swERPSMgmtRAPSRPLOwnerOperState.setDescription('This object indicates actual running RPL owner state.')
swERPSMgmtRAPSRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 78, 3, 1, 1, 100), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swERPSMgmtRAPSRowStatus.setStatus('current')
if mibBuilder.loadTexts: swERPSMgmtRAPSRowStatus.setDescription('This object indicates the RowStatus of this entry.')
swERPSMgmtSubRingCtrlTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 78, 3, 2), )
if mibBuilder.loadTexts: swERPSMgmtSubRingCtrlTable.setStatus('current')
if mibBuilder.loadTexts: swERPSMgmtSubRingCtrlTable.setDescription('This table contains the ERPS sub-ring configuration information.')
swERPSMgmtSubRingCtrlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 78, 3, 2, 1), ).setIndexNames((0, "ERPS-MIB", "swERPSMgmtSubRingCtrlRAPSVlanId"), (0, "ERPS-MIB", "swERPSMgmtSubRingCtrlSubRingRAPSVlanId"))
if mibBuilder.loadTexts: swERPSMgmtSubRingCtrlEntry.setStatus('current')
if mibBuilder.loadTexts: swERPSMgmtSubRingCtrlEntry.setDescription('A list of the ERPS sub-ring configuration information.')
swERPSMgmtSubRingCtrlRAPSVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 78, 3, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: swERPSMgmtSubRingCtrlRAPSVlanId.setStatus('current')
if mibBuilder.loadTexts: swERPSMgmtSubRingCtrlRAPSVlanId.setDescription('The RAPS VLAN is an index of the configuration.')
swERPSMgmtSubRingCtrlSubRingRAPSVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 78, 3, 2, 1, 2), Integer32())
if mibBuilder.loadTexts: swERPSMgmtSubRingCtrlSubRingRAPSVlanId.setStatus('current')
if mibBuilder.loadTexts: swERPSMgmtSubRingCtrlSubRingRAPSVlanId.setDescription('This indicates the ring control VLAN-ID of the sub-ring which connects to another ring.')
swERPSMgmtSubRingCtrlTCPropagationState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 78, 3, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swERPSMgmtSubRingCtrlTCPropagationState.setStatus('current')
if mibBuilder.loadTexts: swERPSMgmtSubRingCtrlTCPropagationState.setDescription('This indicates the state of the sub-ring topology change propagation.')
swERPSMgmtSubRingCtrlRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 78, 3, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swERPSMgmtSubRingCtrlRowStatus.setStatus('current')
if mibBuilder.loadTexts: swERPSMgmtSubRingCtrlRowStatus.setDescription('This object indicates the status of this entry.')
swERPSNotifyPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 78, 4, 0))
swERPSSFDetectedTrap = NotificationType((1, 3, 6, 1, 4, 1, 171, 12, 78, 4, 0, 1)).setObjects(("ERPS-MIB", "swERPSNodeId"))
if mibBuilder.loadTexts: swERPSSFDetectedTrap.setStatus('current')
if mibBuilder.loadTexts: swERPSSFDetectedTrap.setDescription('When a signal failure occurs, a trap will be generated.')
swERPSSFClearedTrap = NotificationType((1, 3, 6, 1, 4, 1, 171, 12, 78, 4, 0, 2)).setObjects(("ERPS-MIB", "swERPSNodeId"))
if mibBuilder.loadTexts: swERPSSFClearedTrap.setStatus('current')
if mibBuilder.loadTexts: swERPSSFClearedTrap.setDescription('When the signal failure clears, a trap will be generated.')
swERPSRPLOwnerConflictTrap = NotificationType((1, 3, 6, 1, 4, 1, 171, 12, 78, 4, 0, 3)).setObjects(("ERPS-MIB", "swERPSNodeId"))
if mibBuilder.loadTexts: swERPSRPLOwnerConflictTrap.setStatus('current')
if mibBuilder.loadTexts: swERPSRPLOwnerConflictTrap.setDescription('When a conflict occurs, a trap will be generated.')
swERPSNotificationBindings = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 78, 4, 2))
swERPSNodeId = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 78, 4, 2, 1), MacAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: swERPSNodeId.setStatus('current')
if mibBuilder.loadTexts: swERPSNodeId.setDescription('This used trap object means the node MAC.')
mibBuilder.exportSymbols("ERPS-MIB", swERPSMgmtRAPSGuardTime=swERPSMgmtRAPSGuardTime, swERPSMgmtRAPSProtectionVlanRangeList1to64=swERPSMgmtRAPSProtectionVlanRangeList1to64, swERPSCtrl=swERPSCtrl, swERPSSFClearedTrap=swERPSSFClearedTrap, swERPSMgmtRAPSProtectionVlanRangeList321to384=swERPSMgmtRAPSProtectionVlanRangeList321to384, swERPSMgmtRAPSRPLPort=swERPSMgmtRAPSRPLPort, swERPSMgmtRAPSOperRPLPort=swERPSMgmtRAPSOperRPLPort, swERPSMgmtRAPSWestPortState=swERPSMgmtRAPSWestPortState, swERPSMgmtRAPSOperEastPort=swERPSMgmtRAPSOperEastPort, swERPSMgmtSubRingCtrlSubRingRAPSVlanId=swERPSMgmtSubRingCtrlSubRingRAPSVlanId, swERPSMgmtRAPSRevertive=swERPSMgmtRAPSRevertive, swERPSMgmtRAPSOperWestPort=swERPSMgmtRAPSOperWestPort, swERPSMgmtSubRingCtrlEntry=swERPSMgmtSubRingCtrlEntry, swERPSMgmtRAPSProtectionVlanRangeList449to512=swERPSMgmtRAPSProtectionVlanRangeList449to512, swERPSMgmtRAPSWTRTime=swERPSMgmtRAPSWTRTime, swERPSMgmtSubRingCtrlRowStatus=swERPSMgmtSubRingCtrlRowStatus, swERPSMgmtRAPSVlanId=swERPSMgmtRAPSVlanId, swERPSMgmtRAPSProtectionVlanRangeList129to192=swERPSMgmtRAPSProtectionVlanRangeList129to192, swERPSMgmtRAPSEastPort=swERPSMgmtRAPSEastPort, swERPSMgmtRAPSRingState=swERPSMgmtRAPSRingState, swERPSMgmtRAPSRPLOwnerAdminState=swERPSMgmtRAPSRPLOwnerAdminState, swERPSMgmtRAPSRingMEL=swERPSMgmtRAPSRingMEL, swERPSMgmtRAPSVlanTable=swERPSMgmtRAPSVlanTable, swERPSMgmtRAPSRPLOwnerOperStatus=swERPSMgmtRAPSRPLOwnerOperStatus, swERPSMgmtRAPSVlanEntry=swERPSMgmtRAPSVlanEntry, swERPSMgmtSubRingCtrlTable=swERPSMgmtSubRingCtrlTable, swERPSMgmtSubRingCtrlTCPropagationState=swERPSMgmtSubRingCtrlTCPropagationState, swERPSMgmtRAPSRPLOwnerOperState=swERPSMgmtRAPSRPLOwnerOperState, swERPSMgmtRAPSProtectionVlanRangeList65to128=swERPSMgmtRAPSProtectionVlanRangeList65to128, swERPSLogState=swERPSLogState, swERPSNotify=swERPSNotify, swERPSMgmtRAPSProtectionVlanRangeList193to256=swERPSMgmtRAPSProtectionVlanRangeList193to256, swERPSMgmtRAPSProtectionVlan=swERPSMgmtRAPSProtectionVlan, PYSNMP_MODULE_ID=swERPSMIB, swERPSMgmtRAPSProtectionVlanRangeList257to320=swERPSMgmtRAPSProtectionVlanRangeList257to320, swERPSMgmtRAPSProtectionVlanRangeList385to448=swERPSMgmtRAPSProtectionVlanRangeList385to448, swERPSNotificationBindings=swERPSNotificationBindings, VidList=VidList, swERPSMgmt=swERPSMgmt, swERPSMgmtSubRingCtrlRAPSVlanId=swERPSMgmtSubRingCtrlRAPSVlanId, swERPSMIB=swERPSMIB, swERPSMgmtRAPSHoldOffTime=swERPSMgmtRAPSHoldOffTime, swERPSMgmtRAPSRingAdminState=swERPSMgmtRAPSRingAdminState, swERPSNodeId=swERPSNodeId, swERPSMgmtRAPSEastPortState=swERPSMgmtRAPSEastPortState, swERPSInfo=swERPSInfo, swERPSMgmtRAPSRowStatus=swERPSMgmtRAPSRowStatus, swERPSSFDetectedTrap=swERPSSFDetectedTrap, swERPSAdminState=swERPSAdminState, swERPSTrapState=swERPSTrapState, swERPSNotifyPrefix=swERPSNotifyPrefix, swERPSRPLOwnerConflictTrap=swERPSRPLOwnerConflictTrap, swERPSMgmtRAPSWestPort=swERPSMgmtRAPSWestPort)
