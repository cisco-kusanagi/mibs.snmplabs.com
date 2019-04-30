#
# PySNMP MIB module RADLAN-SECURITY-SUITE (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RADLAN-SECURITY-SUITE
# Produced by pysmi-0.3.4 at Mon Apr 29 20:40:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
InterfaceIndexOrZero, InterfaceIndex, ifIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero", "InterfaceIndex", "ifIndex")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
Percents, rnd = mibBuilder.importSymbols("RADLAN-MIB", "Percents", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, TimeTicks, Counter32, iso, ObjectIdentity, ModuleIdentity, Counter64, Bits, IpAddress, Integer32, NotificationType, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "TimeTicks", "Counter32", "iso", "ObjectIdentity", "ModuleIdentity", "Counter64", "Bits", "IpAddress", "Integer32", "NotificationType", "Unsigned32")
TextualConvention, RowStatus, DisplayString, TruthValue, RowPointer = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString", "TruthValue", "RowPointer")
rlSecuritySuiteMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 120))
rlSecuritySuiteMib.setRevisions(('2006-01-09 00:00',))
if mibBuilder.loadTexts: rlSecuritySuiteMib.setLastUpdated('200604080000Z')
if mibBuilder.loadTexts: rlSecuritySuiteMib.setOrganization('Radlan Computer Communications Ltd.')
class RlsecuritySuiteGlobalEnableType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("enable-global-rules-only", 1), ("enable-all-rules-types", 2), ("disable", 3))

class RlSecuritySuiteKnownDosAttackType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("stacheldraht", 1), ("invasor-Trojan", 2), ("back-orifice-Trojan", 3))

class RlSecuritySuiteKnownDosAttackProtocolType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("tcp", 1), ("upd", 2))

class RlSecuritySuiteAllMartianEntryType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("reserved", 1), ("static", 2))

class RlSecuritySuiteDenyAttackType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("syn", 1), ("icmp-echo-request", 2), ("fragmented", 3))

class RlSecuritySuiteDenySynFinTcp(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("deny", 1), ("permit", 2))

class RlSecuritySuiteSynProtectionMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("disabled", 1), ("report", 2), ("block", 3))

class RlSecuritySuiteSynProtectionPortMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("normal", 1), ("attacked", 2), ("blocked", 3))

