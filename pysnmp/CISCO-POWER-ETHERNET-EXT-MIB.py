#
# PySNMP MIB module CISCO-POWER-ETHERNET-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-POWER-ETHERNET-EXT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:53:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
EntPhysicalIndexOrZero, = mibBuilder.importSymbols("CISCO-TC", "EntPhysicalIndexOrZero")
pethMainPseGroupIndex, pethPsePortGroupIndex, pethPsePortIndex, pethPsePortEntry = mibBuilder.importSymbols("POWER-ETHERNET-MIB", "pethMainPseGroupIndex", "pethPsePortGroupIndex", "pethPsePortIndex", "pethPsePortEntry")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
TimeTicks, NotificationType, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Integer32, Counter32, ObjectIdentity, Unsigned32, iso, ModuleIdentity, IpAddress, Gauge32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "NotificationType", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Integer32", "Counter32", "ObjectIdentity", "Unsigned32", "iso", "ModuleIdentity", "IpAddress", "Gauge32", "Bits")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
ciscoPowerEthernetExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 402))
ciscoPowerEthernetExtMIB.setRevisions(('2013-07-10 00:00', '2011-07-18 00:00', '2009-12-04 00:00', '2007-04-12 00:00', '2007-02-02 00:00', '2005-06-10 00:00', '2004-04-12 00:00',))
if mibBuilder.loadTexts: ciscoPowerEthernetExtMIB.setLastUpdated('201307100000Z')
if mibBuilder.loadTexts: ciscoPowerEthernetExtMIB.setOrganization('Cisco Systems, Inc.')
cpeExtMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 402, 0))
cpeExtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 402, 1))
cpeExtMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 402, 2))
class CpeExtLldpPwrType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("type1Pd", 1), ("type1Pse", 2), ("type2Pd", 3), ("type2Pse", 4))

class CpeExtLldpPwrSrc(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("pseAndLocal", 1), ("local", 2), ("pse", 3), ("backupSrc", 4), ("primarySrc", 5), ("unknown", 6))

class CpeExtPwrPriority(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("critical", 1), ("high", 2), ("low", 3), ("unknown", 4))

class CpeExtLldpPwrClassOrZero(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("unknown", 0), ("class0", 1), ("class1", 2), ("class2", 3), ("class3", 4), ("class4", 5))

