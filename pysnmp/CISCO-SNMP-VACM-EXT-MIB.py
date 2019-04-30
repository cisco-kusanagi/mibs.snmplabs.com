#
# PySNMP MIB module CISCO-SNMP-VACM-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-SNMP-VACM-EXT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:55:56 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
vacmSecurityModel, vacmSecurityName = mibBuilder.importSymbols("SNMP-VIEW-BASED-ACM-MIB", "vacmSecurityModel", "vacmSecurityName")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
TimeTicks, ObjectIdentity, Unsigned32, IpAddress, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, NotificationType, Gauge32, Bits, Counter32, MibIdentifier, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ObjectIdentity", "Unsigned32", "IpAddress", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "NotificationType", "Gauge32", "Bits", "Counter32", "MibIdentifier", "Integer32", "iso")
RowStatus, DisplayString, StorageType, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "StorageType", "TextualConvention")
ciscoSnmpVacmExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 409))
ciscoSnmpVacmExtMIB.setRevisions(('2004-05-19 00:00',))
if mibBuilder.loadTexts: ciscoSnmpVacmExtMIB.setLastUpdated('200405190000Z')
if mibBuilder.loadTexts: ciscoSnmpVacmExtMIB.setOrganization('Cisco Systems, Inc.')
ciscoSnmpVacmExtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 409, 1))
ciscoSnmpVacmExtMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 409, 2))
cvacmSecurityToGroupTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 409, 1, 1), )
if mibBuilder.loadTexts: cvacmSecurityToGroupTable.setStatus('current')
cvacmSecurityToGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 409, 1, 1, 1), ).setIndexNames((0, "SNMP-VIEW-BASED-ACM-MIB", "vacmSecurityModel"), (0, "SNMP-VIEW-BASED-ACM-MIB", "vacmSecurityName"), (0, "CISCO-SNMP-VACM-EXT-MIB", "cvacmSecurityGrpName"))
if mibBuilder.loadTexts: cvacmSecurityToGroupEntry.setStatus('current')
cvacmSecurityGrpName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 409, 1, 1, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: cvacmSecurityGrpName.setStatus('current')
cvacmSecurityGrpStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 409, 1, 1, 1, 2), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvacmSecurityGrpStorageType.setStatus('current')
cvacmSecurityGrpStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 409, 1, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvacmSecurityGrpStatus.setStatus('current')
ciscoSnmpVacmExtMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 409, 2, 1))
ciscoSnmpVacmExtMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 409, 2, 2))
ciscoSnmpVacmExtMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 409, 2, 1, 1)).setObjects(("CISCO-SNMP-VACM-EXT-MIB", "ciscoSnmpVacmExtGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpVacmExtMIBCompliance = ciscoSnmpVacmExtMIBCompliance.setStatus('current')
ciscoSnmpVacmExtGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 409, 2, 2, 1)).setObjects(("CISCO-SNMP-VACM-EXT-MIB", "cvacmSecurityGrpStorageType"), ("CISCO-SNMP-VACM-EXT-MIB", "cvacmSecurityGrpStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpVacmExtGroup = ciscoSnmpVacmExtGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-SNMP-VACM-EXT-MIB", cvacmSecurityToGroupTable=cvacmSecurityToGroupTable, PYSNMP_MODULE_ID=ciscoSnmpVacmExtMIB, ciscoSnmpVacmExtMIBObjects=ciscoSnmpVacmExtMIBObjects, cvacmSecurityGrpStorageType=cvacmSecurityGrpStorageType, ciscoSnmpVacmExtMIB=ciscoSnmpVacmExtMIB, ciscoSnmpVacmExtMIBCompliance=ciscoSnmpVacmExtMIBCompliance, cvacmSecurityGrpStatus=cvacmSecurityGrpStatus, ciscoSnmpVacmExtMIBGroups=ciscoSnmpVacmExtMIBGroups, ciscoSnmpVacmExtGroup=ciscoSnmpVacmExtGroup, ciscoSnmpVacmExtMIBCompliances=ciscoSnmpVacmExtMIBCompliances, cvacmSecurityToGroupEntry=cvacmSecurityToGroupEntry, cvacmSecurityGrpName=cvacmSecurityGrpName, ciscoSnmpVacmExtMIBConformance=ciscoSnmpVacmExtMIBConformance)
