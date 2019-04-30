#
# PySNMP MIB module ARISTA-BRIDGE-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ARISTA-BRIDGE-EXT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:09:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
aristaMibs, = mibBuilder.importSymbols("ARISTA-SMI-MIB", "aristaMibs")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
dot1qFdbId, dot1qTpFdbAddress = mibBuilder.importSymbols("Q-BRIDGE-MIB", "dot1qFdbId", "dot1qTpFdbAddress")
TimeFilter, = mibBuilder.importSymbols("RMON2-MIB", "TimeFilter")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, iso, Gauge32, IpAddress, Counter32, Unsigned32, ObjectIdentity, Integer32, MibIdentifier, Bits, NotificationType, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "iso", "Gauge32", "IpAddress", "Counter32", "Unsigned32", "ObjectIdentity", "Integer32", "MibIdentifier", "Bits", "NotificationType", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
aristaBridgeExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 30065, 3, 2))
aristaBridgeExtMIB.setRevisions(('2014-08-15 00:00', '2011-03-31 13:00', '2010-05-03 00:00',))
if mibBuilder.loadTexts: aristaBridgeExtMIB.setLastUpdated('201408150000Z')
if mibBuilder.loadTexts: aristaBridgeExtMIB.setOrganization('Arista Networks, Inc.')
aristaDot1qTpFdbTable = MibTable((1, 3, 6, 1, 4, 1, 30065, 3, 2, 1), )
if mibBuilder.loadTexts: aristaDot1qTpFdbTable.setStatus('current')
aristaDot1qTpFdbEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30065, 3, 2, 1, 1), ).setIndexNames((0, "ARISTA-BRIDGE-EXT-MIB", "aristaDot1qTpFdbTimeMark"), (0, "Q-BRIDGE-MIB", "dot1qFdbId"), (0, "Q-BRIDGE-MIB", "dot1qTpFdbAddress"))
if mibBuilder.loadTexts: aristaDot1qTpFdbEntry.setStatus('current')
aristaDot1qTpFdbTimeMark = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 2, 1, 1, 1), TimeFilter())
if mibBuilder.loadTexts: aristaDot1qTpFdbTimeMark.setStatus('current')
aristaDot1qTpFdbNumMoves = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 2, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaDot1qTpFdbNumMoves.setStatus('current')
aristaDot1qTpFdbLastMove = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 2, 1, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaDot1qTpFdbLastMove.setStatus('current')
aristaBridgeExtConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 2, 2))
aristaBridgeExtGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 2, 2, 1))
aristaBridgeExtCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 2, 2, 2))
aristaBridgeExtBaseGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 30065, 3, 2, 2, 1, 1)).setObjects(("ARISTA-BRIDGE-EXT-MIB", "aristaDot1qTpFdbNumMoves"), ("ARISTA-BRIDGE-EXT-MIB", "aristaDot1qTpFdbLastMove"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaBridgeExtBaseGroup = aristaBridgeExtBaseGroup.setStatus('current')
aristaBridgeExtCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 30065, 3, 2, 2, 2, 1)).setObjects(("ARISTA-BRIDGE-EXT-MIB", "aristaBridgeExtBaseGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaBridgeExtCompliance = aristaBridgeExtCompliance.setStatus('current')
mibBuilder.exportSymbols("ARISTA-BRIDGE-EXT-MIB", aristaDot1qTpFdbTimeMark=aristaDot1qTpFdbTimeMark, aristaBridgeExtBaseGroup=aristaBridgeExtBaseGroup, aristaDot1qTpFdbLastMove=aristaDot1qTpFdbLastMove, aristaDot1qTpFdbNumMoves=aristaDot1qTpFdbNumMoves, aristaDot1qTpFdbEntry=aristaDot1qTpFdbEntry, aristaBridgeExtGroups=aristaBridgeExtGroups, aristaDot1qTpFdbTable=aristaDot1qTpFdbTable, aristaBridgeExtMIB=aristaBridgeExtMIB, aristaBridgeExtCompliance=aristaBridgeExtCompliance, PYSNMP_MODULE_ID=aristaBridgeExtMIB, aristaBridgeExtCompliances=aristaBridgeExtCompliances, aristaBridgeExtConformance=aristaBridgeExtConformance)
