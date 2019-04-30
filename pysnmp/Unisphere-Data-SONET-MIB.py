#
# PySNMP MIB module Unisphere-Data-SONET-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-SONET-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:25:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
InterfaceIndexOrZero, ifIndex, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero", "ifIndex", "InterfaceIndex")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter32, Integer32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, iso, Counter64, IpAddress, Unsigned32, ObjectIdentity, Bits, Gauge32, MibIdentifier, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Integer32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "iso", "Counter64", "IpAddress", "Unsigned32", "ObjectIdentity", "Bits", "Gauge32", "MibIdentifier", "ModuleIdentity")
TextualConvention, DisplayString, TruthValue, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue", "RowStatus")
usDataMibs, = mibBuilder.importSymbols("Unisphere-Data-MIBs", "usDataMibs")
UsdNextIfIndex, = mibBuilder.importSymbols("Unisphere-Data-TC", "UsdNextIfIndex")
usdSonetMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7))
usdSonetMIB.setRevisions(('2001-10-10 20:42', '2001-01-02 18:00', '1998-11-13 00:00',))
if mibBuilder.loadTexts: usdSonetMIB.setLastUpdated('200110102042Z')
if mibBuilder.loadTexts: usdSonetMIB.setOrganization('Unisphere Networks, Inc.')
class UsdSonetLineSpeed(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("sonetUnknownSpeed", 0), ("sonetOc1Stm0", 1), ("sonetOc3Stm1", 2), ("sonetOc12Stm3", 3), ("sonetOc48Stm16", 4))

class UsdSonetLogicalPathChannel(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class UsdSonetPathHierarchy(TextualConvention, OctetString):
    reference = 'RFC 854: NVT ASCII character set. See SNMPv2-TC.DisplayString DESCRIPTION for a summary.'
    status = 'current'
    displayHint = '32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class UsdSonetVTType(TextualConvention, Integer32):
    status = 'deprecated'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 3, 4, 5))
    namedValues = NamedValues(("tribVT15TU11", 0), ("tribVT20TU12", 1), ("tribVT3", 3), ("tribVT6", 4), ("tribVT6c", 5))

usdSonetObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 1))
usdSonetPathObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 2))
usdSonetVTObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 3))
usdSonetMediumTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 1, 1), )
if mibBuilder.loadTexts: usdSonetMediumTable.setStatus('current')
usdSonetMediumEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: usdSonetMediumEntry.setStatus('current')
usdSonetMediumType = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("sonet", 1), ("sdh", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: usdSonetMediumType.setStatus('deprecated')
usdSonetMediumLoopbackConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("sonetNoLoop", 0), ("sonetFacilityLoop", 1), ("sonetTerminalLoop", 2), ("sonetOtherLoop", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: usdSonetMediumLoopbackConfig.setStatus('current')
usdSonetMediumTimingSource = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("loop", 0), ("internalModule", 1), ("internalChassis", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: usdSonetMediumTimingSource.setStatus('current')
usdSonetMediumCircuitIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 1, 1, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: usdSonetMediumCircuitIdentifier.setStatus('deprecated')
usdSonetPathCapabilityTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 2, 1), )
if mibBuilder.loadTexts: usdSonetPathCapabilityTable.setStatus('current')
usdSonetPathCapabilityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: usdSonetPathCapabilityEntry.setStatus('current')
usdSonetPathRemoveFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 2, 1, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdSonetPathRemoveFlag.setStatus('current')
usdSonetPathChannelized = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 2, 1, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdSonetPathChannelized.setStatus('current')
usdSonetPathMaximumChannels = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 2, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdSonetPathMaximumChannels.setStatus('current')
usdSonetPathMinimumPathSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 2, 1, 1, 4), UsdSonetLineSpeed()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdSonetPathMinimumPathSpeed.setStatus('current')
usdSonetPathMaximumPathSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 2, 1, 1, 5), UsdSonetLineSpeed()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdSonetPathMaximumPathSpeed.setStatus('current')
usdSonetPathNextIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 2, 2), UsdNextIfIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdSonetPathNextIfIndex.setStatus('current')
usdSonetPathTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 2, 3), )
if mibBuilder.loadTexts: usdSonetPathTable.setStatus('current')
usdSonetPathEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 2, 3, 1), ).setIndexNames((0, "Unisphere-Data-SONET-MIB", "usdSonetPathIfIndex"))
if mibBuilder.loadTexts: usdSonetPathEntry.setStatus('current')
usdSonetPathIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 2, 3, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: usdSonetPathIfIndex.setStatus('current')
usdSonetPathLogicalChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 2, 3, 1, 2), UsdSonetLogicalPathChannel()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdSonetPathLogicalChannel.setStatus('current')
usdSonetPathSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 2, 3, 1, 3), UsdSonetLineSpeed()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdSonetPathSpeed.setStatus('current')
usdSonetPathHierarchy = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 2, 3, 1, 4), UsdSonetPathHierarchy()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdSonetPathHierarchy.setStatus('current')
usdSonetPathLowerIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 2, 3, 1, 5), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdSonetPathLowerIfIndex.setStatus('current')
usdSonetPathRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 2, 3, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdSonetPathRowStatus.setStatus('current')
usdSonetVTNextIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 3, 1), UsdNextIfIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdSonetVTNextIfIndex.setStatus('current')
usdSonetVTTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 3, 2), )
if mibBuilder.loadTexts: usdSonetVTTable.setStatus('current')
usdSonetVTEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 3, 2, 1), ).setIndexNames((0, "Unisphere-Data-SONET-MIB", "usdSonetVTIfIndex"))
if mibBuilder.loadTexts: usdSonetVTEntry.setStatus('current')
usdSonetVTIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 3, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: usdSonetVTIfIndex.setStatus('current')
usdSonetVTPathLogicalChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 3, 2, 1, 2), UsdSonetLogicalPathChannel()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdSonetVTPathLogicalChannel.setStatus('current')
usdSonetVTType = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 3, 2, 1, 3), UsdSonetVTType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdSonetVTType.setStatus('deprecated')
usdSonetVTPathPayload = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 3, 2, 1, 4), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdSonetVTPathPayload.setStatus('current')
usdSonetVTTributaryGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 3, 2, 1, 5), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdSonetVTTributaryGroup.setStatus('current')
usdSonetVTTributarySubChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 3, 2, 1, 6), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdSonetVTTributarySubChannel.setStatus('current')
usdSonetVTLowerIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 3, 2, 1, 7), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdSonetVTLowerIfIndex.setStatus('current')
usdSonetVTRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 3, 2, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdSonetVTRowStatus.setStatus('current')
usdSonetConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 4))
usdSonetCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 4, 1))
usdSonetGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 4, 2))
usdSonetCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 4, 1, 1)).setObjects(("Unisphere-Data-SONET-MIB", "usdSonetGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSonetCompliance = usdSonetCompliance.setStatus('obsolete')
usdSonetCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 4, 1, 2)).setObjects(("Unisphere-Data-SONET-MIB", "usdSonetGroup"), ("Unisphere-Data-SONET-MIB", "usdSonetPathGroup"), ("Unisphere-Data-SONET-MIB", "usdSonetVirtualTributaryGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSonetCompliance2 = usdSonetCompliance2.setStatus('deprecated')
usdSonetCompliance3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 4, 1, 3)).setObjects(("Unisphere-Data-SONET-MIB", "usdSonetGroup2"), ("Unisphere-Data-SONET-MIB", "usdSonetPathGroup"), ("Unisphere-Data-SONET-MIB", "usdSonetVirtualTributaryGroup2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSonetCompliance3 = usdSonetCompliance3.setStatus('current')
usdSonetGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 4, 2, 1)).setObjects(("Unisphere-Data-SONET-MIB", "usdSonetMediumType"), ("Unisphere-Data-SONET-MIB", "usdSonetMediumLoopbackConfig"), ("Unisphere-Data-SONET-MIB", "usdSonetMediumTimingSource"), ("Unisphere-Data-SONET-MIB", "usdSonetMediumCircuitIdentifier"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSonetGroup = usdSonetGroup.setStatus('deprecated')
usdSonetPathGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 4, 2, 2)).setObjects(("Unisphere-Data-SONET-MIB", "usdSonetPathRemoveFlag"), ("Unisphere-Data-SONET-MIB", "usdSonetPathChannelized"), ("Unisphere-Data-SONET-MIB", "usdSonetPathMaximumChannels"), ("Unisphere-Data-SONET-MIB", "usdSonetPathMinimumPathSpeed"), ("Unisphere-Data-SONET-MIB", "usdSonetPathMaximumPathSpeed"), ("Unisphere-Data-SONET-MIB", "usdSonetPathNextIfIndex"), ("Unisphere-Data-SONET-MIB", "usdSonetPathLogicalChannel"), ("Unisphere-Data-SONET-MIB", "usdSonetPathSpeed"), ("Unisphere-Data-SONET-MIB", "usdSonetPathHierarchy"), ("Unisphere-Data-SONET-MIB", "usdSonetPathLowerIfIndex"), ("Unisphere-Data-SONET-MIB", "usdSonetPathRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSonetPathGroup = usdSonetPathGroup.setStatus('current')
usdSonetVirtualTributaryGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 4, 2, 3)).setObjects(("Unisphere-Data-SONET-MIB", "usdSonetVTNextIfIndex"), ("Unisphere-Data-SONET-MIB", "usdSonetVTPathLogicalChannel"), ("Unisphere-Data-SONET-MIB", "usdSonetVTType"), ("Unisphere-Data-SONET-MIB", "usdSonetVTPathPayload"), ("Unisphere-Data-SONET-MIB", "usdSonetVTTributaryGroup"), ("Unisphere-Data-SONET-MIB", "usdSonetVTTributarySubChannel"), ("Unisphere-Data-SONET-MIB", "usdSonetVTLowerIfIndex"), ("Unisphere-Data-SONET-MIB", "usdSonetVTRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSonetVirtualTributaryGroup = usdSonetVirtualTributaryGroup.setStatus('deprecated')
usdSonetGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 4, 2, 4)).setObjects(("Unisphere-Data-SONET-MIB", "usdSonetMediumLoopbackConfig"), ("Unisphere-Data-SONET-MIB", "usdSonetMediumTimingSource"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSonetGroup2 = usdSonetGroup2.setStatus('current')
usdSonetVirtualTributaryGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 7, 4, 2, 5)).setObjects(("Unisphere-Data-SONET-MIB", "usdSonetVTNextIfIndex"), ("Unisphere-Data-SONET-MIB", "usdSonetVTPathLogicalChannel"), ("Unisphere-Data-SONET-MIB", "usdSonetVTPathPayload"), ("Unisphere-Data-SONET-MIB", "usdSonetVTTributaryGroup"), ("Unisphere-Data-SONET-MIB", "usdSonetVTTributarySubChannel"), ("Unisphere-Data-SONET-MIB", "usdSonetVTLowerIfIndex"), ("Unisphere-Data-SONET-MIB", "usdSonetVTRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSonetVirtualTributaryGroup2 = usdSonetVirtualTributaryGroup2.setStatus('current')
mibBuilder.exportSymbols("Unisphere-Data-SONET-MIB", usdSonetMediumCircuitIdentifier=usdSonetMediumCircuitIdentifier, usdSonetVirtualTributaryGroup=usdSonetVirtualTributaryGroup, usdSonetVTObjects=usdSonetVTObjects, usdSonetPathSpeed=usdSonetPathSpeed, usdSonetGroup=usdSonetGroup, usdSonetPathIfIndex=usdSonetPathIfIndex, usdSonetVTTable=usdSonetVTTable, usdSonetPathMaximumChannels=usdSonetPathMaximumChannels, usdSonetPathEntry=usdSonetPathEntry, UsdSonetVTType=UsdSonetVTType, usdSonetObjects=usdSonetObjects, usdSonetPathMaximumPathSpeed=usdSonetPathMaximumPathSpeed, usdSonetCompliances=usdSonetCompliances, usdSonetMediumEntry=usdSonetMediumEntry, usdSonetPathChannelized=usdSonetPathChannelized, usdSonetPathCapabilityTable=usdSonetPathCapabilityTable, PYSNMP_MODULE_ID=usdSonetMIB, usdSonetPathMinimumPathSpeed=usdSonetPathMinimumPathSpeed, usdSonetPathNextIfIndex=usdSonetPathNextIfIndex, usdSonetCompliance2=usdSonetCompliance2, usdSonetVTTributaryGroup=usdSonetVTTributaryGroup, usdSonetPathHierarchy=usdSonetPathHierarchy, usdSonetVTEntry=usdSonetVTEntry, usdSonetMediumTimingSource=usdSonetMediumTimingSource, usdSonetVTTributarySubChannel=usdSonetVTTributarySubChannel, UsdSonetLogicalPathChannel=UsdSonetLogicalPathChannel, usdSonetCompliance3=usdSonetCompliance3, usdSonetVTPathPayload=usdSonetVTPathPayload, usdSonetMIB=usdSonetMIB, usdSonetVTPathLogicalChannel=usdSonetVTPathLogicalChannel, UsdSonetLineSpeed=UsdSonetLineSpeed, usdSonetMediumLoopbackConfig=usdSonetMediumLoopbackConfig, usdSonetPathLowerIfIndex=usdSonetPathLowerIfIndex, usdSonetGroups=usdSonetGroups, usdSonetVTLowerIfIndex=usdSonetVTLowerIfIndex, usdSonetPathTable=usdSonetPathTable, usdSonetMediumType=usdSonetMediumType, usdSonetVirtualTributaryGroup2=usdSonetVirtualTributaryGroup2, usdSonetVTIfIndex=usdSonetVTIfIndex, usdSonetConformance=usdSonetConformance, usdSonetGroup2=usdSonetGroup2, usdSonetPathLogicalChannel=usdSonetPathLogicalChannel, UsdSonetPathHierarchy=UsdSonetPathHierarchy, usdSonetPathGroup=usdSonetPathGroup, usdSonetPathCapabilityEntry=usdSonetPathCapabilityEntry, usdSonetPathObjects=usdSonetPathObjects, usdSonetVTNextIfIndex=usdSonetVTNextIfIndex, usdSonetCompliance=usdSonetCompliance, usdSonetMediumTable=usdSonetMediumTable, usdSonetVTType=usdSonetVTType, usdSonetVTRowStatus=usdSonetVTRowStatus, usdSonetPathRemoveFlag=usdSonetPathRemoveFlag, usdSonetPathRowStatus=usdSonetPathRowStatus)
