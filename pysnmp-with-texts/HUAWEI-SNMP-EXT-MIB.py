#
# PySNMP MIB module HUAWEI-SNMP-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-SNMP-EXT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:48:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
hwDatacomm, = mibBuilder.importSymbols("HUAWEI-MIB", "hwDatacomm")
ifIndex, ifDescr = mibBuilder.importSymbols("IF-MIB", "ifIndex", "ifDescr")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
NotificationType, iso, ModuleIdentity, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter64, Integer32, TimeTicks, IpAddress, Counter32, MibIdentifier, Bits, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "iso", "ModuleIdentity", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter64", "Integer32", "TimeTicks", "IpAddress", "Counter32", "MibIdentifier", "Bits", "Unsigned32")
TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue")
hwSnmpExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 164))
if mibBuilder.loadTexts: hwSnmpExtMIB.setLastUpdated('200801090000Z')
if mibBuilder.loadTexts: hwSnmpExtMIB.setOrganization('Huawei Technologies co.,Ltd.')
if mibBuilder.loadTexts: hwSnmpExtMIB.setContactInfo(' R&D BeiJing, Huawei Technologies co.,Ltd. Huawei Bld.,NO.3 Xinxi Rd., Shang-Di Information Industry Base, Hai-Dian District Beijing P.R. China Zip:100085 Http://www.huawei.com E-mail:support@huawei.com ')
if mibBuilder.loadTexts: hwSnmpExtMIB.setDescription(' Some attribute of SNMP extended content. ')
hwSnmpExtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 164, 1))
hwSnmpExtErrorCodeEnable = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 164, 1, 1), EnabledStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwSnmpExtErrorCodeEnable.setStatus('current')
if mibBuilder.loadTexts: hwSnmpExtErrorCodeEnable.setDescription('Enabled or disabled SNMP extended error status.')
hwSnmpExtConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 164, 2))
hwSnmpExtGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 164, 2, 1))
hwSnmpExtRuleGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 164, 2, 1, 1)).setObjects(("HUAWEI-SNMP-EXT-MIB", "hwSnmpExtErrorCodeEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwSnmpExtRuleGroup = hwSnmpExtRuleGroup.setStatus('current')
if mibBuilder.loadTexts: hwSnmpExtRuleGroup.setDescription('Collection of objects needed for SNMP extended configuration.')
hwSnmpExtCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 164, 2, 2))
hwSnmpExtCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 5, 25, 164, 2, 2, 1)).setObjects(("HUAWEI-SNMP-EXT-MIB", "hwSnmpExtRuleGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwSnmpExtCompliance = hwSnmpExtCompliance.setStatus('current')
if mibBuilder.loadTexts: hwSnmpExtCompliance.setDescription('The compliance statement for implementing the Huawei extended SNMP MIB.')
mibBuilder.exportSymbols("HUAWEI-SNMP-EXT-MIB", hwSnmpExtMIBObjects=hwSnmpExtMIBObjects, hwSnmpExtErrorCodeEnable=hwSnmpExtErrorCodeEnable, hwSnmpExtMIB=hwSnmpExtMIB, PYSNMP_MODULE_ID=hwSnmpExtMIB, hwSnmpExtCompliances=hwSnmpExtCompliances, hwSnmpExtCompliance=hwSnmpExtCompliance, hwSnmpExtRuleGroup=hwSnmpExtRuleGroup, hwSnmpExtConformance=hwSnmpExtConformance, hwSnmpExtGroups=hwSnmpExtGroups)
