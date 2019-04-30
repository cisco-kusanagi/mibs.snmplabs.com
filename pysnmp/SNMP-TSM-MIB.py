#
# PySNMP MIB module SNMP-TSM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SNMP-TSM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:00:25 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, mib_2, TimeTicks, ObjectIdentity, ModuleIdentity, iso, IpAddress, Bits, Counter32, Counter64, NotificationType, Integer32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "mib-2", "TimeTicks", "ObjectIdentity", "ModuleIdentity", "iso", "IpAddress", "Bits", "Counter32", "Counter64", "NotificationType", "Integer32", "Gauge32")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
snmpTsmMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 190))
snmpTsmMIB.setRevisions(('2009-06-09 00:00',))
if mibBuilder.loadTexts: snmpTsmMIB.setLastUpdated('200906090000Z')
if mibBuilder.loadTexts: snmpTsmMIB.setOrganization('ISMS Working Group')
snmpTsmNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 190, 0))
snmpTsmMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 190, 1))
snmpTsmConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 190, 2))
snmpTsmStats = MibIdentifier((1, 3, 6, 1, 2, 1, 190, 1, 1))
snmpTsmInvalidCaches = MibScalar((1, 3, 6, 1, 2, 1, 190, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpTsmInvalidCaches.setStatus('current')
snmpTsmInadequateSecurityLevels = MibScalar((1, 3, 6, 1, 2, 1, 190, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpTsmInadequateSecurityLevels.setStatus('current')
snmpTsmUnknownPrefixes = MibScalar((1, 3, 6, 1, 2, 1, 190, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpTsmUnknownPrefixes.setStatus('current')
snmpTsmInvalidPrefixes = MibScalar((1, 3, 6, 1, 2, 1, 190, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpTsmInvalidPrefixes.setStatus('current')
snmpTsmConfiguration = MibIdentifier((1, 3, 6, 1, 2, 1, 190, 1, 2))
snmpTsmConfigurationUsePrefix = MibScalar((1, 3, 6, 1, 2, 1, 190, 1, 2, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpTsmConfigurationUsePrefix.setStatus('current')
snmpTsmCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 190, 2, 1))
snmpTsmGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 190, 2, 2))
snmpTsmCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 190, 2, 1, 1)).setObjects(("SNMP-TSM-MIB", "snmpTsmGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    snmpTsmCompliance = snmpTsmCompliance.setStatus('current')
snmpTsmGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 190, 2, 2, 2)).setObjects(("SNMP-TSM-MIB", "snmpTsmInvalidCaches"), ("SNMP-TSM-MIB", "snmpTsmInadequateSecurityLevels"), ("SNMP-TSM-MIB", "snmpTsmUnknownPrefixes"), ("SNMP-TSM-MIB", "snmpTsmInvalidPrefixes"), ("SNMP-TSM-MIB", "snmpTsmConfigurationUsePrefix"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    snmpTsmGroup = snmpTsmGroup.setStatus('current')
mibBuilder.exportSymbols("SNMP-TSM-MIB", snmpTsmNotifications=snmpTsmNotifications, snmpTsmStats=snmpTsmStats, snmpTsmInvalidCaches=snmpTsmInvalidCaches, snmpTsmUnknownPrefixes=snmpTsmUnknownPrefixes, snmpTsmMIB=snmpTsmMIB, snmpTsmConfigurationUsePrefix=snmpTsmConfigurationUsePrefix, snmpTsmCompliances=snmpTsmCompliances, snmpTsmGroups=snmpTsmGroups, snmpTsmCompliance=snmpTsmCompliance, snmpTsmInadequateSecurityLevels=snmpTsmInadequateSecurityLevels, snmpTsmMIBObjects=snmpTsmMIBObjects, snmpTsmConformance=snmpTsmConformance, snmpTsmInvalidPrefixes=snmpTsmInvalidPrefixes, PYSNMP_MODULE_ID=snmpTsmMIB, snmpTsmGroup=snmpTsmGroup, snmpTsmConfiguration=snmpTsmConfiguration)
