#
# PySNMP MIB module JUNIPER-JVAE-NODE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/JUNIPER-JVAE-NODE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:48:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
jnxJVAEMibRoot, = mibBuilder.importSymbols("JUNIPER-SMI", "jnxJVAEMibRoot")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Bits, TimeTicks, IpAddress, Integer32, Gauge32, iso, MibIdentifier, ObjectIdentity, Counter64, Unsigned32, Counter32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Bits", "TimeTicks", "IpAddress", "Integer32", "Gauge32", "iso", "MibIdentifier", "ObjectIdentity", "Counter64", "Unsigned32", "Counter32", "NotificationType")
TruthValue, PhysAddress, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "PhysAddress", "DisplayString", "TextualConvention")
jnxJVAENodeMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 69, 2))
jnxJVAENodeMIB.setRevisions(('2012-08-01 00:00',))
if mibBuilder.loadTexts: jnxJVAENodeMIB.setLastUpdated('201208010000Z')
if mibBuilder.loadTexts: jnxJVAENodeMIB.setOrganization('Juniper Networks, Inc.')
jnxJVAENodeNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 0))
jnxJVAENodeObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1))
jnxJVAENodeTables = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1))
jnxJVAECNSysInfoTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 1), )
if mibBuilder.loadTexts: jnxJVAECNSysInfoTable.setStatus('current')
jnxJVAECNSysInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 1, 1), ).setIndexNames((0, "JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSysId"))
if mibBuilder.loadTexts: jnxJVAECNSysInfoEntry.setStatus('current')
jnxJVAECNSysId = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: jnxJVAECNSysId.setStatus('current')
jnxJVAECNSysCpus = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJVAECNSysCpus.setStatus('current')
jnxJVAECNSysProcessingLoad = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('%').setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJVAECNSysProcessingLoad.setStatus('current')
jnxJVAECNSysMemCapacity = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 1, 1, 4), Gauge32()).setUnits('KB').setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJVAECNSysMemCapacity.setStatus('current')
jnxJVAECNSysMemUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 1, 1, 5), Gauge32()).setUnits('KB').setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJVAECNSysMemUsed.setStatus('current')
jnxJVAECNSysMemFree = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 1, 1, 6), Gauge32()).setUnits('KB').setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJVAECNSysMemFree.setStatus('current')
jnxJVAECNSysMemUsedPr = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('%').setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJVAECNSysMemUsedPr.setStatus('current')
jnxJVAECNSysSwapCapacity = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 1, 1, 8), Gauge32()).setUnits('KB').setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJVAECNSysSwapCapacity.setStatus('current')
jnxJVAECNSysSwapFree = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 1, 1, 9), Gauge32()).setUnits('KB').setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJVAECNSysSwapFree.setStatus('current')
jnxJVAECNSysBootMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("unknown", 0), ("network", 1), ("local", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJVAECNSysBootMethod.setStatus('current')
jnxJVAECNSysLastReboot = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 1, 1, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(30, 30)).setFixedLength(30)).setUnits('Secs').setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJVAECNSysLastReboot.setStatus('current')
jnxJVAECNProcessorTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 2), )
if mibBuilder.loadTexts: jnxJVAECNProcessorTable.setStatus('current')
jnxJVAECNProcessorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 2, 1), ).setIndexNames((0, "JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSysId"), (0, "JUNIPER-JVAE-NODE-MIB", "jnxJVAECNProcessorId"))
if mibBuilder.loadTexts: jnxJVAECNProcessorEntry.setStatus('current')
jnxJVAECNProcessorId = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 256)))
if mibBuilder.loadTexts: jnxJVAECNProcessorId.setStatus('current')
jnxJVAECNProcessorLoad = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('%').setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJVAECNProcessorLoad.setStatus('current')
jnxJVAECNifTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 3), )
if mibBuilder.loadTexts: jnxJVAECNifTable.setStatus('current')
jnxJVAECNifEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 3, 1), ).setIndexNames((0, "JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSysId"), (0, "JUNIPER-JVAE-NODE-MIB", "jnxJVAECNifId"))
if mibBuilder.loadTexts: jnxJVAECNifEntry.setStatus('current')
jnxJVAECNifId = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: jnxJVAECNifId.setStatus('current')
jnxJVAECNifName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 3, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJVAECNifName.setStatus('current')
jnxJVAECNifOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("down", 0), ("up", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJVAECNifOperStatus.setStatus('current')
jnxJVAECNifAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("down", 0), ("up", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJVAECNifAdminStatus.setStatus('current')
jnxJVAECNifLinkDetect = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 3, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJVAECNifLinkDetect.setStatus('current')
jnxJVAECNifAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 3, 1, 6), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJVAECNifAddress.setStatus('current')
jnxJVAECNifInPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 3, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJVAECNifInPkts.setStatus('current')
jnxJVAECNifInDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 3, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJVAECNifInDiscards.setStatus('current')
jnxJVAECNifInErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 3, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJVAECNifInErrors.setStatus('current')
jnxJVAECNifOutPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 3, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJVAECNifOutPkts.setStatus('current')
jnxJVAECNifOutDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 3, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJVAECNifOutDiscards.setStatus('current')
jnxJVAECNifOutErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 3, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJVAECNifOutErrors.setStatus('current')
jnxJVAECNFileSysTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 4), )
if mibBuilder.loadTexts: jnxJVAECNFileSysTable.setStatus('current')
jnxJVAECNFileSysEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 4, 1), ).setIndexNames((0, "JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSysId"), (0, "JUNIPER-JVAE-NODE-MIB", "jnxJVAECNFileSysId"))
if mibBuilder.loadTexts: jnxJVAECNFileSysEntry.setStatus('current')
jnxJVAECNFileSysId = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 127)))
if mibBuilder.loadTexts: jnxJVAECNFileSysId.setStatus('current')
jnxJVAECNFileSysMountPoint = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 4, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJVAECNFileSysMountPoint.setStatus('current')
jnxJVAECNFileSysSize = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 4, 1, 3), Gauge32()).setUnits('KB').setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJVAECNFileSysSize.setStatus('current')
jnxJVAECNFileSysUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 4, 1, 4), Gauge32()).setUnits('KB').setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJVAECNFileSysUsed.setStatus('current')
jnxJVAECNFileSysFree = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 4, 1, 5), Gauge32()).setUnits('KB').setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJVAECNFileSysFree.setStatus('current')
jnxJVAECNFileSysUsedPr = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 4, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('%').setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJVAECNFileSysUsedPr.setStatus('current')
jnxJVAECNDiskTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 5), )
if mibBuilder.loadTexts: jnxJVAECNDiskTable.setStatus('current')
jnxJVAECNDiskEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 5, 1), ).setIndexNames((0, "JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSysId"), (0, "JUNIPER-JVAE-NODE-MIB", "jnxJVAECNDiskId"))
if mibBuilder.loadTexts: jnxJVAECNDiskEntry.setStatus('current')
jnxJVAECNDiskId = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 15)))
if mibBuilder.loadTexts: jnxJVAECNDiskId.setStatus('current')
jnxJVAECNDiskSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 5, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 14))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJVAECNDiskSlot.setStatus('current')
jnxJVAECNDiskModel = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 5, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJVAECNDiskModel.setStatus('current')
jnxJVAECNDiskRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 5, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJVAECNDiskRevision.setStatus('current')
jnxJVAECNDiskVendor = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 5, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJVAECNDiskVendor.setStatus('current')
jnxJVAECNDiskOSPath = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 5, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJVAECNDiskOSPath.setStatus('current')
jnxJVAECNRaidTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 6), )
if mibBuilder.loadTexts: jnxJVAECNRaidTable.setStatus('current')
jnxJVAECNRaidEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 6, 1), ).setIndexNames((0, "JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSysId"), (0, "JUNIPER-JVAE-NODE-MIB", "jnxJVAECNRaidId"))
if mibBuilder.loadTexts: jnxJVAECNRaidEntry.setStatus('current')
jnxJVAECNRaidId = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 15)))
if mibBuilder.loadTexts: jnxJVAECNRaidId.setStatus('current')
jnxJVAECNRaidName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 6, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJVAECNRaidName.setStatus('current')
jnxJVAECNRaidState = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 6, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJVAECNRaidState.setStatus('current')
jnxJVAECNRaidLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 6, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJVAECNRaidLevel.setStatus('current')
jnxJVAECNRaidSize = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 6, 1, 5), Gauge32()).setUnits('GB').setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJVAECNRaidSize.setStatus('current')
jnxJVAECNRaidMembers = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 6, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJVAECNRaidMembers.setStatus('current')
jnxJVAECNRaidMemberDiskPartitions = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 6, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJVAECNRaidMemberDiskPartitions.setStatus('current')
jnxJVAECNRaidMemberDiskAtSlots = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 6, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJVAECNRaidMemberDiskAtSlots.setStatus('current')
jnxJVAECNRaidOSPath = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 6, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJVAECNRaidOSPath.setStatus('current')
jnxJVAECNSensorTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 7), )
if mibBuilder.loadTexts: jnxJVAECNSensorTable.setStatus('current')
jnxJVAECNSensorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 7, 1), ).setIndexNames((0, "JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSysId"), (0, "JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSensorId"))
if mibBuilder.loadTexts: jnxJVAECNSensorEntry.setStatus('current')
jnxJVAECNSensorId = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 7, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: jnxJVAECNSensorId.setStatus('current')
jnxJVAECNSensorType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 7, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("voltage", 0), ("temperature", 1), ("fan", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJVAECNSensorType.setStatus('current')
jnxJVAECNSensorValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 7, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJVAECNSensorValue.setStatus('current')
jnxJVAECNSensorRange = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 7, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJVAECNSensorRange.setStatus('current')
jnxJVAECNSensorDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 1, 1, 7, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJVAECNSensorDesc.setStatus('current')
jnxJVAECNMemoryLow = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 0, 1)).setObjects(("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSysId"), ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSysMemCapacity"), ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSysMemUsed"), ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSysMemFree"), ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSysMemUsedPr"), ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSysSwapCapacity"), ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSysSwapFree"))
if mibBuilder.loadTexts: jnxJVAECNMemoryLow.setStatus('current')
jnxJVAECNMemoryOk = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 0, 2)).setObjects(("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSysId"), ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSysMemCapacity"), ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSysMemUsed"), ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSysMemFree"), ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSysMemUsedPr"), ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSysSwapCapacity"), ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSysSwapFree"))
if mibBuilder.loadTexts: jnxJVAECNMemoryOk.setStatus('current')
jnxJVAECNProcessingLoadHigh = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 0, 3)).setObjects(("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSysId"), ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSysProcessingLoad"))
if mibBuilder.loadTexts: jnxJVAECNProcessingLoadHigh.setStatus('current')
jnxJVAECNProcessingLoadOk = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 0, 4)).setObjects(("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSysId"), ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSysProcessingLoad"))
if mibBuilder.loadTexts: jnxJVAECNProcessingLoadOk.setStatus('current')
jnxJVAECNProcessorLoadHigh = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 0, 5)).setObjects(("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSysId"), ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNProcessorId"), ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNProcessorLoad"))
if mibBuilder.loadTexts: jnxJVAECNProcessorLoadHigh.setStatus('current')
jnxJVAECNProcessorLoadOk = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 0, 6)).setObjects(("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSysId"), ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNProcessorId"), ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNProcessorLoad"))
if mibBuilder.loadTexts: jnxJVAECNProcessorLoadOk.setStatus('current')
jnxJVAECNifDown = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 0, 7)).setObjects(("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSysId"), ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNifId"), ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNifName"), ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNifOperStatus"), ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNifAdminStatus"), ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNifLinkDetect"))
if mibBuilder.loadTexts: jnxJVAECNifDown.setStatus('current')
jnxJVAECNifUp = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 0, 8)).setObjects(("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSysId"), ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNifId"), ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNifName"), ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNifOperStatus"), ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNifAdminStatus"), ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNifLinkDetect"))
if mibBuilder.loadTexts: jnxJVAECNifUp.setStatus('current')
jnxJVAECNStorageLow = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 0, 9)).setObjects(("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSysId"), ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNFileSysId"), ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNFileSysMountPoint"), ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNFileSysSize"), ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNFileSysUsed"), ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNFileSysFree"), ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNFileSysUsedPr"))
if mibBuilder.loadTexts: jnxJVAECNStorageLow.setStatus('current')
jnxJVAECNStorageOk = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 0, 10)).setObjects(("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSysId"), ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNFileSysId"), ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNFileSysMountPoint"), ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNFileSysSize"), ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNFileSysUsed"), ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNFileSysFree"), ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNFileSysUsedPr"))
if mibBuilder.loadTexts: jnxJVAECNStorageOk.setStatus('current')
jnxJVAECNRaidError = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 0, 11)).setObjects(("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSysId"), ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNRaidId"), ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNRaidName"), ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNRaidState"), ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNRaidOSPath"))
if mibBuilder.loadTexts: jnxJVAECNRaidError.setStatus('current')
jnxJVAECNRaidOk = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 0, 12)).setObjects(("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSysId"), ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNRaidId"), ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNRaidName"), ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNRaidState"), ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNRaidOSPath"))
if mibBuilder.loadTexts: jnxJVAECNRaidOk.setStatus('current')
jnxJVAECNSensorAlert = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 0, 13)).setObjects(("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSysId"), ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSensorId"), ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSensorValue"), ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSensorType"), ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSensorRange"), ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSensorDesc"))
if mibBuilder.loadTexts: jnxJVAECNSensorAlert.setStatus('current')
jnxJVAECNSensorOk = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 69, 2, 0, 14)).setObjects(("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSysId"), ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSensorId"), ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSensorValue"), ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSensorType"), ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSensorRange"), ("JUNIPER-JVAE-NODE-MIB", "jnxJVAECNSensorDesc"))
if mibBuilder.loadTexts: jnxJVAECNSensorOk.setStatus('current')
mibBuilder.exportSymbols("JUNIPER-JVAE-NODE-MIB", jnxJVAECNSysBootMethod=jnxJVAECNSysBootMethod, jnxJVAECNFileSysEntry=jnxJVAECNFileSysEntry, jnxJVAECNSensorOk=jnxJVAECNSensorOk, jnxJVAECNRaidLevel=jnxJVAECNRaidLevel, jnxJVAECNRaidSize=jnxJVAECNRaidSize, jnxJVAECNRaidOk=jnxJVAECNRaidOk, jnxJVAENodeTables=jnxJVAENodeTables, jnxJVAECNRaidTable=jnxJVAECNRaidTable, jnxJVAECNifEntry=jnxJVAECNifEntry, jnxJVAECNifOutErrors=jnxJVAECNifOutErrors, jnxJVAECNProcessingLoadOk=jnxJVAECNProcessingLoadOk, jnxJVAECNifInPkts=jnxJVAECNifInPkts, jnxJVAECNifTable=jnxJVAECNifTable, jnxJVAECNFileSysFree=jnxJVAECNFileSysFree, jnxJVAECNProcessorLoadOk=jnxJVAECNProcessorLoadOk, jnxJVAECNifOutPkts=jnxJVAECNifOutPkts, jnxJVAECNSysMemUsedPr=jnxJVAECNSysMemUsedPr, jnxJVAECNStorageLow=jnxJVAECNStorageLow, jnxJVAECNDiskSlot=jnxJVAECNDiskSlot, jnxJVAECNSensorId=jnxJVAECNSensorId, jnxJVAECNProcessorLoadHigh=jnxJVAECNProcessorLoadHigh, jnxJVAECNMemoryLow=jnxJVAECNMemoryLow, jnxJVAECNRaidEntry=jnxJVAECNRaidEntry, jnxJVAECNProcessorTable=jnxJVAECNProcessorTable, jnxJVAECNSysSwapFree=jnxJVAECNSysSwapFree, jnxJVAECNSysInfoEntry=jnxJVAECNSysInfoEntry, PYSNMP_MODULE_ID=jnxJVAENodeMIB, jnxJVAECNSysInfoTable=jnxJVAECNSysInfoTable, jnxJVAECNFileSysSize=jnxJVAECNFileSysSize, jnxJVAECNProcessorEntry=jnxJVAECNProcessorEntry, jnxJVAECNifId=jnxJVAECNifId, jnxJVAECNRaidMembers=jnxJVAECNRaidMembers, jnxJVAECNRaidMemberDiskAtSlots=jnxJVAECNRaidMemberDiskAtSlots, jnxJVAECNStorageOk=jnxJVAECNStorageOk, jnxJVAECNDiskEntry=jnxJVAECNDiskEntry, jnxJVAECNFileSysId=jnxJVAECNFileSysId, jnxJVAECNMemoryOk=jnxJVAECNMemoryOk, jnxJVAECNFileSysUsed=jnxJVAECNFileSysUsed, jnxJVAECNifInDiscards=jnxJVAECNifInDiscards, jnxJVAECNSysLastReboot=jnxJVAECNSysLastReboot, jnxJVAECNSensorRange=jnxJVAECNSensorRange, jnxJVAECNifOutDiscards=jnxJVAECNifOutDiscards, jnxJVAECNSensorAlert=jnxJVAECNSensorAlert, jnxJVAECNifUp=jnxJVAECNifUp, jnxJVAECNDiskVendor=jnxJVAECNDiskVendor, jnxJVAECNProcessorLoad=jnxJVAECNProcessorLoad, jnxJVAECNSysMemUsed=jnxJVAECNSysMemUsed, jnxJVAECNSysMemCapacity=jnxJVAECNSysMemCapacity, jnxJVAECNSysProcessingLoad=jnxJVAECNSysProcessingLoad, jnxJVAECNSensorType=jnxJVAECNSensorType, jnxJVAECNifAddress=jnxJVAECNifAddress, jnxJVAECNifLinkDetect=jnxJVAECNifLinkDetect, jnxJVAECNDiskId=jnxJVAECNDiskId, jnxJVAECNifDown=jnxJVAECNifDown, jnxJVAECNSysMemFree=jnxJVAECNSysMemFree, jnxJVAECNRaidError=jnxJVAECNRaidError, jnxJVAECNRaidName=jnxJVAECNRaidName, jnxJVAENodeMIB=jnxJVAENodeMIB, jnxJVAECNSysCpus=jnxJVAECNSysCpus, jnxJVAECNProcessingLoadHigh=jnxJVAECNProcessingLoadHigh, jnxJVAECNSensorDesc=jnxJVAECNSensorDesc, jnxJVAECNifInErrors=jnxJVAECNifInErrors, jnxJVAECNRaidMemberDiskPartitions=jnxJVAECNRaidMemberDiskPartitions, jnxJVAECNFileSysMountPoint=jnxJVAECNFileSysMountPoint, jnxJVAENodeObjects=jnxJVAENodeObjects, jnxJVAECNRaidOSPath=jnxJVAECNRaidOSPath, jnxJVAECNDiskRevision=jnxJVAECNDiskRevision, jnxJVAECNSensorEntry=jnxJVAECNSensorEntry, jnxJVAECNSysId=jnxJVAECNSysId, jnxJVAECNRaidId=jnxJVAECNRaidId, jnxJVAECNifAdminStatus=jnxJVAECNifAdminStatus, jnxJVAECNProcessorId=jnxJVAECNProcessorId, jnxJVAECNSensorValue=jnxJVAECNSensorValue, jnxJVAECNSensorTable=jnxJVAECNSensorTable, jnxJVAECNSysSwapCapacity=jnxJVAECNSysSwapCapacity, jnxJVAECNDiskTable=jnxJVAECNDiskTable, jnxJVAENodeNotifications=jnxJVAENodeNotifications, jnxJVAECNFileSysUsedPr=jnxJVAECNFileSysUsedPr, jnxJVAECNifOperStatus=jnxJVAECNifOperStatus, jnxJVAECNDiskOSPath=jnxJVAECNDiskOSPath, jnxJVAECNFileSysTable=jnxJVAECNFileSysTable, jnxJVAECNifName=jnxJVAECNifName, jnxJVAECNDiskModel=jnxJVAECNDiskModel, jnxJVAECNRaidState=jnxJVAECNRaidState)