rlSecuritySuiteGlobalEnable = MibScalar((1, 3, 6, 1, 4, 1, 89, 120, 1), RlsecuritySuiteGlobalEnableType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSecuritySuiteGlobalEnable.setStatus('current')
rlSecuritySuiteKnownDoSAttacksTable = MibTable((1, 3, 6, 1, 4, 1, 89, 120, 2), )
if mibBuilder.loadTexts: rlSecuritySuiteKnownDoSAttacksTable.setStatus('current')
rlSecuritySuiteKnownDoSAttacksEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 120, 2, 1), ).setIndexNames((0, "RADLAN-SECURITY-SUITE", "rlSecuritySuiteKnownDoSAttack"))
if mibBuilder.loadTexts: rlSecuritySuiteKnownDoSAttacksEntry.setStatus('current')
rlSecuritySuiteKnownDoSAttack = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 120, 2, 1, 1), RlSecuritySuiteKnownDosAttackType())
if mibBuilder.loadTexts: rlSecuritySuiteKnownDoSAttack.setStatus('current')
rlSecuritySuiteKnownDoSAttackEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 120, 2, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSecuritySuiteKnownDoSAttackEnable.setStatus('current')
rlSecuritySuiteKnownDoSAttacksDetailsTable = MibTable((1, 3, 6, 1, 4, 1, 89, 120, 3), )
if mibBuilder.loadTexts: rlSecuritySuiteKnownDoSAttacksDetailsTable.setStatus('current')
rlSecuritySuiteKnownDoSAttacksDetailsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 120, 3, 1), ).setIndexNames((0, "RADLAN-SECURITY-SUITE", "rlSecuritySuiteKnownDoSAttack"))
if mibBuilder.loadTexts: rlSecuritySuiteKnownDoSAttacksDetailsEntry.setStatus('current')
rlSecuritySuiteKnownDoSAttackProtocl = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 120, 3, 1, 1), RlSecuritySuiteKnownDosAttackProtocolType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSecuritySuiteKnownDoSAttackProtocl.setStatus('current')
rlSecuritySuiteKnownDoSAttackSrcTcpUdpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 120, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSecuritySuiteKnownDoSAttackSrcTcpUdpPort.setStatus('current')
rlSecuritySuiteKnownDoSAttackDestTcpUdpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 120, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSecuritySuiteKnownDoSAttackDestTcpUdpPort.setStatus('current')
rlSecuritySuiteReservedMartianAddresses = MibScalar((1, 3, 6, 1, 4, 1, 89, 120, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSecuritySuiteReservedMartianAddresses.setStatus('current')
rlSecuritySuiteMartianAddrAllTable = MibTable((1, 3, 6, 1, 4, 1, 89, 120, 5), )
if mibBuilder.loadTexts: rlSecuritySuiteMartianAddrAllTable.setStatus('current')
rlSecuritySuiteMartianAddrAllEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 120, 5, 1), ).setIndexNames((0, "RADLAN-SECURITY-SUITE", "rlSecuritySuiteMartianAddr"), (0, "RADLAN-SECURITY-SUITE", "rlSecuritySuiteMartianAddrNetMask"))
if mibBuilder.loadTexts: rlSecuritySuiteMartianAddrAllEntry.setStatus('current')
rlSecuritySuiteMartianAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 120, 5, 1, 1), IpAddress())
if mibBuilder.loadTexts: rlSecuritySuiteMartianAddr.setStatus('current')
rlSecuritySuiteMartianAddrNetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 120, 5, 1, 2), IpAddress())
if mibBuilder.loadTexts: rlSecuritySuiteMartianAddrNetMask.setStatus('current')
rlSecuritySuiteAllMartianEntryType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 120, 5, 1, 3), RlSecuritySuiteAllMartianEntryType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSecuritySuiteAllMartianEntryType.setStatus('current')
rlSecuritySuiteMartianAddrTable = MibTable((1, 3, 6, 1, 4, 1, 89, 120, 6), )
if mibBuilder.loadTexts: rlSecuritySuiteMartianAddrTable.setStatus('current')
rlSecuritySuiteMartianAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 120, 6, 1), ).setIndexNames((0, "RADLAN-SECURITY-SUITE", "rlSecuritySuiteMartianAddr"), (0, "RADLAN-SECURITY-SUITE", "rlSecuritySuiteMartianAddrNetMask"))
if mibBuilder.loadTexts: rlSecuritySuiteMartianAddrEntry.setStatus('current')
rlSecuritySuiteMartianAddrStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 120, 6, 1, 1), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlSecuritySuiteMartianAddrStatus.setStatus('current')
rlSecuritySuiteDoSSynAttackTable = MibTable((1, 3, 6, 1, 4, 1, 89, 120, 7), )
if mibBuilder.loadTexts: rlSecuritySuiteDoSSynAttackTable.setStatus('current')
rlSecuritySuiteDoSSynAttackEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 120, 7, 1), ).setIndexNames((0, "RADLAN-SECURITY-SUITE", "rlSecuritySuiteDoSSynAttackIfIndex"), (0, "RADLAN-SECURITY-SUITE", "rlSecuritySuiteDoSSynAttackAddr"), (0, "RADLAN-SECURITY-SUITE", "rlSecuritySuiteDoSSynAttackNetMask"))
if mibBuilder.loadTexts: rlSecuritySuiteDoSSynAttackEntry.setStatus('current')
rlSecuritySuiteDoSSynAttackIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 120, 7, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: rlSecuritySuiteDoSSynAttackIfIndex.setStatus('current')
rlSecuritySuiteDoSSynAttackAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 120, 7, 1, 2), IpAddress())
if mibBuilder.loadTexts: rlSecuritySuiteDoSSynAttackAddr.setStatus('current')
rlSecuritySuiteDoSSynAttackNetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 120, 7, 1, 3), IpAddress())
if mibBuilder.loadTexts: rlSecuritySuiteDoSSynAttackNetMask.setStatus('current')
rlSecuritySuiteDoSSynAttackSynRate = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 120, 7, 1, 4), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlSecuritySuiteDoSSynAttackSynRate.setStatus('current')
rlSecuritySuiteDoSSynAttackStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 120, 7, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlSecuritySuiteDoSSynAttackStatus.setStatus('current')
rlSecuritySuiteDenyTypesTable = MibTable((1, 3, 6, 1, 4, 1, 89, 120, 8), )
if mibBuilder.loadTexts: rlSecuritySuiteDenyTypesTable.setStatus('current')
rlSecuritySuiteDenyTypesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 120, 8, 1), ).setIndexNames((0, "RADLAN-SECURITY-SUITE", "rlSecuritySuiteDenyIfIndex"), (0, "RADLAN-SECURITY-SUITE", "rlSecuritySuiteDenyAttackType"), (0, "RADLAN-SECURITY-SUITE", "rlSecuritySuiteDenyDestAddr"), (0, "RADLAN-SECURITY-SUITE", "rlSecuritySuiteDenyNetMask"), (0, "RADLAN-SECURITY-SUITE", "rlSecuritySuiteDenyDestPort"))
if mibBuilder.loadTexts: rlSecuritySuiteDenyTypesEntry.setStatus('current')
rlSecuritySuiteDenyIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 120, 8, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: rlSecuritySuiteDenyIfIndex.setStatus('current')
rlSecuritySuiteDenyAttackType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 120, 8, 1, 2), RlSecuritySuiteDenyAttackType())
if mibBuilder.loadTexts: rlSecuritySuiteDenyAttackType.setStatus('current')
rlSecuritySuiteDenyDestAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 120, 8, 1, 3), IpAddress())
if mibBuilder.loadTexts: rlSecuritySuiteDenyDestAddr.setStatus('current')
rlSecuritySuiteDenyNetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 120, 8, 1, 4), IpAddress())
if mibBuilder.loadTexts: rlSecuritySuiteDenyNetMask.setStatus('current')
rlSecuritySuiteDenyDestPort = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 120, 8, 1, 5), Integer32())
if mibBuilder.loadTexts: rlSecuritySuiteDenyDestPort.setStatus('current')
rlSecuritySuiteDenyStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 120, 8, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlSecuritySuiteDenyStatus.setStatus('current')
rlSecuritySuiteDenySynFinTcp = MibScalar((1, 3, 6, 1, 4, 1, 89, 120, 9), RlSecuritySuiteDenySynFinTcp()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSecuritySuiteDenySynFinTcp.setStatus('current')
rlSecuritySuiteSynProtectionMode = MibScalar((1, 3, 6, 1, 4, 1, 89, 120, 10), RlSecuritySuiteSynProtectionMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSecuritySuiteSynProtectionMode.setStatus('current')
rlSecuritySuiteSynProtectionTreshold = MibScalar((1, 3, 6, 1, 4, 1, 89, 120, 11), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSecuritySuiteSynProtectionTreshold.setStatus('current')
rlSecuritySuiteSynProtectionRecoveryTimeout = MibScalar((1, 3, 6, 1, 4, 1, 89, 120, 12), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSecuritySuiteSynProtectionRecoveryTimeout.setStatus('current')
rlSecuritySuiteSynProtectionPortTable = MibTable((1, 3, 6, 1, 4, 1, 89, 120, 13), )
if mibBuilder.loadTexts: rlSecuritySuiteSynProtectionPortTable.setStatus('current')
rlSecuritySuiteSynProtectionPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 120, 13, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: rlSecuritySuiteSynProtectionPortEntry.setStatus('current')
rlSecuritySuiteSynProtectionPortMode = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 120, 13, 1, 1), RlSecuritySuiteSynProtectionPortMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSecuritySuiteSynProtectionPortMode.setStatus('current')
rlSecuritySuiteSynProtectionPortModeLastTimeAttack = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 120, 13, 1, 2), RlSecuritySuiteSynProtectionPortMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSecuritySuiteSynProtectionPortModeLastTimeAttack.setStatus('current')
rlSecuritySuiteSynProtectionPortLastTimeAttack = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 120, 13, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSecuritySuiteSynProtectionPortLastTimeAttack.setStatus('current')
mibBuilder.exportSymbols("RADLAN-SECURITY-SUITE", rlSecuritySuiteMib=rlSecuritySuiteMib, rlSecuritySuiteReservedMartianAddresses=rlSecuritySuiteReservedMartianAddresses, rlSecuritySuiteMartianAddrAllTable=rlSecuritySuiteMartianAddrAllTable, rlSecuritySuiteMartianAddrEntry=rlSecuritySuiteMartianAddrEntry, RlSecuritySuiteDenyAttackType=RlSecuritySuiteDenyAttackType, rlSecuritySuiteAllMartianEntryType=rlSecuritySuiteAllMartianEntryType, rlSecuritySuiteKnownDoSAttacksEntry=rlSecuritySuiteKnownDoSAttacksEntry, RlSecuritySuiteSynProtectionMode=RlSecuritySuiteSynProtectionMode, rlSecuritySuiteKnownDoSAttacksDetailsTable=rlSecuritySuiteKnownDoSAttacksDetailsTable, RlSecuritySuiteDenySynFinTcp=RlSecuritySuiteDenySynFinTcp, rlSecuritySuiteKnownDoSAttackEnable=rlSecuritySuiteKnownDoSAttackEnable, rlSecuritySuiteKnownDoSAttackProtocl=rlSecuritySuiteKnownDoSAttackProtocl, rlSecuritySuiteSynProtectionPortTable=rlSecuritySuiteSynProtectionPortTable, rlSecuritySuiteSynProtectionPortEntry=rlSecuritySuiteSynProtectionPortEntry, rlSecuritySuiteDenyDestAddr=rlSecuritySuiteDenyDestAddr, rlSecuritySuiteDoSSynAttackNetMask=rlSecuritySuiteDoSSynAttackNetMask, RlSecuritySuiteAllMartianEntryType=RlSecuritySuiteAllMartianEntryType, rlSecuritySuiteMartianAddrNetMask=rlSecuritySuiteMartianAddrNetMask, rlSecuritySuiteSynProtectionTreshold=rlSecuritySuiteSynProtectionTreshold, rlSecuritySuiteDenyStatus=rlSecuritySuiteDenyStatus, rlSecuritySuiteDenyTypesTable=rlSecuritySuiteDenyTypesTable, PYSNMP_MODULE_ID=rlSecuritySuiteMib, rlSecuritySuiteDenySynFinTcp=rlSecuritySuiteDenySynFinTcp, RlSecuritySuiteKnownDosAttackType=RlSecuritySuiteKnownDosAttackType, rlSecuritySuiteMartianAddr=rlSecuritySuiteMartianAddr, rlSecuritySuiteSynProtectionRecoveryTimeout=rlSecuritySuiteSynProtectionRecoveryTimeout, rlSecuritySuiteDoSSynAttackIfIndex=rlSecuritySuiteDoSSynAttackIfIndex, rlSecuritySuiteMartianAddrTable=rlSecuritySuiteMartianAddrTable, rlSecuritySuiteDenyAttackType=rlSecuritySuiteDenyAttackType, rlSecuritySuiteDoSSynAttackEntry=rlSecuritySuiteDoSSynAttackEntry, rlSecuritySuiteKnownDoSAttackSrcTcpUdpPort=rlSecuritySuiteKnownDoSAttackSrcTcpUdpPort, rlSecuritySuiteKnownDoSAttackDestTcpUdpPort=rlSecuritySuiteKnownDoSAttackDestTcpUdpPort, rlSecuritySuiteKnownDoSAttacksTable=rlSecuritySuiteKnownDoSAttacksTable, rlSecuritySuiteKnownDoSAttack=rlSecuritySuiteKnownDoSAttack, rlSecuritySuiteDoSSynAttackTable=rlSecuritySuiteDoSSynAttackTable, rlSecuritySuiteDoSSynAttackSynRate=rlSecuritySuiteDoSSynAttackSynRate, rlSecuritySuiteDenyNetMask=rlSecuritySuiteDenyNetMask, rlSecuritySuiteSynProtectionMode=rlSecuritySuiteSynProtectionMode, rlSecuritySuiteSynProtectionPortModeLastTimeAttack=rlSecuritySuiteSynProtectionPortModeLastTimeAttack, rlSecuritySuiteDenyIfIndex=rlSecuritySuiteDenyIfIndex, rlSecuritySuiteDoSSynAttackStatus=rlSecuritySuiteDoSSynAttackStatus, rlSecuritySuiteKnownDoSAttacksDetailsEntry=rlSecuritySuiteKnownDoSAttacksDetailsEntry, rlSecuritySuiteSynProtectionPortLastTimeAttack=rlSecuritySuiteSynProtectionPortLastTimeAttack, rlSecuritySuiteDoSSynAttackAddr=rlSecuritySuiteDoSSynAttackAddr, rlSecuritySuiteDenyTypesEntry=rlSecuritySuiteDenyTypesEntry, RlSecuritySuiteKnownDosAttackProtocolType=RlSecuritySuiteKnownDosAttackProtocolType, rlSecuritySuiteGlobalEnable=rlSecuritySuiteGlobalEnable, rlSecuritySuiteMartianAddrStatus=rlSecuritySuiteMartianAddrStatus, RlSecuritySuiteSynProtectionPortMode=RlSecuritySuiteSynProtectionPortMode, rlSecuritySuiteMartianAddrAllEntry=rlSecuritySuiteMartianAddrAllEntry, rlSecuritySuiteDenyDestPort=rlSecuritySuiteDenyDestPort, rlSecuritySuiteSynProtectionPortMode=rlSecuritySuiteSynProtectionPortMode, RlsecuritySuiteGlobalEnableType=RlsecuritySuiteGlobalEnableType)
