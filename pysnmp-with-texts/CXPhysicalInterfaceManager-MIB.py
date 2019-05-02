#
# PySNMP MIB module CXPhysicalInterfaceManager-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CXPhysicalInterfaceManager-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:33:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
cxPortManager, = mibBuilder.importSymbols("CXProduct-SMI", "cxPortManager")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, Integer32, ModuleIdentity, TimeTicks, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, IpAddress, ObjectIdentity, Gauge32, Unsigned32, Bits, iso, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Integer32", "ModuleIdentity", "TimeTicks", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "IpAddress", "ObjectIdentity", "Gauge32", "Unsigned32", "Bits", "iso", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cxPhyIfTable = MibTable((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 16, 3), )
if mibBuilder.loadTexts: cxPhyIfTable.setReference(' ')
if mibBuilder.loadTexts: cxPhyIfTable.setStatus('mandatory')
if mibBuilder.loadTexts: cxPhyIfTable.setDescription('A table of physical interface configuration.')
cxPhyIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 16, 3, 1), ).setIndexNames((0, "CXPhysicalInterfaceManager-MIB", "cxPhyIfIndex"))
if mibBuilder.loadTexts: cxPhyIfEntry.setStatus('mandatory')
if mibBuilder.loadTexts: cxPhyIfEntry.setDescription('Defines a row in the cxPhyIfTable. Each row contains the objects which are used to define a physical interface.')
cxPhyIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 16, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cxPhyIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: cxPhyIfIndex.setDescription('Identifies the port that this table row defines. For the CX900, this object specifies the slot and port number. The first digit identifies the slot number the I/O board resides in, the second digit identifies the number of the port on the I/O board. For example: 11, 21, 31, 41, 51, 61 or 71. For the CX1000, this object specifies the port number only. The range of available port numbers varies according to the type of module. For example, the LAN module supports only one port per I/O board and the Voice module supports only two ports per I/O board, but the Frame Relay module supports four ports per I/O board. You distinguish between module port numbers by specifying the slot number of the I/O board using a different object. Default Value: none')
cxPhyIfType = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 16, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28))).clone(namedValues=NamedValues(("others", 1), ("v24", 2), ("v35", 3), ("x21", 4), ("v34", 5), ("u-isdn-bri", 6), ("st-isdn-bri", 8), ("dds-56k", 10), ("dds-t1e1", 11), ("fxs-voice", 12), ("fxo-voice", 13), ("em-voice", 14), ("ethernet", 15), ("token-ring", 16), ("v35-eu", 17), ("hsIO", 18), ("usIO", 19), ("lanIO", 20), ("elIO", 21), ("voxIO", 22), ("tlIO", 23), ("t1e1IO", 24), ("dvc", 25), ("multi-io", 26), ("fast-ethernet", 27), ("atm-cell-io", 28)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cxPhyIfType.setStatus('mandatory')
if mibBuilder.loadTexts: cxPhyIfType.setDescription('Identifies the physical interface type of the port. Options: others (1) v24 (2) v35 (3) x21 (4) v34 (5) u-isdn-bri (6) u-isdn-pri (7) st-isdn-bri (8) st-isdn-pri (9) dds-56k (10) dds-t1e1 (11) fxs-voice (12) fxo-voice (13) em-voice (14) ethernet (15) token-ring (16) v35-eu (17) HSIO (18) USIO (19) LANIO (20) ELIO (21) VOXIO (22) TLIO (23) T1E1IO (24) DVC (25) multi-io (26) fast-ethernet (27) atm-cell-io (28) The speed that this card can handle is T1/E1 up to T3/E3. Default Value: none')
mibBuilder.exportSymbols("CXPhysicalInterfaceManager-MIB", cxPhyIfIndex=cxPhyIfIndex, cxPhyIfEntry=cxPhyIfEntry, cxPhyIfType=cxPhyIfType, cxPhyIfTable=cxPhyIfTable)
