#
# PySNMP MIB module PEPWAVE-MAX-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PEPWAVE-MAX-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:31:11 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
IpAddress, enterprises, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, iso, Bits, ObjectIdentity, Unsigned32, NotificationType, MibIdentifier, Integer32, Counter32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "enterprises", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "iso", "Bits", "ObjectIdentity", "Unsigned32", "NotificationType", "MibIdentifier", "Integer32", "Counter32", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
pepwaveMAX = ModuleIdentity((1, 3, 6, 1, 4, 1, 27662, 1))
pepwaveMAX.setRevisions(('2012-06-06 00:00',))
if mibBuilder.loadTexts: pepwaveMAX.setLastUpdated('201206060000Z')
if mibBuilder.loadTexts: pepwaveMAX.setOrganization('Pepwave')
class TableIndex(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class ConnectionNum(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class NameString(TextualConvention, OctetString):
    status = 'current'
    displayHint = '80a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 80)

class PortSpeedType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("unknown", 0), ("auto", 1), ("fullDulplex10", 2), ("halfDulplex10", 3), ("fullDulplex100", 4), ("halfDulplex100", 5), ("fullDulplex1000", 6), ("halfDulplex1000", 7))

maxStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 27662, 1, 1))
maxSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 27662, 1, 1, 1))
maxFirmware = MibScalar((1, 3, 6, 1, 4, 1, 27662, 1, 1, 1, 1), NameString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: maxFirmware.setStatus('current')
maxSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 27662, 1, 1, 1, 2), NameString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: maxSerialNumber.setStatus('current')
maxTime = MibScalar((1, 3, 6, 1, 4, 1, 27662, 1, 1, 1, 3), NameString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: maxTime.setStatus('current')
maxUpTime = MibScalar((1, 3, 6, 1, 4, 1, 27662, 1, 1, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: maxUpTime.setStatus('current')
maxLan = MibIdentifier((1, 3, 6, 1, 4, 1, 27662, 1, 1, 1, 6))
maxLanStatus = MibScalar((1, 3, 6, 1, 4, 1, 27662, 1, 1, 1, 6, 1), NameString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: maxLanStatus.setStatus('current')
maxLanIp = MibScalar((1, 3, 6, 1, 4, 1, 27662, 1, 1, 1, 6, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: maxLanIp.setStatus('current')
maxLanSubnetMask = MibScalar((1, 3, 6, 1, 4, 1, 27662, 1, 1, 1, 6, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: maxLanSubnetMask.setStatus('current')
maxLinkStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 27662, 1, 1, 2))
maxLinkNumber = MibScalar((1, 3, 6, 1, 4, 1, 27662, 1, 1, 2, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: maxLinkNumber.setStatus('current')
linkTable = MibTable((1, 3, 6, 1, 4, 1, 27662, 1, 1, 2, 2), )
if mibBuilder.loadTexts: linkTable.setStatus('current')
linkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 27662, 1, 1, 2, 2, 1), ).setIndexNames((0, "PEPWAVE-MAX-MIB", "linkConnNum"))
if mibBuilder.loadTexts: linkEntry.setStatus('current')
linkConnNum = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 1, 1, 2, 2, 1, 1), ConnectionNum())
if mibBuilder.loadTexts: linkConnNum.setStatus('current')
linkName = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 1, 1, 2, 2, 1, 2), NameString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: linkName.setStatus('current')
linkStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 1, 1, 2, 2, 1, 3), NameString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: linkStatus.setStatus('current')
linkThroughputIn = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 1, 1, 2, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: linkThroughputIn.setStatus('current')
linkThroughputOut = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 1, 1, 2, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: linkThroughputOut.setStatus('current')
linkDataTransferred = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 1, 1, 2, 2, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: linkDataTransferred.setStatus('current')
linkIpTable = MibTable((1, 3, 6, 1, 4, 1, 27662, 1, 1, 2, 3), )
if mibBuilder.loadTexts: linkIpTable.setStatus('current')
linkIpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 27662, 1, 1, 2, 3, 1), ).setIndexNames((0, "PEPWAVE-MAX-MIB", "linkIpConnNum"), (0, "PEPWAVE-MAX-MIB", "linkIpIndex"))
if mibBuilder.loadTexts: linkIpEntry.setStatus('current')
linkIpConnNum = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 1, 1, 2, 3, 1, 1), ConnectionNum())
if mibBuilder.loadTexts: linkIpConnNum.setStatus('current')
linkIpIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 1, 1, 2, 3, 1, 2), TableIndex())
if mibBuilder.loadTexts: linkIpIndex.setStatus('current')
linkIp = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 1, 1, 2, 3, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: linkIp.setStatus('current')
wanUsageTable = MibTable((1, 3, 6, 1, 4, 1, 27662, 1, 1, 3), )
if mibBuilder.loadTexts: wanUsageTable.setStatus('current')
wanUsageEntry = MibTableRow((1, 3, 6, 1, 4, 1, 27662, 1, 1, 3, 1), ).setIndexNames((0, "PEPWAVE-MAX-MIB", "wanUsageIndex"))
if mibBuilder.loadTexts: wanUsageEntry.setStatus('current')
wanUsageIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 1, 1, 3, 1, 1), TableIndex())
if mibBuilder.loadTexts: wanUsageIndex.setStatus('current')
wanUsageThroughputIn = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 1, 1, 3, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wanUsageThroughputIn.setStatus('current')
wanUsageThroughputOut = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 1, 1, 3, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wanUsageThroughputOut.setStatus('current')
wanUsageDataTransferred = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 1, 1, 3, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wanUsageDataTransferred.setStatus('current')
maxMaintenance = MibIdentifier((1, 3, 6, 1, 4, 1, 27662, 1, 2))
maxReboot = MibScalar((1, 3, 6, 1, 4, 1, 27662, 1, 2, 1), NameString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: maxReboot.setStatus('current')
maxLanConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 27662, 1, 3))
portLanSpeedConfig = MibScalar((1, 3, 6, 1, 4, 1, 27662, 1, 3, 1), PortSpeedType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: portLanSpeedConfig.setStatus('current')
portWanSpeedConfigTable = MibTable((1, 3, 6, 1, 4, 1, 27662, 1, 3, 2), )
if mibBuilder.loadTexts: portWanSpeedConfigTable.setStatus('current')
portWanSpeedConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 27662, 1, 3, 2, 1), ).setIndexNames((0, "PEPWAVE-MAX-MIB", "portWanSpeedConfigIndex"))
if mibBuilder.loadTexts: portWanSpeedConfigEntry.setStatus('current')
portWanSpeedConfigIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 1, 3, 2, 1, 1), TableIndex())
if mibBuilder.loadTexts: portWanSpeedConfigIndex.setStatus('current')
portWanSpeedConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 1, 3, 2, 1, 2), PortSpeedType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: portWanSpeedConfig.setStatus('current')
lanConfigIp = MibScalar((1, 3, 6, 1, 4, 1, 27662, 1, 3, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lanConfigIp.setStatus('current')
lanConfigSubnetMask = MibScalar((1, 3, 6, 1, 4, 1, 27662, 1, 3, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lanConfigSubnetMask.setStatus('current')
maxConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 27662, 1, 50))
maxCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 27662, 1, 50, 1))
maxGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 27662, 1, 50, 2))
maxCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 27662, 1, 50, 1, 1)).setObjects(("PEPWAVE-MAX-MIB", "maxSystemGroup"), ("PEPWAVE-MAX-MIB", "maxLinkGroup"), ("PEPWAVE-MAX-MIB", "maxWanGroup"), ("PEPWAVE-MAX-MIB", "maxSetGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    maxCompliance = maxCompliance.setStatus('current')
maxSystemGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 27662, 1, 50, 2, 1)).setObjects(("PEPWAVE-MAX-MIB", "maxFirmware"), ("PEPWAVE-MAX-MIB", "maxSerialNumber"), ("PEPWAVE-MAX-MIB", "maxTime"), ("PEPWAVE-MAX-MIB", "maxUpTime"), ("PEPWAVE-MAX-MIB", "maxLanStatus"), ("PEPWAVE-MAX-MIB", "maxLanIp"), ("PEPWAVE-MAX-MIB", "maxLanSubnetMask"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    maxSystemGroup = maxSystemGroup.setStatus('current')
maxLinkGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 27662, 1, 50, 2, 2)).setObjects(("PEPWAVE-MAX-MIB", "maxLinkNumber"), ("PEPWAVE-MAX-MIB", "linkName"), ("PEPWAVE-MAX-MIB", "linkStatus"), ("PEPWAVE-MAX-MIB", "linkIp"), ("PEPWAVE-MAX-MIB", "linkThroughputIn"), ("PEPWAVE-MAX-MIB", "linkThroughputOut"), ("PEPWAVE-MAX-MIB", "linkDataTransferred"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    maxLinkGroup = maxLinkGroup.setStatus('current')
maxWanGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 27662, 1, 50, 2, 3)).setObjects(("PEPWAVE-MAX-MIB", "wanUsageThroughputIn"), ("PEPWAVE-MAX-MIB", "wanUsageThroughputOut"), ("PEPWAVE-MAX-MIB", "wanUsageDataTransferred"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    maxWanGroup = maxWanGroup.setStatus('current')
maxSetGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 27662, 1, 50, 2, 4)).setObjects(("PEPWAVE-MAX-MIB", "maxReboot"), ("PEPWAVE-MAX-MIB", "portWanSpeedConfig"), ("PEPWAVE-MAX-MIB", "portLanSpeedConfig"), ("PEPWAVE-MAX-MIB", "lanConfigIp"), ("PEPWAVE-MAX-MIB", "lanConfigSubnetMask"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    maxSetGroup = maxSetGroup.setStatus('current')
mibBuilder.exportSymbols("PEPWAVE-MAX-MIB", maxLanStatus=maxLanStatus, maxConformance=maxConformance, maxReboot=maxReboot, wanUsageIndex=wanUsageIndex, NameString=NameString, pepwaveMAX=pepwaveMAX, linkName=linkName, linkIpIndex=linkIpIndex, maxWanGroup=maxWanGroup, maxCompliance=maxCompliance, maxGroups=maxGroups, linkIpConnNum=linkIpConnNum, portLanSpeedConfig=portLanSpeedConfig, maxLinkStatus=maxLinkStatus, maxLanSubnetMask=maxLanSubnetMask, maxStatus=maxStatus, wanUsageThroughputOut=wanUsageThroughputOut, PYSNMP_MODULE_ID=pepwaveMAX, portWanSpeedConfigEntry=portWanSpeedConfigEntry, maxLanConfig=maxLanConfig, linkStatus=linkStatus, linkTable=linkTable, maxLan=maxLan, wanUsageEntry=wanUsageEntry, wanUsageTable=wanUsageTable, portWanSpeedConfigIndex=portWanSpeedConfigIndex, maxUpTime=maxUpTime, linkConnNum=linkConnNum, maxTime=maxTime, linkIpEntry=linkIpEntry, maxMaintenance=maxMaintenance, maxSystemGroup=maxSystemGroup, linkIpTable=linkIpTable, linkEntry=linkEntry, maxLanIp=maxLanIp, linkDataTransferred=linkDataTransferred, linkThroughputOut=linkThroughputOut, maxSystem=maxSystem, lanConfigIp=lanConfigIp, lanConfigSubnetMask=lanConfigSubnetMask, maxFirmware=maxFirmware, linkThroughputIn=linkThroughputIn, wanUsageThroughputIn=wanUsageThroughputIn, maxLinkNumber=maxLinkNumber, portWanSpeedConfigTable=portWanSpeedConfigTable, TableIndex=TableIndex, wanUsageDataTransferred=wanUsageDataTransferred, linkIp=linkIp, maxLinkGroup=maxLinkGroup, ConnectionNum=ConnectionNum, portWanSpeedConfig=portWanSpeedConfig, maxCompliances=maxCompliances, maxSerialNumber=maxSerialNumber, maxSetGroup=maxSetGroup, PortSpeedType=PortSpeedType)
