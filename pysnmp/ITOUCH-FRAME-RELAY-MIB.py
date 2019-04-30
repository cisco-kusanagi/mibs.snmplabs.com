#
# PySNMP MIB module ITOUCH-FRAME-RELAY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ITOUCH-FRAME-RELAY-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:46:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
iTouch, = mibBuilder.importSymbols("ITOUCH-MIB", "iTouch")
frCircuitIfIndex, frCircuitDlci = mibBuilder.importSymbols("RFC1315-MIB", "frCircuitIfIndex", "frCircuitDlci")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, Gauge32, iso, Unsigned32, NotificationType, Integer32, MibIdentifier, IpAddress, Bits, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "Gauge32", "iso", "Unsigned32", "NotificationType", "Integer32", "MibIdentifier", "IpAddress", "Bits", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
xFrameRelay = MibIdentifier((1, 3, 6, 1, 4, 1, 33, 23))
xFrCircuitTable = MibTable((1, 3, 6, 1, 4, 1, 33, 23, 1), )
if mibBuilder.loadTexts: xFrCircuitTable.setStatus('mandatory')
xFrCircuitEntry = MibTableRow((1, 3, 6, 1, 4, 1, 33, 23, 1, 1), ).setIndexNames((0, "RFC1315-MIB", "frCircuitIfIndex"), (0, "RFC1315-MIB", "frCircuitDlci"))
if mibBuilder.loadTexts: xFrCircuitEntry.setStatus('mandatory')
xFrCircuitIf = MibTableColumn((1, 3, 6, 1, 4, 1, 33, 23, 1, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xFrCircuitIf.setStatus('mandatory')
mibBuilder.exportSymbols("ITOUCH-FRAME-RELAY-MIB", xFrameRelay=xFrameRelay, xFrCircuitEntry=xFrCircuitEntry, xFrCircuitTable=xFrCircuitTable, xFrCircuitIf=xFrCircuitIf)
