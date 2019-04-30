#
# PySNMP MIB module ZXR10-MSTP (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZXR10-MSTP
# Produced by pysmi-0.3.4 at Mon Apr 29 21:42:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, ModuleIdentity, IpAddress, Gauge32, iso, TimeTicks, Counter64, NotificationType, Counter32, Bits, Integer32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "ModuleIdentity", "IpAddress", "Gauge32", "iso", "TimeTicks", "Counter64", "NotificationType", "Counter32", "Bits", "Integer32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier")
TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString")
zxr10, = mibBuilder.importSymbols("ZXR10-SMI", "zxr10")
mstpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 3902, 3, 127))
if mibBuilder.loadTexts: mstpMIB.setLastUpdated('200609010000Z')
if mibBuilder.loadTexts: mstpMIB.setOrganization('ZTE Corporation')
mstpMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1))
class UINT32(Unsigned32):
    pass

class Char(OctetString):
    pass

class MSTPProtocolType(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("disabled", 0), ("sstp", 1), ("rstp", 2), ("mstp", 3))

class MSTPTransportType(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("untransparent", 0), ("transparent", 1))

class MSTPPortEnable(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("portstpunused", 0), ("portstpused", 1))

class MSTPLinkType(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("share", 0), ("p2p", 1), ("auto", 2))

class MSTPEdgePortEnable(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("edge-disable", 0), ("edge-enable", 1))

class MSTPBPDUGuardEnable(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("bpduguarddisable", 0), ("bpduguardenable", 1))

class MSTPPacketType(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("ieee", 0), ("cisco", 1), ("hammer", 2), ("huawei", 3))

class MSTPPortStatus(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("disabled", 0), ("blocking", 1), ("listening", 2), ("learning", 3), ("forwarding", 4), ("broken", 5))

class MSTPRootGuardEnable(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("rootguarddisable", 0), ("rootguardenable", 1))

class MSTPLoopGuardEnable(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("loopguarddisable", 0), ("loopguardenable", 1))

