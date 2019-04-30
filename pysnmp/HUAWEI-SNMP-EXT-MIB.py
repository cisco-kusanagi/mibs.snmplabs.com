#
# PySNMP MIB module HUAWEI-SNMP-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-SNMP-EXT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:36:53 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
hwDatacomm, = mibBuilder.importSymbols("HUAWEI-MIB", "hwDatacomm")
ifDescr, ifIndex = mibBuilder.importSymbols("IF-MIB", "ifDescr", "ifIndex")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
TimeTicks, Unsigned32, ModuleIdentity, Bits, Integer32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, MibIdentifier, iso, IpAddress, Gauge32, ObjectIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Unsigned32", "ModuleIdentity", "Bits", "Integer32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "MibIdentifier", "iso", "IpAddress", "Gauge32", "ObjectIdentity", "NotificationType")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
hwSnmpExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 164))
if mibBuilder.loadTexts: hwSnmpExtMIB.setLastUpdated('200801090000Z')
if mibBuilder.loadTexts: hwSnmpExtMIB.setOrganization('Huawei Technologies co.,Ltd.')
hwSnmpExtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 164, 1))
hwSnmpExtErrorCodeEnable = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 164, 1, 1), EnabledStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwSnmpExtErrorCodeEnable.setStatus('current')
hwSnmpExtConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 164, 2))
hwSnmpExtGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 164, 2, 1))
hwSnmpExtRuleGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 164, 2, 1, 1)).setObjects(("HUAWEI-SNMP-EXT-MIB", "hwSnmpExtErrorCodeEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwSnmpExtRuleGroup = hwSnmpExtRuleGroup.setStatus('current')
hwSnmpExtCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 164, 2, 2))
hwSnmpExtCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 5, 25, 164, 2, 2, 1)).setObjects(("HUAWEI-SNMP-EXT-MIB", "hwSnmpExtRuleGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwSnmpExtCompliance = hwSnmpExtCompliance.setStatus('current')
mibBuilder.exportSymbols("HUAWEI-SNMP-EXT-MIB", hwSnmpExtGroups=hwSnmpExtGroups, hwSnmpExtErrorCodeEnable=hwSnmpExtErrorCodeEnable, hwSnmpExtMIBObjects=hwSnmpExtMIBObjects, hwSnmpExtConformance=hwSnmpExtConformance, hwSnmpExtCompliances=hwSnmpExtCompliances, PYSNMP_MODULE_ID=hwSnmpExtMIB, hwSnmpExtCompliance=hwSnmpExtCompliance, hwSnmpExtMIB=hwSnmpExtMIB, hwSnmpExtRuleGroup=hwSnmpExtRuleGroup)
