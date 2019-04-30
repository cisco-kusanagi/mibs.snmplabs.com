#
# PySNMP MIB module NSC-BORDERGUARD-TRAP (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NSC-BORDERGUARD-TRAP
# Produced by pysmi-0.3.4 at Mon Apr 29 20:15:17 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
nscBorderGuard, = mibBuilder.importSymbols("NSC-MIB", "nscBorderGuard")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Gauge32, NotificationType, Bits, NotificationType, ObjectIdentity, Unsigned32, TimeTicks, iso, IpAddress, Counter64, ModuleIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Gauge32", "NotificationType", "Bits", "NotificationType", "ObjectIdentity", "Unsigned32", "TimeTicks", "iso", "IpAddress", "Counter64", "ModuleIdentity", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
nscBorderGuardTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 10, 2, 1, 9, 1))
nscBorderGuardTrapsBadImage = MibScalar((1, 3, 6, 1, 4, 1, 10, 2, 1, 9, 1, 1), Integer32())
if mibBuilder.loadTexts: nscBorderGuardTrapsBadImage.setStatus('mandatory')
nscBorderGuardTrapsCurrentImage = MibScalar((1, 3, 6, 1, 4, 1, 10, 2, 1, 9, 1, 2), Integer32())
if mibBuilder.loadTexts: nscBorderGuardTrapsCurrentImage.setStatus('mandatory')
nscBorderGuardTrapsBadFileSystem = MibScalar((1, 3, 6, 1, 4, 1, 10, 2, 1, 9, 1, 3), Integer32())
if mibBuilder.loadTexts: nscBorderGuardTrapsBadFileSystem.setStatus('mandatory')
nscBorderGuardTrapsSoftFault = MibScalar((1, 3, 6, 1, 4, 1, 10, 2, 1, 9, 1, 4), Integer32())
if mibBuilder.loadTexts: nscBorderGuardTrapsSoftFault.setStatus('mandatory')
nscBorderGuardTrapsEventReason = MibScalar((1, 3, 6, 1, 4, 1, 10, 2, 1, 9, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255)))
if mibBuilder.loadTexts: nscBorderGuardTrapsEventReason.setStatus('mandatory')
nscBorderGuardBadCRC = NotificationType((1, 3, 6, 1, 4, 1, 10, 2, 1, 9, 1) + (0,1)).setObjects(("NSC-BORDERGUARD-TRAP", "nscBorderGuardTrapsBadImage"), ("NSC-BORDERGUARD-TRAP", "nscBorderGuardTrapsCurrentImage"), ("NSC-BORDERGUARD-TRAP", "nscBorderGuardTrapsEventReason"))
nscBorderGuardBadFileSystem = NotificationType((1, 3, 6, 1, 4, 1, 10, 2, 1, 9, 1) + (0,2)).setObjects(("NSC-BORDERGUARD-TRAP", "nscBorderGuardTrapsBadFileSystem"), ("NSC-BORDERGUARD-TRAP", "nscBorderGuardTrapsEventReason"))
nscBorderGuardSoftFault = NotificationType((1, 3, 6, 1, 4, 1, 10, 2, 1, 9, 1) + (0,3)).setObjects(("NSC-BORDERGUARD-TRAP", "nscBorderGuardTrapsSoftFault"), ("NSC-BORDERGUARD-TRAP", "nscBorderGuardTrapsEventReason"))
mibBuilder.exportSymbols("NSC-BORDERGUARD-TRAP", nscBorderGuardBadCRC=nscBorderGuardBadCRC, nscBorderGuardTrapsBadImage=nscBorderGuardTrapsBadImage, nscBorderGuardTrapsEventReason=nscBorderGuardTrapsEventReason, nscBorderGuardBadFileSystem=nscBorderGuardBadFileSystem, nscBorderGuardTrapsSoftFault=nscBorderGuardTrapsSoftFault, nscBorderGuardTraps=nscBorderGuardTraps, nscBorderGuardTrapsCurrentImage=nscBorderGuardTrapsCurrentImage, nscBorderGuardSoftFault=nscBorderGuardSoftFault, nscBorderGuardTrapsBadFileSystem=nscBorderGuardTrapsBadFileSystem)
