#
# PySNMP MIB module ZXR10-MSTP (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZXR10-MSTP
# Produced by pysmi-0.3.4 at Wed May  1 15:48:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, Gauge32, ModuleIdentity, NotificationType, iso, TimeTicks, Integer32, MibIdentifier, Bits, ObjectIdentity, Unsigned32, Counter64, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Gauge32", "ModuleIdentity", "NotificationType", "iso", "TimeTicks", "Integer32", "MibIdentifier", "Bits", "ObjectIdentity", "Unsigned32", "Counter64", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString")
zxr10, = mibBuilder.importSymbols("ZXR10-SMI", "zxr10")
mstpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 3902, 3, 127))
if mibBuilder.loadTexts: mstpMIB.setLastUpdated('200609010000Z')
if mibBuilder.loadTexts: mstpMIB.setOrganization('ZTE Corporation')
if mibBuilder.loadTexts: mstpMIB.setContactInfo('ZTE Corporation Nanjing Institute of ZTE Corporation No.68 ZiJinghua Rd. YuHuatai District, Nanjing, China Tel: +86-25-52870000')
if mibBuilder.loadTexts: mstpMIB.setDescription('ZXROS V4.6.03B MSTP MIB')
mstpMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1))
class UINT32(Unsigned32):
    pass

class Char(OctetString):
    pass

class MSTPProtocolType(TextualConvention, Integer32):
    description = 'Spanning Tree Protocol Type'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("disabled", 0), ("sstp", 1), ("rstp", 2), ("mstp", 3))

class MSTPTransportType(TextualConvention, Integer32):
    description = 'Data Packets Transport Type'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("untransparent", 0), ("transparent", 1))

class MSTPPortEnable(TextualConvention, Integer32):
    description = 'Whether Stp Run in Port'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("portstpunused", 0), ("portstpused", 1))

class MSTPLinkType(TextualConvention, Integer32):
    description = 'Link Type'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("share", 0), ("p2p", 1), ("auto", 2))

class MSTPEdgePortEnable(TextualConvention, Integer32):
    description = 'Whether Edge Port'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("edge-disable", 0), ("edge-enable", 1))

class MSTPBPDUGuardEnable(TextualConvention, Integer32):
    description = 'BPDU Guard Function'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("bpduguarddisable", 0), ("bpduguardenable", 1))

class MSTPPacketType(TextualConvention, Integer32):
    description = 'Packet Type'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("ieee", 0), ("cisco", 1), ("hammer", 2), ("huawei", 3))

class MSTPPortStatus(TextualConvention, Integer32):
    description = 'Port Status'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("disabled", 0), ("blocking", 1), ("listening", 2), ("learning", 3), ("forwarding", 4), ("broken", 5))

class MSTPRootGuardEnable(TextualConvention, Integer32):
    description = 'Root Guard Function'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("rootguarddisable", 0), ("rootguardenable", 1))

