#
# PySNMP MIB module CXLANIOGEN-PORT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CXLANIOGEN-PORT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:17:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
cxLanIoPort, = mibBuilder.importSymbols("CXProduct-SMI", "cxLanIoPort")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, Unsigned32, iso, NotificationType, Bits, Integer32, ObjectIdentity, Counter64, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Counter32, IpAddress, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Unsigned32", "iso", "NotificationType", "Bits", "Integer32", "ObjectIdentity", "Counter64", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Counter32", "IpAddress", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class PhysAddress(OctetString):
    pass

cxLanIoGenPortTable = MibTable((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 10, 2), )
if mibBuilder.loadTexts: cxLanIoGenPortTable.setStatus('mandatory')
cxLanIoGenPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 10, 2, 1), ).setIndexNames((0, "CXLANIOGEN-PORT-MIB", "cxLanIoGenPortIndex"))
if mibBuilder.loadTexts: cxLanIoGenPortEntry.setStatus('mandatory')
cxLanIoGenPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 10, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cxLanIoGenPortIndex.setStatus('mandatory')
cxLanIoGenMacAddrSrc = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 10, 2, 1, 2), PhysAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxLanIoGenMacAddrSrc.setStatus('mandatory')
cxLanIoGenMacAddrDst = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 10, 2, 1, 3), PhysAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxLanIoGenMacAddrDst.setStatus('mandatory')
cxLanIoGenType = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 10, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("invalid", 1), ("disabled", 2), ("internalLoopbackLevel1", 3), ("internalLoopbackLevel2", 4), ("noLoopbackFrameVerify", 5), ("noLoopbackFrameForward", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxLanIoGenType.setStatus('mandatory')
cxLanIoGenDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 10, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxLanIoGenDelay.setStatus('mandatory')
cxLanIoGenFrameSize = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 10, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(64, 4096))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxLanIoGenFrameSize.setStatus('mandatory')
cxLanIoGenStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 10, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("disabled", 2), ("internalLoopbackLevel1", 3), ("internalLoopbackLevel2", 4), ("noLoopbackFrameVerify", 5), ("noLoopbackFrameForward", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cxLanIoGenStatus.setStatus('mandatory')
cxLanIoGenRxError = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 10, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cxLanIoGenRxError.setStatus('mandatory')
mibBuilder.exportSymbols("CXLANIOGEN-PORT-MIB", cxLanIoGenPortEntry=cxLanIoGenPortEntry, cxLanIoGenDelay=cxLanIoGenDelay, cxLanIoGenMacAddrSrc=cxLanIoGenMacAddrSrc, cxLanIoGenFrameSize=cxLanIoGenFrameSize, cxLanIoGenMacAddrDst=cxLanIoGenMacAddrDst, cxLanIoGenRxError=cxLanIoGenRxError, cxLanIoGenPortTable=cxLanIoGenPortTable, cxLanIoGenType=cxLanIoGenType, PhysAddress=PhysAddress, cxLanIoGenPortIndex=cxLanIoGenPortIndex, cxLanIoGenStatus=cxLanIoGenStatus)
