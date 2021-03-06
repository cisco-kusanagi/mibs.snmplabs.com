#
# PySNMP MIB module CISCO-UNIFIED-COMPUTING-VERSION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-UNIFIED-COMPUTING-VERSION-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:01:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
Unsigned64, CiscoNetworkAddress, CiscoInetAddressMask, TimeIntervalSec, CiscoAlarmSeverity = mibBuilder.importSymbols("CISCO-TC", "Unsigned64", "CiscoNetworkAddress", "CiscoInetAddressMask", "TimeIntervalSec", "CiscoAlarmSeverity")
CucsManagedObjectId, CucsManagedObjectDn, ciscoUnifiedComputingMIBObjects = mibBuilder.importSymbols("CISCO-UNIFIED-COMPUTING-MIB", "CucsManagedObjectId", "CucsManagedObjectDn", "ciscoUnifiedComputingMIBObjects")
InetAddressIPv4, InetAddressIPv6 = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressIPv4", "InetAddressIPv6")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Counter64, iso, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Gauge32, TimeTicks, Bits, Unsigned32, IpAddress, MibIdentifier, NotificationType, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Counter64", "iso", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Gauge32", "TimeTicks", "Bits", "Unsigned32", "IpAddress", "MibIdentifier", "NotificationType", "ModuleIdentity")
TimeInterval, TruthValue, RowPointer, DateAndTime, TimeStamp, DisplayString, TextualConvention, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "TimeInterval", "TruthValue", "RowPointer", "DateAndTime", "TimeStamp", "DisplayString", "TextualConvention", "MacAddress")
cucsVersionObjects = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 70))
if mibBuilder.loadTexts: cucsVersionObjects.setLastUpdated('201601180000Z')
if mibBuilder.loadTexts: cucsVersionObjects.setOrganization('Cisco Systems Inc.')
cucsVersionApplicationTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 70, 1), )
if mibBuilder.loadTexts: cucsVersionApplicationTable.setStatus('current')
cucsVersionApplicationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 70, 1, 1), ).setIndexNames((0, "CISCO-UNIFIED-COMPUTING-VERSION-MIB", "cucsVersionApplicationInstanceId"))
if mibBuilder.loadTexts: cucsVersionApplicationEntry.setStatus('current')
cucsVersionApplicationInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 70, 1, 1, 1), CucsManagedObjectId())
if mibBuilder.loadTexts: cucsVersionApplicationInstanceId.setStatus('current')
cucsVersionApplicationDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 70, 1, 1, 2), CucsManagedObjectDn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsVersionApplicationDn.setStatus('current')
cucsVersionApplicationRn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 70, 1, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsVersionApplicationRn.setStatus('current')
cucsVersionApplicationDetail = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 70, 1, 1, 4), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsVersionApplicationDetail.setStatus('current')
cucsVersionApplicationTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 70, 1, 1, 5), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsVersionApplicationTime.setStatus('current')
cucsVersionApplicationVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 70, 1, 1, 6), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsVersionApplicationVersion.setStatus('current')
cucsVersionEpTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 70, 2), )
if mibBuilder.loadTexts: cucsVersionEpTable.setStatus('current')
cucsVersionEpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 70, 2, 1), ).setIndexNames((0, "CISCO-UNIFIED-COMPUTING-VERSION-MIB", "cucsVersionEpInstanceId"))
if mibBuilder.loadTexts: cucsVersionEpEntry.setStatus('current')
cucsVersionEpInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 70, 2, 1, 1), CucsManagedObjectId())
if mibBuilder.loadTexts: cucsVersionEpInstanceId.setStatus('current')
cucsVersionEpDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 70, 2, 1, 2), CucsManagedObjectDn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsVersionEpDn.setStatus('current')
cucsVersionEpRn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 70, 2, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsVersionEpRn.setStatus('current')
mibBuilder.exportSymbols("CISCO-UNIFIED-COMPUTING-VERSION-MIB", cucsVersionApplicationRn=cucsVersionApplicationRn, cucsVersionEpInstanceId=cucsVersionEpInstanceId, cucsVersionApplicationTable=cucsVersionApplicationTable, cucsVersionApplicationVersion=cucsVersionApplicationVersion, cucsVersionEpEntry=cucsVersionEpEntry, cucsVersionApplicationTime=cucsVersionApplicationTime, cucsVersionEpTable=cucsVersionEpTable, cucsVersionApplicationInstanceId=cucsVersionApplicationInstanceId, cucsVersionEpRn=cucsVersionEpRn, cucsVersionEpDn=cucsVersionEpDn, cucsVersionObjects=cucsVersionObjects, PYSNMP_MODULE_ID=cucsVersionObjects, cucsVersionApplicationDetail=cucsVersionApplicationDetail, cucsVersionApplicationEntry=cucsVersionApplicationEntry, cucsVersionApplicationDn=cucsVersionApplicationDn)
