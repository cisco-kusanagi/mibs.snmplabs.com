#
# PySNMP MIB module CISCO-UNIFIED-COMPUTING-QUERYRESULT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-UNIFIED-COMPUTING-QUERYRESULT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:17:28 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
Unsigned64, CiscoNetworkAddress, TimeIntervalSec, CiscoAlarmSeverity, CiscoInetAddressMask = mibBuilder.importSymbols("CISCO-TC", "Unsigned64", "CiscoNetworkAddress", "TimeIntervalSec", "CiscoAlarmSeverity", "CiscoInetAddressMask")
CucsManagedObjectDn, CucsManagedObjectId, ciscoUnifiedComputingMIBObjects = mibBuilder.importSymbols("CISCO-UNIFIED-COMPUTING-MIB", "CucsManagedObjectDn", "CucsManagedObjectId", "ciscoUnifiedComputingMIBObjects")
InetAddressIPv4, InetAddressIPv6 = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressIPv4", "InetAddressIPv6")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, Gauge32, TimeTicks, ModuleIdentity, Integer32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, Bits, iso, Unsigned32, Counter64, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Gauge32", "TimeTicks", "ModuleIdentity", "Integer32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "Bits", "iso", "Unsigned32", "Counter64", "IpAddress")
TimeInterval, DisplayString, RowPointer, MacAddress, TimeStamp, DateAndTime, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TimeInterval", "DisplayString", "RowPointer", "MacAddress", "TimeStamp", "DateAndTime", "TruthValue", "TextualConvention")
cucsQueryresultObjects = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 75))
if mibBuilder.loadTexts: cucsQueryresultObjects.setLastUpdated('201601180000Z')
if mibBuilder.loadTexts: cucsQueryresultObjects.setOrganization('Cisco Systems Inc.')
if mibBuilder.loadTexts: cucsQueryresultObjects.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553 -NETS E-mail: cs-san@cisco.com, cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: cucsQueryresultObjects.setDescription('MIB representation of the Cisco Unified Computing System QUERYRESULT management information model package')
cucsQueryresultDependencyTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 75, 1), )
if mibBuilder.loadTexts: cucsQueryresultDependencyTable.setStatus('current')
if mibBuilder.loadTexts: cucsQueryresultDependencyTable.setDescription('Cisco UCS queryresult:Dependency managed object table')
cucsQueryresultDependencyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 75, 1, 1), ).setIndexNames((0, "CISCO-UNIFIED-COMPUTING-QUERYRESULT-MIB", "cucsQueryresultDependencyInstanceId"))
if mibBuilder.loadTexts: cucsQueryresultDependencyEntry.setStatus('current')
if mibBuilder.loadTexts: cucsQueryresultDependencyEntry.setDescription('Entry for the cucsQueryresultDependencyTable table.')
cucsQueryresultDependencyInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 75, 1, 1, 1), CucsManagedObjectId())
if mibBuilder.loadTexts: cucsQueryresultDependencyInstanceId.setStatus('current')
if mibBuilder.loadTexts: cucsQueryresultDependencyInstanceId.setDescription('Instance identifier of the managed object.')
cucsQueryresultDependencyDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 75, 1, 1, 2), CucsManagedObjectDn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsQueryresultDependencyDn.setStatus('current')
if mibBuilder.loadTexts: cucsQueryresultDependencyDn.setDescription('Cisco UCS queryresult:Dependency:dn managed object property')
cucsQueryresultDependencyRn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 75, 1, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsQueryresultDependencyRn.setStatus('current')
if mibBuilder.loadTexts: cucsQueryresultDependencyRn.setDescription('Cisco UCS queryresult:Dependency:rn managed object property')
cucsQueryresultDependencyClassType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 75, 1, 1, 4), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsQueryresultDependencyClassType.setStatus('current')
if mibBuilder.loadTexts: cucsQueryresultDependencyClassType.setDescription('Cisco UCS queryresult:Dependency:classType managed object property')
cucsQueryresultDependencyIsImportable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 75, 1, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsQueryresultDependencyIsImportable.setStatus('current')
if mibBuilder.loadTexts: cucsQueryresultDependencyIsImportable.setDescription('Cisco UCS queryresult:Dependency:isImportable managed object property')
cucsQueryresultDependencyPolicyOwner = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 75, 1, 1, 6), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsQueryresultDependencyPolicyOwner.setStatus('current')
if mibBuilder.loadTexts: cucsQueryresultDependencyPolicyOwner.setDescription('Cisco UCS queryresult:Dependency:policyOwner managed object property')
cucsQueryresultDependencyRefConvertedDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 75, 1, 1, 7), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsQueryresultDependencyRefConvertedDn.setStatus('current')
if mibBuilder.loadTexts: cucsQueryresultDependencyRefConvertedDn.setDescription('Cisco UCS queryresult:Dependency:refConvertedDn managed object property')
cucsQueryresultDependencyRefDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 75, 1, 1, 8), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsQueryresultDependencyRefDn.setStatus('current')
if mibBuilder.loadTexts: cucsQueryresultDependencyRefDn.setDescription('Cisco UCS queryresult:Dependency:refDn managed object property')
cucsQueryresultDependencyRefName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 75, 1, 1, 9), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsQueryresultDependencyRefName.setStatus('current')
if mibBuilder.loadTexts: cucsQueryresultDependencyRefName.setDescription('Cisco UCS queryresult:Dependency:refName managed object property')
cucsQueryresultUsageTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 75, 2), )
if mibBuilder.loadTexts: cucsQueryresultUsageTable.setStatus('current')
if mibBuilder.loadTexts: cucsQueryresultUsageTable.setDescription('Cisco UCS queryresult:Usage managed object table')
cucsQueryresultUsageEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 75, 2, 1), ).setIndexNames((0, "CISCO-UNIFIED-COMPUTING-QUERYRESULT-MIB", "cucsQueryresultUsageInstanceId"))
if mibBuilder.loadTexts: cucsQueryresultUsageEntry.setStatus('current')
if mibBuilder.loadTexts: cucsQueryresultUsageEntry.setDescription('Entry for the cucsQueryresultUsageTable table.')
cucsQueryresultUsageInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 75, 2, 1, 1), CucsManagedObjectId())
if mibBuilder.loadTexts: cucsQueryresultUsageInstanceId.setStatus('current')
if mibBuilder.loadTexts: cucsQueryresultUsageInstanceId.setDescription('Instance identifier of the managed object.')
cucsQueryresultUsageDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 75, 2, 1, 2), CucsManagedObjectDn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsQueryresultUsageDn.setStatus('current')
if mibBuilder.loadTexts: cucsQueryresultUsageDn.setDescription('Cisco UCS queryresult:Usage:dn managed object property')
cucsQueryresultUsageRn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 75, 2, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsQueryresultUsageRn.setStatus('current')
if mibBuilder.loadTexts: cucsQueryresultUsageRn.setDescription('Cisco UCS queryresult:Usage:rn managed object property')
cucsQueryresultUsageClassType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 75, 2, 1, 4), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsQueryresultUsageClassType.setStatus('current')
if mibBuilder.loadTexts: cucsQueryresultUsageClassType.setDescription('Cisco UCS queryresult:Usage:classType managed object property')
cucsQueryresultUsageIsServiceTemplate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 75, 2, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsQueryresultUsageIsServiceTemplate.setStatus('current')
if mibBuilder.loadTexts: cucsQueryresultUsageIsServiceTemplate.setDescription('Cisco UCS queryresult:Usage:isServiceTemplate managed object property')
cucsQueryresultUsagePolicyOwner = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 75, 2, 1, 6), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsQueryresultUsagePolicyOwner.setStatus('current')
if mibBuilder.loadTexts: cucsQueryresultUsagePolicyOwner.setDescription('Cisco UCS queryresult:Usage:policyOwner managed object property')
cucsQueryresultUsageRefConvertedDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 75, 2, 1, 7), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsQueryresultUsageRefConvertedDn.setStatus('current')
if mibBuilder.loadTexts: cucsQueryresultUsageRefConvertedDn.setDescription('Cisco UCS queryresult:Usage:refConvertedDn managed object property')
cucsQueryresultUsageRefDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 75, 2, 1, 8), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsQueryresultUsageRefDn.setStatus('current')
if mibBuilder.loadTexts: cucsQueryresultUsageRefDn.setDescription('Cisco UCS queryresult:Usage:refDn managed object property')
cucsQueryresultUsageRefName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 75, 2, 1, 9), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsQueryresultUsageRefName.setStatus('current')
if mibBuilder.loadTexts: cucsQueryresultUsageRefName.setDescription('Cisco UCS queryresult:Usage:refName managed object property')
mibBuilder.exportSymbols("CISCO-UNIFIED-COMPUTING-QUERYRESULT-MIB", cucsQueryresultUsageRefConvertedDn=cucsQueryresultUsageRefConvertedDn, cucsQueryresultDependencyRefDn=cucsQueryresultDependencyRefDn, cucsQueryresultDependencyEntry=cucsQueryresultDependencyEntry, cucsQueryresultUsageRefName=cucsQueryresultUsageRefName, cucsQueryresultUsageClassType=cucsQueryresultUsageClassType, cucsQueryresultDependencyInstanceId=cucsQueryresultDependencyInstanceId, cucsQueryresultDependencyRefName=cucsQueryresultDependencyRefName, cucsQueryresultUsagePolicyOwner=cucsQueryresultUsagePolicyOwner, cucsQueryresultUsageRefDn=cucsQueryresultUsageRefDn, cucsQueryresultUsageRn=cucsQueryresultUsageRn, PYSNMP_MODULE_ID=cucsQueryresultObjects, cucsQueryresultDependencyIsImportable=cucsQueryresultDependencyIsImportable, cucsQueryresultUsageInstanceId=cucsQueryresultUsageInstanceId, cucsQueryresultDependencyRefConvertedDn=cucsQueryresultDependencyRefConvertedDn, cucsQueryresultDependencyClassType=cucsQueryresultDependencyClassType, cucsQueryresultDependencyRn=cucsQueryresultDependencyRn, cucsQueryresultUsageIsServiceTemplate=cucsQueryresultUsageIsServiceTemplate, cucsQueryresultDependencyTable=cucsQueryresultDependencyTable, cucsQueryresultUsageTable=cucsQueryresultUsageTable, cucsQueryresultDependencyPolicyOwner=cucsQueryresultDependencyPolicyOwner, cucsQueryresultDependencyDn=cucsQueryresultDependencyDn, cucsQueryresultUsageEntry=cucsQueryresultUsageEntry, cucsQueryresultUsageDn=cucsQueryresultUsageDn, cucsQueryresultObjects=cucsQueryresultObjects)
