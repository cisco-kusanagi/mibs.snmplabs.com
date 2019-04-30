#
# PySNMP MIB module CXFLT-IPX-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CXFLT-IPX-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:17:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
cxFltIpx, = mibBuilder.importSymbols("CXProduct-SMI", "cxFltIpx")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, TimeTicks, iso, ModuleIdentity, Unsigned32, Integer32, Counter32, Counter64, Bits, IpAddress, NotificationType, Gauge32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "TimeTicks", "iso", "ModuleIdentity", "Unsigned32", "Integer32", "Counter32", "Counter64", "Bits", "IpAddress", "NotificationType", "Gauge32", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class NetNumber(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

cxFltIpxAddrTable = MibTable((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 22, 1), )
if mibBuilder.loadTexts: cxFltIpxAddrTable.setStatus('mandatory')
cxFltIpxAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 22, 1, 1), ).setIndexNames((0, "CXFLT-IPX-MIB", "cxFltIpxIndex"))
if mibBuilder.loadTexts: cxFltIpxAddrEntry.setStatus('mandatory')
cxFltIpxIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 22, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxFltIpxIndex.setStatus('mandatory')
cxFltIpxSrcAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 22, 1, 1, 2), NetNumber()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxFltIpxSrcAddr.setStatus('mandatory')
cxFltIpxDstAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 22, 1, 1, 3), NetNumber()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxFltIpxDstAddr.setStatus('mandatory')
cxFltIpxParameter = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 22, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("discard", 1), ("forward", 2), ("priority-low", 3), ("priority-high", 4))).clone('discard')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxFltIpxParameter.setStatus('mandatory')
cxFltIpxRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 22, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("invalid", 1), ("valid", 2))).clone('valid')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxFltIpxRowStatus.setStatus('mandatory')
mibBuilder.exportSymbols("CXFLT-IPX-MIB", cxFltIpxRowStatus=cxFltIpxRowStatus, cxFltIpxParameter=cxFltIpxParameter, cxFltIpxDstAddr=cxFltIpxDstAddr, cxFltIpxSrcAddr=cxFltIpxSrcAddr, cxFltIpxAddrTable=cxFltIpxAddrTable, cxFltIpxIndex=cxFltIpxIndex, NetNumber=NetNumber, cxFltIpxAddrEntry=cxFltIpxAddrEntry)
