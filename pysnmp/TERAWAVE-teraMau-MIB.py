#
# PySNMP MIB module TERAWAVE-teraMau-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TERAWAVE-teraMau-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:08:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
enterprises, Integer32, iso, ObjectIdentity, IpAddress, Bits, TimeTicks, Counter32, Counter64, NotificationType, ModuleIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "Integer32", "iso", "ObjectIdentity", "IpAddress", "Bits", "TimeTicks", "Counter32", "Counter64", "NotificationType", "ModuleIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
terawave = MibIdentifier((1, 3, 6, 1, 4, 1, 4513))
teraMauTable = MibTable((1, 3, 6, 1, 4, 1, 4513, 18), )
if mibBuilder.loadTexts: teraMauTable.setStatus('mandatory')
teraMauTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4513, 18, 1), ).setIndexNames((0, "TERAWAVE-teraMau-MIB", "ifMauIfIndex"), (0, "TERAWAVE-teraMau-MIB", "ifMauIndex"))
if mibBuilder.loadTexts: teraMauTableEntry.setStatus('mandatory')
teraMauLinkState = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 18, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraMauLinkState.setStatus('mandatory')
teraMauDuplexMode = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 18, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("fDX", 1), ("hDX", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraMauDuplexMode.setStatus('mandatory')
teraMauSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 18, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("mbps100", 1), ("mbps10", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: teraMauSpeed.setStatus('mandatory')
teraMauPauseHighThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 18, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: teraMauPauseHighThreshold.setStatus('mandatory')
teraMauPauseLowThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 4513, 18, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: teraMauPauseLowThreshold.setStatus('mandatory')
mibBuilder.exportSymbols("TERAWAVE-teraMau-MIB", teraMauPauseLowThreshold=teraMauPauseLowThreshold, teraMauPauseHighThreshold=teraMauPauseHighThreshold, teraMauTableEntry=teraMauTableEntry, teraMauLinkState=teraMauLinkState, teraMauSpeed=teraMauSpeed, teraMauTable=teraMauTable, terawave=terawave, teraMauDuplexMode=teraMauDuplexMode)
