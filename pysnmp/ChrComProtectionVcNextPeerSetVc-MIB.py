#
# PySNMP MIB module ChrComProtectionVcNextPeerSetVc-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ChrComProtectionVcNextPeerSetVc-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:20:50 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
chrComProtectionVc, = mibBuilder.importSymbols("Chromatis-MIB", "chrComProtectionVc")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, TimeTicks, IpAddress, Bits, iso, MibIdentifier, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ObjectIdentity, Gauge32, NotificationType, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "iso", "MibIdentifier", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ObjectIdentity", "Gauge32", "NotificationType", "Integer32", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
chrComProtectionVcNextPeerSetVcTable = MibTable((1, 3, 6, 1, 4, 1, 3695, 1, 12, 3, 3), )
if mibBuilder.loadTexts: chrComProtectionVcNextPeerSetVcTable.setStatus('current')
chrComProtectionVcNextPeerSetVcEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3695, 1, 12, 3, 3, 1), ).setIndexNames((0, "ChrComProtectionVcNextPeerSetVc-MIB", "chrComProtectionVcNextVCPeerSetID"))
if mibBuilder.loadTexts: chrComProtectionVcNextPeerSetVcEntry.setStatus('current')
chrComProtectionVcNextVCPeerSetID = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 12, 3, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComProtectionVcNextVCPeerSetID.setStatus('current')
mibBuilder.exportSymbols("ChrComProtectionVcNextPeerSetVc-MIB", chrComProtectionVcNextVCPeerSetID=chrComProtectionVcNextVCPeerSetID, chrComProtectionVcNextPeerSetVcTable=chrComProtectionVcNextPeerSetVcTable, chrComProtectionVcNextPeerSetVcEntry=chrComProtectionVcNextPeerSetVcEntry)
