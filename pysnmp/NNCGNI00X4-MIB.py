#
# PySNMP MIB module NNCGNI00X4-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NNCGNI00X4-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:13:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
nncExtPosition, = mibBuilder.importSymbols("NNCGNI00X1-SMI", "nncExtPosition")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, ObjectIdentity, IpAddress, Bits, MibIdentifier, Gauge32, Integer32, NotificationType, Unsigned32, iso, Counter32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "ObjectIdentity", "IpAddress", "Bits", "MibIdentifier", "Gauge32", "Integer32", "NotificationType", "Unsigned32", "iso", "Counter32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class PositionIndex(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class PositionCardType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 46, 108, 109, 110, 111, 120, 6, 5))
    namedValues = NamedValues(("noCard", 1), ("ctlCard", 46), ("x21Card", 108), ("v24Card", 109), ("v35Card", 110), ("ethernetCard", 111), ("hubCard", 120), ("t1Card", 6), ("e1Card", 5))

class PositionModuleType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 24, 25, 26, 27, 28, 29))
    namedValues = NamedValues(("noModule", 1), ("thinModule", 24), ("tpModule", 25), ("auiModule", 26), ("nullAUIModule", 27), ("foirlModule", 28), ("hubModule", 29))

class PositionCardId(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 2, 4, 6, 1, 12, 8, 10, 24, 28))
    namedValues = NamedValues(("ctlCardId", 0), ("x21CardId", 2), ("v24CardId", 4), ("v35CardId", 6), ("ethernetCardId", 1), ("e1CoaxCardId", 12), ("t1DsxCardId", 8), ("t1CsuCardId", 10), ("e1TpCardId", 24), ("hubCardId", 28))

class PositionModuleId(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 4, 5, 6, 0))
    namedValues = NamedValues(("thinModId", 1), ("hubModId", 2), ("tpModId", 4), ("foirlModId", 5), ("nullAUIModId", 6), ("auiModId", 0))