class MSTPLoopGuardEnable(TextualConvention, Integer32):
    description = 'Loop Guard Function'
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
if mibBuilder.loadTexts: stpProtocolSpecification.setDescription('Configure STP Protocol Type.')
stpMaxAge = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 1, 2), UINT32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stpMaxAge.setStatus('current')
if mibBuilder.loadTexts: stpMaxAge.setDescription('Root Bridge Max Age.')
stpHelloTime = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 1, 3), UINT32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stpHelloTime.setStatus('current')
if mibBuilder.loadTexts: stpHelloTime.setDescription('Root Bridge Hello Time.')
stpHoldTime = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 1, 4), UINT32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stpHoldTime.setStatus('current')
if mibBuilder.loadTexts: stpHoldTime.setDescription('Root Bridge Hold Time.')
stpForwardDelay = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 1, 5), UINT32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stpForwardDelay.setStatus('current')
if mibBuilder.loadTexts: stpForwardDelay.setDescription('Root Bridge Forward Delay Time.')
stpBridgeMaxAge = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 1, 6), UINT32().subtype(subtypeSpec=ValueRangeConstraint(6, 40))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stpBridgeMaxAge.setStatus('current')
if mibBuilder.loadTexts: stpBridgeMaxAge.setDescription('Bridge Max Age.')
stpBridgeHelloTime = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 1, 7), UINT32().subtype(subtypeSpec=ValueRangeConstraint(1, 10))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stpBridgeHelloTime.setStatus('current')
if mibBuilder.loadTexts: stpBridgeHelloTime.setDescription('Bridge Hello Time.')
stpBridgeForwardDelay = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 1, 8), UINT32().subtype(subtypeSpec=ValueRangeConstraint(4, 30))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stpBridgeForwardDelay.setStatus('current')
if mibBuilder.loadTexts: stpBridgeForwardDelay.setDescription('Bridge Forward Delay Time.')
stpTransparentEnable = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 1, 9), MSTPTransportType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stpTransparentEnable.setStatus('current')
if mibBuilder.loadTexts: stpTransparentEnable.setDescription('Packet Transparent method.')
stpRevision = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 1, 10), UINT32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stpRevision.setStatus('current')
if mibBuilder.loadTexts: stpRevision.setDescription('Vision.')
stpConfigName = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 1, 11), Char().subtype(subtypeSpec=ValueSizeConstraint(0, 33))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stpConfigName.setStatus('current')
if mibBuilder.loadTexts: stpConfigName.setDescription('Bridge Name in Region.')
stpHmd5Digest = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 1, 12), Char().subtype(subtypeSpec=ValueSizeConstraint(0, 35))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stpHmd5Digest.setStatus('current')
if mibBuilder.loadTexts: stpHmd5Digest.setDescription('Hmd5Digest.')
stpHmd5Key = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 1, 13), Char().subtype(subtypeSpec=ValueSizeConstraint(0, 35))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stpHmd5Key.setStatus('current')
if mibBuilder.loadTexts: stpHmd5Key.setDescription('Hmd5Key.')
mstpInstanceTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 2, 1), )
if mibBuilder.loadTexts: mstpInstanceTable.setStatus('current')
if mibBuilder.loadTexts: mstpInstanceTable.setDescription('Configure MSTP instance parameters.')
mstpInstanceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 2, 1, 1), ).setIndexNames((0, "ZXR10-MSTP", "stpInstanceID"))
if mibBuilder.loadTexts: mstpInstanceEntry.setStatus('current')
if mibBuilder.loadTexts: mstpInstanceEntry.setDescription('Each row index by StpInstanceID And contain imformation of Instance.')
stpInstanceID = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 2, 1, 1, 1), UINT32().subtype(subtypeSpec=ValueRangeConstraint(0, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stpInstanceID.setStatus('current')
if mibBuilder.loadTexts: stpInstanceID.setDescription('Instance ID.')
stpBridgePriority = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 2, 1, 1, 2), UINT32().subtype(subtypeSpec=ValueRangeConstraint(0, 61440))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stpBridgePriority.setStatus('current')
if mibBuilder.loadTexts: stpBridgePriority.setDescription('Bridge Priority.')
stpBridgeMac = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 2, 1, 1, 3), Char()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stpBridgeMac.setStatus('current')
if mibBuilder.loadTexts: stpBridgeMac.setDescription('Bridge Mac.')
stpInstanceRootPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 2, 1, 1, 4), UINT32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stpInstanceRootPriority.setStatus('current')
if mibBuilder.loadTexts: stpInstanceRootPriority.setDescription('Instance Root Bridge Priority.')
stpInstanceRootMac = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 2, 1, 1, 5), Char()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stpInstanceRootMac.setStatus('current')
if mibBuilder.loadTexts: stpInstanceRootMac.setDescription('Instance Root Bridge Mac.')
stpRemainHops = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 2, 1, 1, 6), UINT32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stpRemainHops.setStatus('current')
if mibBuilder.loadTexts: stpRemainHops.setDescription('BPDU Packet Reamin Hops.')
stpVlanMaps = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 2, 1, 1, 7), Char().subtype(subtypeSpec=ValueSizeConstraint(100, 100)).setFixedLength(100)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stpVlanMaps.setStatus('current')
if mibBuilder.loadTexts: stpVlanMaps.setDescription("VLAN Tag spearated by ',' or '-'.")
stpMAXHops = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 2, 1, 1, 8), UINT32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stpMAXHops.setStatus('current')
if mibBuilder.loadTexts: stpMAXHops.setDescription('Root Bridge Max Hops.')
stpBridgeMAXHops = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 2, 1, 1, 9), UINT32().subtype(subtypeSpec=ValueRangeConstraint(1, 40))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stpBridgeMAXHops.setStatus('current')
if mibBuilder.loadTexts: stpBridgeMAXHops.setDescription('Bridge Max Hops.')
stpInstanceRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 2, 1, 1, 10), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stpInstanceRowStatus.setStatus('current')
if mibBuilder.loadTexts: stpInstanceRowStatus.setDescription('This variable is used to create, modify, and/or delete a row in this table.')
mstpPortTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 3, 1), )
if mibBuilder.loadTexts: mstpPortTable.setStatus('current')
if mibBuilder.loadTexts: mstpPortTable.setDescription('Configure MSTP Port parameters.')
mstpPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 3, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: mstpPortEntry.setStatus('current')
if mibBuilder.loadTexts: mstpPortEntry.setDescription('Each row index by ifIndex And contain stp imformation of Port.')
stpPortEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 3, 1, 1, 1), MSTPPortEnable()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stpPortEnable.setStatus('current')
if mibBuilder.loadTexts: stpPortEnable.setDescription('STP Protocol status on port.')
stpLinkType = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 3, 1, 1, 2), MSTPLinkType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stpLinkType.setStatus('current')
if mibBuilder.loadTexts: stpLinkType.setDescription('Link Type.')
stpEdgedPortEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 3, 1, 1, 3), MSTPEdgePortEnable()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stpEdgedPortEnable.setStatus('current')
if mibBuilder.loadTexts: stpEdgedPortEnable.setDescription('Whether EdgedPort.')
stpBPDUGuardEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 3, 1, 1, 4), MSTPBPDUGuardEnable()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stpBPDUGuardEnable.setStatus('current')
if mibBuilder.loadTexts: stpBPDUGuardEnable.setDescription('BPDU Guard Function status.')
stpPacketType = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 3, 1, 1, 5), MSTPPacketType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stpPacketType.setStatus('current')
if mibBuilder.loadTexts: stpPacketType.setDescription('BPDU Packet Type.')
stpIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 3, 1, 1, 6), Char()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stpIfName.setStatus('current')
if mibBuilder.loadTexts: stpIfName.setDescription('Interface Name.')
mstpPortInstanceTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 4, 1), )
if mibBuilder.loadTexts: mstpPortInstanceTable.setStatus('current')
if mibBuilder.loadTexts: mstpPortInstanceTable.setDescription('Configure MSTP Port Instance parameters.')
mstpPortInstanceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 4, 1, 1), ).setIndexNames((0, "ZXR10-MSTP", "stpPortInstanceID"), (0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: mstpPortInstanceEntry.setStatus('current')
if mibBuilder.loadTexts: mstpPortInstanceEntry.setDescription('Each row index by stpPortInstanceID and ifIndex And contain imformation of Port-Instance.')
stpPortInstanceID = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 4, 1, 1, 1), UINT32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stpPortInstanceID.setStatus('current')
if mibBuilder.loadTexts: stpPortInstanceID.setDescription('Instance ID.')
stpPortName = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 4, 1, 1, 2), Char()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stpPortName.setStatus('current')
if mibBuilder.loadTexts: stpPortName.setDescription('Interface Name.')
stpPortPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 4, 1, 1, 3), UINT32().subtype(subtypeSpec=ValueRangeConstraint(0, 240))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stpPortPriority.setStatus('current')
if mibBuilder.loadTexts: stpPortPriority.setDescription('Port Priority.')
stpPortPathCost = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 4, 1, 1, 4), UINT32().subtype(subtypeSpec=ValueRangeConstraint(1, 2000000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stpPortPathCost.setStatus('current')
if mibBuilder.loadTexts: stpPortPathCost.setDescription('Port Cost.')
stpPortState = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 4, 1, 1, 5), MSTPPortStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stpPortState.setStatus('current')
if mibBuilder.loadTexts: stpPortState.setDescription('Port Status.')
stpPortDesignatedCost = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 4, 1, 1, 6), UINT32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stpPortDesignatedCost.setStatus('current')
if mibBuilder.loadTexts: stpPortDesignatedCost.setDescription('Cost To Root Bridge.')
stpPortDesignatedBridgePriority = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 4, 1, 1, 7), UINT32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stpPortDesignatedBridgePriority.setStatus('current')
if mibBuilder.loadTexts: stpPortDesignatedBridgePriority.setDescription('Priority of Designated Bridge.')
stpPortDesignatedBridgeMac = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 4, 1, 1, 8), Char()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stpPortDesignatedBridgeMac.setStatus('current')
if mibBuilder.loadTexts: stpPortDesignatedBridgeMac.setDescription('MAC address of Designated Bridge.')
stpPortDesignatedPort = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 4, 1, 1, 9), UINT32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stpPortDesignatedPort.setStatus('current')
if mibBuilder.loadTexts: stpPortDesignatedPort.setDescription('Port ID.')
stpRootGuardEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 4, 1, 1, 10), MSTPRootGuardEnable()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stpRootGuardEnable.setStatus('current')
if mibBuilder.loadTexts: stpRootGuardEnable.setDescription('Root Guard Function Status.')
stpLoopGuardEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 4, 1, 1, 11), MSTPLoopGuardEnable()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stpLoopGuardEnable.setStatus('current')
if mibBuilder.loadTexts: stpLoopGuardEnable.setDescription('Loop Guard Function Status.')
mibBuilder.exportSymbols("ZXR10-MSTP", PYSNMP_MODULE_ID=mstpMIB, stpConfigName=stpConfigName, mstpPortInstanceTable=mstpPortInstanceTable, stpBridgeMAXHops=stpBridgeMAXHops, stpPortInstanceID=stpPortInstanceID, stpPortDesignatedPort=stpPortDesignatedPort, mstpPortInstanceEntry=mstpPortInstanceEntry, stpBPDUGuardEnable=stpBPDUGuardEnable, stpPortPathCost=stpPortPathCost, mstpPortTable=mstpPortTable, stpPortDesignatedBridgeMac=stpPortDesignatedBridgeMac, stpRevision=stpRevision, stpBridgeMac=stpBridgeMac, MSTPPortEnable=MSTPPortEnable, stpHoldTime=stpHoldTime, stpBridgeHelloTime=stpBridgeHelloTime, stpPortState=stpPortState, mstpInstance=mstpInstance, UINT32=UINT32, mstpInstanceTable=mstpInstanceTable, MSTPEdgePortEnable=MSTPEdgePortEnable, stpForwardDelay=stpForwardDelay, MSTPPacketType=MSTPPacketType, mstpPortInstance=mstpPortInstance, stpHmd5Digest=stpHmd5Digest, stpHmd5Key=stpHmd5Key, MSTPPortStatus=MSTPPortStatus, stpLinkType=stpLinkType, stpRootGuardEnable=stpRootGuardEnable, stpInstanceRowStatus=stpInstanceRowStatus, stpPortEnable=stpPortEnable, mstpMIB=mstpMIB, stpPortName=stpPortName, MSTPLinkType=MSTPLinkType, stpPortDesignatedCost=stpPortDesignatedCost, stpProtocolSpecification=stpProtocolSpecification, stpBridgeMaxAge=stpBridgeMaxAge, mstpPortEntry=mstpPortEntry, stpInstanceID=stpInstanceID, stpPortPriority=stpPortPriority, stpMaxAge=stpMaxAge, stpInstanceRootMac=stpInstanceRootMac, stpPortDesignatedBridgePriority=stpPortDesignatedBridgePriority, stpRemainHops=stpRemainHops, mstpGlobalPara=mstpGlobalPara, MSTPProtocolType=MSTPProtocolType, stpPacketType=stpPacketType, stpVlanMaps=stpVlanMaps, MSTPBPDUGuardEnable=MSTPBPDUGuardEnable, MSTPRootGuardEnable=MSTPRootGuardEnable, mstpMibObjects=mstpMibObjects, stpBridgePriority=stpBridgePriority, MSTPLoopGuardEnable=MSTPLoopGuardEnable, Char=Char, stpBridgeForwardDelay=stpBridgeForwardDelay, stpHelloTime=stpHelloTime, stpLoopGuardEnable=stpLoopGuardEnable, mstpPort=mstpPort, stpEdgedPortEnable=stpEdgedPortEnable, mstpInstanceEntry=mstpInstanceEntry, stpInstanceRootPriority=stpInstanceRootPriority, stpIfName=stpIfName, MSTPTransportType=MSTPTransportType, stpTransparentEnable=stpTransparentEnable, stpMAXHops=stpMAXHops)
