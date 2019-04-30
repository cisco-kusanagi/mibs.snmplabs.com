#
# PySNMP MIB module HP-ICF-GENERIC-VLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HP-ICF-GENERIC-VLAN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:21:28 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
dot1qTpFdbEntry, VlanId = mibBuilder.importSymbols("Q-BRIDGE-MIB", "dot1qTpFdbEntry", "VlanId")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
iso, Counter32, TimeTicks, NotificationType, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Integer32, Gauge32, ObjectIdentity, IpAddress, ModuleIdentity, Counter64, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter32", "TimeTicks", "NotificationType", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Integer32", "Gauge32", "ObjectIdentity", "IpAddress", "ModuleIdentity", "Counter64", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hpicfGenericVlanMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 67))
hpicfGenericVlanMIB.setRevisions(('2017-06-28 00:00', '2010-02-08 00:00',))
if mibBuilder.loadTexts: hpicfGenericVlanMIB.setLastUpdated('201706280000Z')
if mibBuilder.loadTexts: hpicfGenericVlanMIB.setOrganization('HP Networking')
hpicfGenericVlanFeaturesObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 67, 1))
hpicfGenericVlanFeaturesConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 67, 2))
hpicfGenericVlanFeaturesTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 67, 1, 1), )
if mibBuilder.loadTexts: hpicfGenericVlanFeaturesTable.setStatus('current')
hpicfGenericVlanFeaturesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 67, 1, 1, 1), )
dot1qTpFdbEntry.registerAugmentions(("HP-ICF-GENERIC-VLAN-MIB", "hpicfGenericVlanFeaturesEntry"))
hpicfGenericVlanFeaturesEntry.setIndexNames(*dot1qTpFdbEntry.getIndexNames())
if mibBuilder.loadTexts: hpicfGenericVlanFeaturesEntry.setStatus('current')
hpicfMacNotifyClearVlanControl = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 67, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noOperation", 1), ("macNotifyClearVlan", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfMacNotifyClearVlanControl.setStatus('current')
hpicfDot1qTpFdbVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 67, 1, 1, 1, 2), VlanId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfDot1qTpFdbVlanId.setStatus('current')
hpicfDot1qTpFdbInstalledTime = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 67, 1, 1, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfDot1qTpFdbInstalledTime.setStatus('current')
hpicfGenericVlanFeaturesCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 67, 2, 1))
hpicfGenericVlanFeaturesGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 67, 2, 2))
hpicfGenericVlanFeaturesCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 67, 2, 1, 1)).setObjects(("HP-ICF-GENERIC-VLAN-MIB", "hpicfGenericVlanFeaturesConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfGenericVlanFeaturesCompliance = hpicfGenericVlanFeaturesCompliance.setStatus('deprecated')
hpicfGenericVlanFeaturesComp1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 67, 2, 1, 2)).setObjects(("HP-ICF-GENERIC-VLAN-MIB", "hpicfGenericVlanFeaturesConfGrp1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfGenericVlanFeaturesComp1 = hpicfGenericVlanFeaturesComp1.setStatus('current')
hpicfGenericVlanFeaturesConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 67, 2, 2, 2)).setObjects(("HP-ICF-GENERIC-VLAN-MIB", "hpicfMacNotifyClearVlanControl"), ("HP-ICF-GENERIC-VLAN-MIB", "hpicfDot1qTpFdbVlanId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfGenericVlanFeaturesConfigGroup = hpicfGenericVlanFeaturesConfigGroup.setStatus('deprecated')
hpicfGenericVlanFeaturesConfGrp1 = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 67, 2, 2, 3)).setObjects(("HP-ICF-GENERIC-VLAN-MIB", "hpicfMacNotifyClearVlanControl"), ("HP-ICF-GENERIC-VLAN-MIB", "hpicfDot1qTpFdbVlanId"), ("HP-ICF-GENERIC-VLAN-MIB", "hpicfDot1qTpFdbInstalledTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfGenericVlanFeaturesConfGrp1 = hpicfGenericVlanFeaturesConfGrp1.setStatus('current')
mibBuilder.exportSymbols("HP-ICF-GENERIC-VLAN-MIB", hpicfGenericVlanMIB=hpicfGenericVlanMIB, hpicfDot1qTpFdbVlanId=hpicfDot1qTpFdbVlanId, hpicfDot1qTpFdbInstalledTime=hpicfDot1qTpFdbInstalledTime, hpicfGenericVlanFeaturesConfigGroup=hpicfGenericVlanFeaturesConfigGroup, PYSNMP_MODULE_ID=hpicfGenericVlanMIB, hpicfGenericVlanFeaturesGroups=hpicfGenericVlanFeaturesGroups, hpicfMacNotifyClearVlanControl=hpicfMacNotifyClearVlanControl, hpicfGenericVlanFeaturesCompliances=hpicfGenericVlanFeaturesCompliances, hpicfGenericVlanFeaturesTable=hpicfGenericVlanFeaturesTable, hpicfGenericVlanFeaturesComp1=hpicfGenericVlanFeaturesComp1, hpicfGenericVlanFeaturesConfGrp1=hpicfGenericVlanFeaturesConfGrp1, hpicfGenericVlanFeaturesCompliance=hpicfGenericVlanFeaturesCompliance, hpicfGenericVlanFeaturesEntry=hpicfGenericVlanFeaturesEntry, hpicfGenericVlanFeaturesConformance=hpicfGenericVlanFeaturesConformance, hpicfGenericVlanFeaturesObjects=hpicfGenericVlanFeaturesObjects)
