#
# PySNMP MIB module CXPhysicalInterfaceManager-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CXPhysicalInterfaceManager-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:17:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
cxPortManager, = mibBuilder.importSymbols("CXProduct-SMI", "cxPortManager")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, IpAddress, MibIdentifier, Gauge32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Unsigned32, Counter64, Counter32, iso, TimeTicks, Bits, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "IpAddress", "MibIdentifier", "Gauge32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Unsigned32", "Counter64", "Counter32", "iso", "TimeTicks", "Bits", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
cxPhyIfTable = MibTable((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 16, 3), )
if mibBuilder.loadTexts: cxPhyIfTable.setStatus('mandatory')
cxPhyIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 16, 3, 1), ).setIndexNames((0, "CXPhysicalInterfaceManager-MIB", "cxPhyIfIndex"))
if mibBuilder.loadTexts: cxPhyIfEntry.setStatus('mandatory')
cxPhyIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 16, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cxPhyIfIndex.setStatus('mandatory')
cxPhyIfType = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 16, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28))).clone(namedValues=NamedValues(("others", 1), ("v24", 2), ("v35", 3), ("x21", 4), ("v34", 5), ("u-isdn-bri", 6), ("st-isdn-bri", 8), ("dds-56k", 10), ("dds-t1e1", 11), ("fxs-voice", 12), ("fxo-voice", 13), ("em-voice", 14), ("ethernet", 15), ("token-ring", 16), ("v35-eu", 17), ("hsIO", 18), ("usIO", 19), ("lanIO", 20), ("elIO", 21), ("voxIO", 22), ("tlIO", 23), ("t1e1IO", 24), ("dvc", 25), ("multi-io", 26), ("fast-ethernet", 27), ("atm-cell-io", 28)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cxPhyIfType.setStatus('mandatory')
mibBuilder.exportSymbols("CXPhysicalInterfaceManager-MIB", cxPhyIfIndex=cxPhyIfIndex, cxPhyIfTable=cxPhyIfTable, cxPhyIfEntry=cxPhyIfEntry, cxPhyIfType=cxPhyIfType)
