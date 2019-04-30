#
# PySNMP MIB module CISCO-WAN-PERSISTENT-XGCP-EVENTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-WAN-PERSISTENT-XGCP-EVENTS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:02:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoWan, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWan")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
IpAddress, Counter32, TimeTicks, Gauge32, Unsigned32, MibIdentifier, Bits, iso, ObjectIdentity, Counter64, ModuleIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Counter32", "TimeTicks", "Gauge32", "Unsigned32", "MibIdentifier", "Bits", "iso", "ObjectIdentity", "Counter64", "ModuleIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
ciscoWanPersistentXgcpEventsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 150, 18))
ciscoWanPersistentXgcpEventsMIB.setRevisions(('2003-10-20 00:00',))
if mibBuilder.loadTexts: ciscoWanPersistentXgcpEventsMIB.setLastUpdated('200310200000Z')
if mibBuilder.loadTexts: ciscoWanPersistentXgcpEventsMIB.setOrganization('Cisco Systems, Inc.')
ciscoWanPersistentXgcpEventsMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 18, 1))
persistentXgcpEvents = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 18, 1, 1))
persistentXgcpEventsTable = MibTable((1, 3, 6, 1, 4, 1, 351, 150, 18, 1, 1, 1), )
if mibBuilder.loadTexts: persistentXgcpEventsTable.setStatus('current')
persistentXgcpEventsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 150, 18, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-WAN-PERSISTENT-XGCP-EVENTS-MIB", "persistentXgcpEventNum"))
if mibBuilder.loadTexts: persistentXgcpEventsEntry.setStatus('current')
persistentXgcpEventNum = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 18, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16)))
if mibBuilder.loadTexts: persistentXgcpEventNum.setStatus('current')
persistentXgcpEventName = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 18, 1, 1, 1, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: persistentXgcpEventName.setStatus('current')
persistentXgcpEventRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 18, 1, 1, 1, 1, 3), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: persistentXgcpEventRowStatus.setStatus('current')
persistentXgcpEventsMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 18, 2))
persistentXgcpEventsMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 18, 2, 1))
persistentXgcpEventsMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 18, 2, 2))
persistentXgcpEventsMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 351, 150, 18, 2, 1, 1)).setObjects(("CISCO-WAN-PERSISTENT-XGCP-EVENTS-MIB", "persistentXgcpEventsMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    persistentXgcpEventsMIBCompliance = persistentXgcpEventsMIBCompliance.setStatus('current')
persistentXgcpEventsMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 18, 2, 2, 1)).setObjects(("CISCO-WAN-PERSISTENT-XGCP-EVENTS-MIB", "persistentXgcpEventName"), ("CISCO-WAN-PERSISTENT-XGCP-EVENTS-MIB", "persistentXgcpEventRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    persistentXgcpEventsMIBGroup = persistentXgcpEventsMIBGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-WAN-PERSISTENT-XGCP-EVENTS-MIB", ciscoWanPersistentXgcpEventsMIB=ciscoWanPersistentXgcpEventsMIB, persistentXgcpEventName=persistentXgcpEventName, persistentXgcpEventsMIBConformance=persistentXgcpEventsMIBConformance, persistentXgcpEventsEntry=persistentXgcpEventsEntry, PYSNMP_MODULE_ID=ciscoWanPersistentXgcpEventsMIB, persistentXgcpEventsMIBCompliance=persistentXgcpEventsMIBCompliance, persistentXgcpEventsMIBGroups=persistentXgcpEventsMIBGroups, persistentXgcpEventsTable=persistentXgcpEventsTable, persistentXgcpEventRowStatus=persistentXgcpEventRowStatus, persistentXgcpEventsMIBGroup=persistentXgcpEventsMIBGroup, persistentXgcpEventNum=persistentXgcpEventNum, persistentXgcpEventsMIBCompliances=persistentXgcpEventsMIBCompliances, ciscoWanPersistentXgcpEventsMIBObjects=ciscoWanPersistentXgcpEventsMIBObjects, persistentXgcpEvents=persistentXgcpEvents)
