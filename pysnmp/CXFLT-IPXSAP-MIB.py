#
# PySNMP MIB module CXFLT-IPXSAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CXFLT-IPXSAP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:17:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
cxIpx, = mibBuilder.importSymbols("CXProduct-SMI", "cxIpx")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, Counter32, iso, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, TimeTicks, Integer32, NotificationType, ModuleIdentity, IpAddress, Gauge32, Bits, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Counter32", "iso", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "TimeTicks", "Integer32", "NotificationType", "ModuleIdentity", "IpAddress", "Gauge32", "Bits", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cxFltIpxSapTable = MibTable((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 13, 3), )
if mibBuilder.loadTexts: cxFltIpxSapTable.setStatus('mandatory')
cxFltIpxSapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 13, 3, 1), ).setIndexNames((0, "CXFLT-IPXSAP-MIB", "cxFltIpxSapIndex"))
if mibBuilder.loadTexts: cxFltIpxSapEntry.setStatus('mandatory')
cxFltIpxSapIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 13, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cxFltIpxSapIndex.setStatus('mandatory')
cxFltIpxSapType = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 13, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxFltIpxSapType.setStatus('mandatory')
cxFltIpxSapName = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 13, 3, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 48))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxFltIpxSapName.setStatus('mandatory')
cxFltIpxSapStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 13, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("discard", 1), ("nodiscard", 2))).clone('discard')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxFltIpxSapStatus.setStatus('mandatory')
cxFltIpxSapRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 13, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("invalid", 1), ("valid", 2))).clone('valid')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxFltIpxSapRowStatus.setStatus('mandatory')
mibBuilder.exportSymbols("CXFLT-IPXSAP-MIB", cxFltIpxSapTable=cxFltIpxSapTable, cxFltIpxSapStatus=cxFltIpxSapStatus, cxFltIpxSapIndex=cxFltIpxSapIndex, cxFltIpxSapEntry=cxFltIpxSapEntry, cxFltIpxSapName=cxFltIpxSapName, cxFltIpxSapType=cxFltIpxSapType, cxFltIpxSapRowStatus=cxFltIpxSapRowStatus)
