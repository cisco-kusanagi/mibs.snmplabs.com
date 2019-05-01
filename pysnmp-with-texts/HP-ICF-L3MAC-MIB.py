#
# PySNMP MIB module HP-ICF-L3MAC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HP-ICF-L3MAC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:34:31 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
ifRcvAddressEntry, = mibBuilder.importSymbols("IF-MIB", "ifRcvAddressEntry")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Bits, Integer32, ModuleIdentity, Counter64, MibIdentifier, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Gauge32, IpAddress, ObjectIdentity, NotificationType, iso, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "ModuleIdentity", "Counter64", "MibIdentifier", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Gauge32", "IpAddress", "ObjectIdentity", "NotificationType", "iso", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hpicfL3MacConfigMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 36))
hpicfL3MacConfigMIB.setRevisions(('2008-10-01 00:00', '2006-08-08 16:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hpicfL3MacConfigMIB.setRevisionsDescriptions(('Added hpSwitch reference to imports section.', 'Initial version.',))
if mibBuilder.loadTexts: hpicfL3MacConfigMIB.setLastUpdated('200810010000Z')
if mibBuilder.loadTexts: hpicfL3MacConfigMIB.setOrganization('HP Networking')
if mibBuilder.loadTexts: hpicfL3MacConfigMIB.setContactInfo('Hewlett Packard Company 8000 Foothills Blvd. Roseville, CA 95747')
if mibBuilder.loadTexts: hpicfL3MacConfigMIB.setDescription('This MIB module describes extension objects to the per-interface MAC address configuration for devices in the HP Integrated Communication Facility product line.')
hpicfL3MacConfigObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 36, 1))
hpicfL3MacConfigConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 36, 2))
hpicfL3MacConfigIfTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 36, 1, 1), )
if mibBuilder.loadTexts: hpicfL3MacConfigIfTable.setStatus('current')
if mibBuilder.loadTexts: hpicfL3MacConfigIfTable.setDescription('This table contains l3-mac configuration information of each vlan interface.')
hpicfL3MacConfigIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 36, 1, 1, 1), )
ifRcvAddressEntry.registerAugmentions(("HP-ICF-L3MAC-MIB", "hpicfL3MacConfigIfEntry"))
hpicfL3MacConfigIfEntry.setIndexNames(*ifRcvAddressEntry.getIndexNames())
if mibBuilder.loadTexts: hpicfL3MacConfigIfEntry.setStatus('current')
if mibBuilder.loadTexts: hpicfL3MacConfigIfEntry.setDescription('An entry in the hpicfL3MacConfigIfEntry contains the l3-mac feature specific configuration information. This table augments the ifRcvAddressTable.')
hpicfL3MacConfigIfAdvTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 36, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(60)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfL3MacConfigIfAdvTimer.setStatus('current')
if mibBuilder.loadTexts: hpicfL3MacConfigIfAdvTimer.setDescription('Timeout in seconds when an advertisement packets will be sent out with the ifRcvAddressAddress of this entry as the source MAC so that the downstream switches learn this MAC-address.')
hpicfL3MacConfigMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 36, 2, 1))
hpicfL3MacConfigMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 36, 2, 2))
hpicfL3MacConfigMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 36, 2, 1, 1)).setObjects(("HP-ICF-L3MAC-MIB", "hpicfL3MacConfigGroup"), ("HP-ICF-L3MAC-MIB", "hpicfL3MacConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfL3MacConfigMIBCompliance = hpicfL3MacConfigMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: hpicfL3MacConfigMIBCompliance.setDescription('The compliance statement for HP routers running L3-Mac feature and implementing the HP-ICF-L3MAC-MIB.')
hpicfL3MacConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 36, 2, 2, 1)).setObjects(("HP-ICF-L3MAC-MIB", "hpicfL3MacConfigIfAdvTimer"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfL3MacConfigGroup = hpicfL3MacConfigGroup.setStatus('current')
if mibBuilder.loadTexts: hpicfL3MacConfigGroup.setDescription('A collection of HP proprietary objects to support L3-Mac feature on HP routers.')
mibBuilder.exportSymbols("HP-ICF-L3MAC-MIB", hpicfL3MacConfigIfTable=hpicfL3MacConfigIfTable, hpicfL3MacConfigIfEntry=hpicfL3MacConfigIfEntry, hpicfL3MacConfigMIBGroups=hpicfL3MacConfigMIBGroups, hpicfL3MacConfigGroup=hpicfL3MacConfigGroup, hpicfL3MacConfigMIB=hpicfL3MacConfigMIB, hpicfL3MacConfigObjects=hpicfL3MacConfigObjects, hpicfL3MacConfigConformance=hpicfL3MacConfigConformance, hpicfL3MacConfigMIBCompliance=hpicfL3MacConfigMIBCompliance, hpicfL3MacConfigIfAdvTimer=hpicfL3MacConfigIfAdvTimer, PYSNMP_MODULE_ID=hpicfL3MacConfigMIB, hpicfL3MacConfigMIBCompliances=hpicfL3MacConfigMIBCompliances)
