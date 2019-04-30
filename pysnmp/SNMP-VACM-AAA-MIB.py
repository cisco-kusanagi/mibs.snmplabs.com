#
# PySNMP MIB module SNMP-VACM-AAA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SNMP-VACM-AAA-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:00:31 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
SnmpAdminString, SnmpSecurityModel = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString", "SnmpSecurityModel")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
iso, NotificationType, TimeTicks, Counter32, IpAddress, Counter64, Bits, Integer32, Gauge32, ModuleIdentity, Unsigned32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, mib_2, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "NotificationType", "TimeTicks", "Counter32", "IpAddress", "Counter64", "Bits", "Integer32", "Gauge32", "ModuleIdentity", "Unsigned32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "mib-2", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
vacmAaaMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 199))
vacmAaaMIB.setRevisions(('2010-12-09 00:00',))
if mibBuilder.loadTexts: vacmAaaMIB.setLastUpdated('201012090000Z')
if mibBuilder.loadTexts: vacmAaaMIB.setOrganization('ISMS Working Group')
vacmAaaMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 199, 1))
vacmAaaMIBConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 199, 2))
vacmAaaSecurityToGroupTable = MibTable((1, 3, 6, 1, 2, 1, 199, 1, 1), )
if mibBuilder.loadTexts: vacmAaaSecurityToGroupTable.setStatus('current')
vacmAaaSecurityToGroupEntry = MibTableRow((1, 3, 6, 1, 2, 1, 199, 1, 1, 1), ).setIndexNames((0, "SNMP-VACM-AAA-MIB", "vacmAaaSecurityModel"), (0, "SNMP-VACM-AAA-MIB", "vacmAaaSecurityName"), (0, "SNMP-VACM-AAA-MIB", "vacmAaaSessionID"))
if mibBuilder.loadTexts: vacmAaaSecurityToGroupEntry.setStatus('current')
vacmAaaSecurityModel = MibTableColumn((1, 3, 6, 1, 2, 1, 199, 1, 1, 1, 1), SnmpSecurityModel().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: vacmAaaSecurityModel.setStatus('current')
vacmAaaSecurityName = MibTableColumn((1, 3, 6, 1, 2, 1, 199, 1, 1, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: vacmAaaSecurityName.setStatus('current')
vacmAaaSessionID = MibTableColumn((1, 3, 6, 1, 2, 1, 199, 1, 1, 1, 3), Unsigned32())
if mibBuilder.loadTexts: vacmAaaSessionID.setStatus('current')
vacmAaaGroupName = MibTableColumn((1, 3, 6, 1, 2, 1, 199, 1, 1, 1, 4), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vacmAaaGroupName.setStatus('current')
vacmAaaMIBCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 199, 2, 1))
vacmAaaMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 199, 2, 2))
vacmAaaMIBBasicCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 199, 2, 1, 1)).setObjects(("SNMP-VACM-AAA-MIB", "vacmAaaGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vacmAaaMIBBasicCompliance = vacmAaaMIBBasicCompliance.setStatus('current')
vacmAaaGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 199, 2, 2, 1)).setObjects(("SNMP-VACM-AAA-MIB", "vacmAaaGroupName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vacmAaaGroup = vacmAaaGroup.setStatus('current')
mibBuilder.exportSymbols("SNMP-VACM-AAA-MIB", vacmAaaMIBConformance=vacmAaaMIBConformance, PYSNMP_MODULE_ID=vacmAaaMIB, vacmAaaSecurityToGroupTable=vacmAaaSecurityToGroupTable, vacmAaaSessionID=vacmAaaSessionID, vacmAaaSecurityModel=vacmAaaSecurityModel, vacmAaaMIBObjects=vacmAaaMIBObjects, vacmAaaMIBGroups=vacmAaaMIBGroups, vacmAaaMIBBasicCompliance=vacmAaaMIBBasicCompliance, vacmAaaMIB=vacmAaaMIB, vacmAaaSecurityToGroupEntry=vacmAaaSecurityToGroupEntry, vacmAaaSecurityName=vacmAaaSecurityName, vacmAaaGroupName=vacmAaaGroupName, vacmAaaMIBCompliances=vacmAaaMIBCompliances, vacmAaaGroup=vacmAaaGroup)
