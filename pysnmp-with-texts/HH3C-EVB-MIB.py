#
# PySNMP MIB module HH3C-EVB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-EVB-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:26:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
hh3cCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cCommon")
IEEE8021BridgePortNumber, = mibBuilder.importSymbols("IEEE8021-TC-MIB", "IEEE8021BridgePortNumber")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
VlanIndex, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, Unsigned32, TimeTicks, Integer32, Counter64, IpAddress, Bits, Gauge32, ObjectIdentity, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Counter32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Unsigned32", "TimeTicks", "Integer32", "Counter64", "IpAddress", "Bits", "Gauge32", "ObjectIdentity", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Counter32", "NotificationType")
RowStatus, TruthValue, DisplayString, MacAddress, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TruthValue", "DisplayString", "MacAddress", "TextualConvention")
hh3cEvb = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 134))
hh3cEvb.setRevisions(('2012-12-21 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hh3cEvb.setRevisionsDescriptions(('Created by Guo Xiangbin.',))
if mibBuilder.loadTexts: hh3cEvb.setLastUpdated('201212211200Z')
if mibBuilder.loadTexts: hh3cEvb.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
if mibBuilder.loadTexts: hh3cEvb.setContactInfo('Platform Team Hangzhou H3C Tech. Co., Ltd. Haidian District Beijing P.R. China http://www.h3c.com Zip:100085 ')
if mibBuilder.loadTexts: hh3cEvb.setDescription('EVB management information base for managing devices that support Ethernet Virtual Bridging. This MIB is an extension of IEEE8021-EVB-MIB.')
hh3cEvbSysObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 134, 1))
hh3cEvbPortObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 134, 2))
hh3cFlex10Objects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 134, 3))
hh3cEvbSetResult = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 134, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 1), ("processing", 2), ("success", 3), ("failed", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cEvbSetResult.setStatus('current')
if mibBuilder.loadTexts: hh3cEvbSetResult.setDescription('If a set operation on EVB-MIB-tables returns success, this object indicates the actual result of this operation. Otherwise, it is meaningless. unknown: The set operation on the node has been completed, but the result could only be got from the table which the set operation happended. processing: The set operation is in process. Another set operation cannot be performed at this time. success: The set operation has succeeded. failed: The set operation has failed.')
hh3cEvbDefaultManagerTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 134, 1, 2), )
if mibBuilder.loadTexts: hh3cEvbDefaultManagerTable.setStatus('current')
if mibBuilder.loadTexts: hh3cEvbDefaultManagerTable.setDescription('A table that contains configuration information for the default Virtual Station Interface (VSI) manager.')
hh3cEvbDefaultManagerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 134, 1, 2, 1), ).setIndexNames((0, "HH3C-EVB-MIB", "hh3cEvbManagerIndex"))
if mibBuilder.loadTexts: hh3cEvbDefaultManagerEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cEvbDefaultManagerEntry.setDescription('A list of objects containing information for the default VSI manager.')
hh3cEvbManagerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 134, 1, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: hh3cEvbManagerIndex.setStatus('current')
if mibBuilder.loadTexts: hh3cEvbManagerIndex.setDescription('Index of the default manager table.')
hh3cEvbManagerType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 134, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("ipv4", 1), ("ipv6", 2), ("name", 3), ("local", 4)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cEvbManagerType.setStatus('current')
if mibBuilder.loadTexts: hh3cEvbManagerType.setDescription('Type of the default VSI manager. ipv4: Specifies the IPv4 address of the default VSI manager. ipv6: Specifies the IPv6 address of the default VSI manager. name: Specifies the name of the default VSI manager, a case-insensitive string of 1 to 127 characters. local: Specifies the device as the default VSI manager.')
hh3cEvbManagerID = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 134, 1, 2, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 127))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cEvbManagerID.setStatus('current')
if mibBuilder.loadTexts: hh3cEvbManagerID.setDescription("Default VSI manager. The value is zero-length string when the VSI manager type is 'local'.")
hh3cEvbManagerPort = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 134, 1, 2, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(8080)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cEvbManagerPort.setStatus('current')
if mibBuilder.loadTexts: hh3cEvbManagerPort.setDescription("Port number of the default VSI manager. Optional when the VSI manager type is not 'local'. If the VSI manager type is 'local', it returns zero.")
hh3cEvbManagerRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 134, 1, 2, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cEvbManagerRowStatus.setStatus('current')
if mibBuilder.loadTexts: hh3cEvbManagerRowStatus.setDescription('Row status: CreateAndGo, Active, or Destroy.')
hh3cEvbPortConfigTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 134, 2, 1), )
if mibBuilder.loadTexts: hh3cEvbPortConfigTable.setStatus('current')
if mibBuilder.loadTexts: hh3cEvbPortConfigTable.setDescription('A table that contains configuration information for the EVB bridge port.')
hh3cEvbPortConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 134, 2, 1, 1), ).setIndexNames((0, "HH3C-EVB-MIB", "hh3cEvbPortNumber"))
if mibBuilder.loadTexts: hh3cEvbPortConfigEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cEvbPortConfigEntry.setDescription('A list of objects containing information for the EVB bridge port.')
hh3cEvbPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 134, 2, 1, 1, 1), IEEE8021BridgePortNumber())
if mibBuilder.loadTexts: hh3cEvbPortNumber.setStatus('current')
if mibBuilder.loadTexts: hh3cEvbPortNumber.setDescription('Port number.')
hh3cEvbRWD = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 134, 2, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(15, 31)).clone(20)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cEvbRWD.setStatus('current')
if mibBuilder.loadTexts: hh3cEvbRWD.setDescription('VDP resource wait delay exponent.')
hh3cEvbRKA = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 134, 2, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(14, 31)).clone(20)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cEvbRKA.setStatus('current')
if mibBuilder.loadTexts: hh3cEvbRKA.setDescription('VDP keepalive exponent.')
hh3cEvbSchannelConfigTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 134, 2, 2), )
if mibBuilder.loadTexts: hh3cEvbSchannelConfigTable.setStatus('current')
if mibBuilder.loadTexts: hh3cEvbSchannelConfigTable.setDescription('A table that contains configuration information for the S-channel.')
hh3cEvbSchannelConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 134, 2, 2, 1), ).setIndexNames((0, "HH3C-EVB-MIB", "hh3cEvbPortNumber"), (0, "HH3C-EVB-MIB", "hh3cEvbSchannelID"))
if mibBuilder.loadTexts: hh3cEvbSchannelConfigEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cEvbSchannelConfigEntry.setDescription('A list of objects containing information for the S-channel.')
hh3cEvbSchannelID = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 134, 2, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: hh3cEvbSchannelID.setStatus('current')
if mibBuilder.loadTexts: hh3cEvbSchannelID.setDescription('S-channel ID.')
hh3cEvbSchannelSVLAN = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 134, 2, 2, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4094))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cEvbSchannelSVLAN.setStatus('current')
if mibBuilder.loadTexts: hh3cEvbSchannelSVLAN.setDescription('S-VLAN ID. 0 means that the S-channel is not bound to any S-VLAN. 1 represents the SVID for the default S-channel S-channel 1.')
hh3cEvbMacLearningStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 134, 2, 2, 1, 3), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cEvbMacLearningStatus.setStatus('current')
if mibBuilder.loadTexts: hh3cEvbMacLearningStatus.setDescription('The MAC address learning function is enabled or not.')
hh3cEvbRRStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 134, 2, 2, 1, 4), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cEvbRRStatus.setStatus('current')
if mibBuilder.loadTexts: hh3cEvbRRStatus.setDescription('The RR mode for the S-channel is enabled or not.')
hh3cEvbSchannelRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 134, 2, 2, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cEvbSchannelRowStatus.setStatus('current')
if mibBuilder.loadTexts: hh3cEvbSchannelRowStatus.setDescription('Row status: CreateAndGo, Active, or Destroy.')
hh3cEvbVSIConfigTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 134, 2, 3), )
if mibBuilder.loadTexts: hh3cEvbVSIConfigTable.setStatus('current')
if mibBuilder.loadTexts: hh3cEvbVSIConfigTable.setDescription('A table that contains configuration information for the VSI.')
hh3cEvbVSIConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 134, 2, 3, 1), ).setIndexNames((0, "HH3C-EVB-MIB", "hh3cEvbSBPPortNumber"), (0, "HH3C-EVB-MIB", "hh3cEvbVSILocalID"))
if mibBuilder.loadTexts: hh3cEvbVSIConfigEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cEvbVSIConfigEntry.setDescription('A list of objects containing information for the VSI.')
hh3cEvbSBPPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 134, 2, 3, 1, 1), IEEE8021BridgePortNumber())
if mibBuilder.loadTexts: hh3cEvbSBPPortNumber.setStatus('current')
if mibBuilder.loadTexts: hh3cEvbSBPPortNumber.setDescription('The Station-facing Bridge Port (SBP) port number.')
hh3cEvbVSILocalID = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 134, 2, 3, 1, 2), Unsigned32())
if mibBuilder.loadTexts: hh3cEvbVSILocalID.setStatus('current')
if mibBuilder.loadTexts: hh3cEvbVSILocalID.setDescription('VSI local ID.')
hh3cEvbVSICommand = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 134, 2, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("preAssociate", 1), ("preAssociateWithRsrcReservation", 2), ("associate", 3), ("deAssociate", 4)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cEvbVSICommand.setStatus('current')
if mibBuilder.loadTexts: hh3cEvbVSICommand.setDescription('This object indicates the association or pre-associate property of the VSI.')
hh3cEvbVSIIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 134, 2, 3, 1, 4), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cEvbVSIIfIndex.setStatus('current')
if mibBuilder.loadTexts: hh3cEvbVSIIfIndex.setDescription('VSI interface index.')
hh3cEvbVSIIsActive = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 134, 2, 3, 1, 5), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cEvbVSIIsActive.setStatus('current')
if mibBuilder.loadTexts: hh3cEvbVSIIsActive.setDescription('The VSI is activated or not. Activate a VSI after configuring a VSI filter, and deactivate a VSI before removing a VSI filter.')
hh3cEvbVSIRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 134, 2, 3, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cEvbVSIRowStatus.setStatus('current')
if mibBuilder.loadTexts: hh3cEvbVSIRowStatus.setDescription('Row status: CreateAndGo, Active, or Destroy.')
hh3cEvbVSIFilterConfigTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 134, 2, 4), )
if mibBuilder.loadTexts: hh3cEvbVSIFilterConfigTable.setStatus('current')
if mibBuilder.loadTexts: hh3cEvbVSIFilterConfigTable.setDescription('A table that contains configuration information for filters of the VSI.')
hh3cEvbVSIFilterConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 134, 2, 4, 1), ).setIndexNames((0, "HH3C-EVB-MIB", "hh3cEvbSBPPortNumber"), (0, "HH3C-EVB-MIB", "hh3cEvbVSILocalID"), (0, "HH3C-EVB-MIB", "hh3cEvbGroupID"), (0, "HH3C-EVB-MIB", "hh3cEvbVSIMac"), (0, "HH3C-EVB-MIB", "hh3cEvbVSIVlanId"))
if mibBuilder.loadTexts: hh3cEvbVSIFilterConfigEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cEvbVSIFilterConfigEntry.setDescription('A list of objects containing information for filters of the VSI.')
hh3cEvbGroupID = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 134, 2, 4, 1, 1), Unsigned32())
if mibBuilder.loadTexts: hh3cEvbGroupID.setStatus('current')
if mibBuilder.loadTexts: hh3cEvbGroupID.setDescription('Group ID.')
hh3cEvbVSIMac = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 134, 2, 4, 1, 2), MacAddress())
if mibBuilder.loadTexts: hh3cEvbVSIMac.setStatus('current')
if mibBuilder.loadTexts: hh3cEvbVSIMac.setDescription('The MAC address part of the MAC/VLANs for a VSI.')
hh3cEvbVSIVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 134, 2, 4, 1, 3), VlanIndex())
if mibBuilder.loadTexts: hh3cEvbVSIVlanId.setStatus('current')
if mibBuilder.loadTexts: hh3cEvbVSIVlanId.setDescription('The VLAN ID part of the MAC/VLANs for a VSI.')
hh3cEvbVSIFilterRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 134, 2, 4, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cEvbVSIFilterRowStatus.setStatus('current')
if mibBuilder.loadTexts: hh3cEvbVSIFilterRowStatus.setDescription('Row status: CreateAndGo, Active, or Destroy.')
hh3cFlex10PortConfigTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 134, 3, 1), )
if mibBuilder.loadTexts: hh3cFlex10PortConfigTable.setStatus('current')
if mibBuilder.loadTexts: hh3cFlex10PortConfigTable.setDescription('A table that contains configuration information for the flex10 bridge port.')
hh3cFlex10PortConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 134, 3, 1, 1), ).setIndexNames((0, "HH3C-EVB-MIB", "hh3cFlex10PortNumber"))
if mibBuilder.loadTexts: hh3cFlex10PortConfigEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cFlex10PortConfigEntry.setDescription('A list of objects containing information for the flex10 bridge port.')
hh3cFlex10PortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 134, 3, 1, 1, 1), IEEE8021BridgePortNumber())
if mibBuilder.loadTexts: hh3cFlex10PortNumber.setStatus('current')
if mibBuilder.loadTexts: hh3cFlex10PortNumber.setDescription('Port number.')
hh3cFlex10PortEnableStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 134, 3, 1, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cFlex10PortEnableStatus.setStatus('current')
if mibBuilder.loadTexts: hh3cFlex10PortEnableStatus.setDescription('The flex10 function is enabled or not.')
hh3cFlex10RemoteSchannelTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 134, 3, 2), )
if mibBuilder.loadTexts: hh3cFlex10RemoteSchannelTable.setStatus('current')
if mibBuilder.loadTexts: hh3cFlex10RemoteSchannelTable.setDescription('A table that contains remote S-channel details.')
hh3cFlex10RemoteSchannelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 134, 3, 2, 1), ).setIndexNames((0, "HH3C-EVB-MIB", "hh3cFlex10PortNumber"), (0, "HH3C-EVB-MIB", "hh3cEvbSchannelID"))
if mibBuilder.loadTexts: hh3cFlex10RemoteSchannelEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cFlex10RemoteSchannelEntry.setDescription('A list of objects describing remote S-channels.')
hh3cFlex10RemSchDesFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 134, 3, 2, 1, 1), Bits().clone(namedValues=NamedValues(("format0", 0), ("format1", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFlex10RemSchDesFormat.setStatus('current')
if mibBuilder.loadTexts: hh3cFlex10RemSchDesFormat.setDescription('Description format of the remote S-channel.')
hh3cFlex10RemSchTerminationType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 134, 3, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFlex10RemSchTerminationType.setStatus('current')
if mibBuilder.loadTexts: hh3cFlex10RemSchTerminationType.setDescription('Termination type of the remote S-channel. 0: PCI Physical Function (Primary). 1: SRIOV Virtual Function. 2: PCI Physical Function (Secondary). 3: Virtual Switch Port. 4: NCSI Port. 2147483647: This value means a Description TLV with format 0 has not been received. other: Unknown termination type.')
hh3cFlex10RemSchTerminationCap = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 134, 3, 2, 1, 3), Bits().clone(namedValues=NamedValues(("ethernet", 0), ("fCOE", 1), ("iSCSI", 2), ("roCEE", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFlex10RemSchTerminationCap.setStatus('current')
if mibBuilder.loadTexts: hh3cFlex10RemSchTerminationCap.setDescription('Termination capabilities of the remote S-channel. If a Description TLV with format 0 has not been received, it returns all zeros.')
hh3cFlex10RemSchTrafficClass = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 134, 3, 2, 1, 4), Bits().clone(namedValues=NamedValues(("class0", 0), ("class1", 1), ("class2", 2), ("class3", 3), ("class4", 4), ("class5", 5), ("class6", 6), ("class7", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFlex10RemSchTrafficClass.setStatus('current')
if mibBuilder.loadTexts: hh3cFlex10RemSchTrafficClass.setDescription('Traffic classes of the remote S-channel. If a Description TLV with format 0 has not been received, it returns all zeros.')
hh3cFlex10RemSchCir = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 134, 3, 2, 1, 5), Integer32()).setUnits('mbps').setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFlex10RemSchCir.setStatus('current')
if mibBuilder.loadTexts: hh3cFlex10RemSchCir.setDescription('Committed Information Rate (CIR) of the remote S-channel. If a Description TLV with format 0 has not been received, it returns 0.')
hh3cFlex10RemSchPir = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 134, 3, 2, 1, 6), Integer32()).setUnits('mbps').setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFlex10RemSchPir.setStatus('current')
if mibBuilder.loadTexts: hh3cFlex10RemSchPir.setDescription('Peak Information Rate (PIR) of the remote S-channel. If a Description TLV with format 0 has not been received, it returns 0.')
hh3cFlex10RemSchConnectionID = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 134, 3, 2, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFlex10RemSchConnectionID.setStatus('current')
if mibBuilder.loadTexts: hh3cFlex10RemSchConnectionID.setDescription('Connection instance ID of the remote S-channel. The value is a zero-length string if a Description TLV with format 1 has not been received. Otherwise it returns a string with length 16.')
hh3cFlex10SchannelLinkCtlTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 134, 3, 3), )
if mibBuilder.loadTexts: hh3cFlex10SchannelLinkCtlTable.setStatus('current')
if mibBuilder.loadTexts: hh3cFlex10SchannelLinkCtlTable.setDescription('A table that contains link status information for the S-channel.')
hh3cFlex10SchannelLinkCtlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 134, 3, 3, 1), ).setIndexNames((0, "HH3C-EVB-MIB", "hh3cFlex10PortNumber"), (0, "HH3C-EVB-MIB", "hh3cEvbSchannelID"))
if mibBuilder.loadTexts: hh3cFlex10SchannelLinkCtlEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cFlex10SchannelLinkCtlEntry.setDescription('A list of objects containing information for the S-channel.')
hh3cFlex10SchannelSVID = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 134, 3, 3, 1, 1), VlanIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFlex10SchannelSVID.setStatus('current')
if mibBuilder.loadTexts: hh3cFlex10SchannelSVID.setDescription('S-VLAN ID for the S-channel.')
hh3cFlex10SchannelLocalStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 134, 3, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFlex10SchannelLocalStatus.setStatus('current')
if mibBuilder.loadTexts: hh3cFlex10SchannelLocalStatus.setDescription('Link status of the local S-channel.')
hh3cFlex10SchannelRemoteStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 134, 3, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFlex10SchannelRemoteStatus.setStatus('current')
if mibBuilder.loadTexts: hh3cFlex10SchannelRemoteStatus.setDescription('Link status of the remote S-channel.')
mibBuilder.exportSymbols("HH3C-EVB-MIB", hh3cEvb=hh3cEvb, hh3cEvbRRStatus=hh3cEvbRRStatus, hh3cFlex10PortConfigTable=hh3cFlex10PortConfigTable, PYSNMP_MODULE_ID=hh3cEvb, hh3cEvbSysObjects=hh3cEvbSysObjects, hh3cEvbManagerType=hh3cEvbManagerType, hh3cEvbVSIConfigTable=hh3cEvbVSIConfigTable, hh3cFlex10RemoteSchannelEntry=hh3cFlex10RemoteSchannelEntry, hh3cEvbPortConfigTable=hh3cEvbPortConfigTable, hh3cEvbVSILocalID=hh3cEvbVSILocalID, hh3cFlex10PortNumber=hh3cFlex10PortNumber, hh3cFlex10RemSchTerminationType=hh3cFlex10RemSchTerminationType, hh3cFlex10RemSchTrafficClass=hh3cFlex10RemSchTrafficClass, hh3cFlex10RemSchConnectionID=hh3cFlex10RemSchConnectionID, hh3cEvbGroupID=hh3cEvbGroupID, hh3cEvbDefaultManagerTable=hh3cEvbDefaultManagerTable, hh3cEvbVSIVlanId=hh3cEvbVSIVlanId, hh3cFlex10RemSchTerminationCap=hh3cFlex10RemSchTerminationCap, hh3cFlex10SchannelLinkCtlEntry=hh3cFlex10SchannelLinkCtlEntry, hh3cEvbManagerPort=hh3cEvbManagerPort, hh3cFlex10Objects=hh3cFlex10Objects, hh3cEvbRWD=hh3cEvbRWD, hh3cFlex10SchannelSVID=hh3cFlex10SchannelSVID, hh3cFlex10SchannelRemoteStatus=hh3cFlex10SchannelRemoteStatus, hh3cEvbVSIConfigEntry=hh3cEvbVSIConfigEntry, hh3cEvbManagerRowStatus=hh3cEvbManagerRowStatus, hh3cEvbVSIFilterConfigEntry=hh3cEvbVSIFilterConfigEntry, hh3cEvbSchannelRowStatus=hh3cEvbSchannelRowStatus, hh3cEvbPortObjects=hh3cEvbPortObjects, hh3cEvbRKA=hh3cEvbRKA, hh3cEvbVSIFilterRowStatus=hh3cEvbVSIFilterRowStatus, hh3cFlex10PortConfigEntry=hh3cFlex10PortConfigEntry, hh3cFlex10RemSchDesFormat=hh3cFlex10RemSchDesFormat, hh3cEvbVSIFilterConfigTable=hh3cEvbVSIFilterConfigTable, hh3cEvbSchannelConfigEntry=hh3cEvbSchannelConfigEntry, hh3cEvbPortNumber=hh3cEvbPortNumber, hh3cEvbVSIMac=hh3cEvbVSIMac, hh3cFlex10RemoteSchannelTable=hh3cFlex10RemoteSchannelTable, hh3cEvbVSICommand=hh3cEvbVSICommand, hh3cEvbVSIIsActive=hh3cEvbVSIIsActive, hh3cEvbSBPPortNumber=hh3cEvbSBPPortNumber, hh3cEvbSetResult=hh3cEvbSetResult, hh3cEvbPortConfigEntry=hh3cEvbPortConfigEntry, hh3cFlex10PortEnableStatus=hh3cFlex10PortEnableStatus, hh3cEvbVSIRowStatus=hh3cEvbVSIRowStatus, hh3cFlex10RemSchCir=hh3cFlex10RemSchCir, hh3cFlex10SchannelLinkCtlTable=hh3cFlex10SchannelLinkCtlTable, hh3cEvbVSIIfIndex=hh3cEvbVSIIfIndex, hh3cFlex10SchannelLocalStatus=hh3cFlex10SchannelLocalStatus, hh3cEvbSchannelConfigTable=hh3cEvbSchannelConfigTable, hh3cEvbDefaultManagerEntry=hh3cEvbDefaultManagerEntry, hh3cEvbSchannelSVLAN=hh3cEvbSchannelSVLAN, hh3cEvbManagerIndex=hh3cEvbManagerIndex, hh3cFlex10RemSchPir=hh3cFlex10RemSchPir, hh3cEvbMacLearningStatus=hh3cEvbMacLearningStatus, hh3cEvbSchannelID=hh3cEvbSchannelID, hh3cEvbManagerID=hh3cEvbManagerID)
