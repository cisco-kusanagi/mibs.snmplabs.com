#
# PySNMP MIB module MARVELL-ERRDISABLE-RECOVERY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MARVELL-ERRDISABLE-RECOVERY-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:59:22 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, ModuleIdentity, Gauge32, ObjectIdentity, Counter64, IpAddress, TimeTicks, Unsigned32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "ModuleIdentity", "Gauge32", "ObjectIdentity", "Counter64", "IpAddress", "TimeTicks", "Unsigned32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Integer32", "iso")
TruthValue, RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowStatus", "TextualConvention", "DisplayString")
rlErrdisableRecovery = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 128))
rlErrdisableRecovery.setRevisions(('2007-11-07 00:00',))
if mibBuilder.loadTexts: rlErrdisableRecovery.setLastUpdated('200711070000Z')
if mibBuilder.loadTexts: rlErrdisableRecovery.setOrganization('Marvell Semiconductor, Inc.')
class RlErrdisableRecoveryCauseType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("loopback-detection", 1), ("port-security", 2), ("dot1x-src-address", 3), ("acl-deny", 4), ("stp-bpdu-guard", 5), ("stp-loopback-guard", 6), ("pcb-overheat", 7), ("udld", 8), ("storm-control", 9), ("link-flapping", 10))

rlErrdisableRecoveryInterval = MibScalar((1, 3, 6, 1, 4, 1, 89, 128, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(30, 86400))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlErrdisableRecoveryInterval.setStatus('current')
rlErrdisableRecoveryCauseTable = MibTable((1, 3, 6, 1, 4, 1, 89, 128, 2), )
if mibBuilder.loadTexts: rlErrdisableRecoveryCauseTable.setStatus('current')
rlErrdisableRecoveryCauseEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 128, 2, 1), ).setIndexNames((0, "MARVELL-ERRDISABLE-RECOVERY-MIB", "rlErrdisableRecoveryCause"))
if mibBuilder.loadTexts: rlErrdisableRecoveryCauseEntry.setStatus('current')
rlErrdisableRecoveryCause = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 128, 2, 1, 1), RlErrdisableRecoveryCauseType())
if mibBuilder.loadTexts: rlErrdisableRecoveryCause.setStatus('current')
rlErrdisableRecoveryEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 128, 2, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlErrdisableRecoveryEnable.setStatus('current')
rlErrdisableRecoveryIfTable = MibTable((1, 3, 6, 1, 4, 1, 89, 128, 3), )
if mibBuilder.loadTexts: rlErrdisableRecoveryIfTable.setStatus('current')
rlErrdisableRecoveryIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 128, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: rlErrdisableRecoveryIfEntry.setStatus('current')
rlErrdisableRecoveryIfReason = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 128, 3, 1, 1), RlErrdisableRecoveryCauseType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlErrdisableRecoveryIfReason.setStatus('current')
rlErrdisableRecoveryIfEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 128, 3, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlErrdisableRecoveryIfEnable.setStatus('current')
mibBuilder.exportSymbols("MARVELL-ERRDISABLE-RECOVERY-MIB", rlErrdisableRecoveryCause=rlErrdisableRecoveryCause, rlErrdisableRecoveryIfEntry=rlErrdisableRecoveryIfEntry, rlErrdisableRecoveryCauseTable=rlErrdisableRecoveryCauseTable, RlErrdisableRecoveryCauseType=RlErrdisableRecoveryCauseType, rlErrdisableRecoveryCauseEntry=rlErrdisableRecoveryCauseEntry, rlErrdisableRecoveryEnable=rlErrdisableRecoveryEnable, rlErrdisableRecoveryIfTable=rlErrdisableRecoveryIfTable, rlErrdisableRecoveryIfEnable=rlErrdisableRecoveryIfEnable, PYSNMP_MODULE_ID=rlErrdisableRecovery, rlErrdisableRecovery=rlErrdisableRecovery, rlErrdisableRecoveryInterval=rlErrdisableRecoveryInterval, rlErrdisableRecoveryIfReason=rlErrdisableRecoveryIfReason)
