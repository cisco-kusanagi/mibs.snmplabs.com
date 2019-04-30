#
# PySNMP MIB module CISCO-FLOW-CLONE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-FLOW-CLONE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:41:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Gauge32, iso, IpAddress, Counter32, MibIdentifier, Unsigned32, NotificationType, TimeTicks, Integer32, Counter64, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Gauge32", "iso", "IpAddress", "Counter32", "MibIdentifier", "Unsigned32", "NotificationType", "TimeTicks", "Integer32", "Counter64", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity")
StorageType, DisplayString, TextualConvention, TimeStamp, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "StorageType", "DisplayString", "TextualConvention", "TimeStamp", "RowStatus")
ciscoFlowCloneMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 765))
ciscoFlowCloneMIB.setRevisions(('2010-07-08 00:00',))
if mibBuilder.loadTexts: ciscoFlowCloneMIB.setLastUpdated('201010190000Z')
if mibBuilder.loadTexts: ciscoFlowCloneMIB.setOrganization('Cisco Systems, Inc.')
ciscoFlowCloneMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 765, 0))
ciscoFlowCloneMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 765, 1))
ciscoFlowCloneMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 765, 2))
class CloneProfileIdentifier(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class CloneFlowIdentifier(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class CloneProfilePointType(TextualConvention, Integer32):
    reference = "K. McCloghrie and F. Kastenholz, 'The Interfaces Group MIB', RFC-2863, June 2000."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("none", 3), ("interface", 4))

class CloneProfilePointIdentifier(InterfaceIndexOrZero):
    status = 'current'

cfcCloneProfiles = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 1))
cfcCloneProfileIdNext = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 1, 1), CloneProfileIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfcCloneProfileIdNext.setStatus('current')
cfcCloneProfileTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 1, 2), )
if mibBuilder.loadTexts: cfcCloneProfileTable.setStatus('current')
cfcCloneProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 1, 2, 1), ).setIndexNames((0, "CISCO-FLOW-CLONE-MIB", "cfcCloneProfileId"))
if mibBuilder.loadTexts: cfcCloneProfileEntry.setStatus('current')
cfcCloneProfileId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 1, 2, 1, 1), CloneProfileIdentifier())
if mibBuilder.loadTexts: cfcCloneProfileId.setStatus('current')
cfcCloneProfileStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 1, 2, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfcCloneProfileStatus.setStatus('current')
cfcCloneProfileStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 1, 2, 1, 3), StorageType().clone('volatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfcCloneProfileStorageType.setStatus('current')
cfcCloneProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 1, 2, 1, 4), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfcCloneProfileName.setStatus('current')
cfcCloneProfileDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 1, 2, 1, 5), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfcCloneProfileDescription.setStatus('current')
cfcCloneProfileCreateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 1, 2, 1, 6), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfcCloneProfileCreateTime.setStatus('current')
cfcCloneProfileFlowCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 1, 2, 1, 7), Gauge32()).setUnits('traffic flows').setMaxAccess("readonly")
if mibBuilder.loadTexts: cfcCloneProfileFlowCount.setStatus('current')
cfcCloneProfileFlowType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("ip", 1)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfcCloneProfileFlowType.setStatus('current')
cfcCloneTargetType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 1, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("system", 2), ("interface", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfcCloneTargetType.setStatus('current')
cfcCloneTargetIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 1, 2, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfcCloneTargetIfIndex.setStatus('current')
cfcCloneProfileEgressIfType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 1, 2, 1, 11), CloneProfilePointType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfcCloneProfileEgressIfType.setStatus('current')
cfcCloneProfileEgressIf = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 1, 2, 1, 12), CloneProfilePointIdentifier()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfcCloneProfileEgressIf.setStatus('current')
cfcCloneProfileTableChanged = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 1, 3), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfcCloneProfileTableChanged.setStatus('current')
cfcFlows = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 2))
cfcFlowIpTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 2, 1), )
if mibBuilder.loadTexts: cfcFlowIpTable.setStatus('current')
cfcFlowIpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 2, 1, 1), ).setIndexNames((0, "CISCO-FLOW-CLONE-MIB", "cfcCloneProfileId"), (0, "CISCO-FLOW-CLONE-MIB", "cfcFlowIndex"))
if mibBuilder.loadTexts: cfcFlowIpEntry.setStatus('current')
cfcFlowIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 2, 1, 1, 1), CloneFlowIdentifier())
if mibBuilder.loadTexts: cfcFlowIndex.setStatus('current')
cfcFlowIpStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 2, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfcFlowIpStatus.setStatus('current')
cfcFlowIpStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 2, 1, 1, 3), StorageType().clone('volatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfcFlowIpStorageType.setStatus('current')
cfcFlowIpAddrSrcType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 2, 1, 1, 4), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfcFlowIpAddrSrcType.setStatus('current')
cfcFlowIpAddrSrc = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 2, 1, 1, 5), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfcFlowIpAddrSrc.setStatus('current')
cfcFlowIpAddrDstType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 2, 1, 1, 6), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfcFlowIpAddrDstType.setStatus('current')
cfcFlowIpAddrDst = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 2, 1, 1, 7), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfcFlowIpAddrDst.setStatus('current')
cfcFlowIpCreateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 2, 1, 1, 8), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfcFlowIpCreateTime.setStatus('current')
cfcFlowStats = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 3))
cfcFlowStatsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 3, 1), )
if mibBuilder.loadTexts: cfcFlowStatsTable.setStatus('current')
cfcFlowStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 3, 1, 1), ).setIndexNames((0, "CISCO-FLOW-CLONE-MIB", "cfcCloneProfileId"), (0, "CISCO-FLOW-CLONE-MIB", "cfcFlowIndex"))
if mibBuilder.loadTexts: cfcFlowStatsEntry.setStatus('current')
cfcFlowPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 3, 1, 1, 1), Counter64()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cfcFlowPkts.setStatus('current')
cfcFlowOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 3, 1, 1, 2), Counter64()).setUnits('octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cfcFlowOctets.setStatus('current')
ciscoFlowCloneMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 765, 2, 1))
ciscoFlowCloneMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 765, 2, 2))
ciscoCloneFlowCompliance01 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 765, 2, 1, 1)).setObjects(("CISCO-FLOW-CLONE-MIB", "cfcCloneProfileGroup"), ("CISCO-FLOW-CLONE-MIB", "cfcFlowGroup"), ("CISCO-FLOW-CLONE-MIB", "cfcFlowStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCloneFlowCompliance01 = ciscoCloneFlowCompliance01.setStatus('current')
cfcCloneProfileGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 765, 2, 2, 1)).setObjects(("CISCO-FLOW-CLONE-MIB", "cfcCloneProfileIdNext"), ("CISCO-FLOW-CLONE-MIB", "cfcCloneProfileStatus"), ("CISCO-FLOW-CLONE-MIB", "cfcCloneProfileStorageType"), ("CISCO-FLOW-CLONE-MIB", "cfcCloneProfileName"), ("CISCO-FLOW-CLONE-MIB", "cfcCloneProfileDescription"), ("CISCO-FLOW-CLONE-MIB", "cfcCloneProfileCreateTime"), ("CISCO-FLOW-CLONE-MIB", "cfcCloneProfileFlowCount"), ("CISCO-FLOW-CLONE-MIB", "cfcCloneProfileFlowType"), ("CISCO-FLOW-CLONE-MIB", "cfcCloneTargetType"), ("CISCO-FLOW-CLONE-MIB", "cfcCloneTargetIfIndex"), ("CISCO-FLOW-CLONE-MIB", "cfcCloneProfileEgressIfType"), ("CISCO-FLOW-CLONE-MIB", "cfcCloneProfileEgressIf"), ("CISCO-FLOW-CLONE-MIB", "cfcCloneProfileTableChanged"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfcCloneProfileGroup = cfcCloneProfileGroup.setStatus('current')
cfcFlowGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 765, 2, 2, 2)).setObjects(("CISCO-FLOW-CLONE-MIB", "cfcFlowIpStatus"), ("CISCO-FLOW-CLONE-MIB", "cfcFlowIpStorageType"), ("CISCO-FLOW-CLONE-MIB", "cfcFlowIpAddrSrcType"), ("CISCO-FLOW-CLONE-MIB", "cfcFlowIpAddrSrc"), ("CISCO-FLOW-CLONE-MIB", "cfcFlowIpAddrDstType"), ("CISCO-FLOW-CLONE-MIB", "cfcFlowIpAddrDst"), ("CISCO-FLOW-CLONE-MIB", "cfcFlowIpCreateTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfcFlowGroup = cfcFlowGroup.setStatus('current')
cfcFlowStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 765, 2, 2, 3)).setObjects(("CISCO-FLOW-CLONE-MIB", "cfcFlowPkts"), ("CISCO-FLOW-CLONE-MIB", "cfcFlowOctets"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfcFlowStatsGroup = cfcFlowStatsGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-FLOW-CLONE-MIB", cfcCloneProfileFlowType=cfcCloneProfileFlowType, cfcFlowStats=cfcFlowStats, cfcFlowIpAddrSrcType=cfcFlowIpAddrSrcType, CloneProfileIdentifier=CloneProfileIdentifier, cfcCloneProfileDescription=cfcCloneProfileDescription, cfcFlowIpAddrDstType=cfcFlowIpAddrDstType, cfcCloneProfileStorageType=cfcCloneProfileStorageType, cfcCloneProfileCreateTime=cfcCloneProfileCreateTime, CloneProfilePointType=CloneProfilePointType, ciscoFlowCloneMIBGroups=ciscoFlowCloneMIBGroups, cfcFlowPkts=cfcFlowPkts, cfcFlowIpCreateTime=cfcFlowIpCreateTime, cfcCloneProfileFlowCount=cfcCloneProfileFlowCount, cfcCloneProfileStatus=cfcCloneProfileStatus, cfcCloneProfileTableChanged=cfcCloneProfileTableChanged, ciscoFlowCloneMIBCompliances=ciscoFlowCloneMIBCompliances, cfcFlowIpAddrDst=cfcFlowIpAddrDst, cfcFlowOctets=cfcFlowOctets, cfcFlowStatsTable=cfcFlowStatsTable, ciscoFlowCloneMIBConformance=ciscoFlowCloneMIBConformance, cfcCloneProfileEgressIf=cfcCloneProfileEgressIf, CloneFlowIdentifier=CloneFlowIdentifier, cfcCloneProfileEgressIfType=cfcCloneProfileEgressIfType, cfcCloneProfileIdNext=cfcCloneProfileIdNext, cfcFlowIpStorageType=cfcFlowIpStorageType, cfcFlowGroup=cfcFlowGroup, ciscoFlowCloneMIB=ciscoFlowCloneMIB, ciscoCloneFlowCompliance01=ciscoCloneFlowCompliance01, PYSNMP_MODULE_ID=ciscoFlowCloneMIB, cfcCloneTargetIfIndex=cfcCloneTargetIfIndex, cfcFlowIpEntry=cfcFlowIpEntry, ciscoFlowCloneMIBObjects=ciscoFlowCloneMIBObjects, cfcCloneProfiles=cfcCloneProfiles, cfcFlowStatsEntry=cfcFlowStatsEntry, cfcCloneTargetType=cfcCloneTargetType, cfcFlowIpAddrSrc=cfcFlowIpAddrSrc, cfcFlowIndex=cfcFlowIndex, cfcCloneProfileId=cfcCloneProfileId, CloneProfilePointIdentifier=CloneProfilePointIdentifier, cfcCloneProfileEntry=cfcCloneProfileEntry, cfcFlowIpTable=cfcFlowIpTable, cfcFlowStatsGroup=cfcFlowStatsGroup, cfcCloneProfileGroup=cfcCloneProfileGroup, cfcCloneProfileTable=cfcCloneProfileTable, cfcCloneProfileName=cfcCloneProfileName, cfcFlows=cfcFlows, cfcFlowIpStatus=cfcFlowIpStatus, ciscoFlowCloneMIBNotifications=ciscoFlowCloneMIBNotifications)
