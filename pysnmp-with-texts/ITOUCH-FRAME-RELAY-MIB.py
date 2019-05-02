#
# PySNMP MIB module ITOUCH-FRAME-RELAY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ITOUCH-FRAME-RELAY-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:57:53 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
iTouch, = mibBuilder.importSymbols("ITOUCH-MIB", "iTouch")
frCircuitIfIndex, frCircuitDlci = mibBuilder.importSymbols("RFC1315-MIB", "frCircuitIfIndex", "frCircuitDlci")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, ModuleIdentity, Counter64, iso, IpAddress, TimeTicks, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, NotificationType, Counter32, Integer32, ObjectIdentity, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "ModuleIdentity", "Counter64", "iso", "IpAddress", "TimeTicks", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "NotificationType", "Counter32", "Integer32", "ObjectIdentity", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
xFrameRelay = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 23))
xFrCircuitTable = MibTable((1, 3, 6, 1, 4, 1, 33, 23, 1), )
if mibBuilder.loadTexts: xFrCircuitTable.setStatus('mandatory')
if mibBuilder.loadTexts: xFrCircuitTable.setDescription('A table containing iTouch extensions to the standard Frame Relay Circuit table.')
xFrCircuitEntry = MibTableRow((1, 3, 6, 1, 4, 1, 33, 23, 1, 1), ).setIndexNames((0, "RFC1315-MIB", "frCircuitIfIndex"), (0, "RFC1315-MIB", "frCircuitDlci"))
if mibBuilder.loadTexts: xFrCircuitEntry.setStatus('mandatory')
if mibBuilder.loadTexts: xFrCircuitEntry.setDescription('Entry parameters.')
xFrCircuitIf = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 23, 1, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xFrCircuitIf.setStatus('mandatory')
if mibBuilder.loadTexts: xFrCircuitIf.setDescription('The ifIndex value of the corresponding ifEntry, that is, the interface to which the DLCI is attached.')
mibBuilder.exportSymbols("ITOUCH-FRAME-RELAY-MIB", xFrCircuitIf=xFrCircuitIf, xFrameRelay=xFrameRelay, xFrCircuitTable=xFrCircuitTable, xFrCircuitEntry=xFrCircuitEntry)
