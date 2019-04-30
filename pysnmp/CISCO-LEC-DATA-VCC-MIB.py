#
# PySNMP MIB module CISCO-LEC-DATA-VCC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-LEC-DATA-VCC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:47:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
atmVclVci, atmVclVpi = mibBuilder.importSymbols("ATM-MIB", "atmVclVci", "atmVclVpi")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
AtmLaneAddress, lecIndex = mibBuilder.importSymbols("LAN-EMULATION-CLIENT-MIB", "AtmLaneAddress", "lecIndex")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Bits, ObjectIdentity, Counter64, Integer32, ModuleIdentity, TimeTicks, IpAddress, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "ObjectIdentity", "Counter64", "Integer32", "ModuleIdentity", "TimeTicks", "IpAddress", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoLecDataVccMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 69))
ciscoLecDataVccMIB.setRevisions(('1997-01-06 00:00',))
if mibBuilder.loadTexts: ciscoLecDataVccMIB.setLastUpdated('9701060000Z')
if mibBuilder.loadTexts: ciscoLecDataVccMIB.setOrganization('Cisco Systems, Inc.')
ciscoLecDataVccMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 69, 1))
cLecDataDirectVcc = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 69, 1, 1))
cLecDataDirectVccTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 69, 1, 1, 1), )
if mibBuilder.loadTexts: cLecDataDirectVccTable.setStatus('current')
cLecDataDirectVccEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 69, 1, 1, 1, 1), ).setIndexNames((0, "LAN-EMULATION-CLIENT-MIB", "lecIndex"), (0, "IF-MIB", "ifIndex"), (0, "ATM-MIB", "atmVclVpi"), (0, "ATM-MIB", "atmVclVci"))
if mibBuilder.loadTexts: cLecDataDirectVccEntry.setStatus('current')
cLecDataDirectLocalAtmAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 69, 1, 1, 1, 1, 1), AtmLaneAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLecDataDirectLocalAtmAddress.setStatus('current')
cLecDataDirectRemoteAtmAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 69, 1, 1, 1, 1, 2), AtmLaneAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLecDataDirectRemoteAtmAddress.setStatus('current')
ciscoLecDataVccMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 69, 2))
ciscoLecDataVccMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 69, 2, 0))
ciscoLecDataVccMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 69, 3))
ciscoLecDataVccMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 69, 3, 1))
ciscoLecDataVccMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 69, 3, 2))
ciscoLecDataVccMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 69, 3, 1, 1)).setObjects(("CISCO-LEC-DATA-VCC-MIB", "ciscoLecDataVccBaseMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLecDataVccMIBCompliance = ciscoLecDataVccMIBCompliance.setStatus('current')
ciscoLecDataVccBaseMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 69, 3, 2, 1)).setObjects(("CISCO-LEC-DATA-VCC-MIB", "cLecDataDirectLocalAtmAddress"), ("CISCO-LEC-DATA-VCC-MIB", "cLecDataDirectRemoteAtmAddress"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLecDataVccBaseMIBGroup = ciscoLecDataVccBaseMIBGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-LEC-DATA-VCC-MIB", ciscoLecDataVccMIBGroups=ciscoLecDataVccMIBGroups, cLecDataDirectRemoteAtmAddress=cLecDataDirectRemoteAtmAddress, PYSNMP_MODULE_ID=ciscoLecDataVccMIB, ciscoLecDataVccMIB=ciscoLecDataVccMIB, cLecDataDirectVccTable=cLecDataDirectVccTable, ciscoLecDataVccMIBCompliance=ciscoLecDataVccMIBCompliance, ciscoLecDataVccMIBNotifications=ciscoLecDataVccMIBNotifications, ciscoLecDataVccBaseMIBGroup=ciscoLecDataVccBaseMIBGroup, ciscoLecDataVccMIBConformance=ciscoLecDataVccMIBConformance, cLecDataDirectVcc=cLecDataDirectVcc, cLecDataDirectLocalAtmAddress=cLecDataDirectLocalAtmAddress, ciscoLecDataVccMIBCompliances=ciscoLecDataVccMIBCompliances, ciscoLecDataVccMIBObjects=ciscoLecDataVccMIBObjects, cLecDataDirectVccEntry=cLecDataDirectVccEntry, ciscoLecDataVccMIBNotificationPrefix=ciscoLecDataVccMIBNotificationPrefix)
