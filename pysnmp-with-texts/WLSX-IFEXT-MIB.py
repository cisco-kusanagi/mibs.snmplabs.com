#
# PySNMP MIB module WLSX-IFEXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/WLSX-IFEXT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:36:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
wlsxEnterpriseMibModules, = mibBuilder.importSymbols("ARUBA-MIB", "wlsxEnterpriseMibModules")
ArubaPortMode, ArubaVlanValidRange, ArubaIfType, ArubaPortDuplex, ArubaEnableValue, ArubaDot1dState, ArubaPortType, ArubaPortSpeed, ArubaPoeState, ArubaOperStateValue = mibBuilder.importSymbols("ARUBA-TC", "ArubaPortMode", "ArubaVlanValidRange", "ArubaIfType", "ArubaPortDuplex", "ArubaEnableValue", "ArubaDot1dState", "ArubaPortType", "ArubaPortSpeed", "ArubaPoeState", "ArubaOperStateValue")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Gauge32, ModuleIdentity, iso, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ObjectIdentity, IpAddress, TimeTicks, Unsigned32, Integer32, NotificationType, TextualConvention, MibIdentifier, Counter32, snmpModules = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ModuleIdentity", "iso", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ObjectIdentity", "IpAddress", "TimeTicks", "Unsigned32", "Integer32", "NotificationType", "TextualConvention", "MibIdentifier", "Counter32", "snmpModules")
TimeInterval, TestAndIncr, PhysAddress, TruthValue, RowStatus, MacAddress, TextualConvention, DisplayString, StorageType, TDomain, TAddress = mibBuilder.importSymbols("SNMPv2-TC", "TimeInterval", "TestAndIncr", "PhysAddress", "TruthValue", "RowStatus", "MacAddress", "TextualConvention", "DisplayString", "StorageType", "TDomain", "TAddress")
wlsxIfExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3))
wlsxIfExtMIB.setRevisions(('2012-07-12 00:00', '1910-01-26 18:06',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: wlsxIfExtMIB.setRevisionsDescriptions(('Deprecated wlsxIfExtPortTable and added new table wlsxIfExtNPortTable', 'The initial revision.',))
if mibBuilder.loadTexts: wlsxIfExtMIB.setLastUpdated('201207120000Z')
if mibBuilder.loadTexts: wlsxIfExtMIB.setOrganization('Aruba Wireless Networks')
if mibBuilder.loadTexts: wlsxIfExtMIB.setContactInfo('Postal: 1322 Crossman Avenue Sunnyvale, CA 94089 E-mail: dl-support@arubanetworks.com Phone: +1 408 227 4500')
if mibBuilder.loadTexts: wlsxIfExtMIB.setDescription('This MIB module defines MIB objects which provide System level information about the Aruba controller.')
wlsxIfExtGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1))
wlsxIfExtPortTable = MibTable((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1), )
if mibBuilder.loadTexts: wlsxIfExtPortTable.setStatus('deprecated')
if mibBuilder.loadTexts: wlsxIfExtPortTable.setDescription(' The table of processors contained by the controller. This table is deprecated in favor of wlsxIfExtNPortTable. ')
wlsxIfExtPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1), ).setIndexNames((0, "WLSX-IFEXT-MIB", "ifExtSlotNumber"), (0, "WLSX-IFEXT-MIB", "ifExtPortNumber"))
if mibBuilder.loadTexts: wlsxIfExtPortEntry.setStatus('deprecated')
if mibBuilder.loadTexts: wlsxIfExtPortEntry.setDescription(' An entry for one processor contained by the controller. ')
ifExtSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: ifExtSlotNumber.setStatus('deprecated')
if mibBuilder.loadTexts: ifExtSlotNumber.setDescription(' This object represents the Physical Slot of the Interface. ')
ifExtPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 2), Integer32())
if mibBuilder.loadTexts: ifExtPortNumber.setStatus('deprecated')
if mibBuilder.loadTexts: ifExtPortNumber.setDescription(' This object represents the Physical Port of the Interface. ')
ifExtPortIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifExtPortIfIndex.setStatus('deprecated')
if mibBuilder.loadTexts: ifExtPortIfIndex.setDescription(' This is the ifIndex in ifTable, representing this slot and port. This object is deprecated in favour of ifExtNPortIfIndex. ')
ifExtAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 4), ArubaEnableValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtAdminState.setStatus('deprecated')
if mibBuilder.loadTexts: ifExtAdminState.setDescription(' The desired state of the interface. This object is deprecated in favour of ifExtNAdminState. ')
ifExtOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifExtOperState.setStatus('deprecated')
if mibBuilder.loadTexts: ifExtOperState.setDescription(' The current operational state of the interface. This object is deprecated in favour of ifExtNOperState. ')
ifExtPoeState = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 6), ArubaPoeState()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtPoeState.setStatus('deprecated')
if mibBuilder.loadTexts: ifExtPoeState.setDescription(' The current state of the power over ethernet capability of the port. This object is deprecated in favour of ifExtNPoeState. ')
ifExtIsTrusted = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 7), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtIsTrusted.setStatus('deprecated')
if mibBuilder.loadTexts: ifExtIsTrusted.setDescription(' The object indicates if the port is used in the trusted side of the network or the untrusted side. This object is deprecated in favour of ifExtNIsTrusted. ')
ifExtDot1DState = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 8), ArubaDot1dState()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtDot1DState.setStatus('deprecated')
if mibBuilder.loadTexts: ifExtDot1DState.setDescription(' Current Dot1d state of the Port. If ifExtIsMonitoring is true(1), then this object provides disabled(1) as value. This object is deprecated in favour of ifExtNDot1DState. ')
ifExtMode = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 9), ArubaPortMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtMode.setStatus('deprecated')
if mibBuilder.loadTexts: ifExtMode.setDescription(' This object indicates if the port is in a Trunk mode or access mode. This object provides default switch port value if ifExtIsMonitoring is true(1). This object is deprecated in favour of ifExtNMode. ')
ifExtAccessVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 10), ArubaVlanValidRange()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtAccessVlanId.setStatus('deprecated')
if mibBuilder.loadTexts: ifExtAccessVlanId.setDescription(' The VLAN Id when the port is in Access Mode. This object provides default switch port value if ifExtIsMonitoring is true(1). This object is deprecated in favour of ifExtNAccessVlanId. ')
ifExtTrunkNativeVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 11), ArubaVlanValidRange()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtTrunkNativeVlanId.setStatus('deprecated')
if mibBuilder.loadTexts: ifExtTrunkNativeVlanId.setDescription(' The native VLAN Id of the Port, when the port is in dot1q mode. This object provides default switch port value if ifExtIsMonitoring is true(1). This object is deprecated in favour of ifExtNTrunkNativeVlanId. ')
ifExtTrunkIsAllowedAll = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 12), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtTrunkIsAllowedAll.setStatus('deprecated')
if mibBuilder.loadTexts: ifExtTrunkIsAllowedAll.setDescription(' When the mode of the port is Trunk, this Object indicates if the port is part of all the configured Vlans. This object provides default switch port value if ifExtIsMonitoring is true(1). This object is deprecated in favour of ifExtNTrunkIsAllowedAll. ')
ifExtTrunkAllowedVlanList = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 13), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 512))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtTrunkAllowedVlanList.setStatus('deprecated')
if mibBuilder.loadTexts: ifExtTrunkAllowedVlanList.setDescription(" A string of octets containing one bit per VLAN for a total of 4096 VLANs in the management domain. The most significant bit of the octet string is the lowest value VLAN of 4096 VLANs. By setting the bit(1) we indicate that the vlan is part of the interface. The most significant bit of the bitmap is transmitted first. Note that if the length of this string is less than 512 octets, any 'missing' octets are assumed to contain the value zero. This object provides default switch port value if ifExtIsMonitoring is true(1). This object is deprecated in favour of ifExtNTrunkAllowedVlanList. ")
ifExtIngressACLName = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 14), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtIngressACLName.setStatus('deprecated')
if mibBuilder.loadTexts: ifExtIngressACLName.setDescription(' This object represents the Ingress ACL name applied to the port. An Empty string indicates that there is not ACL applied on this port. This object is deprecated in favour of ifExtNIngressACLName. ')
ifExtEgressACLName = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 15), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtEgressACLName.setStatus('deprecated')
if mibBuilder.loadTexts: ifExtEgressACLName.setDescription(' This object represents the Egress ACL name applied to the port. An Empty string indicates that there is not ACL applied on this port. This object is deprecated in favour of ifExtNEgressACLName. ')
ifExtSessionACLName = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 16), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtSessionACLName.setStatus('deprecated')
if mibBuilder.loadTexts: ifExtSessionACLName.setDescription(' This object represents the Session ACL name applied to the port. An Empty string indicates that there is not ACL applied on this port. This object is deprecated in favour of ifExtNEgressACLName. ')
ifExtXsecVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 17), ArubaVlanValidRange()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtXsecVlan.setStatus('deprecated')
if mibBuilder.loadTexts: ifExtXsecVlan.setDescription(' This object indicates if the port is an Xsec Port. This object is deprecated in favour of ifExtNXsecVlan. ')
ifExtIsMonitoring = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 18), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtIsMonitoring.setStatus('deprecated')
if mibBuilder.loadTexts: ifExtIsMonitoring.setDescription(' This object indicates if the port is used for Port monitoring. When the value of this object is true(1), then below objects provide default switch port values configured on this port. ifExtMode, ifExtAccessVlanId, ifExtTrunkNativeVlanId, ifExtTrunkIsAllowedAll, ifExtTrunkAllowedVlanList This object is deprecated in favour of ifExtNIsMonitoring. ')
ifExtIsMux = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 19), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtIsMux.setStatus('deprecated')
if mibBuilder.loadTexts: ifExtIsMux.setDescription(' This object indicates if the port is used as a MUX Port. This object is deprecated in favour of ifExtNIsMux. ')
ifExtUserSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 20), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifExtUserSlotNumber.setStatus('deprecated')
if mibBuilder.loadTexts: ifExtUserSlotNumber.setDescription(' The user-visible (zero-based) slot number. ')
ifExtUserPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 21), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifExtUserPortNumber.setStatus('deprecated')
if mibBuilder.loadTexts: ifExtUserPortNumber.setDescription(' The user-visible (zero-based) port number. ')
ifExtPortSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 22), ArubaPortSpeed()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifExtPortSpeed.setStatus('deprecated')
if mibBuilder.loadTexts: ifExtPortSpeed.setDescription(' Speed of the Port. This object is deprecated in favour of ifExtNPortSpeed. ')
ifExtPortDuplex = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 23), ArubaPortDuplex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifExtPortDuplex.setStatus('deprecated')
if mibBuilder.loadTexts: ifExtPortDuplex.setDescription(' Duplexity of the Port. This object is deprecated in favour of ifExtNPortDuplex. ')
ifExtPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 24), ArubaPortType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifExtPortType.setStatus('deprecated')
if mibBuilder.loadTexts: ifExtPortType.setDescription(' Type of the Port. This object is deprecated in favour of ifExtNPortType. ')
ifExtDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 25), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifExtDescr.setStatus('deprecated')
if mibBuilder.loadTexts: ifExtDescr.setDescription(' Port Description. This object is deprecated in favour of ifExtNDescr. ')
ifExtUserModuleNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 26), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifExtUserModuleNumber.setStatus('deprecated')
if mibBuilder.loadTexts: ifExtUserModuleNumber.setDescription(' The user-visible (zero-based) module number. ')
wlsxIfExtVlanTable = MibTable((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 2), )
if mibBuilder.loadTexts: wlsxIfExtVlanTable.setStatus('current')
if mibBuilder.loadTexts: wlsxIfExtVlanTable.setDescription(' ')
wlsxIfExtVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 2, 1), ).setIndexNames((0, "WLSX-IFEXT-MIB", "ifExtVlanId"))
if mibBuilder.loadTexts: wlsxIfExtVlanEntry.setStatus('current')
if mibBuilder.loadTexts: wlsxIfExtVlanEntry.setDescription(' An entry for one processor contained by the controller. ')
ifExtVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 2, 1, 1), ArubaVlanValidRange())
if mibBuilder.loadTexts: ifExtVlanId.setStatus('current')
if mibBuilder.loadTexts: ifExtVlanId.setDescription(' This object represents the VLAN Id of the Interface. ')
ifExtVlanName = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ifExtVlanName.setStatus('current')
if mibBuilder.loadTexts: ifExtVlanName.setDescription(' Name of the VLAN. ')
ifExtVlanStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ifExtVlanStatus.setStatus('current')
if mibBuilder.loadTexts: ifExtVlanStatus.setDescription(' A Row status Object used to create/modify the row. ')
wlsxIfExtVlanMemberTable = MibTable((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 3), )
if mibBuilder.loadTexts: wlsxIfExtVlanMemberTable.setStatus('current')
if mibBuilder.loadTexts: wlsxIfExtVlanMemberTable.setDescription(' ')
wlsxIfExtVlanMemberEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 3, 1), ).setIndexNames((0, "WLSX-IFEXT-MIB", "ifExtVlanId"), (0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: wlsxIfExtVlanMemberEntry.setStatus('current')
if mibBuilder.loadTexts: wlsxIfExtVlanMemberEntry.setDescription(' An entry for one processor contained by the controller. ')
ifExtVlanMemberStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 3, 1, 1), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ifExtVlanMemberStatus.setStatus('current')
if mibBuilder.loadTexts: ifExtVlanMemberStatus.setDescription(' A Row status Object used to create/modify and indicate the status row. ')
ifExtVlanMemberSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifExtVlanMemberSlot.setStatus('current')
if mibBuilder.loadTexts: ifExtVlanMemberSlot.setDescription(' The slot index of the slot referred to by this row (1-based). ')
ifExtVlanMemberPort = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifExtVlanMemberPort.setStatus('current')
if mibBuilder.loadTexts: ifExtVlanMemberPort.setDescription(' The slot index of the slot referred to by this row (1-based). ')
ifExtVlanMemberType = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 3, 1, 4), ArubaIfType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifExtVlanMemberType.setStatus('current')
if mibBuilder.loadTexts: ifExtVlanMemberType.setDescription(' The VLAN member type. ')
wlsxIfExtVlanInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 4), )
if mibBuilder.loadTexts: wlsxIfExtVlanInterfaceTable.setStatus('current')
if mibBuilder.loadTexts: wlsxIfExtVlanInterfaceTable.setDescription(' ')
wlsxIfExtVlanInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 4, 1), ).setIndexNames((0, "WLSX-IFEXT-MIB", "ifExtVlanId"))
if mibBuilder.loadTexts: wlsxIfExtVlanInterfaceEntry.setStatus('current')
if mibBuilder.loadTexts: wlsxIfExtVlanInterfaceEntry.setDescription(' An entry for one processor contained by the controller. ')
ifExtVlanInterfaceIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 4, 1, 1), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ifExtVlanInterfaceIfIndex.setStatus('current')
if mibBuilder.loadTexts: ifExtVlanInterfaceIfIndex.setDescription(' This is the ifIndex in ifTable, representing VLAN Interface. ')
ifExtVlanInterfaceDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 4, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ifExtVlanInterfaceDescription.setStatus('current')
if mibBuilder.loadTexts: ifExtVlanInterfaceDescription.setDescription(' This Object indicates the description of the Interface. ')
ifExtVlanInterfaceBWContract = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 4, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ifExtVlanInterfaceBWContract.setStatus('current')
if mibBuilder.loadTexts: ifExtVlanInterfaceBWContract.setDescription(' This Object indicates the Bandwidth contract on the interface. ')
ifExtVlanInterfaceAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 4, 1, 4), ArubaEnableValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ifExtVlanInterfaceAdminState.setStatus('current')
if mibBuilder.loadTexts: ifExtVlanInterfaceAdminState.setDescription(' This Object indicates the administrative state of the Interface. ')
ifExtVlanInterfaceOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 4, 1, 5), ArubaOperStateValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ifExtVlanInterfaceOperState.setStatus('current')
if mibBuilder.loadTexts: ifExtVlanInterfaceOperState.setDescription(' This Object indicates the operational state of the Interface. ')
ifExtVlanInterfaceIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 4, 1, 6), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ifExtVlanInterfaceIpAddress.setStatus('current')
if mibBuilder.loadTexts: ifExtVlanInterfaceIpAddress.setDescription(' This Object indicates the IP Address of the Interface. ')
ifExtVlanInterfaceIpMask = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 4, 1, 7), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ifExtVlanInterfaceIpMask.setStatus('current')
if mibBuilder.loadTexts: ifExtVlanInterfaceIpMask.setDescription(' This Object indicates the subnet mask of the Interface. ')
ifExtVlanInterfaceIsLocalArp = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 4, 1, 8), ArubaEnableValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ifExtVlanInterfaceIsLocalArp.setStatus('current')
if mibBuilder.loadTexts: ifExtVlanInterfaceIsLocalArp.setDescription(' This Object indicates if the Local Arp is set on the Interface. ')
ifExtVlanInterfaceStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 4, 1, 9), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ifExtVlanInterfaceStatus.setStatus('current')
if mibBuilder.loadTexts: ifExtVlanInterfaceStatus.setDescription(' A Row status Object used to create/modify and indicate the status row. ')
ifExtVlanInterfaceIpRouting = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 4, 1, 10), ArubaEnableValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ifExtVlanInterfaceIpRouting.setStatus('current')
if mibBuilder.loadTexts: ifExtVlanInterfaceIpRouting.setDescription(' This Object indicates if the IP routing is set on the Interface. ')
ifExtVlanInterfaceIpNatInside = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 4, 1, 11), ArubaEnableValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ifExtVlanInterfaceIpNatInside.setStatus('current')
if mibBuilder.loadTexts: ifExtVlanInterfaceIpNatInside.setDescription(' This Object indicates if the IP nat inside is set on the Interface. ')
ifExtVlanInterfaceIpIgmpSnooping = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 4, 1, 12), ArubaEnableValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ifExtVlanInterfaceIpIgmpSnooping.setStatus('current')
if mibBuilder.loadTexts: ifExtVlanInterfaceIpIgmpSnooping.setDescription(' This Object indicates if the IP IGMP snooping is set on the Interface. ')
wlsxIfExtNPortTable = MibTable((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5), )
if mibBuilder.loadTexts: wlsxIfExtNPortTable.setStatus('current')
if mibBuilder.loadTexts: wlsxIfExtNPortTable.setDescription(' The table of interface details. ')
wlsxIfExtNPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1), ).setIndexNames((0, "WLSX-IFEXT-MIB", "ifExtNSlotNumber"), (0, "WLSX-IFEXT-MIB", "ifExtNModuleNumber"), (0, "WLSX-IFEXT-MIB", "ifExtNPortNumber"))
if mibBuilder.loadTexts: wlsxIfExtNPortEntry.setStatus('current')
if mibBuilder.loadTexts: wlsxIfExtNPortEntry.setDescription(' An entry in wlsxIfExtNPortTable. ')
ifExtNSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 1), Integer32())
if mibBuilder.loadTexts: ifExtNSlotNumber.setStatus('current')
if mibBuilder.loadTexts: ifExtNSlotNumber.setDescription(' This object represents the user-visible (zero-based) Physical Slot of the Interface. ')
ifExtNModuleNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 2), Integer32())
if mibBuilder.loadTexts: ifExtNModuleNumber.setStatus('current')
if mibBuilder.loadTexts: ifExtNModuleNumber.setDescription(' This object represents the user-visible (zero-based) Physical Module of the Interface. ')
ifExtNPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 3), Integer32())
if mibBuilder.loadTexts: ifExtNPortNumber.setStatus('current')
if mibBuilder.loadTexts: ifExtNPortNumber.setDescription(' This object represents the user-visible (zero-based) Physical Port of the Interface. ')
ifExtNPortIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifExtNPortIfIndex.setStatus('current')
if mibBuilder.loadTexts: ifExtNPortIfIndex.setDescription(' This is the ifIndex in ifTable, representing this slot, module and port. ')
ifExtNAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 5), ArubaEnableValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtNAdminState.setStatus('current')
if mibBuilder.loadTexts: ifExtNAdminState.setDescription(' The desired state of the interface. ')
ifExtNOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifExtNOperState.setStatus('current')
if mibBuilder.loadTexts: ifExtNOperState.setDescription(' The current operational state of the interface. ')
ifExtNPoeState = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 7), ArubaPoeState()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtNPoeState.setStatus('current')
if mibBuilder.loadTexts: ifExtNPoeState.setDescription(' The current state of the power over ethernet capability of the port. ')
ifExtNIsTrusted = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 8), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtNIsTrusted.setStatus('current')
if mibBuilder.loadTexts: ifExtNIsTrusted.setDescription(' The object indicates if the port is used in the trusted side of the network or the untrusted side. ')
ifExtNDot1DState = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 9), ArubaDot1dState()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtNDot1DState.setStatus('current')
if mibBuilder.loadTexts: ifExtNDot1DState.setDescription(' Current Dot1d state of the Port. ')
ifExtNMode = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 10), ArubaPortMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtNMode.setStatus('current')
if mibBuilder.loadTexts: ifExtNMode.setDescription(' This object indicates if the port is in a Trunk mode or access mode. This object provides default switch port value if ifExtIsMonitoring is true(1). ')
ifExtNAccessVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 11), ArubaVlanValidRange()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtNAccessVlanId.setStatus('current')
if mibBuilder.loadTexts: ifExtNAccessVlanId.setDescription(' The VLAN Id when the port is in Access Mode. This object provides default switch port value if ifExtIsMonitoring is true(1). ')
ifExtNTrunkNativeVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 12), ArubaVlanValidRange()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtNTrunkNativeVlanId.setStatus('current')
if mibBuilder.loadTexts: ifExtNTrunkNativeVlanId.setDescription(' The native VLAN Id of the Port, when the port is in dot1q mode. This object provides default switch port value if ifExtIsMonitoring is true(1). ')
ifExtNTrunkIsAllowedAll = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 13), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtNTrunkIsAllowedAll.setStatus('current')
if mibBuilder.loadTexts: ifExtNTrunkIsAllowedAll.setDescription(' When the mode of the port is Trunk, this Object indicates if the port is part of all the configured Vlans. This object provides default switch port value if ifExtIsMonitoring is true(1). ')
ifExtNTrunkAllowedVlanList = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 14), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 512))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtNTrunkAllowedVlanList.setStatus('current')
if mibBuilder.loadTexts: ifExtNTrunkAllowedVlanList.setDescription(" A string of octets containing one bit per VLAN for a total of 4096 VLANs in the management domain. The most significant bit of the octet string is the lowest value VLAN of 4096 VLANs. By setting the bit(1) we indicate that the vlan is part of the interface. The most significant bit of the bitmap is transmitted first. Note that if the length of this string is less than 512 octets, any 'missing' octets are assumed to contain the value zero. This object provides default switch port value if ifExtIsMonitoring is true(1). ")
ifExtNIngressACLName = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 15), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtNIngressACLName.setStatus('current')
if mibBuilder.loadTexts: ifExtNIngressACLName.setDescription(' This object represents the Ingress ACL name applied to the port. An Empty string indicates that there is not ACL applied on this port. ')
ifExtNEgressACLName = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 16), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtNEgressACLName.setStatus('current')
if mibBuilder.loadTexts: ifExtNEgressACLName.setDescription(' This object represents the Egress ACL name applied to the port. An Empty string indicates that there is not ACL applied on this port. ')
ifExtNSessionACLName = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 17), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtNSessionACLName.setStatus('current')
if mibBuilder.loadTexts: ifExtNSessionACLName.setDescription(' This object represents the Session ACL name applied to the port. An Empty string indicates that there is not ACL applied on this port. ')
ifExtNXsecVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 18), ArubaVlanValidRange()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtNXsecVlan.setStatus('current')
if mibBuilder.loadTexts: ifExtNXsecVlan.setDescription(' This object indicates if the port is an Xsec Port. ')
ifExtNIsMonitoring = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 19), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtNIsMonitoring.setStatus('current')
if mibBuilder.loadTexts: ifExtNIsMonitoring.setDescription(' This object indicates if the port is used for Port monitoring. When the value of this object is true(1), then below objects provide default switch port values configured on this port. ifExtNMode, ifExtNAccessVlanId, ifExtNTrunkNativeVlanId, ifExtNTrunkIsAllowedAll, ifExtNTrunkAllowedVlanList ')
ifExtNIsMux = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 20), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtNIsMux.setStatus('current')
if mibBuilder.loadTexts: ifExtNIsMux.setDescription(' This object indicates if the port is used as a MUX Port. ')
ifExtNPortSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 21), ArubaPortSpeed()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifExtNPortSpeed.setStatus('current')
if mibBuilder.loadTexts: ifExtNPortSpeed.setDescription(' Speed of the Port. ')
ifExtNPortDuplex = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 22), ArubaPortDuplex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifExtNPortDuplex.setStatus('current')
if mibBuilder.loadTexts: ifExtNPortDuplex.setDescription(' Duplexity of the Port. ')
ifExtNPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 23), ArubaPortType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifExtNPortType.setStatus('current')
if mibBuilder.loadTexts: ifExtNPortType.setDescription(' Type of the Port. ')
ifExtNDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 24), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifExtNDescr.setStatus('current')
if mibBuilder.loadTexts: ifExtNDescr.setDescription(' Port Description. ')
mibBuilder.exportSymbols("WLSX-IFEXT-MIB", wlsxIfExtPortTable=wlsxIfExtPortTable, ifExtPoeState=ifExtPoeState, ifExtNPortDuplex=ifExtNPortDuplex, ifExtPortIfIndex=ifExtPortIfIndex, ifExtTrunkIsAllowedAll=ifExtTrunkIsAllowedAll, ifExtVlanMemberPort=ifExtVlanMemberPort, ifExtIngressACLName=ifExtIngressACLName, ifExtIsMux=ifExtIsMux, ifExtVlanInterfaceIpAddress=ifExtVlanInterfaceIpAddress, ifExtSessionACLName=ifExtSessionACLName, ifExtIsTrusted=ifExtIsTrusted, ifExtNOperState=ifExtNOperState, ifExtNSlotNumber=ifExtNSlotNumber, ifExtNMode=ifExtNMode, ifExtNSessionACLName=ifExtNSessionACLName, ifExtVlanInterfaceIfIndex=ifExtVlanInterfaceIfIndex, ifExtNIsMux=ifExtNIsMux, ifExtVlanInterfaceStatus=ifExtVlanInterfaceStatus, ifExtMode=ifExtMode, wlsxIfExtVlanMemberTable=wlsxIfExtVlanMemberTable, ifExtVlanInterfaceBWContract=ifExtVlanInterfaceBWContract, wlsxIfExtNPortTable=wlsxIfExtNPortTable, ifExtTrunkNativeVlanId=ifExtTrunkNativeVlanId, ifExtAccessVlanId=ifExtAccessVlanId, ifExtNPortIfIndex=ifExtNPortIfIndex, ifExtNAccessVlanId=ifExtNAccessVlanId, ifExtPortNumber=ifExtPortNumber, ifExtNModuleNumber=ifExtNModuleNumber, ifExtXsecVlan=ifExtXsecVlan, ifExtVlanInterfaceOperState=ifExtVlanInterfaceOperState, ifExtVlanId=ifExtVlanId, ifExtNTrunkNativeVlanId=ifExtNTrunkNativeVlanId, ifExtPortDuplex=ifExtPortDuplex, ifExtTrunkAllowedVlanList=ifExtTrunkAllowedVlanList, ifExtNDescr=ifExtNDescr, ifExtNIngressACLName=ifExtNIngressACLName, wlsxIfExtPortEntry=wlsxIfExtPortEntry, wlsxIfExtVlanInterfaceTable=wlsxIfExtVlanInterfaceTable, ifExtNDot1DState=ifExtNDot1DState, ifExtSlotNumber=ifExtSlotNumber, ifExtNPortNumber=ifExtNPortNumber, ifExtNPortType=ifExtNPortType, ifExtNEgressACLName=ifExtNEgressACLName, ifExtOperState=ifExtOperState, wlsxIfExtVlanTable=wlsxIfExtVlanTable, ifExtNTrunkIsAllowedAll=ifExtNTrunkIsAllowedAll, ifExtVlanInterfaceIpMask=ifExtVlanInterfaceIpMask, ifExtNAdminState=ifExtNAdminState, ifExtVlanMemberType=ifExtVlanMemberType, ifExtUserModuleNumber=ifExtUserModuleNumber, ifExtNIsTrusted=ifExtNIsTrusted, ifExtVlanInterfaceIpRouting=ifExtVlanInterfaceIpRouting, ifExtNPortSpeed=ifExtNPortSpeed, PYSNMP_MODULE_ID=wlsxIfExtMIB, ifExtDot1DState=ifExtDot1DState, ifExtVlanStatus=ifExtVlanStatus, ifExtVlanMemberStatus=ifExtVlanMemberStatus, ifExtUserSlotNumber=ifExtUserSlotNumber, ifExtIsMonitoring=ifExtIsMonitoring, ifExtPortSpeed=ifExtPortSpeed, ifExtVlanInterfaceIpNatInside=ifExtVlanInterfaceIpNatInside, ifExtNXsecVlan=ifExtNXsecVlan, ifExtDescr=ifExtDescr, ifExtNPoeState=ifExtNPoeState, wlsxIfExtGroup=wlsxIfExtGroup, ifExtVlanMemberSlot=ifExtVlanMemberSlot, ifExtVlanInterfaceAdminState=ifExtVlanInterfaceAdminState, ifExtVlanInterfaceIsLocalArp=ifExtVlanInterfaceIsLocalArp, wlsxIfExtVlanEntry=wlsxIfExtVlanEntry, ifExtUserPortNumber=ifExtUserPortNumber, ifExtVlanInterfaceDescription=ifExtVlanInterfaceDescription, wlsxIfExtVlanInterfaceEntry=wlsxIfExtVlanInterfaceEntry, ifExtVlanInterfaceIpIgmpSnooping=ifExtVlanInterfaceIpIgmpSnooping, wlsxIfExtMIB=wlsxIfExtMIB, ifExtNIsMonitoring=ifExtNIsMonitoring, ifExtPortType=ifExtPortType, ifExtEgressACLName=ifExtEgressACLName, ifExtAdminState=ifExtAdminState, wlsxIfExtVlanMemberEntry=wlsxIfExtVlanMemberEntry, wlsxIfExtNPortEntry=wlsxIfExtNPortEntry, ifExtNTrunkAllowedVlanList=ifExtNTrunkAllowedVlanList, ifExtVlanName=ifExtVlanName)
