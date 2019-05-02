#
# PySNMP MIB module HP-ICF-GENERIC-VLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HP-ICF-GENERIC-VLAN-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:34:05 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
VlanId, dot1qTpFdbEntry = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanId", "dot1qTpFdbEntry")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Integer32, MibIdentifier, IpAddress, TimeTicks, Counter32, Counter64, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ModuleIdentity, NotificationType, ObjectIdentity, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibIdentifier", "IpAddress", "TimeTicks", "Counter32", "Counter64", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ModuleIdentity", "NotificationType", "ObjectIdentity", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hpicfGenericVlanMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 67))
hpicfGenericVlanMIB.setRevisions(('2017-06-28 00:00', '2010-02-08 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hpicfGenericVlanMIB.setRevisionsDescriptions(('Added hpicfDot1qTpFdbInstalledTime object. Added hpicfGenericVlanFeaturesConfGrp1. Added hpicfGenericVlanFeaturesComp1. Deprecated hpicfGenericVlanFeaturesCompliance. Deprecated hpicfGenericVlanFeaturesConfigGroup.', 'The initial revision.',))
if mibBuilder.loadTexts: hpicfGenericVlanMIB.setLastUpdated('201706280000Z')
if mibBuilder.loadTexts: hpicfGenericVlanMIB.setOrganization('HP Networking')
if mibBuilder.loadTexts: hpicfGenericVlanMIB.setContactInfo('Hewlett Packard Company 8000 Foothills Blvd. Roseville, CA 95747')
if mibBuilder.loadTexts: hpicfGenericVlanMIB.setDescription('The MIB module for generic VLAN features')
hpicfGenericVlanFeaturesObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 67, 1))
hpicfGenericVlanFeaturesConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 67, 2))
hpicfGenericVlanFeaturesTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 67, 1, 1), )
if mibBuilder.loadTexts: hpicfGenericVlanFeaturesTable.setStatus('current')
if mibBuilder.loadTexts: hpicfGenericVlanFeaturesTable.setDescription('This table contains objects that are generic to multiple VLAN features, using the same indices as dot1qTpFdbEntry')
hpicfGenericVlanFeaturesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 67, 1, 1, 1), )
dot1qTpFdbEntry.registerAugmentions(("HP-ICF-GENERIC-VLAN-MIB", "hpicfGenericVlanFeaturesEntry"))
hpicfGenericVlanFeaturesEntry.setIndexNames(*dot1qTpFdbEntry.getIndexNames())
if mibBuilder.loadTexts: hpicfGenericVlanFeaturesEntry.setStatus('current')
if mibBuilder.loadTexts: hpicfGenericVlanFeaturesEntry.setDescription('A row in a table, containing the VLAN ID.')
hpicfMacNotifyClearVlanControl = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 67, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noOperation", 1), ("macNotifyClearVlan", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfMacNotifyClearVlanControl.setStatus('current')
if mibBuilder.loadTexts: hpicfMacNotifyClearVlanControl.setDescription('This variable uniquely identifies the operation that will be executed on the object this entry applies to. When read, noOperation(1) should be returned.')
hpicfDot1qTpFdbVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 67, 1, 1, 1, 2), VlanId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfDot1qTpFdbVlanId.setStatus('current')
if mibBuilder.loadTexts: hpicfDot1qTpFdbVlanId.setDescription('The VLAN ID to which this entry belongs.')
hpicfDot1qTpFdbInstalledTime = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 67, 1, 1, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfDot1qTpFdbInstalledTime.setStatus('current')
if mibBuilder.loadTexts: hpicfDot1qTpFdbInstalledTime.setDescription('The time (in hundredths of a second) when the mac-address got installed in Master,with respect to System Up time.')
hpicfGenericVlanFeaturesCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 67, 2, 1))
hpicfGenericVlanFeaturesGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 67, 2, 2))
hpicfGenericVlanFeaturesCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 67, 2, 1, 1)).setObjects(("HP-ICF-GENERIC-VLAN-MIB", "hpicfGenericVlanFeaturesConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfGenericVlanFeaturesCompliance = hpicfGenericVlanFeaturesCompliance.setStatus('deprecated')
if mibBuilder.loadTexts: hpicfGenericVlanFeaturesCompliance.setDescription('The compliance statement for SNMP entities which implement the MAC Notify MIB.')
hpicfGenericVlanFeaturesComp1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 67, 2, 1, 2)).setObjects(("HP-ICF-GENERIC-VLAN-MIB", "hpicfGenericVlanFeaturesConfGrp1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfGenericVlanFeaturesComp1 = hpicfGenericVlanFeaturesComp1.setStatus('current')
if mibBuilder.loadTexts: hpicfGenericVlanFeaturesComp1.setDescription('The compliance statement for SNMP entities which implement the MAC Notify MIB.')
hpicfGenericVlanFeaturesConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 67, 2, 2, 2)).setObjects(("HP-ICF-GENERIC-VLAN-MIB", "hpicfMacNotifyClearVlanControl"), ("HP-ICF-GENERIC-VLAN-MIB", "hpicfDot1qTpFdbVlanId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfGenericVlanFeaturesConfigGroup = hpicfGenericVlanFeaturesConfigGroup.setStatus('deprecated')
if mibBuilder.loadTexts: hpicfGenericVlanFeaturesConfigGroup.setDescription('A collection of objects used for generic VLAN operations.')
hpicfGenericVlanFeaturesConfGrp1 = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 67, 2, 2, 3)).setObjects(("HP-ICF-GENERIC-VLAN-MIB", "hpicfMacNotifyClearVlanControl"), ("HP-ICF-GENERIC-VLAN-MIB", "hpicfDot1qTpFdbVlanId"), ("HP-ICF-GENERIC-VLAN-MIB", "hpicfDot1qTpFdbInstalledTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfGenericVlanFeaturesConfGrp1 = hpicfGenericVlanFeaturesConfGrp1.setStatus('current')
if mibBuilder.loadTexts: hpicfGenericVlanFeaturesConfGrp1.setDescription('A collection of objects used for generic VLAN operations.')
mibBuilder.exportSymbols("HP-ICF-GENERIC-VLAN-MIB", hpicfGenericVlanFeaturesGroups=hpicfGenericVlanFeaturesGroups, hpicfGenericVlanFeaturesConfGrp1=hpicfGenericVlanFeaturesConfGrp1, hpicfDot1qTpFdbVlanId=hpicfDot1qTpFdbVlanId, hpicfGenericVlanFeaturesConfigGroup=hpicfGenericVlanFeaturesConfigGroup, hpicfGenericVlanFeaturesEntry=hpicfGenericVlanFeaturesEntry, hpicfGenericVlanMIB=hpicfGenericVlanMIB, hpicfMacNotifyClearVlanControl=hpicfMacNotifyClearVlanControl, hpicfGenericVlanFeaturesCompliance=hpicfGenericVlanFeaturesCompliance, hpicfGenericVlanFeaturesTable=hpicfGenericVlanFeaturesTable, hpicfDot1qTpFdbInstalledTime=hpicfDot1qTpFdbInstalledTime, hpicfGenericVlanFeaturesObjects=hpicfGenericVlanFeaturesObjects, PYSNMP_MODULE_ID=hpicfGenericVlanMIB, hpicfGenericVlanFeaturesConformance=hpicfGenericVlanFeaturesConformance, hpicfGenericVlanFeaturesCompliances=hpicfGenericVlanFeaturesCompliances, hpicfGenericVlanFeaturesComp1=hpicfGenericVlanFeaturesComp1)
