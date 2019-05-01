#
# PySNMP MIB module CISCOSB-ERRDISABLE-RECOVERY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCOSB-ERRDISABLE-RECOVERY-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:22:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
switch001, = mibBuilder.importSymbols("CISCOSB-MIB", "switch001")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, TimeTicks, Gauge32, MibIdentifier, Unsigned32, IpAddress, ObjectIdentity, ModuleIdentity, NotificationType, Bits, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "TimeTicks", "Gauge32", "MibIdentifier", "Unsigned32", "IpAddress", "ObjectIdentity", "ModuleIdentity", "NotificationType", "Bits", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter32")
DisplayString, TextualConvention, RowStatus, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus", "TruthValue")
rlErrdisableRecovery = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 128))
rlErrdisableRecovery.setRevisions(('2007-11-07 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlErrdisableRecovery.setRevisionsDescriptions(('Initial version of this MIB.',))
if mibBuilder.loadTexts: rlErrdisableRecovery.setLastUpdated('200711070000Z')
if mibBuilder.loadTexts: rlErrdisableRecovery.setOrganization('Cisco Small Business')
if mibBuilder.loadTexts: rlErrdisableRecovery.setContactInfo('Postal: 170 West Tasman Drive San Jose , CA 95134-1706 USA Website: Cisco Small Business Home http://www.cisco.com/smb>;, Cisco Small Business Support Community <http://www.cisco.com/go/smallbizsupport>')
if mibBuilder.loadTexts: rlErrdisableRecovery.setDescription('The private MIB module definition for Errdisable Recovery MIB.')
class RlErrdisableRecoveryCauseType(TextualConvention, Integer32):
    description = 'Errdisable Recovery Cause Type.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("loopback-detection", 1), ("port-security", 2), ("dot1x-src-address", 3), ("acl-deny", 4), ("stp-bpdu-guard", 5), ("stp-loopback-guard", 6), ("pcb-overheat", 7), ("udld", 8))

rlErrdisableRecoveryInterval = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 128, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(30, 86400))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlErrdisableRecoveryInterval.setStatus('current')
if mibBuilder.loadTexts: rlErrdisableRecoveryInterval.setDescription('Timeout interval in seconds for automatic activation of an interface after shutdown.')
rlErrdisableRecoveryCauseTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 128, 2), )
if mibBuilder.loadTexts: rlErrdisableRecoveryCauseTable.setStatus('current')
if mibBuilder.loadTexts: rlErrdisableRecoveryCauseTable.setDescription('The table is used to enable or disable auto-recovery for specific application causes port suspend. The table includes entries for all applications.')
rlErrdisableRecoveryCauseEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 128, 2, 1), ).setIndexNames((0, "CISCOSB-ERRDISABLE-RECOVERY-MIB", "rlErrdisableRecoveryCause"))
if mibBuilder.loadTexts: rlErrdisableRecoveryCauseEntry.setStatus('current')
if mibBuilder.loadTexts: rlErrdisableRecoveryCauseEntry.setDescription('An entry (conceptual row) in the rlErrdisableRecoveryCauseEntry.')
rlErrdisableRecoveryCause = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 128, 2, 1, 1), RlErrdisableRecoveryCauseType())
if mibBuilder.loadTexts: rlErrdisableRecoveryCause.setStatus('current')
if mibBuilder.loadTexts: rlErrdisableRecoveryCause.setDescription('Type of recovery cause.')
rlErrdisableRecoveryEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 128, 2, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlErrdisableRecoveryEnable.setStatus('current')
if mibBuilder.loadTexts: rlErrdisableRecoveryEnable.setDescription('Enable/Disable automatic recovery.')
rlErrdisableRecoveryIfTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 128, 3), )
if mibBuilder.loadTexts: rlErrdisableRecoveryIfTable.setStatus('current')
if mibBuilder.loadTexts: rlErrdisableRecoveryIfTable.setDescription('The table is used for show the reason of shutdown the port in errdisable state. The table includes only suspended interfaces.')
rlErrdisableRecoveryIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 128, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: rlErrdisableRecoveryIfEntry.setStatus('current')
if mibBuilder.loadTexts: rlErrdisableRecoveryIfEntry.setDescription('An entry (conceptual row) in the rlErrdisableRecoveryIfEntry.')
rlErrdisableRecoveryIfReason = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 128, 3, 1, 1), RlErrdisableRecoveryCauseType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlErrdisableRecoveryIfReason.setStatus('current')
if mibBuilder.loadTexts: rlErrdisableRecoveryIfReason.setDescription(' The reason of shutdown the port in errdisable state.')
rlErrdisableRecoveryIfEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 128, 3, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlErrdisableRecoveryIfEnable.setStatus('current')
if mibBuilder.loadTexts: rlErrdisableRecoveryIfEnable.setDescription('Enable/Disable automatic recovery status.')
mibBuilder.exportSymbols("CISCOSB-ERRDISABLE-RECOVERY-MIB", rlErrdisableRecoveryCauseEntry=rlErrdisableRecoveryCauseEntry, rlErrdisableRecoveryIfReason=rlErrdisableRecoveryIfReason, rlErrdisableRecoveryEnable=rlErrdisableRecoveryEnable, rlErrdisableRecoveryCause=rlErrdisableRecoveryCause, rlErrdisableRecoveryIfEntry=rlErrdisableRecoveryIfEntry, rlErrdisableRecovery=rlErrdisableRecovery, rlErrdisableRecoveryInterval=rlErrdisableRecoveryInterval, rlErrdisableRecoveryIfTable=rlErrdisableRecoveryIfTable, RlErrdisableRecoveryCauseType=RlErrdisableRecoveryCauseType, rlErrdisableRecoveryCauseTable=rlErrdisableRecoveryCauseTable, PYSNMP_MODULE_ID=rlErrdisableRecovery, rlErrdisableRecoveryIfEnable=rlErrdisableRecoveryIfEnable)