class PositionVariantId(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

class RevisionNumber(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

class PositionAdminStatus(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("inUse", 1), ("busiedOut", 2), ("reset", 3))

class PositionOperStatus(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 9, 12))
    namedValues = NamedValues(("empty", 1), ("ok", 2), ("fault-on-module", 3), ("module-dead", 4), ("unknown-module-type", 5), ("module-type-mismatch", 6), ("sub-module-type-mismatch", 7), ("wrong-firmware", 9), ("wrong-variant", 12))

nncExtPositionMaxPossible = MibScalar((1, 3, 6, 1, 4, 1, 123, 3, 8, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtPositionMaxPossible.setStatus('mandatory')
nncExtPositionTable = MibTable((1, 3, 6, 1, 4, 1, 123, 3, 8, 2), )
if mibBuilder.loadTexts: nncExtPositionTable.setStatus('mandatory')
nncExtPositionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 123, 3, 8, 2, 1), ).setIndexNames((0, "NNCGNI00X4-MIB", "nncExtPositionIndex"))
if mibBuilder.loadTexts: nncExtPositionEntry.setStatus('mandatory')
nncExtPositionIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 8, 2, 1, 1), PositionIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtPositionIndex.setStatus('mandatory')
nncExtPositionProgCard = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 8, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 46, 108, 109, 110, 111, 120, 6, 5))).clone(namedValues=NamedValues(("noCard", 1), ("ctlCard", 46), ("x21Card", 108), ("v24Card", 109), ("v35Card", 110), ("ethernetCard", 111), ("hubCard", 120), ("t1Card", 6), ("e1Card", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nncExtPositionProgCard.setStatus('mandatory')
nncExtPositionProgModule = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 8, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 24, 25, 26, 27, 28, 29))).clone(namedValues=NamedValues(("noModule", 1), ("thinModule", 24), ("tpModule", 25), ("auiModule", 26), ("nullAUIModule", 27), ("foirlModule", 28), ("hubModule", 29)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nncExtPositionProgModule.setStatus('mandatory')
nncExtPositionCurrentCard = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 8, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 46, 108, 109, 110, 111, 120, 6, 5))).clone(namedValues=NamedValues(("noCard", 1), ("ctlCard", 46), ("x21Card", 108), ("v24Card", 109), ("v35Card", 110), ("ethernetCard", 111), ("hubCard", 120), ("t1Card", 6), ("e1Card", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtPositionCurrentCard.setStatus('mandatory')
nncExtPositionCurrentModule = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 8, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 24, 25, 26, 27, 28, 29))).clone(namedValues=NamedValues(("noModule", 1), ("thinModule", 24), ("tpModule", 25), ("auiModule", 26), ("nullAUIModule", 27), ("foirlModule", 28), ("hubModule", 29)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtPositionCurrentModule.setStatus('mandatory')
nncExtPositionOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 8, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 9, 12))).clone(namedValues=NamedValues(("empty", 1), ("ok", 2), ("fault-on-module", 3), ("module-dead", 4), ("unknown-module-type", 5), ("module-type-mismatch", 6), ("sub-module-type-mismatch", 7), ("wrong-firmware", 9), ("wrong-variant", 12)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtPositionOperStatus.setStatus('mandatory')
nncExtPositionAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 8, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("inUse", 1), ("busiedOut", 2), ("reset", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nncExtPositionAdminStatus.setStatus('mandatory')
nncExtPositionCardId = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 8, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 2, 4, 6, 1, 12, 8, 10, 24, 28))).clone(namedValues=NamedValues(("ctlCardId", 0), ("x21CardId", 2), ("v24CardId", 4), ("v35CardId", 6), ("ethernetCardId", 1), ("e1CoaxCardId", 12), ("t1DsxCardId", 8), ("t1CsuCardId", 10), ("e1TpCardId", 24), ("hubCardId", 28)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtPositionCardId.setStatus('mandatory')
nncExtPositionModuleId = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 8, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 4, 5, 6, 0))).clone(namedValues=NamedValues(("thinModId", 1), ("hubModId", 2), ("tpModId", 4), ("foirlModId", 5), ("nullAUIModId", 6), ("auiModId", 0)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtPositionModuleId.setStatus('mandatory')
nncExtPositionVariantId = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 8, 2, 1, 10), PositionVariantId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtPositionVariantId.setStatus('mandatory')
nncExtPositionHardwareRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 8, 2, 1, 11), RevisionNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtPositionHardwareRevision.setStatus('mandatory')
nncExtPositionFirmwareRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 8, 2, 1, 12), RevisionNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtPositionFirmwareRevision.setStatus('mandatory')
nncExtPositionUIName = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 8, 2, 1, 13), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtPositionUIName.setStatus('mandatory')
nncExtPositionName = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 8, 2, 1, 14), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 8))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nncExtPositionName.setStatus('mandatory')
nncExtPositionBackplaneIdAndRev = MibScalar((1, 3, 6, 1, 4, 1, 123, 3, 8, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtPositionBackplaneIdAndRev.setStatus('mandatory')
nncExtPositionDisplayIdAndRev = MibScalar((1, 3, 6, 1, 4, 1, 123, 3, 8, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtPositionDisplayIdAndRev.setStatus('mandatory')
mibBuilder.exportSymbols("NNCGNI00X4-MIB", nncExtPositionName=nncExtPositionName, nncExtPositionFirmwareRevision=nncExtPositionFirmwareRevision, PositionIndex=PositionIndex, PositionModuleType=PositionModuleType, PositionOperStatus=PositionOperStatus, PositionCardId=PositionCardId, nncExtPositionHardwareRevision=nncExtPositionHardwareRevision, nncExtPositionDisplayIdAndRev=nncExtPositionDisplayIdAndRev, nncExtPositionOperStatus=nncExtPositionOperStatus, nncExtPositionProgModule=nncExtPositionProgModule, nncExtPositionCurrentCard=nncExtPositionCurrentCard, PositionModuleId=PositionModuleId, RevisionNumber=RevisionNumber, nncExtPositionBackplaneIdAndRev=nncExtPositionBackplaneIdAndRev, PositionVariantId=PositionVariantId, nncExtPositionMaxPossible=nncExtPositionMaxPossible, nncExtPositionCurrentModule=nncExtPositionCurrentModule, nncExtPositionCardId=nncExtPositionCardId, nncExtPositionIndex=nncExtPositionIndex, nncExtPositionVariantId=nncExtPositionVariantId, nncExtPositionTable=nncExtPositionTable, nncExtPositionModuleId=nncExtPositionModuleId, nncExtPositionEntry=nncExtPositionEntry, nncExtPositionProgCard=nncExtPositionProgCard, nncExtPositionAdminStatus=nncExtPositionAdminStatus, nncExtPositionUIName=nncExtPositionUIName, PositionCardType=PositionCardType, PositionAdminStatus=PositionAdminStatus)
