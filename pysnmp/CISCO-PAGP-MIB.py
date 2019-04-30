#
# PySNMP MIB module CISCO-PAGP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-PAGP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:52:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
InterfaceIndexOrZero, = mibBuilder.importSymbols("CISCO-TC", "InterfaceIndexOrZero")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
TimeTicks, Gauge32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter64, iso, MibIdentifier, ModuleIdentity, Bits, ObjectIdentity, IpAddress, Counter32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Gauge32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter64", "iso", "MibIdentifier", "ModuleIdentity", "Bits", "ObjectIdentity", "IpAddress", "Counter32", "Unsigned32")
TimeStamp, MacAddress, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "MacAddress", "TextualConvention", "DisplayString")
ciscoPagpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 98))
ciscoPagpMIB.setRevisions(('2010-10-20 00:00', '2008-02-01 00:00', '2002-12-13 00:00', '2002-01-02 00:00', '1999-03-04 00:00', '1998-04-09 00:00',))
if mibBuilder.loadTexts: ciscoPagpMIB.setLastUpdated('201010200000Z')
if mibBuilder.loadTexts: ciscoPagpMIB.setOrganization('Cisco Systems, Inc.')
ciscoPagpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 98, 1))
pagpGroupCapabilityConfiguration = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 98, 1, 1))
pagpProtocol = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 98, 1, 2))
class PagpGroupCapability(TextualConvention, Integer32):
    status = 'current'

class PagpEthcOperationMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("off", 1), ("manual", 2), ("pagpOn", 3))

class PagpPortPriority(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

class PagpOperationMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("desirable", 1), ("desirableSilent", 2), ("automatic", 3), ("automaticSilent", 4))

class PagpLearnMethod(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("physPort", 1), ("agPort", 2), ("undefined", 3))

pagpEtherChannelTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 98, 1, 1, 1), )
if mibBuilder.loadTexts: pagpEtherChannelTable.setStatus('current')
pagpEtherChannelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 98, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: pagpEtherChannelEntry.setStatus('current')
pagpEthcOperationMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 98, 1, 1, 1, 1, 1), PagpEthcOperationMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pagpEthcOperationMode.setStatus('current')
pagpDeviceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 98, 1, 1, 1, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pagpDeviceId.setStatus('current')
pagpPhysGroupCapability = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 98, 1, 1, 1, 1, 3), PagpGroupCapability()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pagpPhysGroupCapability.setStatus('current')
pagpOperGroupCapability = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 98, 1, 1, 1, 1, 4), PagpGroupCapability()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pagpOperGroupCapability.setStatus('current')
pagpAdminGroupCapability = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 98, 1, 1, 1, 1, 5), PagpGroupCapability()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pagpAdminGroupCapability.setStatus('current')
pagpPortPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 98, 1, 1, 1, 1, 6), PagpPortPriority()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pagpPortPriority.setStatus('current')
pagpLearnMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 98, 1, 1, 1, 1, 7), PagpLearnMethod()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pagpLearnMethod.setStatus('current')
pagpGroupIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 98, 1, 1, 1, 1, 8), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pagpGroupIfIndex.setStatus('current')
pagpDistributionProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 98, 1, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("ip", 1), ("mac", 2), ("port", 3), ("vlanIpPort", 4), ("vlanIp", 5), ("ipPort", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pagpDistributionProtocol.setStatus('current')
pagpDistributionAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 98, 1, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("source", 1), ("destination", 2), ("both", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pagpDistributionAddress.setStatus('current')
pagpRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 98, 1, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("fast", 1), ("normal", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pagpRate.setStatus('current')
pagpInPacketTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 98, 1, 1, 1, 1, 12), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setUnits('Seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: pagpInPacketTimeout.setStatus('current')
pagpProtocolConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 98, 1, 2, 1), )
if mibBuilder.loadTexts: pagpProtocolConfigTable.setStatus('current')
pagpProtocolConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 98, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: pagpProtocolConfigEntry.setStatus('current')
pagpOperationMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 98, 1, 2, 1, 1, 1), PagpOperationMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pagpOperationMode.setStatus('current')
pagpPortState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 98, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("portDown", 1), ("portUp", 2), ("dataReceived", 3), ("upData", 4), ("pagpReceived", 5), ("biDirectional", 6), ("upPagp", 7), ("upMult", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pagpPortState.setStatus('current')
pagpLastStateChange = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 98, 1, 2, 1, 1, 3), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pagpLastStateChange.setStatus('current')
pagpHelloFrequency = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 98, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("fast", 1), ("slow", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pagpHelloFrequency.setStatus('current')
pagpDistributionAlgorithm = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 98, 1, 2, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pagpDistributionAlgorithm.setStatus('current')
pagpPartnerCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 98, 1, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("one", 2), ("many", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pagpPartnerCount.setStatus('current')
pagpPartnerDeviceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 98, 1, 2, 1, 1, 7), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pagpPartnerDeviceId.setStatus('current')
pagpPartnerLearnMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 98, 1, 2, 1, 1, 8), PagpLearnMethod()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pagpPartnerLearnMethod.setStatus('current')
pagpPartnerPortPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 98, 1, 2, 1, 1, 9), PagpPortPriority()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pagpPartnerPortPriority.setStatus('current')
pagpPartnerIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 98, 1, 2, 1, 1, 10), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pagpPartnerIfIndex.setStatus('current')
pagpPartnerGroupCapability = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 98, 1, 2, 1, 1, 11), PagpGroupCapability()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pagpPartnerGroupCapability.setStatus('current')
pagpPartnerGroupIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 98, 1, 2, 1, 1, 12), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pagpPartnerGroupIfIndex.setStatus('current')
pagpPartnerDeviceName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 98, 1, 2, 1, 1, 13), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pagpPartnerDeviceName.setStatus('current')
pagpPartnerPortName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 98, 1, 2, 1, 1, 14), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pagpPartnerPortName.setStatus('current')
pagpPartnerAgportMACAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 98, 1, 2, 1, 1, 15), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pagpPartnerAgportMACAddress.setStatus('current')
pagpProtocolStatsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 98, 1, 2, 2), )
if mibBuilder.loadTexts: pagpProtocolStatsTable.setStatus('current')
pagpProtocolStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 98, 1, 2, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: pagpProtocolStatsEntry.setStatus('current')
pagpInPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 98, 1, 2, 2, 1, 3), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: pagpInPackets.setStatus('current')
pagpOutPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 98, 1, 2, 2, 1, 4), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: pagpOutPackets.setStatus('current')
pagpInFlushes = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 98, 1, 2, 2, 1, 5), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: pagpInFlushes.setStatus('current')
pagpReturnedFlushes = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 98, 1, 2, 2, 1, 6), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: pagpReturnedFlushes.setStatus('current')
pagpOutFlushes = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 98, 1, 2, 2, 1, 7), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: pagpOutFlushes.setStatus('current')
pagpInErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 98, 1, 2, 2, 1, 8), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: pagpInErrors.setStatus('current')
ciscoPagpMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 98, 3))
ciscoPagpMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 98, 3, 1))
ciscoPagpMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 98, 3, 2))
ciscoPagpMIBComplianceV1R1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 98, 3, 1, 1)).setObjects(("CISCO-PAGP-MIB", "ciscoPagpEthcGroupV1R1"), ("CISCO-PAGP-MIB", "ciscoPagpPagpGroupV1R1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPagpMIBComplianceV1R1 = ciscoPagpMIBComplianceV1R1.setStatus('obsolete')
ciscoPagpMIBComplianceV2R2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 98, 3, 1, 2)).setObjects(("CISCO-PAGP-MIB", "ciscoPagpEthcGroupV2R2"), ("CISCO-PAGP-MIB", "ciscoPagpPagpGroupV1R1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPagpMIBComplianceV2R2 = ciscoPagpMIBComplianceV2R2.setStatus('deprecated')
ciscoPagpMIBComplianceV3R3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 98, 3, 1, 3)).setObjects(("CISCO-PAGP-MIB", "ciscoPagpEthcGroupV2R2"), ("CISCO-PAGP-MIB", "ciscoPagpPagpGroupV1R1"), ("CISCO-PAGP-MIB", "ciscoPagpRateAndTimeOutGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPagpMIBComplianceV3R3 = ciscoPagpMIBComplianceV3R3.setStatus('current')
ciscoPagpEthcGroupV1R1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 98, 3, 2, 1)).setObjects(("CISCO-PAGP-MIB", "pagpEthcOperationMode"), ("CISCO-PAGP-MIB", "pagpDeviceId"), ("CISCO-PAGP-MIB", "pagpPhysGroupCapability"), ("CISCO-PAGP-MIB", "pagpOperGroupCapability"), ("CISCO-PAGP-MIB", "pagpAdminGroupCapability"), ("CISCO-PAGP-MIB", "pagpPortPriority"), ("CISCO-PAGP-MIB", "pagpLearnMethod"), ("CISCO-PAGP-MIB", "pagpGroupIfIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPagpEthcGroupV1R1 = ciscoPagpEthcGroupV1R1.setStatus('obsolete')
ciscoPagpPagpGroupV1R1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 98, 3, 2, 2)).setObjects(("CISCO-PAGP-MIB", "pagpOperationMode"), ("CISCO-PAGP-MIB", "pagpPortState"), ("CISCO-PAGP-MIB", "pagpLastStateChange"), ("CISCO-PAGP-MIB", "pagpHelloFrequency"), ("CISCO-PAGP-MIB", "pagpDistributionAlgorithm"), ("CISCO-PAGP-MIB", "pagpPartnerCount"), ("CISCO-PAGP-MIB", "pagpPartnerDeviceId"), ("CISCO-PAGP-MIB", "pagpPartnerLearnMethod"), ("CISCO-PAGP-MIB", "pagpPartnerPortPriority"), ("CISCO-PAGP-MIB", "pagpPartnerIfIndex"), ("CISCO-PAGP-MIB", "pagpPartnerGroupCapability"), ("CISCO-PAGP-MIB", "pagpPartnerGroupIfIndex"), ("CISCO-PAGP-MIB", "pagpPartnerDeviceName"), ("CISCO-PAGP-MIB", "pagpPartnerPortName"), ("CISCO-PAGP-MIB", "pagpPartnerAgportMACAddress"), ("CISCO-PAGP-MIB", "pagpInPackets"), ("CISCO-PAGP-MIB", "pagpOutPackets"), ("CISCO-PAGP-MIB", "pagpInFlushes"), ("CISCO-PAGP-MIB", "pagpReturnedFlushes"), ("CISCO-PAGP-MIB", "pagpOutFlushes"), ("CISCO-PAGP-MIB", "pagpInErrors"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPagpPagpGroupV1R1 = ciscoPagpPagpGroupV1R1.setStatus('current')
ciscoPagpEthcGroupV2R2 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 98, 3, 2, 3)).setObjects(("CISCO-PAGP-MIB", "pagpEthcOperationMode"), ("CISCO-PAGP-MIB", "pagpDeviceId"), ("CISCO-PAGP-MIB", "pagpPhysGroupCapability"), ("CISCO-PAGP-MIB", "pagpOperGroupCapability"), ("CISCO-PAGP-MIB", "pagpAdminGroupCapability"), ("CISCO-PAGP-MIB", "pagpPortPriority"), ("CISCO-PAGP-MIB", "pagpLearnMethod"), ("CISCO-PAGP-MIB", "pagpGroupIfIndex"), ("CISCO-PAGP-MIB", "pagpDistributionProtocol"), ("CISCO-PAGP-MIB", "pagpDistributionAddress"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPagpEthcGroupV2R2 = ciscoPagpEthcGroupV2R2.setStatus('current')
ciscoPagpRateAndTimeOutGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 98, 3, 2, 4)).setObjects(("CISCO-PAGP-MIB", "pagpRate"), ("CISCO-PAGP-MIB", "pagpInPacketTimeout"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPagpRateAndTimeOutGroup = ciscoPagpRateAndTimeOutGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-PAGP-MIB", ciscoPagpMIB=ciscoPagpMIB, pagpLearnMethod=pagpLearnMethod, pagpAdminGroupCapability=pagpAdminGroupCapability, pagpPartnerAgportMACAddress=pagpPartnerAgportMACAddress, ciscoPagpRateAndTimeOutGroup=ciscoPagpRateAndTimeOutGroup, pagpLastStateChange=pagpLastStateChange, pagpReturnedFlushes=pagpReturnedFlushes, ciscoPagpMIBCompliances=ciscoPagpMIBCompliances, ciscoPagpMIBConformance=ciscoPagpMIBConformance, pagpOperationMode=pagpOperationMode, pagpPartnerIfIndex=pagpPartnerIfIndex, pagpProtocolStatsEntry=pagpProtocolStatsEntry, pagpDeviceId=pagpDeviceId, pagpRate=pagpRate, pagpPartnerPortName=pagpPartnerPortName, pagpPartnerLearnMethod=pagpPartnerLearnMethod, pagpPartnerPortPriority=pagpPartnerPortPriority, pagpPartnerGroupIfIndex=pagpPartnerGroupIfIndex, pagpOutFlushes=pagpOutFlushes, ciscoPagpMIBObjects=ciscoPagpMIBObjects, pagpGroupCapabilityConfiguration=pagpGroupCapabilityConfiguration, PagpPortPriority=PagpPortPriority, pagpProtocol=pagpProtocol, pagpPhysGroupCapability=pagpPhysGroupCapability, PagpGroupCapability=PagpGroupCapability, pagpInErrors=pagpInErrors, pagpEthcOperationMode=pagpEthcOperationMode, pagpGroupIfIndex=pagpGroupIfIndex, pagpHelloFrequency=pagpHelloFrequency, ciscoPagpEthcGroupV1R1=ciscoPagpEthcGroupV1R1, PagpOperationMode=PagpOperationMode, pagpPortPriority=pagpPortPriority, pagpPartnerCount=pagpPartnerCount, ciscoPagpMIBComplianceV1R1=ciscoPagpMIBComplianceV1R1, ciscoPagpMIBComplianceV3R3=ciscoPagpMIBComplianceV3R3, ciscoPagpEthcGroupV2R2=ciscoPagpEthcGroupV2R2, ciscoPagpMIBComplianceV2R2=ciscoPagpMIBComplianceV2R2, PagpLearnMethod=PagpLearnMethod, ciscoPagpMIBGroups=ciscoPagpMIBGroups, ciscoPagpPagpGroupV1R1=ciscoPagpPagpGroupV1R1, pagpDistributionAlgorithm=pagpDistributionAlgorithm, pagpPartnerDeviceName=pagpPartnerDeviceName, pagpInPackets=pagpInPackets, pagpProtocolConfigEntry=pagpProtocolConfigEntry, PagpEthcOperationMode=PagpEthcOperationMode, pagpDistributionProtocol=pagpDistributionProtocol, pagpDistributionAddress=pagpDistributionAddress, pagpProtocolConfigTable=pagpProtocolConfigTable, pagpPartnerGroupCapability=pagpPartnerGroupCapability, pagpEtherChannelEntry=pagpEtherChannelEntry, pagpPortState=pagpPortState, pagpProtocolStatsTable=pagpProtocolStatsTable, pagpOutPackets=pagpOutPackets, pagpInPacketTimeout=pagpInPacketTimeout, pagpEtherChannelTable=pagpEtherChannelTable, pagpPartnerDeviceId=pagpPartnerDeviceId, pagpInFlushes=pagpInFlushes, pagpOperGroupCapability=pagpOperGroupCapability, PYSNMP_MODULE_ID=ciscoPagpMIB)
