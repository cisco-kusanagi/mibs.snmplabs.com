#
# PySNMP MIB module HUAWEI-DAD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-DAD-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:43:57 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
hwDatacomm, = mibBuilder.importSymbols("HUAWEI-MIB", "hwDatacomm")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
IpAddress, Integer32, ObjectIdentity, TimeTicks, ModuleIdentity, Counter32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, iso, Unsigned32, Gauge32, NotificationType, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Integer32", "ObjectIdentity", "TimeTicks", "ModuleIdentity", "Counter32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "iso", "Unsigned32", "Gauge32", "NotificationType", "MibIdentifier")
TruthValue, MacAddress, DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "MacAddress", "DisplayString", "RowStatus", "TextualConvention")
hwDadMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 246))
if mibBuilder.loadTexts: hwDadMIB.setLastUpdated('201109142130Z')
if mibBuilder.loadTexts: hwDadMIB.setOrganization('Huawei Technologies co.,Ltd.')
if mibBuilder.loadTexts: hwDadMIB.setContactInfo('Huawei Nanjing R&D Center 101 Software Avenue, Yuhuatai District, Nanjing city Zip:210012 Http://www.huawei.com E-mail:support@huawei.com Zip:100000 ')
if mibBuilder.loadTexts: hwDadMIB.setDescription('This MIB contains private managed object definitions for dual-active detection.')
class PortIndex(TextualConvention, Integer32):
    description = 'Each port is uniquely identified by a port number. The port number ranges from 0 to 575.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 575)

hwDadTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 246, 1))
hwDadConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 246, 2))
hwDadConflictDetect = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 246, 1, 1))
if mibBuilder.loadTexts: hwDadConflictDetect.setStatus('current')
if mibBuilder.loadTexts: hwDadConflictDetect.setDescription('Notify the NMS that dual-active scenario is detected.')
hwDadConflictResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 246, 1, 2))
if mibBuilder.loadTexts: hwDadConflictResume.setStatus('current')
if mibBuilder.loadTexts: hwDadConflictResume.setDescription('Notify the NMS that dual-active scenario is merged.')
hwDadCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 246, 2, 1))
hwDadGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 246, 2, 2))
hwDadCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 5, 25, 246, 2, 1, 1)).setObjects(("HUAWEI-DAD-MIB", "hwDadTrapGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwDadCompliance = hwDadCompliance.setStatus('current')
if mibBuilder.loadTexts: hwDadCompliance.setDescription('The compliance statement for SNMP entities which implement the HUAWEI-DAD-MIB.')
hwDadTrapGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 246, 2, 2, 1)).setObjects(("HUAWEI-DAD-MIB", "hwDadConflictDetect"), ("HUAWEI-DAD-MIB", "hwDadConflictResume"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwDadTrapGroup = hwDadTrapGroup.setStatus('current')
if mibBuilder.loadTexts: hwDadTrapGroup.setDescription('The collection of notifications used to indicate that the HUAWEI-DAD-MIB data is consistent and indicate the general status information. This group is mandatory for agents which implement the DAD and have the capability of receiving DAD frames.')
mibBuilder.exportSymbols("HUAWEI-DAD-MIB", hwDadGroups=hwDadGroups, hwDadTrapGroup=hwDadTrapGroup, hwDadConflictResume=hwDadConflictResume, hwDadCompliance=hwDadCompliance, hwDadCompliances=hwDadCompliances, hwDadTraps=hwDadTraps, hwDadMIB=hwDadMIB, hwDadConflictDetect=hwDadConflictDetect, PYSNMP_MODULE_ID=hwDadMIB, PortIndex=PortIndex, hwDadConformance=hwDadConformance)
