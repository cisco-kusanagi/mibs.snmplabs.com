#
# PySNMP MIB module HP-ICF-L3MAC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HP-ICF-L3MAC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:21:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
ifRcvAddressEntry, = mibBuilder.importSymbols("IF-MIB", "ifRcvAddressEntry")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter32, ModuleIdentity, Bits, Counter64, TimeTicks, Gauge32, Unsigned32, IpAddress, Integer32, NotificationType, MibIdentifier, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter32", "ModuleIdentity", "Bits", "Counter64", "TimeTicks", "Gauge32", "Unsigned32", "IpAddress", "Integer32", "NotificationType", "MibIdentifier", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hpicfL3MacConfigMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 36))
hpicfL3MacConfigMIB.setRevisions(('2008-10-01 00:00', '2006-08-08 16:00',))
if mibBuilder.loadTexts: hpicfL3MacConfigMIB.setLastUpdated('200810010000Z')
if mibBuilder.loadTexts: hpicfL3MacConfigMIB.setOrganization('HP Networking')
hpicfL3MacConfigObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 36, 1))
hpicfL3MacConfigConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 36, 2))
hpicfL3MacConfigIfTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 36, 1, 1), )
if mibBuilder.loadTexts: hpicfL3MacConfigIfTable.setStatus('current')
hpicfL3MacConfigIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 36, 1, 1, 1), )
ifRcvAddressEntry.registerAugmentions(("HP-ICF-L3MAC-MIB", "hpicfL3MacConfigIfEntry"))
hpicfL3MacConfigIfEntry.setIndexNames(*ifRcvAddressEntry.getIndexNames())
if mibBuilder.loadTexts: hpicfL3MacConfigIfEntry.setStatus('current')
hpicfL3MacConfigIfAdvTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 36, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(60)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfL3MacConfigIfAdvTimer.setStatus('current')
hpicfL3MacConfigMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 36, 2, 1))
hpicfL3MacConfigMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 36, 2, 2))
hpicfL3MacConfigMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 36, 2, 1, 1)).setObjects(("HP-ICF-L3MAC-MIB", "hpicfL3MacConfigGroup"), ("HP-ICF-L3MAC-MIB", "hpicfL3MacConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfL3MacConfigMIBCompliance = hpicfL3MacConfigMIBCompliance.setStatus('current')
hpicfL3MacConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 36, 2, 2, 1)).setObjects(("HP-ICF-L3MAC-MIB", "hpicfL3MacConfigIfAdvTimer"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfL3MacConfigGroup = hpicfL3MacConfigGroup.setStatus('current')
mibBuilder.exportSymbols("HP-ICF-L3MAC-MIB", hpicfL3MacConfigMIBCompliances=hpicfL3MacConfigMIBCompliances, hpicfL3MacConfigIfEntry=hpicfL3MacConfigIfEntry, hpicfL3MacConfigMIB=hpicfL3MacConfigMIB, hpicfL3MacConfigGroup=hpicfL3MacConfigGroup, hpicfL3MacConfigIfAdvTimer=hpicfL3MacConfigIfAdvTimer, hpicfL3MacConfigIfTable=hpicfL3MacConfigIfTable, hpicfL3MacConfigObjects=hpicfL3MacConfigObjects, hpicfL3MacConfigMIBCompliance=hpicfL3MacConfigMIBCompliance, hpicfL3MacConfigMIBGroups=hpicfL3MacConfigMIBGroups, PYSNMP_MODULE_ID=hpicfL3MacConfigMIB, hpicfL3MacConfigConformance=hpicfL3MacConfigConformance)
