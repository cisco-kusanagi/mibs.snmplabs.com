#
# PySNMP MIB module PDN-VLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PDN-VLAN-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:39:52 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
pdn_common, = mibBuilder.importSymbols("PDN-HEADER-MIB", "pdn-common")
VlanIndex, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanIndex")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Bits, ObjectIdentity, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Gauge32, IpAddress, MibIdentifier, NotificationType, Integer32, Counter32, TimeTicks, Counter64, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "ObjectIdentity", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Gauge32", "IpAddress", "MibIdentifier", "NotificationType", "Integer32", "Counter32", "TimeTicks", "Counter64", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
pdnVlanMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 46))
pdnVlanMIB.setRevisions(('2003-11-12 00:00', '2003-04-24 00:00', '2003-04-11 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: pdnVlanMIB.setRevisionsDescriptions(('Added a second VlanId for in-band mgmt', 'Changed the compliance/conformance section to be consistent with standard MIBs.', 'Initial release.',))
if mibBuilder.loadTexts: pdnVlanMIB.setLastUpdated('200311120000Z')
if mibBuilder.loadTexts: pdnVlanMIB.setOrganization('Paradyne Networks MIB Working Group Other information about group editing the MIB')
if mibBuilder.loadTexts: pdnVlanMIB.setContactInfo('Paradyne Networks, Inc. 8545 126th Avenue North Largo, FL 33733 www.paradyne.com General Comments to: mibwg_team@paradyne.com Editors Clay Sikes, Jesus A. Pinto')
if mibBuilder.loadTexts: pdnVlanMIB.setDescription('This MIB module contains objects pertaining to VLANs.')
pdnVlanNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 46, 0))
pdnVlanObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 46, 1))
pdnVlanAFNs = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 46, 2))
pdnVlanConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 46, 3))
pdnVlanReservedBlockStart = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 46, 1, 1), VlanIndex()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnVlanReservedBlockStart.setStatus('current')
if mibBuilder.loadTexts: pdnVlanReservedBlockStart.setDescription('This object defines the starting VLAN for a sequential block of VLANS that are to be reserved for internal use. The actual size of the block reserved is not specified as it could be implementation specific. The size of the actual block being reserved should be clearly specified in the SNMP Operational Specification for the particular implementaion.')
pdnVlanInbandMgmtVlanId = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 46, 1, 2), VlanIndex()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnVlanInbandMgmtVlanId.setStatus('current')
if mibBuilder.loadTexts: pdnVlanInbandMgmtVlanId.setDescription('The VLAN ID assigned to the In-Band Management Channel.')
pdnVlanInbandMgmtVlanId2 = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 46, 1, 3), VlanIndex()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnVlanInbandMgmtVlanId2.setStatus('current')
if mibBuilder.loadTexts: pdnVlanInbandMgmtVlanId2.setDescription('The VLAN ID assigned to the second In-Band Management Channel. If the agent does not support a second In-Band Management Channel, it should return NO-SUCH-NAME for the object. *** A VALUE OF 0 IS NOT PERMITTED TO BE RETURNED *** ')
pdnVlanCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 46, 3, 1))
pdnVlanGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 46, 3, 2))
pdnVlanMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 46, 3, 1, 1)).setObjects(("PDN-VLAN-MIB", "pdnVlanReservedBlockGroup"), ("PDN-VLAN-MIB", "pdnVlanInbandMgmtVlanGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnVlanMIBCompliance = pdnVlanMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: pdnVlanMIBCompliance.setDescription('The compliance statement for the pdnVlan entities which implement the pdnVlanMIB.')
pdnVlanObjGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 46, 3, 2, 1))
pdnVlanAfnGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 46, 3, 2, 2))
pdnVlanNtfyGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 46, 3, 2, 3))
pdnVlanReservedBlockGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 46, 3, 2, 1, 1)).setObjects(("PDN-VLAN-MIB", "pdnVlanReservedBlockStart"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnVlanReservedBlockGroup = pdnVlanReservedBlockGroup.setStatus('current')
if mibBuilder.loadTexts: pdnVlanReservedBlockGroup.setDescription('Objects grouped for reserving a block of sequential VLANs.')
pdnVlanInbandMgmtVlanGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 46, 3, 2, 1, 2)).setObjects(("PDN-VLAN-MIB", "pdnVlanInbandMgmtVlanId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnVlanInbandMgmtVlanGroup = pdnVlanInbandMgmtVlanGroup.setStatus('current')
if mibBuilder.loadTexts: pdnVlanInbandMgmtVlanGroup.setDescription('Objects grouped relating to the In-Band Managment VLAN.')
pdnVlanInbandMgmtVlan2Group = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 46, 3, 2, 1, 3)).setObjects(("PDN-VLAN-MIB", "pdnVlanInbandMgmtVlanId"), ("PDN-VLAN-MIB", "pdnVlanInbandMgmtVlanId2"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnVlanInbandMgmtVlan2Group = pdnVlanInbandMgmtVlan2Group.setStatus('current')
if mibBuilder.loadTexts: pdnVlanInbandMgmtVlan2Group.setDescription('Multiples objects grouped relating to the In-Band Managment VLAN.')
mibBuilder.exportSymbols("PDN-VLAN-MIB", pdnVlanObjects=pdnVlanObjects, PYSNMP_MODULE_ID=pdnVlanMIB, pdnVlanMIB=pdnVlanMIB, pdnVlanAFNs=pdnVlanAFNs, pdnVlanReservedBlockStart=pdnVlanReservedBlockStart, pdnVlanMIBCompliance=pdnVlanMIBCompliance, pdnVlanObjGroups=pdnVlanObjGroups, pdnVlanAfnGroups=pdnVlanAfnGroups, pdnVlanInbandMgmtVlanGroup=pdnVlanInbandMgmtVlanGroup, pdnVlanGroups=pdnVlanGroups, pdnVlanConformance=pdnVlanConformance, pdnVlanInbandMgmtVlanId=pdnVlanInbandMgmtVlanId, pdnVlanInbandMgmtVlanId2=pdnVlanInbandMgmtVlanId2, pdnVlanCompliances=pdnVlanCompliances, pdnVlanNotifications=pdnVlanNotifications, pdnVlanNtfyGroups=pdnVlanNtfyGroups, pdnVlanReservedBlockGroup=pdnVlanReservedBlockGroup, pdnVlanInbandMgmtVlan2Group=pdnVlanInbandMgmtVlan2Group)
