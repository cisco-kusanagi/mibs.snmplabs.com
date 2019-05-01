#
# PySNMP MIB module CISCO-IMAGE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IMAGE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:01:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, Counter32, Bits, ObjectIdentity, Gauge32, IpAddress, NotificationType, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter64, Unsigned32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Counter32", "Bits", "ObjectIdentity", "Gauge32", "IpAddress", "NotificationType", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter64", "Unsigned32", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoImageMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 25))
ciscoImageMIB.setRevisions(('1995-08-15 00:00', '1995-01-16 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoImageMIB.setRevisionsDescriptions(('Specify a correct (non-negative) range for an index object.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoImageMIB.setLastUpdated('9508150000Z')
if mibBuilder.loadTexts: ciscoImageMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoImageMIB.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoImageMIB.setDescription('Router image MIB which identify the capabilities and characteristics of the image')
ciscoImageMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 25, 1))
ciscoImageTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 25, 1, 1), )
if mibBuilder.loadTexts: ciscoImageTable.setStatus('current')
if mibBuilder.loadTexts: ciscoImageTable.setDescription('A table provides content information describing the executing IOS image.')
ciscoImageEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 25, 1, 1, 1), ).setIndexNames((0, "CISCO-IMAGE-MIB", "ciscoImageIndex"))
if mibBuilder.loadTexts: ciscoImageEntry.setStatus('current')
if mibBuilder.loadTexts: ciscoImageEntry.setDescription('A image characteristic string entry.')
ciscoImageIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 25, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: ciscoImageIndex.setStatus('current')
if mibBuilder.loadTexts: ciscoImageIndex.setDescription('A sequence number for each string stored in the IOS image.')
ciscoImageString = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 25, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoImageString.setStatus('current')
if mibBuilder.loadTexts: ciscoImageString.setDescription('The string of this entry.')
ciscoImageMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 25, 2))
ciscoImageMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 25, 2, 1))
ciscoImageMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 25, 2, 2))
ciscoImageMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 25, 2, 1, 1)).setObjects(("CISCO-IMAGE-MIB", "ciscoImageMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoImageMIBCompliance = ciscoImageMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoImageMIBCompliance.setDescription('The compliance statement for entities which implement the Cisco Image MIB')
ciscoImageMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 25, 2, 2, 1)).setObjects(("CISCO-IMAGE-MIB", "ciscoImageString"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoImageMIBGroup = ciscoImageMIBGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoImageMIBGroup.setDescription('A collection of objects providing IOS image characteristics')
mibBuilder.exportSymbols("CISCO-IMAGE-MIB", ciscoImageMIBCompliances=ciscoImageMIBCompliances, ciscoImageTable=ciscoImageTable, ciscoImageString=ciscoImageString, ciscoImageIndex=ciscoImageIndex, ciscoImageMIB=ciscoImageMIB, ciscoImageMIBCompliance=ciscoImageMIBCompliance, ciscoImageEntry=ciscoImageEntry, ciscoImageMIBObjects=ciscoImageMIBObjects, ciscoImageMIBGroup=ciscoImageMIBGroup, ciscoImageMIBGroups=ciscoImageMIBGroups, PYSNMP_MODULE_ID=ciscoImageMIB, ciscoImageMIBConformance=ciscoImageMIBConformance)
