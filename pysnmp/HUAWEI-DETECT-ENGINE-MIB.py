#
# PySNMP MIB module HUAWEI-DETECT-ENGINE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-DETECT-ENGINE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:32:05 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
hwDatacomm, = mibBuilder.importSymbols("HUAWEI-MIB", "hwDatacomm")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Unsigned32, Bits, Counter64, Integer32, iso, Gauge32, ModuleIdentity, Counter32, Bits, MibIdentifier, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Unsigned32", "Bits", "Counter64", "Integer32", "iso", "Gauge32", "ModuleIdentity", "Counter32", "Bits", "MibIdentifier", "NotificationType")
AutonomousType, TextualConvention, DateAndTime, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "AutonomousType", "TextualConvention", "DateAndTime", "DisplayString", "RowStatus")
hwDetectEngineMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 308))
hwDetectEngineMIB.setRevisions(('2012-08-30 09:36',))
if mibBuilder.loadTexts: hwDetectEngineMIB.setLastUpdated('201208300936Z')
if mibBuilder.loadTexts: hwDetectEngineMIB.setOrganization('Huawei Technologies Co.,Ltd.')
hwDetectEngineObject = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 308, 1))
hwDetectEngineGlobalObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 308, 1, 1))
hwDetectEngineOAMEnable = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 308, 1, 1, 1), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwDetectEngineOAMEnable.setStatus('current')
hwDetectEngineNQAEnable = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 308, 1, 1, 2), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwDetectEngineNQAEnable.setStatus('current')
hwDetectEngineConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 308, 100))
hwDetectEngineCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 308, 100, 1))
hwDetectEngineCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 5, 25, 308, 100, 1, 1)).setObjects(("HUAWEI-DETECT-ENGINE-MIB", "hwDetectEngineGlobalObjectGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwDetectEngineCompliance = hwDetectEngineCompliance.setStatus('current')
hwDetectEngineGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 308, 100, 2))
hwDetectEngineGlobalObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 308, 100, 2, 1)).setObjects(("HUAWEI-DETECT-ENGINE-MIB", "hwDetectEngineOAMEnable"), ("HUAWEI-DETECT-ENGINE-MIB", "hwDetectEngineNQAEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwDetectEngineGlobalObjectGroup = hwDetectEngineGlobalObjectGroup.setStatus('current')
mibBuilder.exportSymbols("HUAWEI-DETECT-ENGINE-MIB", hwDetectEngineCompliance=hwDetectEngineCompliance, hwDetectEngineObject=hwDetectEngineObject, PYSNMP_MODULE_ID=hwDetectEngineMIB, hwDetectEngineOAMEnable=hwDetectEngineOAMEnable, hwDetectEngineMIB=hwDetectEngineMIB, hwDetectEngineNQAEnable=hwDetectEngineNQAEnable, hwDetectEngineGlobalObjectGroup=hwDetectEngineGlobalObjectGroup, hwDetectEngineGlobalObjects=hwDetectEngineGlobalObjects, hwDetectEngineConformance=hwDetectEngineConformance, hwDetectEngineCompliances=hwDetectEngineCompliances, hwDetectEngineGroups=hwDetectEngineGroups)
