#
# PySNMP MIB module HUAWEI-DETECT-ENGINE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-DETECT-ENGINE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:44:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
hwDatacomm, = mibBuilder.importSymbols("HUAWEI-MIB", "hwDatacomm")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
iso, NotificationType, Unsigned32, Counter64, Gauge32, Bits, TimeTicks, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Counter32, IpAddress, MibIdentifier, Integer32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "NotificationType", "Unsigned32", "Counter64", "Gauge32", "Bits", "TimeTicks", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Counter32", "IpAddress", "MibIdentifier", "Integer32", "ObjectIdentity")
DisplayString, TextualConvention, AutonomousType, DateAndTime, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "AutonomousType", "DateAndTime", "RowStatus")
hwDetectEngineMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 308))
hwDetectEngineMIB.setRevisions(('2012-08-30 09:36',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hwDetectEngineMIB.setRevisionsDescriptions(('ver 1.0',))
if mibBuilder.loadTexts: hwDetectEngineMIB.setLastUpdated('201208300936Z')
if mibBuilder.loadTexts: hwDetectEngineMIB.setOrganization('Huawei Technologies Co.,Ltd.')
if mibBuilder.loadTexts: hwDetectEngineMIB.setContactInfo("Huawei Industrial Base Bantian, Longgang Shenzhen 518129 People's Republic of China Website: http://www.huawei.com Email: support@huawei.com ")
if mibBuilder.loadTexts: hwDetectEngineMIB.setDescription('The HUAWEI-DETECT-ENGINE-MIB contains objects to configure Logic module, including switching logic startup file. This MIB module objects can switch logic startup file for NQA-RTP module or OAM module. ')
hwDetectEngineObject = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 308, 1))
hwDetectEngineGlobalObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 308, 1, 1))
hwDetectEngineOAMEnable = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 308, 1, 1, 1), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwDetectEngineOAMEnable.setStatus('current')
if mibBuilder.loadTexts: hwDetectEngineOAMEnable.setDescription('Globally enable or disable the detect-engine for oam. If the hwDetectEngineOAMEnable is 1, detect-engine for oam is enabled. If the hwDetectEngineOAMEnable is 2, detect-engine for oam is disabled. By default, detect-engine for oam is enabled.')
hwDetectEngineNQAEnable = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 308, 1, 1, 2), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwDetectEngineNQAEnable.setStatus('current')
if mibBuilder.loadTexts: hwDetectEngineNQAEnable.setDescription('Globally enable or disable the detect-engine for nqa-rtp. If the hwDetectEngineNQAEnable is 1, detect-engine for nqa-rtp is enabled. If the hwDetectEngineNQAEnable is 2, detect-engine for nqa-rtp is disabled. By default, detect-engine for nqa-rtp is disabled.')
hwDetectEngineConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 308, 100))
hwDetectEngineCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 308, 100, 1))
hwDetectEngineCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 5, 25, 308, 100, 1, 1)).setObjects(("HUAWEI-DETECT-ENGINE-MIB", "hwDetectEngineGlobalObjectGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwDetectEngineCompliance = hwDetectEngineCompliance.setStatus('current')
if mibBuilder.loadTexts: hwDetectEngineCompliance.setDescription('Compliance statement for agents that provide full support for hwDetectEngineMIB.')
hwDetectEngineGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 308, 100, 2))
hwDetectEngineGlobalObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 308, 100, 2, 1)).setObjects(("HUAWEI-DETECT-ENGINE-MIB", "hwDetectEngineOAMEnable"), ("HUAWEI-DETECT-ENGINE-MIB", "hwDetectEngineNQAEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwDetectEngineGlobalObjectGroup = hwDetectEngineGlobalObjectGroup.setStatus('current')
if mibBuilder.loadTexts: hwDetectEngineGlobalObjectGroup.setDescription('Group for base trap objects.')
mibBuilder.exportSymbols("HUAWEI-DETECT-ENGINE-MIB", hwDetectEngineCompliance=hwDetectEngineCompliance, hwDetectEngineGlobalObjectGroup=hwDetectEngineGlobalObjectGroup, hwDetectEngineCompliances=hwDetectEngineCompliances, hwDetectEngineOAMEnable=hwDetectEngineOAMEnable, hwDetectEngineGroups=hwDetectEngineGroups, hwDetectEngineMIB=hwDetectEngineMIB, hwDetectEngineConformance=hwDetectEngineConformance, hwDetectEngineGlobalObjects=hwDetectEngineGlobalObjects, hwDetectEngineNQAEnable=hwDetectEngineNQAEnable, PYSNMP_MODULE_ID=hwDetectEngineMIB, hwDetectEngineObject=hwDetectEngineObject)
