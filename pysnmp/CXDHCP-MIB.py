#
# PySNMP MIB module CXDHCP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CXDHCP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:16:56 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
cxCfgIp, = mibBuilder.importSymbols("CXProduct-SMI", "cxCfgIp")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, ModuleIdentity, Counter32, IpAddress, MibIdentifier, Counter64, NotificationType, TimeTicks, Bits, Integer32, Unsigned32, ObjectIdentity, iso, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ModuleIdentity", "Counter32", "IpAddress", "MibIdentifier", "Counter64", "NotificationType", "TimeTicks", "Bits", "Integer32", "Unsigned32", "ObjectIdentity", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cxCfgDhcpRATable = MibTable((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 16, 4), )
if mibBuilder.loadTexts: cxCfgDhcpRATable.setStatus('mandatory')
cxCfgDhcpRAEntry = MibTableRow((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 16, 4, 1), ).setIndexNames((0, "CXDHCP-MIB", "cxCfgDhcpRAIndex"))
if mibBuilder.loadTexts: cxCfgDhcpRAEntry.setStatus('mandatory')
cxCfgDhcpRAIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 16, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxCfgDhcpRAIndex.setStatus('mandatory')
cxCfgDhcpRASrvAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 16, 4, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxCfgDhcpRASrvAddr.setStatus('mandatory')
cxCfgDhcpRARowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 16, 4, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("invalid", 1), ("valid", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxCfgDhcpRARowStatus.setStatus('mandatory')
cxCfgDhcpRAStatTx = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 16, 4, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cxCfgDhcpRAStatTx.setStatus('mandatory')
cxCfgDhcpRAStatRx = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 16, 4, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cxCfgDhcpRAStatRx.setStatus('mandatory')
mibBuilder.exportSymbols("CXDHCP-MIB", cxCfgDhcpRAEntry=cxCfgDhcpRAEntry, cxCfgDhcpRASrvAddr=cxCfgDhcpRASrvAddr, cxCfgDhcpRATable=cxCfgDhcpRATable, cxCfgDhcpRARowStatus=cxCfgDhcpRARowStatus, cxCfgDhcpRAIndex=cxCfgDhcpRAIndex, cxCfgDhcpRAStatTx=cxCfgDhcpRAStatTx, cxCfgDhcpRAStatRx=cxCfgDhcpRAStatRx)