cpeExtDefaultAllocation = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 1), Unsigned32()).setUnits('milliwatts').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cpeExtDefaultAllocation.setStatus('current')
cpeExtPsePortTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 2), )
if mibBuilder.loadTexts: cpeExtPsePortTable.setStatus('current')
cpeExtPsePortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 2, 1), )
pethPsePortEntry.registerAugmentions(("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPsePortEntry"))
cpeExtPsePortEntry.setIndexNames(*pethPsePortEntry.getIndexNames())
if mibBuilder.loadTexts: cpeExtPsePortEntry.setStatus('current')
cpeExtPsePortEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("auto", 1), ("static", 2), ("limit", 3), ("disable", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cpeExtPsePortEnable.setStatus('current')
cpeExtPsePortDiscoverMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("unknown", 1), ("off", 2), ("ieee", 3), ("cisco", 4), ("ieeeAndCisco", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpeExtPsePortDiscoverMode.setStatus('current')
cpeExtPsePortDeviceDetected = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 2, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpeExtPsePortDeviceDetected.setStatus('current')
cpeExtPsePortIeeePd = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 2, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpeExtPsePortIeeePd.setStatus('current')
cpeExtPsePortAdditionalStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 2, 1, 5), Bits().clone(namedValues=NamedValues(("deny", 0), ("overdraw", 1), ("overdrawLog", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpeExtPsePortAdditionalStatus.setStatus('current')
cpeExtPsePortPwrMax = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 2, 1, 6), Unsigned32()).setUnits('milliwatts').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cpeExtPsePortPwrMax.setStatus('current')
cpeExtPsePortPwrAllocated = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 2, 1, 7), Unsigned32()).setUnits('milliwatts').setMaxAccess("readonly")
if mibBuilder.loadTexts: cpeExtPsePortPwrAllocated.setStatus('current')
cpeExtPsePortPwrAvailable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 2, 1, 8), Unsigned32()).setUnits('milliwatts').setMaxAccess("readonly")
if mibBuilder.loadTexts: cpeExtPsePortPwrAvailable.setStatus('current')
cpeExtPsePortPwrConsumption = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 2, 1, 9), Unsigned32()).setUnits('milliwatts').setMaxAccess("readonly")
if mibBuilder.loadTexts: cpeExtPsePortPwrConsumption.setStatus('current')
cpeExtPsePortMaxPwrDrawn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 2, 1, 10), Unsigned32()).setUnits('milliwatts').setMaxAccess("readonly")
if mibBuilder.loadTexts: cpeExtPsePortMaxPwrDrawn.setStatus('current')
cpeExtPsePortEntPhyIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 2, 1, 11), EntPhysicalIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpeExtPsePortEntPhyIndex.setStatus('current')
cpeExtPsePortPolicingCapable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 2, 1, 12), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpeExtPsePortPolicingCapable.setStatus('current')
cpeExtPsePortPolicingEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 2, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cpeExtPsePortPolicingEnable.setStatus('current')
cpeExtPsePortPolicingAction = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 2, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("deny", 1), ("logOnly", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cpeExtPsePortPolicingAction.setStatus('current')
cpeExtPsePortPwrManAlloc = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 2, 1, 15), Unsigned32()).setUnits('milliwatts').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cpeExtPsePortPwrManAlloc.setStatus('current')
cpeExtPsePortCapabilities = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 2, 1, 16), Bits().clone(namedValues=NamedValues(("policing", 0), ("poePlus", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpeExtPsePortCapabilities.setStatus('current')
cpeExtMainPseTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 3), )
if mibBuilder.loadTexts: cpeExtMainPseTable.setStatus('current')
cpeExtMainPseEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 3, 1), ).setIndexNames((0, "POWER-ETHERNET-MIB", "pethMainPseGroupIndex"))
if mibBuilder.loadTexts: cpeExtMainPseEntry.setStatus('current')
cpeExtMainPseEntPhyIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 3, 1, 1), EntPhysicalIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpeExtMainPseEntPhyIndex.setStatus('current')
cpeExtMainPseDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 3, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpeExtMainPseDescr.setStatus('current')
cpeExtMainPsePwrMonitorCapable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 3, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpeExtMainPsePwrMonitorCapable.setStatus('current')
cpeExtPdStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 4))
cpeExtPdStatsTotalDevices = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 4, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpeExtPdStatsTotalDevices.setStatus('current')
cpeExtPdStatsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 4, 2), )
if mibBuilder.loadTexts: cpeExtPdStatsTable.setStatus('current')
cpeExtPdStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 4, 2, 1), ).setIndexNames((0, "CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPdStatsClass"))
if mibBuilder.loadTexts: cpeExtPdStatsEntry.setStatus('current')
cpeExtPdStatsClass = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 4, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("cisco", 1), ("class0", 2), ("class1", 3), ("class2", 4), ("class3", 5), ("class4", 6))))
if mibBuilder.loadTexts: cpeExtPdStatsClass.setStatus('current')
cpeExtPdStatsDeviceCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 4, 2, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpeExtPdStatsDeviceCount.setStatus('current')
cpeExtPolicingNotifEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 5), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cpeExtPolicingNotifEnable.setStatus('current')
cpeExtPowerPriorityEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 6), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cpeExtPowerPriorityEnable.setStatus('current')
cpeExtPsePortLldpTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 7), )
if mibBuilder.loadTexts: cpeExtPsePortLldpTable.setStatus('current')
cpeExtPsePortLldpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 7, 1), ).setIndexNames((0, "POWER-ETHERNET-MIB", "pethPsePortGroupIndex"), (0, "POWER-ETHERNET-MIB", "pethPsePortIndex"))
if mibBuilder.loadTexts: cpeExtPsePortLldpEntry.setStatus('current')
cpeExtPsePortLldpPwrType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 7, 1, 1), CpeExtLldpPwrType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpeExtPsePortLldpPwrType.setStatus('current')
cpeExtPsePortLldpPdPwrType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 7, 1, 2), CpeExtLldpPwrType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpeExtPsePortLldpPdPwrType.setStatus('current')
cpeExtPsePortLldpPwrSrc = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 7, 1, 3), CpeExtLldpPwrSrc()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpeExtPsePortLldpPwrSrc.setStatus('current')
cpeExtPsePortLldpPdPwrSrc = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 7, 1, 4), CpeExtLldpPwrSrc()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpeExtPsePortLldpPdPwrSrc.setStatus('current')
cpeExtPsePortLldpPwrPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 7, 1, 5), CpeExtPwrPriority()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpeExtPsePortLldpPwrPriority.setStatus('current')
cpeExtPsePortLldpPdPwrPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 7, 1, 6), CpeExtPwrPriority()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpeExtPsePortLldpPdPwrPriority.setStatus('current')
cpeExtPsePortLldpPwrReq = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 7, 1, 7), Unsigned32()).setUnits('milliwatts').setMaxAccess("readonly")
if mibBuilder.loadTexts: cpeExtPsePortLldpPwrReq.setStatus('current')
cpeExtPsePortLldpPdPwrReq = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 7, 1, 8), Unsigned32()).setUnits('milliwatts').setMaxAccess("readonly")
if mibBuilder.loadTexts: cpeExtPsePortLldpPdPwrReq.setStatus('current')
cpeExtPsePortLldpPwrAlloc = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 7, 1, 9), Unsigned32()).setUnits('milliwatts').setMaxAccess("readonly")
if mibBuilder.loadTexts: cpeExtPsePortLldpPwrAlloc.setStatus('current')
cpeExtPsePortLldpPdPwrAlloc = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 7, 1, 10), Unsigned32()).setUnits('milliwatts').setMaxAccess("readonly")
if mibBuilder.loadTexts: cpeExtPsePortLldpPdPwrAlloc.setStatus('current')
cpeExtPsePortLldpPwrClass = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 7, 1, 11), CpeExtLldpPwrClassOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpeExtPsePortLldpPwrClass.setStatus('current')
cpeExtPsePortLldpPdPwrClass = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 7, 1, 12), CpeExtLldpPwrClassOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpeExtPsePortLldpPdPwrClass.setStatus('current')
cpeExtPsePortLldpPdPwrSupport = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 7, 1, 13), Bits().clone(namedValues=NamedValues(("portClass", 0), ("pseMdiPwrSupport", 1), ("pseMdiPwrState", 2), ("psePairCtrlAbility", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpeExtPsePortLldpPdPwrSupport.setStatus('current')
cpeExtPsePortLldpPdPwrPairsOrZero = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 402, 1, 7, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("unknown", 0), ("signal", 1), ("spare", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpeExtPsePortLldpPdPwrPairsOrZero.setStatus('current')
cpeExtPolicingNotif = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 402, 0, 1)).setObjects(("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPsePortPolicingAction"), ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPsePortAdditionalStatus"), ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPsePortPwrAllocated"), ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPsePortMaxPwrDrawn"))
if mibBuilder.loadTexts: cpeExtPolicingNotif.setStatus('current')
cpeExtMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 402, 2, 1))
cpeExtMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 402, 2, 2))
cpeExtMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 402, 2, 1, 1)).setObjects(("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPsePortGroup"), ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPsePortGlobalConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpeExtMIBCompliance = cpeExtMIBCompliance.setStatus('deprecated')
cpeExtMIBCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 402, 2, 1, 2)).setObjects(("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPsePortGroup"), ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPsePortGlobalConfigGroup"), ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPsePortPwrMonitorGroup"), ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtMainPseGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpeExtMIBCompliance2 = cpeExtMIBCompliance2.setStatus('deprecated')
cpeExtMIBCompliance3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 402, 2, 1, 3)).setObjects(("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPsePortGroup"), ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPsePortGlobalConfigGroup"), ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPsePortPwrMonitorGroup"), ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtMainPseGroup2"), ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPseGrpPwrGroup"), ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPortEntityIndexGroup"), ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPortPolicingGroup"), ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPdStatsGroup"), ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPortPolicingActionGroup"), ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPortPwrManAllocGroup"), ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPolicingNotifEnableGroup"), ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPolicingNotifGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpeExtMIBCompliance3 = cpeExtMIBCompliance3.setStatus('deprecated')
cpeExtMIBCompliance4 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 402, 2, 1, 4)).setObjects(("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPsePortGroup"), ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPsePortGlobalConfigGroup"), ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPsePortPwrMonitorGroup"), ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtMainPseGroup2"), ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPseGrpPwrGroup"), ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPortEntityIndexGroup"), ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPortPolicingGroup"), ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPdStatsGroup"), ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPortPolicingActionGroup"), ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPortPwrManAllocGroup"), ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPolicingNotifEnableGroup"), ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPolicingNotifGroup"), ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPowerPriorityGroup"), ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPsePortLldpGroup"), ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPsePortCapabilitiesGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpeExtMIBCompliance4 = cpeExtMIBCompliance4.setStatus('deprecated')
cpeExtMIBCompliance5 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 402, 2, 1, 5)).setObjects(("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPsePortGroup"), ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPsePortGlobalConfigGroup"), ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPsePortPwrMonitorGroup"), ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtMainPseGroup2"), ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPseGrpPwrGroup"), ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPortEntityIndexGroup"), ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPortPolicingGroup"), ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPdStatsGroup"), ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPortPolicingActionGroup"), ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPortPwrManAllocGroup"), ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPolicingNotifEnableGroup"), ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPolicingNotifGroup"), ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPowerPriorityGroup"), ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPsePortLldpGroup"), ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPsePortCapabilitiesGroup"), ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPsePortLldpPowerGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpeExtMIBCompliance5 = cpeExtMIBCompliance5.setStatus('current')
cpeExtPsePortGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 402, 2, 2, 1)).setObjects(("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPsePortEnable"), ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPsePortDiscoverMode"), ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPsePortDeviceDetected"), ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPsePortIeeePd"), ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPsePortAdditionalStatus"), ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPsePortPwrMax"), ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPsePortPwrAllocated"), ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPsePortPwrAvailable"), ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPsePortPwrConsumption"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpeExtPsePortGroup = cpeExtPsePortGroup.setStatus('current')
cpeExtPsePortGlobalConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 402, 2, 2, 2)).setObjects(("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtDefaultAllocation"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpeExtPsePortGlobalConfigGroup = cpeExtPsePortGlobalConfigGroup.setStatus('current')
cpeExtPsePortPwrMonitorGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 402, 2, 2, 3)).setObjects(("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPsePortMaxPwrDrawn"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpeExtPsePortPwrMonitorGroup = cpeExtPsePortPwrMonitorGroup.setStatus('current')
cpeExtMainPseGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 402, 2, 2, 4)).setObjects(("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtMainPseEntPhyIndex"), ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtMainPseDescr"), ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtMainPsePwrMonitorCapable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpeExtMainPseGroup = cpeExtMainPseGroup.setStatus('deprecated')
cpeExtPortEntityIndexGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 402, 2, 2, 5)).setObjects(("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPsePortEntPhyIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpeExtPortEntityIndexGroup = cpeExtPortEntityIndexGroup.setStatus('current')
cpeExtPortPolicingGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 402, 2, 2, 6)).setObjects(("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPsePortPolicingCapable"), ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPsePortPolicingEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpeExtPortPolicingGroup = cpeExtPortPolicingGroup.setStatus('current')
cpeExtPdStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 402, 2, 2, 7)).setObjects(("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPdStatsTotalDevices"), ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPdStatsDeviceCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpeExtPdStatsGroup = cpeExtPdStatsGroup.setStatus('current')
cpeExtMainPseGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 402, 2, 2, 8)).setObjects(("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtMainPseEntPhyIndex"), ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtMainPseDescr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpeExtMainPseGroup2 = cpeExtMainPseGroup2.setStatus('current')
cpeExtPseGrpPwrGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 402, 2, 2, 9)).setObjects(("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtMainPsePwrMonitorCapable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpeExtPseGrpPwrGroup = cpeExtPseGrpPwrGroup.setStatus('current')
cpeExtPortPolicingActionGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 402, 2, 2, 10)).setObjects(("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPsePortPolicingAction"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpeExtPortPolicingActionGroup = cpeExtPortPolicingActionGroup.setStatus('current')
cpeExtPortPwrManAllocGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 402, 2, 2, 11)).setObjects(("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPsePortPwrManAlloc"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpeExtPortPwrManAllocGroup = cpeExtPortPwrManAllocGroup.setStatus('current')
cpeExtPolicingNotifEnableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 402, 2, 2, 12)).setObjects(("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPolicingNotifEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpeExtPolicingNotifEnableGroup = cpeExtPolicingNotifEnableGroup.setStatus('current')
cpeExtPolicingNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 402, 2, 2, 13)).setObjects(("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPolicingNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpeExtPolicingNotifGroup = cpeExtPolicingNotifGroup.setStatus('current')
cpeExtPowerPriorityGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 402, 2, 2, 14)).setObjects(("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPowerPriorityEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpeExtPowerPriorityGroup = cpeExtPowerPriorityGroup.setStatus('current')
cpeExtPsePortLldpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 402, 2, 2, 15)).setObjects(("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPsePortLldpPwrType"), ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPsePortLldpPdPwrType"), ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPsePortLldpPwrSrc"), ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPsePortLldpPdPwrSrc"), ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPsePortLldpPwrPriority"), ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPsePortLldpPdPwrPriority"), ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPsePortLldpPwrReq"), ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPsePortLldpPdPwrReq"), ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPsePortLldpPwrAlloc"), ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPsePortLldpPdPwrAlloc"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpeExtPsePortLldpGroup = cpeExtPsePortLldpGroup.setStatus('current')
cpeExtPsePortCapabilitiesGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 402, 2, 2, 16)).setObjects(("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPsePortCapabilities"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpeExtPsePortCapabilitiesGroup = cpeExtPsePortCapabilitiesGroup.setStatus('current')
cpeExtPsePortLldpPowerGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 402, 2, 2, 17)).setObjects(("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPsePortLldpPwrClass"), ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPsePortLldpPdPwrClass"), ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPsePortLldpPdPwrSupport"), ("CISCO-POWER-ETHERNET-EXT-MIB", "cpeExtPsePortLldpPdPwrPairsOrZero"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpeExtPsePortLldpPowerGroup = cpeExtPsePortLldpPowerGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-POWER-ETHERNET-EXT-MIB", cpeExtPsePortPwrMax=cpeExtPsePortPwrMax, cpeExtPortPolicingGroup=cpeExtPortPolicingGroup, cpeExtMIBConformance=cpeExtMIBConformance, cpeExtPdStatsTotalDevices=cpeExtPdStatsTotalDevices, cpeExtPsePortLldpPwrSrc=cpeExtPsePortLldpPwrSrc, cpeExtPsePortDiscoverMode=cpeExtPsePortDiscoverMode, cpeExtPortPwrManAllocGroup=cpeExtPortPwrManAllocGroup, cpeExtMIBObjects=cpeExtMIBObjects, cpeExtPsePortLldpPwrAlloc=cpeExtPsePortLldpPwrAlloc, cpeExtPortEntityIndexGroup=cpeExtPortEntityIndexGroup, cpeExtPsePortAdditionalStatus=cpeExtPsePortAdditionalStatus, cpeExtPdStatsEntry=cpeExtPdStatsEntry, CpeExtLldpPwrClassOrZero=CpeExtLldpPwrClassOrZero, cpeExtPsePortCapabilitiesGroup=cpeExtPsePortCapabilitiesGroup, CpeExtPwrPriority=CpeExtPwrPriority, cpeExtPsePortPwrMonitorGroup=cpeExtPsePortPwrMonitorGroup, cpeExtPsePortPwrManAlloc=cpeExtPsePortPwrManAlloc, cpeExtMainPsePwrMonitorCapable=cpeExtMainPsePwrMonitorCapable, cpeExtMIBNotifs=cpeExtMIBNotifs, cpeExtPowerPriorityGroup=cpeExtPowerPriorityGroup, cpeExtPdStatsGroup=cpeExtPdStatsGroup, cpeExtPsePortEntPhyIndex=cpeExtPsePortEntPhyIndex, cpeExtPsePortGlobalConfigGroup=cpeExtPsePortGlobalConfigGroup, cpeExtPsePortEntry=cpeExtPsePortEntry, cpeExtMIBGroups=cpeExtMIBGroups, cpeExtPsePortLldpPdPwrSupport=cpeExtPsePortLldpPdPwrSupport, cpeExtPsePortLldpGroup=cpeExtPsePortLldpGroup, cpeExtPsePortLldpPdPwrPairsOrZero=cpeExtPsePortLldpPdPwrPairsOrZero, cpeExtPsePortIeeePd=cpeExtPsePortIeeePd, cpeExtPolicingNotifEnableGroup=cpeExtPolicingNotifEnableGroup, cpeExtPsePortPwrConsumption=cpeExtPsePortPwrConsumption, cpeExtPsePortLldpPdPwrPriority=cpeExtPsePortLldpPdPwrPriority, cpeExtPdStatistics=cpeExtPdStatistics, cpeExtPsePortLldpPdPwrAlloc=cpeExtPsePortLldpPdPwrAlloc, cpeExtMIBCompliance5=cpeExtMIBCompliance5, cpeExtMainPseEntry=cpeExtMainPseEntry, ciscoPowerEthernetExtMIB=ciscoPowerEthernetExtMIB, cpeExtPsePortLldpEntry=cpeExtPsePortLldpEntry, cpeExtPsePortEnable=cpeExtPsePortEnable, cpeExtPsePortPolicingAction=cpeExtPsePortPolicingAction, cpeExtPolicingNotifGroup=cpeExtPolicingNotifGroup, PYSNMP_MODULE_ID=ciscoPowerEthernetExtMIB, cpeExtPsePortPwrAvailable=cpeExtPsePortPwrAvailable, cpeExtPsePortLldpPwrType=cpeExtPsePortLldpPwrType, cpeExtPsePortLldpPdPwrClass=cpeExtPsePortLldpPdPwrClass, cpeExtPdStatsClass=cpeExtPdStatsClass, cpeExtPsePortMaxPwrDrawn=cpeExtPsePortMaxPwrDrawn, cpeExtMainPseGroup2=cpeExtMainPseGroup2, cpeExtPolicingNotif=cpeExtPolicingNotif, cpeExtPseGrpPwrGroup=cpeExtPseGrpPwrGroup, cpeExtPsePortLldpPdPwrType=cpeExtPsePortLldpPdPwrType, cpeExtPsePortLldpTable=cpeExtPsePortLldpTable, cpeExtPortPolicingActionGroup=cpeExtPortPolicingActionGroup, cpeExtMainPseGroup=cpeExtMainPseGroup, cpeExtPsePortLldpPwrReq=cpeExtPsePortLldpPwrReq, cpeExtPsePortLldpPwrClass=cpeExtPsePortLldpPwrClass, CpeExtLldpPwrType=CpeExtLldpPwrType, cpeExtMIBCompliance3=cpeExtMIBCompliance3, cpeExtPolicingNotifEnable=cpeExtPolicingNotifEnable, cpeExtMIBCompliance=cpeExtMIBCompliance, cpeExtPsePortPolicingEnable=cpeExtPsePortPolicingEnable, cpeExtPsePortLldpPdPwrReq=cpeExtPsePortLldpPdPwrReq, CpeExtLldpPwrSrc=CpeExtLldpPwrSrc, cpeExtPsePortCapabilities=cpeExtPsePortCapabilities, cpeExtPdStatsTable=cpeExtPdStatsTable, cpeExtMIBCompliance4=cpeExtMIBCompliance4, cpeExtPsePortLldpPdPwrSrc=cpeExtPsePortLldpPdPwrSrc, cpeExtPsePortGroup=cpeExtPsePortGroup, cpeExtPsePortLldpPwrPriority=cpeExtPsePortLldpPwrPriority, cpeExtPowerPriorityEnable=cpeExtPowerPriorityEnable, cpeExtMIBCompliances=cpeExtMIBCompliances, cpeExtPsePortTable=cpeExtPsePortTable, cpeExtMainPseTable=cpeExtMainPseTable, cpeExtDefaultAllocation=cpeExtDefaultAllocation, cpeExtPdStatsDeviceCount=cpeExtPdStatsDeviceCount, cpeExtPsePortPolicingCapable=cpeExtPsePortPolicingCapable, cpeExtMainPseDescr=cpeExtMainPseDescr, cpeExtPsePortDeviceDetected=cpeExtPsePortDeviceDetected, cpeExtMainPseEntPhyIndex=cpeExtMainPseEntPhyIndex, cpeExtPsePortLldpPowerGroup=cpeExtPsePortLldpPowerGroup, cpeExtMIBCompliance2=cpeExtMIBCompliance2, cpeExtPsePortPwrAllocated=cpeExtPsePortPwrAllocated)
