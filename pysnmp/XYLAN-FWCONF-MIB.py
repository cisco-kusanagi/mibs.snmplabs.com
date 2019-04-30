#
# PySNMP MIB module XYLAN-FWCONF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/XYLAN-FWCONF-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:38:36 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, Bits, NotificationType, Gauge32, iso, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter64, Counter32, IpAddress, Unsigned32, Integer32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Bits", "NotificationType", "Gauge32", "iso", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter64", "Counter32", "IpAddress", "Unsigned32", "Integer32", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
xylanFwArch, = mibBuilder.importSymbols("XYLAN-BASE-MIB", "xylanFwArch")
xylanFwConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 800, 2, 12, 1))
xylanFwStatus = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 12, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanFwStatus.setStatus('mandatory')
xylanFwMode = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 12, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("blocked", 1), ("open", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanFwMode.setStatus('mandatory')
xylanFwPrimaryAddr = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 12, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanFwPrimaryAddr.setStatus('mandatory')
xylanFwPrimaryPassword = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 12, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanFwPrimaryPassword.setStatus('mandatory')
xylanFwBackupAddr = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 12, 1, 5), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanFwBackupAddr.setStatus('mandatory')
xylanFwBackupPassword = MibScalar((1, 3, 6, 1, 4, 1, 800, 2, 12, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanFwBackupPassword.setStatus('mandatory')
mibBuilder.exportSymbols("XYLAN-FWCONF-MIB", xylanFwPrimaryPassword=xylanFwPrimaryPassword, xylanFwPrimaryAddr=xylanFwPrimaryAddr, xylanFwBackupPassword=xylanFwBackupPassword, xylanFwConfig=xylanFwConfig, xylanFwBackupAddr=xylanFwBackupAddr, xylanFwStatus=xylanFwStatus, xylanFwMode=xylanFwMode)
