#
# PySNMP MIB module CISCO-SNMP-VACM-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-SNMP-VACM-EXT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:12:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
vacmSecurityModel, vacmSecurityName = mibBuilder.importSymbols("SNMP-VIEW-BASED-ACM-MIB", "vacmSecurityModel", "vacmSecurityName")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
NotificationType, Gauge32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter64, Unsigned32, IpAddress, Counter32, MibIdentifier, ObjectIdentity, ModuleIdentity, Integer32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Gauge32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter64", "Unsigned32", "IpAddress", "Counter32", "MibIdentifier", "ObjectIdentity", "ModuleIdentity", "Integer32", "TimeTicks")
TextualConvention, DisplayString, StorageType, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "StorageType", "RowStatus")
ciscoSnmpVacmExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 409))
ciscoSnmpVacmExtMIB.setRevisions(('2004-05-19 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSnmpVacmExtMIB.setRevisionsDescriptions(('Initial version of this MIB.',))
if mibBuilder.loadTexts: ciscoSnmpVacmExtMIB.setLastUpdated('200405190000Z')
if mibBuilder.loadTexts: ciscoSnmpVacmExtMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoSnmpVacmExtMIB.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoSnmpVacmExtMIB.setDescription("The management information definitions to extend the View-based Access Control Model (RFC3415) for SNMP. This MIB extends the 'SNMP-VIEW-BASED-ACM-MIB' to allow each combination of a 'securityModel' and a 'securityName' to be mapped into additional groupNames. The groups identified by these mappings are in addition to those identified by 'vacmGroupName' of the 'vacmSecurityToGroupTable'. ")
ciscoSnmpVacmExtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 409, 1))
ciscoSnmpVacmExtMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 409, 2))
cvacmSecurityToGroupTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 409, 1, 1), )
if mibBuilder.loadTexts: cvacmSecurityToGroupTable.setReference(' [RFC3415] View-based Access Control Model (VACM) for the Simple Network Management Protocol (SNMP), STD 62 . ')
if mibBuilder.loadTexts: cvacmSecurityToGroupTable.setStatus('current')
if mibBuilder.loadTexts: cvacmSecurityToGroupTable.setDescription("An Extension table to the 'vacmSecurityToGroupTable' defined in 'SNMP-VIEW-BASED-ACM-MIB. This table provides a mechanism to map a combination of 'securityModel' and 'securityName' into one or more groups in addition to the 'vacmGroupName' mapped in the 'vacmSecurityToGroupTable'. These groups provide additional access control policies for a principal. The agent must allow the same group mapping entry to be present in both the 'cvacmSecurityToGroupTable' and the 'vacmSecurityToGroupTable'. A row in this table can not exist without a corresponding row for the same combination of 'securityModel' and 'securityName in the 'vacmSecurityToGroupTable'. While creating a row in this table, if there is no corresponding row for the same combination of 'securityModel' and 'securityName in the 'vacmSecurityToGroupTable', the same mapping entry in is created in the 'vacmSecurityToGroupTable' by the agent using the values of instance variables of the entry in this table. The deletion of a row in the 'vacmSecurityToGroupTable' also causes the deletion of all the group mapping entries for the same combination of 'vacmSecurityModel' and 'vacmSecurityName' in the 'cvacmSecurityToGroupTable'. The deletion of a row in this table does not affect 'vacmSecurityToGroupTable'entries. ")
cvacmSecurityToGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 409, 1, 1, 1), ).setIndexNames((0, "SNMP-VIEW-BASED-ACM-MIB", "vacmSecurityModel"), (0, "SNMP-VIEW-BASED-ACM-MIB", "vacmSecurityName"), (0, "CISCO-SNMP-VACM-EXT-MIB", "cvacmSecurityGrpName"))
if mibBuilder.loadTexts: cvacmSecurityToGroupEntry.setStatus('current')
if mibBuilder.loadTexts: cvacmSecurityToGroupEntry.setDescription("An entry (conceptual row) in the 'cvacmSecurityToGroupTable'. Each row represents one groupName mapping for the combination of 'securityModel' and 'securityName' in the system. ")
cvacmSecurityGrpName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 409, 1, 1, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: cvacmSecurityGrpName.setStatus('current')
if mibBuilder.loadTexts: cvacmSecurityGrpName.setDescription("The name of the group for the mapping represented by this row. This is in addition to the 'vacmGroupName' mapped in the 'vacmSecurityToGroupTable'. For example a user principal represented by 'securityName' maps to a group represented by 'cvacmSecurityGrpName' under a security model represented by 'securityModel'. This groupName is used as index into the 'vacmAccessTable' to select an access control policy. However, a value in this table does not imply that an instance with the value exists in table 'vacmAccesTable'. ")
cvacmSecurityGrpStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 409, 1, 1, 1, 2), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvacmSecurityGrpStorageType.setStatus('current')
if mibBuilder.loadTexts: cvacmSecurityGrpStorageType.setDescription("The storage type for this conceptual row. Conceptual rows having the value 'permanent' need not allow write-access to any columnar objects in the row. ")
cvacmSecurityGrpStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 409, 1, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvacmSecurityGrpStatus.setStatus('current')
if mibBuilder.loadTexts: cvacmSecurityGrpStatus.setDescription('The status of this conceptual row. The value of this object has no effect on whether other objects in this conceptual row can be modified. ')
ciscoSnmpVacmExtMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 409, 2, 1))
ciscoSnmpVacmExtMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 409, 2, 2))
ciscoSnmpVacmExtMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 409, 2, 1, 1)).setObjects(("CISCO-SNMP-VACM-EXT-MIB", "ciscoSnmpVacmExtGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpVacmExtMIBCompliance = ciscoSnmpVacmExtMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoSnmpVacmExtMIBCompliance.setDescription('The compliance statement for SNMP engines which implement the CISCO-SNMP-VACM-EXT-MIB.')
ciscoSnmpVacmExtGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 409, 2, 2, 1)).setObjects(("CISCO-SNMP-VACM-EXT-MIB", "cvacmSecurityGrpStorageType"), ("CISCO-SNMP-VACM-EXT-MIB", "cvacmSecurityGrpStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpVacmExtGroup = ciscoSnmpVacmExtGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoSnmpVacmExtGroup.setDescription('A collection of objects providing for remote configuration of an SNMP engine which extends the SNMP View-based Access Control Model.')
mibBuilder.exportSymbols("CISCO-SNMP-VACM-EXT-MIB", ciscoSnmpVacmExtMIB=ciscoSnmpVacmExtMIB, cvacmSecurityGrpName=cvacmSecurityGrpName, ciscoSnmpVacmExtGroup=ciscoSnmpVacmExtGroup, cvacmSecurityToGroupTable=cvacmSecurityToGroupTable, cvacmSecurityGrpStatus=cvacmSecurityGrpStatus, ciscoSnmpVacmExtMIBCompliance=ciscoSnmpVacmExtMIBCompliance, cvacmSecurityToGroupEntry=cvacmSecurityToGroupEntry, ciscoSnmpVacmExtMIBObjects=ciscoSnmpVacmExtMIBObjects, ciscoSnmpVacmExtMIBCompliances=ciscoSnmpVacmExtMIBCompliances, ciscoSnmpVacmExtMIBGroups=ciscoSnmpVacmExtMIBGroups, PYSNMP_MODULE_ID=ciscoSnmpVacmExtMIB, cvacmSecurityGrpStorageType=cvacmSecurityGrpStorageType, ciscoSnmpVacmExtMIBConformance=ciscoSnmpVacmExtMIBConformance)
