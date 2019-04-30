#
# PySNMP MIB module RADLAN-Redistribute (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RADLAN-Redistribute
# Produced by pysmi-0.3.4 at Mon Apr 29 20:40:28 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ipSpec, = mibBuilder.importSymbols("RADLAN-IP", "ipSpec")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, Counter64, ModuleIdentity, Gauge32, Integer32, Bits, NotificationType, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Counter32, ObjectIdentity, MibIdentifier, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Counter64", "ModuleIdentity", "Gauge32", "Integer32", "Bits", "NotificationType", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Counter32", "ObjectIdentity", "MibIdentifier", "iso")
RowStatus, TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString", "TruthValue")
class RlRedistSrcProtocol(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("rlRedistProtocolConnected", 1), ("rlRedistProtocolStatic", 2), ("rlRedistProtocolRip", 3), ("rlRedistProtocolOspfv2", 4), ("rlRedistProtocolOspfv3", 5), ("rlRedistProtocolBgp", 6), ("rlRedistProtocolEigrp", 7), ("rlRedistProtocolIsIs", 8), ("rlRedistProtocolMobile", 9), ("rlRedistProtocolAll", 10))

class RlRedistDstProtocol(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("rlRedistProtocolRip", 3), ("rlRedistProtocolOspfv2", 4), ("rlRedistProtocolOspfv3", 5), ("rlRedistProtocolBgp", 6), ("rlRedistProtocolEigrp", 7), ("rlRedistProtocolIsIs", 8), ("rlRedistProtocolMobile", 9))

class RlRedistMatchType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("rlRedistMatchTypeNone", 0), ("rlRedistMatchTypeInternal", 1), ("rlRedistMatchTypeExternalOne", 2), ("rlRedistMatchTypeExternalTwo", 3))

class RlRedistMetricType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("rlRedistMetricTypeNone", 0), ("rlRedistMetricTypeExternalOne", 1), ("rlRedistMetricTypeExternalTwo", 2))

rlRedistribute = MibIdentifier((1, 3, 6, 1, 4, 1, 89, 26, 27))
rlRedistTable = MibTable((1, 3, 6, 1, 4, 1, 89, 26, 27, 1), )
if mibBuilder.loadTexts: rlRedistTable.setStatus('current')
rlRedistEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 26, 27, 1, 1), ).setIndexNames((0, "RADLAN-Redistribute", "rlRedistDstProtocol"), (0, "RADLAN-Redistribute", "rlRedistSrcProtocol"), (0, "RADLAN-Redistribute", "rlRedistDstProcessId"), (0, "RADLAN-Redistribute", "rlRedistSrcProcessId"), (0, "RADLAN-Redistribute", "rlRedistMatchType"), (0, "RADLAN-Redistribute", "rlRedistRoutMapName"))
if mibBuilder.loadTexts: rlRedistEntry.setStatus('current')
rlRedistDstProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 27, 1, 1, 1), RlRedistDstProtocol())
if mibBuilder.loadTexts: rlRedistDstProtocol.setStatus('current')
rlRedistSrcProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 27, 1, 1, 2), RlRedistSrcProtocol())
if mibBuilder.loadTexts: rlRedistSrcProtocol.setStatus('current')
rlRedistDstProcessId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 27, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: rlRedistDstProcessId.setStatus('current')
rlRedistSrcProcessId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 27, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: rlRedistSrcProcessId.setStatus('current')
rlRedistMatchType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 27, 1, 1, 5), RlRedistMatchType())
if mibBuilder.loadTexts: rlRedistMatchType.setStatus('current')
rlRedistRoutMapName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 27, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)))
if mibBuilder.loadTexts: rlRedistRoutMapName.setStatus('current')
rlRedistAsNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 27, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlRedistAsNumber.setStatus('current')
rlRedistMetricTransparent = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 27, 1, 1, 8), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlRedistMetricTransparent.setStatus('current')
rlRedistMetricValue = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 27, 1, 1, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlRedistMetricValue.setStatus('current')
rlRedistMetricType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 27, 1, 1, 10), RlRedistMetricType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlRedistMetricType.setStatus('current')
rlRedistSubnets = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 27, 1, 1, 11), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlRedistSubnets.setStatus('current')
rlRedistOnlyNSSA = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 27, 1, 1, 12), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlRedistOnlyNSSA.setStatus('current')
rlRedistRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 27, 1, 1, 13), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlRedistRowStatus.setStatus('current')
rlRedistFilterListName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 26, 27, 1, 1, 14), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlRedistFilterListName.setStatus('current')
mibBuilder.exportSymbols("RADLAN-Redistribute", RlRedistMetricType=RlRedistMetricType, rlRedistSrcProcessId=rlRedistSrcProcessId, rlRedistTable=rlRedistTable, rlRedistDstProcessId=rlRedistDstProcessId, RlRedistDstProtocol=RlRedistDstProtocol, rlRedistOnlyNSSA=rlRedistOnlyNSSA, rlRedistMatchType=rlRedistMatchType, rlRedistSrcProtocol=rlRedistSrcProtocol, rlRedistMetricValue=rlRedistMetricValue, rlRedistEntry=rlRedistEntry, rlRedistFilterListName=rlRedistFilterListName, rlRedistribute=rlRedistribute, RlRedistMatchType=RlRedistMatchType, rlRedistRoutMapName=rlRedistRoutMapName, rlRedistAsNumber=rlRedistAsNumber, rlRedistMetricType=rlRedistMetricType, rlRedistSubnets=rlRedistSubnets, rlRedistMetricTransparent=rlRedistMetricTransparent, rlRedistRowStatus=rlRedistRowStatus, RlRedistSrcProtocol=RlRedistSrcProtocol, rlRedistDstProtocol=rlRedistDstProtocol)