mstpGlobalPara = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 1))
mstpInstance = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 2))
mstpPort = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 3))
mstpPortInstance = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 4))
stpProtocolSpecification = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 1, 1), MSTPProtocolType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stpProtocolSpecification.setStatus('current')
stpMaxAge = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 1, 2), UINT32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stpMaxAge.setStatus('current')
stpHelloTime = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 1, 3), UINT32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stpHelloTime.setStatus('current')
stpHoldTime = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 1, 4), UINT32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stpHoldTime.setStatus('current')
stpForwardDelay = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 1, 5), UINT32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stpForwardDelay.setStatus('current')
stpBridgeMaxAge = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 1, 6), UINT32().subtype(subtypeSpec=ValueRangeConstraint(6, 40))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stpBridgeMaxAge.setStatus('current')
stpBridgeHelloTime = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 1, 7), UINT32().subtype(subtypeSpec=ValueRangeConstraint(1, 10))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stpBridgeHelloTime.setStatus('current')
stpBridgeForwardDelay = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 1, 8), UINT32().subtype(subtypeSpec=ValueRangeConstraint(4, 30))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stpBridgeForwardDelay.setStatus('current')
stpTransparentEnable = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 1, 9), MSTPTransportType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stpTransparentEnable.setStatus('current')
stpRevision = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 1, 10), UINT32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stpRevision.setStatus('current')
stpConfigName = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 1, 11), Char().subtype(subtypeSpec=ValueSizeConstraint(0, 33))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stpConfigName.setStatus('current')
stpHmd5Digest = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 1, 12), Char().subtype(subtypeSpec=ValueSizeConstraint(0, 35))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stpHmd5Digest.setStatus('current')
stpHmd5Key = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 1, 13), Char().subtype(subtypeSpec=ValueSizeConstraint(0, 35))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stpHmd5Key.setStatus('current')
mstpInstanceTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 2, 1), )
if mibBuilder.loadTexts: mstpInstanceTable.setStatus('current')
mstpInstanceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 2, 1, 1), ).setIndexNames((0, "ZXR10-MSTP", "stpInstanceID"))
if mibBuilder.loadTexts: mstpInstanceEntry.setStatus('current')
stpInstanceID = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 2, 1, 1, 1), UINT32().subtype(subtypeSpec=ValueRangeConstraint(0, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stpInstanceID.setStatus('current')
stpBridgePriority = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 2, 1, 1, 2), UINT32().subtype(subtypeSpec=ValueRangeConstraint(0, 61440))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stpBridgePriority.setStatus('current')
stpBridgeMac = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 2, 1, 1, 3), Char()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stpBridgeMac.setStatus('current')
stpInstanceRootPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 2, 1, 1, 4), UINT32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stpInstanceRootPriority.setStatus('current')
stpInstanceRootMac = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 2, 1, 1, 5), Char()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stpInstanceRootMac.setStatus('current')
stpRemainHops = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 2, 1, 1, 6), UINT32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stpRemainHops.setStatus('current')
stpVlanMaps = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 2, 1, 1, 7), Char().subtype(subtypeSpec=ValueSizeConstraint(100, 100)).setFixedLength(100)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stpVlanMaps.setStatus('current')
stpMAXHops = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 2, 1, 1, 8), UINT32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stpMAXHops.setStatus('current')
stpBridgeMAXHops = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 2, 1, 1, 9), UINT32().subtype(subtypeSpec=ValueRangeConstraint(1, 40))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stpBridgeMAXHops.setStatus('current')
stpInstanceRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 2, 1, 1, 10), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stpInstanceRowStatus.setStatus('current')
mstpPortTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 3, 1), )
if mibBuilder.loadTexts: mstpPortTable.setStatus('current')
mstpPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 3, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: mstpPortEntry.setStatus('current')
stpPortEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 3, 1, 1, 1), MSTPPortEnable()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stpPortEnable.setStatus('current')
stpLinkType = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 3, 1, 1, 2), MSTPLinkType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stpLinkType.setStatus('current')
stpEdgedPortEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 3, 1, 1, 3), MSTPEdgePortEnable()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stpEdgedPortEnable.setStatus('current')
stpBPDUGuardEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 3, 1, 1, 4), MSTPBPDUGuardEnable()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stpBPDUGuardEnable.setStatus('current')
stpPacketType = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 3, 1, 1, 5), MSTPPacketType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stpPacketType.setStatus('current')
stpIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 3, 1, 1, 6), Char()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stpIfName.setStatus('current')
mstpPortInstanceTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 4, 1), )
if mibBuilder.loadTexts: mstpPortInstanceTable.setStatus('current')
mstpPortInstanceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 4, 1, 1), ).setIndexNames((0, "ZXR10-MSTP", "stpPortInstanceID"), (0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: mstpPortInstanceEntry.setStatus('current')
stpPortInstanceID = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 4, 1, 1, 1), UINT32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stpPortInstanceID.setStatus('current')
stpPortName = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 4, 1, 1, 2), Char()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stpPortName.setStatus('current')
stpPortPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 4, 1, 1, 3), UINT32().subtype(subtypeSpec=ValueRangeConstraint(0, 240))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stpPortPriority.setStatus('current')
stpPortPathCost = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 4, 1, 1, 4), UINT32().subtype(subtypeSpec=ValueRangeConstraint(1, 2000000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stpPortPathCost.setStatus('current')
stpPortState = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 4, 1, 1, 5), MSTPPortStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stpPortState.setStatus('current')
stpPortDesignatedCost = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 4, 1, 1, 6), UINT32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stpPortDesignatedCost.setStatus('current')
stpPortDesignatedBridgePriority = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 4, 1, 1, 7), UINT32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stpPortDesignatedBridgePriority.setStatus('current')
stpPortDesignatedBridgeMac = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 4, 1, 1, 8), Char()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stpPortDesignatedBridgeMac.setStatus('current')
stpPortDesignatedPort = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 4, 1, 1, 9), UINT32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stpPortDesignatedPort.setStatus('current')
stpRootGuardEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 4, 1, 1, 10), MSTPRootGuardEnable()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stpRootGuardEnable.setStatus('current')
stpLoopGuardEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 4, 1, 1, 11), MSTPLoopGuardEnable()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stpLoopGuardEnable.setStatus('current')
mibBuilder.exportSymbols("ZXR10-MSTP", MSTPEdgePortEnable=MSTPEdgePortEnable, mstpPort=mstpPort, MSTPRootGuardEnable=MSTPRootGuardEnable, stpBridgePriority=stpBridgePriority, MSTPLoopGuardEnable=MSTPLoopGuardEnable, stpPortPathCost=stpPortPathCost, stpVlanMaps=stpVlanMaps, mstpPortEntry=mstpPortEntry, mstpPortInstanceTable=mstpPortInstanceTable, mstpInstanceTable=mstpInstanceTable, stpLoopGuardEnable=stpLoopGuardEnable, mstpMIB=mstpMIB, MSTPProtocolType=MSTPProtocolType, stpHmd5Digest=stpHmd5Digest, MSTPPortStatus=MSTPPortStatus, stpIfName=stpIfName, stpPortDesignatedBridgeMac=stpPortDesignatedBridgeMac, mstpInstance=mstpInstance, stpMaxAge=stpMaxAge, stpPortInstanceID=stpPortInstanceID, stpPacketType=stpPacketType, stpPortDesignatedCost=stpPortDesignatedCost, stpHmd5Key=stpHmd5Key, stpPortDesignatedBridgePriority=stpPortDesignatedBridgePriority, mstpMibObjects=mstpMibObjects, stpTransparentEnable=stpTransparentEnable, stpInstanceRootMac=stpInstanceRootMac, stpPortEnable=stpPortEnable, UINT32=UINT32, stpInstanceID=stpInstanceID, mstpPortInstanceEntry=mstpPortInstanceEntry, stpBPDUGuardEnable=stpBPDUGuardEnable, stpBridgeMaxAge=stpBridgeMaxAge, stpLinkType=stpLinkType, stpProtocolSpecification=stpProtocolSpecification, stpEdgedPortEnable=stpEdgedPortEnable, mstpPortInstance=mstpPortInstance, stpPortState=stpPortState, stpConfigName=stpConfigName, PYSNMP_MODULE_ID=mstpMIB, MSTPTransportType=MSTPTransportType, MSTPPacketType=MSTPPacketType, stpHelloTime=stpHelloTime, stpBridgeMac=stpBridgeMac, MSTPPortEnable=MSTPPortEnable, stpRemainHops=stpRemainHops, stpPortDesignatedPort=stpPortDesignatedPort, stpBridgeMAXHops=stpBridgeMAXHops, mstpPortTable=mstpPortTable, stpForwardDelay=stpForwardDelay, stpPortPriority=stpPortPriority, stpBridgeHelloTime=stpBridgeHelloTime, mstpInstanceEntry=mstpInstanceEntry, stpRevision=stpRevision, stpHoldTime=stpHoldTime, stpRootGuardEnable=stpRootGuardEnable, MSTPBPDUGuardEnable=MSTPBPDUGuardEnable, mstpGlobalPara=mstpGlobalPara, stpInstanceRootPriority=stpInstanceRootPriority, stpInstanceRowStatus=stpInstanceRowStatus, stpBridgeForwardDelay=stpBridgeForwardDelay, Char=Char, stpPortName=stpPortName, MSTPLinkType=MSTPLinkType, stpMAXHops=stpMAXHops)
