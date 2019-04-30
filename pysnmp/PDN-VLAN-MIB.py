#
# PySNMP MIB module PDN-VLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PDN-VLAN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:30:58 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
pdn_common, = mibBuilder.importSymbols("PDN-HEADER-MIB", "pdn-common")
VlanIndex, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter32, Counter64, Gauge32, ObjectIdentity, IpAddress, TimeTicks, Bits, ModuleIdentity, Unsigned32, MibIdentifier, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter32", "Counter64", "Gauge32", "ObjectIdentity", "IpAddress", "TimeTicks", "Bits", "ModuleIdentity", "Unsigned32", "MibIdentifier", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
pdnVlanMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 46))
pdnVlanMIB.setRevisions(('2003-11-12 00:00', '2003-04-24 00:00', '2003-04-11 00:00',))
if mibBuilder.loadTexts: pdnVlanMIB.setLastUpdated('200311120000Z')
if mibBuilder.loadTexts: pdnVlanMIB.setOrganization('Paradyne Networks MIB Working Group Other information about group editing the MIB')
pdnVlanNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 46, 0))
pdnVlanObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 46, 1))
pdnVlanAFNs = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 46, 2))
pdnVlanConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 46, 3))
pdnVlanReservedBlockStart = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 46, 1, 1), VlanIndex()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnVlanReservedBlockStart.setStatus('current')
pdnVlanInbandMgmtVlanId = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 46, 1, 2), VlanIndex()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnVlanInbandMgmtVlanId.setStatus('current')
pdnVlanInbandMgmtVlanId2 = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 46, 1, 3), VlanIndex()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnVlanInbandMgmtVlanId2.setStatus('current')
pdnVlanCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 46, 3, 1))
pdnVlanGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 46, 3, 2))
pdnVlanMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 46, 3, 1, 1)).setObjects(("PDN-VLAN-MIB", "pdnVlanReservedBlockGroup"), ("PDN-VLAN-MIB", "pdnVlanInbandMgmtVlanGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnVlanMIBCompliance = pdnVlanMIBCompliance.setStatus('current')
pdnVlanObjGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 46, 3, 2, 1))
pdnVlanAfnGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 46, 3, 2, 2))
pdnVlanNtfyGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 46, 3, 2, 3))
pdnVlanReservedBlockGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 46, 3, 2, 1, 1)).setObjects(("PDN-VLAN-MIB", "pdnVlanReservedBlockStart"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnVlanReservedBlockGroup = pdnVlanReservedBlockGroup.setStatus('current')
pdnVlanInbandMgmtVlanGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 46, 3, 2, 1, 2)).setObjects(("PDN-VLAN-MIB", "pdnVlanInbandMgmtVlanId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnVlanInbandMgmtVlanGroup = pdnVlanInbandMgmtVlanGroup.setStatus('current')
pdnVlanInbandMgmtVlan2Group = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 46, 3, 2, 1, 3)).setObjects(("PDN-VLAN-MIB", "pdnVlanInbandMgmtVlanId"), ("PDN-VLAN-MIB", "pdnVlanInbandMgmtVlanId2"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnVlanInbandMgmtVlan2Group = pdnVlanInbandMgmtVlan2Group.setStatus('current')
mibBuilder.exportSymbols("PDN-VLAN-MIB", pdnVlanGroups=pdnVlanGroups, pdnVlanNotifications=pdnVlanNotifications, pdnVlanCompliances=pdnVlanCompliances, pdnVlanInbandMgmtVlanId2=pdnVlanInbandMgmtVlanId2, pdnVlanInbandMgmtVlanId=pdnVlanInbandMgmtVlanId, pdnVlanConformance=pdnVlanConformance, pdnVlanReservedBlockGroup=pdnVlanReservedBlockGroup, pdnVlanObjects=pdnVlanObjects, pdnVlanAfnGroups=pdnVlanAfnGroups, pdnVlanInbandMgmtVlan2Group=pdnVlanInbandMgmtVlan2Group, PYSNMP_MODULE_ID=pdnVlanMIB, pdnVlanNtfyGroups=pdnVlanNtfyGroups, pdnVlanInbandMgmtVlanGroup=pdnVlanInbandMgmtVlanGroup, pdnVlanMIBCompliance=pdnVlanMIBCompliance, pdnVlanReservedBlockStart=pdnVlanReservedBlockStart, pdnVlanMIB=pdnVlanMIB, pdnVlanObjGroups=pdnVlanObjGroups, pdnVlanAFNs=pdnVlanAFNs)
