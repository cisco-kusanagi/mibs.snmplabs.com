#
# PySNMP MIB module DEVHW-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DEVHW-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:26:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
device, = mibBuilder.importSymbols("ANIROOT-MIB", "device")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Integer32, Bits, Unsigned32, IpAddress, MibIdentifier, ModuleIdentity, Counter64, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, ObjectIdentity, iso, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Integer32", "Bits", "Unsigned32", "IpAddress", "MibIdentifier", "ModuleIdentity", "Counter64", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "ObjectIdentity", "iso", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
aniDevHardware = ModuleIdentity((1, 3, 6, 1, 4, 1, 4325, 2, 3))
if mibBuilder.loadTexts: aniDevHardware.setLastUpdated('0105091130Z')
if mibBuilder.loadTexts: aniDevHardware.setOrganization('Aperto Networks')
aniDevHwRevision = MibScalar((1, 3, 6, 1, 4, 1, 4325, 2, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aniDevHwRevision.setStatus('current')
aniDevHwSpeed = MibScalar((1, 3, 6, 1, 4, 1, 4325, 2, 3, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aniDevHwSpeed.setStatus('current')
aniDevHwBuildDate = MibScalar((1, 3, 6, 1, 4, 1, 4325, 2, 3, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 22))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aniDevHwBuildDate.setStatus('current')
aniDevHwSerialNum = MibScalar((1, 3, 6, 1, 4, 1, 4325, 2, 3, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aniDevHwSerialNum.setStatus('current')
aniDevHwBoardRevision = MibScalar((1, 3, 6, 1, 4, 1, 4325, 2, 3, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aniDevHwBoardRevision.setStatus('current')
mibBuilder.exportSymbols("DEVHW-MIB", aniDevHwBuildDate=aniDevHwBuildDate, aniDevHardware=aniDevHardware, aniDevHwBoardRevision=aniDevHwBoardRevision, aniDevHwSerialNum=aniDevHwSerialNum, aniDevHwSpeed=aniDevHwSpeed, PYSNMP_MODULE_ID=aniDevHardware, aniDevHwRevision=aniDevHwRevision)
