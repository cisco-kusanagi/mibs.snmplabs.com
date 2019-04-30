#
# PySNMP MIB module XYLAN-ATMLSM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/XYLAN-ATMLSM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:38:19 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, ObjectIdentity, MibIdentifier, Counter64, NotificationType, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter32, Unsigned32, IpAddress, iso, Integer32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "ObjectIdentity", "MibIdentifier", "Counter64", "NotificationType", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter32", "Unsigned32", "IpAddress", "iso", "Integer32", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
atmxLsmGroup, = mibBuilder.importSymbols("XYLAN-ATM-MIB", "atmxLsmGroup")
class AtmForumLaneAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(20, 20)
    fixedLength = 20

atmxLesConfTable = MibTable((1, 3, 6, 1, 4, 1, 800, 2, 4, 13, 1), )
if mibBuilder.loadTexts: atmxLesConfTable.setStatus('mandatory')
atmxLesConfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 800, 2, 4, 13, 1, 1), ).setIndexNames((0, "XYLAN-ATMLSM-MIB", "atmxlesConfIndex"))
if mibBuilder.loadTexts: atmxLesConfEntry.setStatus('mandatory')
atmxlesConfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 4, 13, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: atmxlesConfIndex.setStatus('mandatory')
atmxLesRedundancyEnabled = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 4, 13, 1, 1, 19), Integer32().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmxLesRedundancyEnabled.setStatus('mandatory')
atmxLesRedundancyRole = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 4, 13, 1, 1, 20), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmxLesRedundancyRole.setStatus('mandatory')
atmxSecondaryLESAtmAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 4, 13, 1, 1, 21), AtmForumLaneAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmxSecondaryLESAtmAddr.setStatus('mandatory')
mibBuilder.exportSymbols("XYLAN-ATMLSM-MIB", atmxlesConfIndex=atmxlesConfIndex, atmxLesConfEntry=atmxLesConfEntry, atmxSecondaryLESAtmAddr=atmxSecondaryLESAtmAddr, AtmForumLaneAddress=AtmForumLaneAddress, atmxLesConfTable=atmxLesConfTable, atmxLesRedundancyEnabled=atmxLesRedundancyEnabled, atmxLesRedundancyRole=atmxLesRedundancyRole)
