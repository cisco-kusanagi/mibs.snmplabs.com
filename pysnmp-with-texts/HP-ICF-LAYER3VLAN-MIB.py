#
# PySNMP MIB module HP-ICF-LAYER3VLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HP-ICF-LAYER3VLAN-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:34:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
NotificationType, ModuleIdentity, Unsigned32, TimeTicks, Integer32, Bits, IpAddress, Gauge32, iso, ObjectIdentity, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ModuleIdentity", "Unsigned32", "TimeTicks", "Integer32", "Bits", "IpAddress", "Gauge32", "iso", "ObjectIdentity", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hpicfLayer3VlanConfigMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 70))
hpicfLayer3VlanConfigMIB.setRevisions(('2010-03-23 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hpicfLayer3VlanConfigMIB.setRevisionsDescriptions(('Initial version.',))
if mibBuilder.loadTexts: hpicfLayer3VlanConfigMIB.setLastUpdated('201003230000Z')
if mibBuilder.loadTexts: hpicfLayer3VlanConfigMIB.setOrganization('HP Networking')
if mibBuilder.loadTexts: hpicfLayer3VlanConfigMIB.setContactInfo('Hewlett Packard Company 8000 Foothills Blvd. Roseville, CA 95747')
if mibBuilder.loadTexts: hpicfLayer3VlanConfigMIB.setDescription('This MIB module describes objects to enable/disable layer 3 interface on a VLAN for devices in the HP Integrated Communication Facility product line.')
hpicfLayer3VlanConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 70, 1))
hpicfLayer3VlanConfigConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 70, 2))
hpicfLayer3VlanConfigTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 70, 1, 1), )
if mibBuilder.loadTexts: hpicfLayer3VlanConfigTable.setStatus('current')
if mibBuilder.loadTexts: hpicfLayer3VlanConfigTable.setDescription('This table contains layer 3 adminStatus configuration information for each VLAN interface.')
hpicfLayer3VlanConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 70, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hpicfLayer3VlanConfigEntry.setStatus('current')
if mibBuilder.loadTexts: hpicfLayer3VlanConfigEntry.setDescription('An entry in the hpicfLayer3VlanConfigEntry contains objects for configuring layer 3 adminStatus for a VLAN interface.')
hpicfLayer3VlanStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 70, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfLayer3VlanStatus.setStatus('current')
if mibBuilder.loadTexts: hpicfLayer3VlanStatus.setDescription("The object contains the desired adminStatus of layer 3 on a VLAN. If set to 'enable' then layer 3(IPv4/IPv6) is enabled on that VLAN. If set to 'disable' then layer 3 is disabled on that VLAN.")
hpicfL3VlanConfigMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 70, 2, 1))
hpicfLayer3VlanConfigMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 70, 2, 2))
hpicfL3VlanConfigMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 70, 2, 1, 1)).setObjects(("HP-ICF-LAYER3VLAN-MIB", "hpicfLayer3VlanConfigGroup"), ("HP-ICF-LAYER3VLAN-MIB", "hpicfLayer3VlanConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfL3VlanConfigMIBCompliance = hpicfL3VlanConfigMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: hpicfL3VlanConfigMIBCompliance.setDescription("The compliance statement for HP routers having layer 3 enable/disable of 'All VLANs' feature and implementing the HP-ICF-LAYER3VLAN-MIB.")
hpicfLayer3VlanConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 70, 2, 2, 1)).setObjects(("HP-ICF-LAYER3VLAN-MIB", "hpicfLayer3VlanStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfLayer3VlanConfigGroup = hpicfLayer3VlanConfigGroup.setStatus('current')
if mibBuilder.loadTexts: hpicfLayer3VlanConfigGroup.setDescription('A collection of HP proprietary objects to support enabling/disabling layer 3 on VLANs on HP routers.')
mibBuilder.exportSymbols("HP-ICF-LAYER3VLAN-MIB", hpicfLayer3VlanConfigMIB=hpicfLayer3VlanConfigMIB, PYSNMP_MODULE_ID=hpicfLayer3VlanConfigMIB, hpicfL3VlanConfigMIBCompliance=hpicfL3VlanConfigMIBCompliance, hpicfLayer3VlanStatus=hpicfLayer3VlanStatus, hpicfLayer3VlanConfigMIBGroups=hpicfLayer3VlanConfigMIBGroups, hpicfL3VlanConfigMIBCompliances=hpicfL3VlanConfigMIBCompliances, hpicfLayer3VlanConfigGroup=hpicfLayer3VlanConfigGroup, hpicfLayer3VlanConfigTable=hpicfLayer3VlanConfigTable, hpicfLayer3VlanConfigConformance=hpicfLayer3VlanConfigConformance, hpicfLayer3VlanConfigEntry=hpicfLayer3VlanConfigEntry, hpicfLayer3VlanConfig=hpicfLayer3VlanConfig)
