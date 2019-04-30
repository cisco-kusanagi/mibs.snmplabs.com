#
# PySNMP MIB module XEDIA-NETWORK-TIME-PROTOCOL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/XEDIA-NETWORK-TIME-PROTOCOL-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:36:29 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Integer32, Gauge32, MibIdentifier, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, ObjectIdentity, NotificationType, IpAddress, iso, TimeTicks, ModuleIdentity, Bits, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Gauge32", "MibIdentifier", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "ObjectIdentity", "NotificationType", "IpAddress", "iso", "TimeTicks", "ModuleIdentity", "Bits", "Counter64")
TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString")
xediaMibs, = mibBuilder.importSymbols("XEDIA-REG", "xediaMibs")
xediaNetworkTimeProtocolMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 838, 3, 26))
if mibBuilder.loadTexts: xediaNetworkTimeProtocolMIB.setLastUpdated('9812151655Z')
if mibBuilder.loadTexts: xediaNetworkTimeProtocolMIB.setOrganization('Xedia Corp.')
xntpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 838, 3, 26, 1))
xntpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 838, 3, 26, 2))
class XntpIpAddress(TextualConvention, IpAddress):
    status = 'current'

class XntpPort(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 65535)

class XntpDateAndTime(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(26, 26)
    fixedLength = 26

class XntpSeconds(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(13, 13)
    fixedLength = 13

class XntpAssociationMode(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("unspecifed", 0), ("symActive", 1), ("symPassive", 2), ("client", 3), ("server", 4))

class XntpLeapIndication(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("noWarning", 0), ("insertSecond", 1), ("deleteSecond", 2), ("unsyncronized", 3))

class XntpCounter(TextualConvention, Counter32):
    status = 'current'
    displayHint = 'd'

class XntpAssociationCondition(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("rejected", 0), ("eliminated", 1), ("falseticker", 2), ("outlyer", 3), ("syncCandidate", 4), ("distSysPeer", 5), ("sysPeer", 6))

class XntpReachability(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'o'

xntpSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 1))
xntpAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xntpAdminStatus.setStatus('current')
xntpSrcAddressStatus = MibScalar((1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xntpSrcAddressStatus.setStatus('current')
xntpStratum = MibScalar((1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xntpStratum.setStatus('current')
xntpMode = MibScalar((1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 1, 4), XntpAssociationMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xntpMode.setStatus('current')
xntpPrecision = MibScalar((1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xntpPrecision.setStatus('current')
xntpClockSource = MibScalar((1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 1, 6), XntpIpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xntpClockSource.setStatus('current')
xntpPollInterval = MibScalar((1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xntpPollInterval.setStatus('current')
xntpLeapIndicator = MibScalar((1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 1, 8), XntpLeapIndication()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xntpLeapIndicator.setStatus('current')
xntpRootDelay = MibScalar((1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 1, 9), XntpSeconds()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xntpRootDelay.setStatus('current')
xntpRootDispersion = MibScalar((1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 1, 10), XntpSeconds()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xntpRootDispersion.setStatus('current')
xntpReferenceTimestamp = MibScalar((1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 1, 11), XntpDateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xntpReferenceTimestamp.setStatus('current')
xntpLocalTime = MibScalar((1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 1, 12), XntpDateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xntpLocalTime.setStatus('current')
xntpCounters = MibIdentifier((1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 2))
xntpPacketsIn = MibScalar((1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 2, 1), XntpCounter()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xntpPacketsIn.setStatus('current')
xntpBadVersion = MibScalar((1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 2, 2), XntpCounter()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xntpBadVersion.setStatus('current')
xntpBadStratum = MibScalar((1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 2, 3), XntpCounter()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xntpBadStratum.setStatus('current')
xntpBadLength = MibScalar((1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 2, 4), XntpCounter()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xntpBadLength.setStatus('current')
xntpBadMode = MibScalar((1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 2, 5), XntpCounter()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xntpBadMode.setStatus('current')
xntpBadHeader = MibScalar((1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 2, 6), XntpCounter()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xntpBadHeader.setStatus('current')
xntpBadData = MibScalar((1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 2, 7), XntpCounter()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xntpBadData.setStatus('current')
xntpPacketsOut = MibScalar((1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 2, 8), XntpCounter()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xntpPacketsOut.setStatus('current')
xntpPhaseAdjustments = MibScalar((1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 2, 9), XntpCounter()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xntpPhaseAdjustments.setStatus('current')
xntpStepAdjustments = MibScalar((1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 2, 10), XntpCounter()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xntpStepAdjustments.setStatus('current')
xntpServerTable = MibTable((1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 3), )
if mibBuilder.loadTexts: xntpServerTable.setStatus('current')
xntpServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 3, 1), ).setIndexNames((0, "XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpServer"))
if mibBuilder.loadTexts: xntpServerEntry.setStatus('current')
xntpServer = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 3, 1, 1), XntpIpAddress())
if mibBuilder.loadTexts: xntpServer.setStatus('current')
xntpServerVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 3, 1, 2), Integer32().clone(3)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: xntpServerVersion.setStatus('current')
xntpServerMinPoll = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 3, 1, 3), Integer32().clone(6)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: xntpServerMinPoll.setStatus('current')
xntpServerMaxPoll = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 3, 1, 4), Integer32().clone(10)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: xntpServerMaxPoll.setStatus('current')
xntpServerRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 3, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: xntpServerRowStatus.setStatus('current')
xntpSAPeerTable = MibTable((1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 4), )
if mibBuilder.loadTexts: xntpSAPeerTable.setStatus('current')
xntpSAPeerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 4, 1), ).setIndexNames((0, "XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpSAPeer"))
if mibBuilder.loadTexts: xntpSAPeerEntry.setStatus('current')
xntpSAPeer = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 4, 1, 1), XntpIpAddress())
if mibBuilder.loadTexts: xntpSAPeer.setStatus('current')
xntpSAPeerVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 4, 1, 2), Integer32().clone(3)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: xntpSAPeerVersion.setStatus('current')
xntpSAPeerMinPoll = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 4, 1, 3), Integer32().clone(6)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: xntpSAPeerMinPoll.setStatus('current')
xntpSAPeerMaxPoll = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 4, 1, 4), Integer32().clone(10)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: xntpSAPeerMaxPoll.setStatus('current')
xntpSAPeerRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 4, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: xntpSAPeerRowStatus.setStatus('current')
xntpAssocTable = MibTable((1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 5), )
if mibBuilder.loadTexts: xntpAssocTable.setStatus('current')
xntpAssocEntry = MibTableRow((1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 5, 1), ).setIndexNames((0, "XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpAssocPeerAddr"))
if mibBuilder.loadTexts: xntpAssocEntry.setStatus('current')
xntpAssocPeerAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 5, 1, 1), XntpIpAddress())
if mibBuilder.loadTexts: xntpAssocPeerAddr.setStatus('current')
xntpAssocPeerPort = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 5, 1, 2), XntpPort()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xntpAssocPeerPort.setStatus('current')
xntpAssocPeerPoll = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 5, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xntpAssocPeerPoll.setStatus('current')
xntpAssocHostAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 5, 1, 4), XntpIpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xntpAssocHostAddr.setStatus('current')
xntpAssocHostPort = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 5, 1, 5), XntpPort()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xntpAssocHostPort.setStatus('current')
xntpAssocHostPoll = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 5, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xntpAssocHostPoll.setStatus('current')
xntpAssocHostMode = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 5, 1, 7), XntpAssociationMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xntpAssocHostMode.setStatus('current')
xntpAssocPeerMode = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 5, 1, 8), XntpAssociationMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xntpAssocPeerMode.setStatus('current')
xntpAssocPeerStratum = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 5, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xntpAssocPeerStratum.setStatus('current')
xntpAssocPeerPrecision = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 5, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xntpAssocPeerPrecision.setStatus('current')
xntpAssocPeerLeap = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 5, 1, 11), XntpLeapIndication()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xntpAssocPeerLeap.setStatus('current')
xntpAssocPeerCondition = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 5, 1, 12), XntpAssociationCondition()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xntpAssocPeerCondition.setStatus('current')
xntpAssocPeerConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 5, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("dynamic", 0), ("configured", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xntpAssocPeerConfig.setStatus('current')
xntpAssocPeerRootDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 5, 1, 14), XntpSeconds()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xntpAssocPeerRootDelay.setStatus('current')
xntpAssocPeerRootDispersion = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 5, 1, 15), XntpSeconds()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xntpAssocPeerRootDispersion.setStatus('current')
xntpAssocPeerOffset = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 5, 1, 16), XntpSeconds()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xntpAssocPeerOffset.setStatus('current')
xntpAssocPeerDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 5, 1, 17), XntpSeconds()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xntpAssocPeerDelay.setStatus('current')
xntpAssocPeerDispersion = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 5, 1, 18), XntpSeconds()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xntpAssocPeerDispersion.setStatus('current')
xntpAssocPeerReachability = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 5, 1, 19), XntpReachability()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xntpAssocPeerReachability.setStatus('current')
xntpAssocPeerRefrTimestamp = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 5, 1, 20), XntpDateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xntpAssocPeerRefrTimestamp.setStatus('current')
xntpAssocPeerXmitTimestamp = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 5, 1, 21), XntpDateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xntpAssocPeerXmitTimestamp.setStatus('current')
xntpAssocPeerOrigTimestamp = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 5, 1, 22), XntpDateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xntpAssocPeerOrigTimestamp.setStatus('current')
xntpAssocPeerRecvTimestamp = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 26, 1, 5, 1, 23), XntpDateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xntpAssocPeerRecvTimestamp.setStatus('current')
xntpCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 838, 3, 26, 2, 1))
xntpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 838, 3, 26, 2, 2))
xntpCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 838, 3, 26, 2, 1, 1)).setObjects(("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpSystemGroup"), ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpCountersGroup"), ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpServerGroup"), ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpSAPeerGroup"), ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpAssocGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    xntpCompliance = xntpCompliance.setStatus('current')
xntpSystemGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 838, 3, 26, 2, 2, 1)).setObjects(("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpAdminStatus"), ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpSrcAddressStatus"), ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpStratum"), ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpMode"), ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpPrecision"), ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpClockSource"), ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpPollInterval"), ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpLeapIndicator"), ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpRootDelay"), ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpRootDispersion"), ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpReferenceTimestamp"), ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpLocalTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    xntpSystemGroup = xntpSystemGroup.setStatus('current')
xntpCountersGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 838, 3, 26, 2, 2, 2)).setObjects(("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpPacketsIn"), ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpBadVersion"), ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpBadStratum"), ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpBadLength"), ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpBadMode"), ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpBadHeader"), ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpBadData"), ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpPacketsOut"), ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpPhaseAdjustments"), ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpStepAdjustments"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    xntpCountersGroup = xntpCountersGroup.setStatus('current')
xntpServerGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 838, 3, 26, 2, 2, 3)).setObjects(("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpServerVersion"), ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpServerMinPoll"), ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpServerMaxPoll"), ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpServerRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    xntpServerGroup = xntpServerGroup.setStatus('current')
xntpSAPeerGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 838, 3, 26, 2, 2, 4)).setObjects(("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpSAPeerVersion"), ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpSAPeerMinPoll"), ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpSAPeerMaxPoll"), ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpSAPeerRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    xntpSAPeerGroup = xntpSAPeerGroup.setStatus('current')
xntpAssocGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 838, 3, 26, 2, 2, 5)).setObjects(("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpAssocPeerPort"), ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpAssocPeerPoll"), ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpAssocHostAddr"), ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpAssocHostPort"), ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpAssocHostPoll"), ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpAssocHostMode"), ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpAssocPeerMode"), ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpAssocPeerStratum"), ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpAssocPeerPrecision"), ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpAssocPeerLeap"), ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpAssocPeerCondition"), ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpAssocPeerConfig"), ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpAssocPeerRootDelay"), ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpAssocPeerRootDispersion"), ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpAssocPeerOffset"), ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpAssocPeerDelay"), ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpAssocPeerDispersion"), ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpAssocPeerReachability"), ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpAssocPeerRefrTimestamp"), ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpAssocPeerXmitTimestamp"), ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpAssocPeerOrigTimestamp"), ("XEDIA-NETWORK-TIME-PROTOCOL-MIB", "xntpAssocPeerRecvTimestamp"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    xntpAssocGroup = xntpAssocGroup.setStatus('current')
mibBuilder.exportSymbols("XEDIA-NETWORK-TIME-PROTOCOL-MIB", xntpBadHeader=xntpBadHeader, xntpServerVersion=xntpServerVersion, xntpGroups=xntpGroups, xntpAssocPeerRootDelay=xntpAssocPeerRootDelay, xntpSystemGroup=xntpSystemGroup, xntpAssocPeerStratum=xntpAssocPeerStratum, xntpAssocGroup=xntpAssocGroup, xntpLocalTime=xntpLocalTime, xntpSAPeerMinPoll=xntpSAPeerMinPoll, xntpAssocEntry=xntpAssocEntry, xntpAssocPeerRecvTimestamp=xntpAssocPeerRecvTimestamp, xntpSystem=xntpSystem, xntpServerMaxPoll=xntpServerMaxPoll, xntpSAPeerVersion=xntpSAPeerVersion, xntpServerEntry=xntpServerEntry, xntpAssocHostAddr=xntpAssocHostAddr, xntpAssocHostPoll=xntpAssocHostPoll, XntpSeconds=XntpSeconds, xntpAssocPeerRootDispersion=xntpAssocPeerRootDispersion, xntpObjects=xntpObjects, xntpAssocPeerPort=xntpAssocPeerPort, xntpAssocTable=xntpAssocTable, xntpPollInterval=xntpPollInterval, xntpAssocPeerPrecision=xntpAssocPeerPrecision, xntpSAPeerGroup=xntpSAPeerGroup, xntpAdminStatus=xntpAdminStatus, XntpReachability=XntpReachability, xntpStratum=xntpStratum, xntpAssocPeerOffset=xntpAssocPeerOffset, xntpAssocPeerDispersion=xntpAssocPeerDispersion, xntpCounters=xntpCounters, xntpSAPeerRowStatus=xntpSAPeerRowStatus, xntpServerTable=xntpServerTable, xntpAssocPeerLeap=xntpAssocPeerLeap, xntpPhaseAdjustments=xntpPhaseAdjustments, xntpStepAdjustments=xntpStepAdjustments, xntpPacketsIn=xntpPacketsIn, XntpCounter=XntpCounter, xntpAssocPeerPoll=xntpAssocPeerPoll, xntpCountersGroup=xntpCountersGroup, xediaNetworkTimeProtocolMIB=xediaNetworkTimeProtocolMIB, XntpAssociationCondition=XntpAssociationCondition, xntpAssocPeerXmitTimestamp=xntpAssocPeerXmitTimestamp, xntpAssocPeerDelay=xntpAssocPeerDelay, xntpBadMode=xntpBadMode, xntpAssocPeerRefrTimestamp=xntpAssocPeerRefrTimestamp, PYSNMP_MODULE_ID=xediaNetworkTimeProtocolMIB, XntpIpAddress=XntpIpAddress, xntpBadStratum=xntpBadStratum, xntpSAPeerEntry=xntpSAPeerEntry, xntpAssocPeerReachability=xntpAssocPeerReachability, xntpAssocPeerConfig=xntpAssocPeerConfig, xntpSrcAddressStatus=xntpSrcAddressStatus, XntpAssociationMode=XntpAssociationMode, xntpMode=xntpMode, xntpAssocHostMode=xntpAssocHostMode, XntpLeapIndication=XntpLeapIndication, xntpBadLength=xntpBadLength, xntpCompliances=xntpCompliances, xntpRootDispersion=xntpRootDispersion, xntpServerMinPoll=xntpServerMinPoll, xntpAssocPeerOrigTimestamp=xntpAssocPeerOrigTimestamp, xntpServerGroup=xntpServerGroup, xntpAssocHostPort=xntpAssocHostPort, xntpAssocPeerCondition=xntpAssocPeerCondition, xntpReferenceTimestamp=xntpReferenceTimestamp, xntpRootDelay=xntpRootDelay, xntpPacketsOut=xntpPacketsOut, xntpPrecision=xntpPrecision, xntpBadVersion=xntpBadVersion, xntpCompliance=xntpCompliance, xntpSAPeerTable=xntpSAPeerTable, xntpSAPeer=xntpSAPeer, xntpAssocPeerAddr=xntpAssocPeerAddr, xntpConformance=xntpConformance, xntpAssocPeerMode=xntpAssocPeerMode, XntpPort=XntpPort, xntpBadData=xntpBadData, xntpClockSource=xntpClockSource, xntpServer=xntpServer, XntpDateAndTime=XntpDateAndTime, xntpServerRowStatus=xntpServerRowStatus, xntpLeapIndicator=xntpLeapIndicator, xntpSAPeerMaxPoll=xntpSAPeerMaxPoll)
