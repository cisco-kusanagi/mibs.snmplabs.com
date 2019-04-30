#
# PySNMP MIB module HUAWEI-DAD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-DAD-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:31:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
hwDatacomm, = mibBuilder.importSymbols("HUAWEI-MIB", "hwDatacomm")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
TimeTicks, IpAddress, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ModuleIdentity, iso, Counter32, Unsigned32, ObjectIdentity, Gauge32, MibIdentifier, NotificationType, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "IpAddress", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ModuleIdentity", "iso", "Counter32", "Unsigned32", "ObjectIdentity", "Gauge32", "MibIdentifier", "NotificationType", "Integer32")
MacAddress, TextualConvention, TruthValue, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TextualConvention", "TruthValue", "DisplayString", "RowStatus")
hwDadMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 246))
if mibBuilder.loadTexts: hwDadMIB.setLastUpdated('201109142130Z')
if mibBuilder.loadTexts: hwDadMIB.setOrganization('Huawei Technologies co.,Ltd.')
class PortIndex(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 575)

hwDadTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 246, 1))
hwDadConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 246, 2))
hwDadConflictDetect = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 246, 1, 1))
if mibBuilder.loadTexts: hwDadConflictDetect.setStatus('current')
hwDadConflictResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 246, 1, 2))
if mibBuilder.loadTexts: hwDadConflictResume.setStatus('current')
hwDadCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 246, 2, 1))
hwDadGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 246, 2, 2))
hwDadCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 5, 25, 246, 2, 1, 1)).setObjects(("HUAWEI-DAD-MIB", "hwDadTrapGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwDadCompliance = hwDadCompliance.setStatus('current')
hwDadTrapGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 246, 2, 2, 1)).setObjects(("HUAWEI-DAD-MIB", "hwDadConflictDetect"), ("HUAWEI-DAD-MIB", "hwDadConflictResume"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwDadTrapGroup = hwDadTrapGroup.setStatus('current')
mibBuilder.exportSymbols("HUAWEI-DAD-MIB", hwDadGroups=hwDadGroups, hwDadTrapGroup=hwDadTrapGroup, hwDadConflictDetect=hwDadConflictDetect, hwDadConflictResume=hwDadConflictResume, PortIndex=PortIndex, hwDadConformance=hwDadConformance, hwDadCompliance=hwDadCompliance, PYSNMP_MODULE_ID=hwDadMIB, hwDadCompliances=hwDadCompliances, hwDadMIB=hwDadMIB, hwDadTraps=hwDadTraps)
