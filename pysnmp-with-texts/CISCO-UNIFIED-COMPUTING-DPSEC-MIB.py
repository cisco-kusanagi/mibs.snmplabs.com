#
# PySNMP MIB module CISCO-UNIFIED-COMPUTING-DPSEC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-UNIFIED-COMPUTING-DPSEC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:15:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
TimeIntervalSec, Unsigned64, CiscoInetAddressMask, CiscoAlarmSeverity, CiscoNetworkAddress = mibBuilder.importSymbols("CISCO-TC", "TimeIntervalSec", "Unsigned64", "CiscoInetAddressMask", "CiscoAlarmSeverity", "CiscoNetworkAddress")
CucsManagedObjectDn, CucsManagedObjectId, ciscoUnifiedComputingMIBObjects = mibBuilder.importSymbols("CISCO-UNIFIED-COMPUTING-MIB", "CucsManagedObjectDn", "CucsManagedObjectId", "ciscoUnifiedComputingMIBObjects")
CucsDpsecForgedTransmit, CucsPolicyPolicyOwner = mibBuilder.importSymbols("CISCO-UNIFIED-COMPUTING-TC-MIB", "CucsDpsecForgedTransmit", "CucsPolicyPolicyOwner")
InetAddressIPv6, InetAddressIPv4 = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressIPv6", "InetAddressIPv4")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, Unsigned32, NotificationType, Bits, ModuleIdentity, Gauge32, TimeTicks, iso, MibIdentifier, Counter64, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Unsigned32", "NotificationType", "Bits", "ModuleIdentity", "Gauge32", "TimeTicks", "iso", "MibIdentifier", "Counter64", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Counter32")
TextualConvention, TimeStamp, RowPointer, TruthValue, TimeInterval, DateAndTime, DisplayString, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TimeStamp", "RowPointer", "TruthValue", "TimeInterval", "DateAndTime", "DisplayString", "MacAddress")
cucsDpsecObjects = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 13))
if mibBuilder.loadTexts: cucsDpsecObjects.setLastUpdated('201601180000Z')
if mibBuilder.loadTexts: cucsDpsecObjects.setOrganization('Cisco Systems Inc.')
if mibBuilder.loadTexts: cucsDpsecObjects.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553 -NETS E-mail: cs-san@cisco.com, cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: cucsDpsecObjects.setDescription('MIB representation of the Cisco Unified Computing System DPSEC management information model package')
cucsDpsecMacTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 13, 1), )
if mibBuilder.loadTexts: cucsDpsecMacTable.setStatus('current')
if mibBuilder.loadTexts: cucsDpsecMacTable.setDescription('Cisco UCS dpsec:Mac managed object table')
cucsDpsecMacEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 13, 1, 1), ).setIndexNames((0, "CISCO-UNIFIED-COMPUTING-DPSEC-MIB", "cucsDpsecMacInstanceId"))
if mibBuilder.loadTexts: cucsDpsecMacEntry.setStatus('current')
if mibBuilder.loadTexts: cucsDpsecMacEntry.setDescription('Entry for the cucsDpsecMacTable table.')
cucsDpsecMacInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 13, 1, 1, 1), CucsManagedObjectId())
if mibBuilder.loadTexts: cucsDpsecMacInstanceId.setStatus('current')
if mibBuilder.loadTexts: cucsDpsecMacInstanceId.setDescription('Instance identifier of the managed object.')
cucsDpsecMacDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 13, 1, 1, 2), CucsManagedObjectDn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDpsecMacDn.setStatus('current')
if mibBuilder.loadTexts: cucsDpsecMacDn.setDescription('Cisco UCS dpsec:Mac:dn managed object property')
cucsDpsecMacRn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 13, 1, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDpsecMacRn.setStatus('current')
if mibBuilder.loadTexts: cucsDpsecMacRn.setDescription('Cisco UCS dpsec:Mac:rn managed object property')
cucsDpsecMacDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 13, 1, 1, 4), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDpsecMacDescr.setStatus('current')
if mibBuilder.loadTexts: cucsDpsecMacDescr.setDescription('Cisco UCS dpsec:Mac:descr managed object property')
cucsDpsecMacForge = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 13, 1, 1, 5), CucsDpsecForgedTransmit()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDpsecMacForge.setStatus('current')
if mibBuilder.loadTexts: cucsDpsecMacForge.setDescription('Cisco UCS dpsec:Mac:forge managed object property')
cucsDpsecMacIntId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 13, 1, 1, 6), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDpsecMacIntId.setStatus('current')
if mibBuilder.loadTexts: cucsDpsecMacIntId.setDescription('Cisco UCS dpsec:Mac:intId managed object property')
cucsDpsecMacName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 13, 1, 1, 7), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDpsecMacName.setStatus('current')
if mibBuilder.loadTexts: cucsDpsecMacName.setDescription('Cisco UCS dpsec:Mac:name managed object property')
cucsDpsecMacPolicyLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 13, 1, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDpsecMacPolicyLevel.setStatus('current')
if mibBuilder.loadTexts: cucsDpsecMacPolicyLevel.setDescription('Cisco UCS dpsec:Mac:policyLevel managed object property')
cucsDpsecMacPolicyOwner = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 13, 1, 1, 9), CucsPolicyPolicyOwner()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDpsecMacPolicyOwner.setStatus('current')
if mibBuilder.loadTexts: cucsDpsecMacPolicyOwner.setDescription('Cisco UCS dpsec:Mac:policyOwner managed object property')
cucsDpsecMacPropAcl = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 13, 1, 1, 10), Unsigned64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsDpsecMacPropAcl.setStatus('current')
if mibBuilder.loadTexts: cucsDpsecMacPropAcl.setDescription('Cisco UCS dpsec:Mac:propAcl managed object property')
mibBuilder.exportSymbols("CISCO-UNIFIED-COMPUTING-DPSEC-MIB", cucsDpsecMacDescr=cucsDpsecMacDescr, cucsDpsecMacIntId=cucsDpsecMacIntId, cucsDpsecMacEntry=cucsDpsecMacEntry, cucsDpsecMacName=cucsDpsecMacName, cucsDpsecMacTable=cucsDpsecMacTable, cucsDpsecObjects=cucsDpsecObjects, PYSNMP_MODULE_ID=cucsDpsecObjects, cucsDpsecMacPropAcl=cucsDpsecMacPropAcl, cucsDpsecMacForge=cucsDpsecMacForge, cucsDpsecMacPolicyOwner=cucsDpsecMacPolicyOwner, cucsDpsecMacRn=cucsDpsecMacRn, cucsDpsecMacPolicyLevel=cucsDpsecMacPolicyLevel, cucsDpsecMacDn=cucsDpsecMacDn, cucsDpsecMacInstanceId=cucsDpsecMacInstanceId)
