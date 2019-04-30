#
# PySNMP MIB module CISCO-LAG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-LAG-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:47:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
CiscoInterfaceIndexList, = mibBuilder.importSymbols("CISCO-TC", "CiscoInterfaceIndexList")
dot3adAggPortListEntry, dot3adAggPortEntry = mibBuilder.importSymbols("IEEE8023-LAG-MIB", "dot3adAggPortListEntry", "dot3adAggPortEntry")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
TimeTicks, NotificationType, IpAddress, Counter64, MibIdentifier, ObjectIdentity, Integer32, Bits, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, iso, Gauge32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "NotificationType", "IpAddress", "Counter64", "MibIdentifier", "ObjectIdentity", "Integer32", "Bits", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "iso", "Gauge32", "Counter32")
TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue")
ciscoLagMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 225))
ciscoLagMIB.setRevisions(('2014-01-14 00:00', '2010-10-20 00:00', '2009-11-19 00:00', '2008-01-08 00:00', '2006-06-21 00:00', '2004-06-11 00:00', '2002-12-13 00:00', '2002-01-02 00:00', '2001-10-23 00:00',))
if mibBuilder.loadTexts: ciscoLagMIB.setLastUpdated('201401140000Z')
if mibBuilder.loadTexts: ciscoLagMIB.setOrganization('Cisco Systems, Inc.')
clagMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 225, 1))
class ClagDistributionProtocol(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("ip", 1), ("mac", 2), ("port", 3), ("vlanIpPort", 4), ("vlanIp", 5), ("ipPort", 6))

class ClagDistributionAddressMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("source", 1), ("destination", 2), ("both", 3))

class ClagDistributionMplsProtocol(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("label", 1), ("labelIp", 2))

class ClagAggregationProtocol(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("lacp", 1), ("pagp", 2))

class ClagPortAdminStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("off", 1), ("on", 2), ("active", 3), ("passive", 4))

clagGlobalConfigObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 225, 1, 1))
clagAgg = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 225, 1, 2))
clagAggPort = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 225, 1, 3))
clagAggPortList = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 225, 1, 4))
clagAggChannelIntf = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 225, 1, 5))
clagAggDistributionProtocol = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 225, 1, 1, 1), ClagDistributionProtocol()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clagAggDistributionProtocol.setStatus('current')
clagAggDistributionAddressMode = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 225, 1, 1, 2), ClagDistributionAddressMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clagAggDistributionAddressMode.setStatus('current')
clagAggDistributionMplsProtocol = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 225, 1, 1, 3), ClagDistributionMplsProtocol()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clagAggDistributionMplsProtocol.setStatus('current')
clagAggMaxAggregators = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 225, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clagAggMaxAggregators.setStatus('current')
clagAggHashDistMethodGlobalConfig = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 225, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("adaptive", 1), ("fixed", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clagAggHashDistMethodGlobalConfig.setStatus('current')
clagAggProtocolTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 225, 1, 2, 1), )
if mibBuilder.loadTexts: clagAggProtocolTable.setStatus('current')
clagAggProtocolEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 225, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: clagAggProtocolEntry.setStatus('current')
clagAggProtocolType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 225, 1, 2, 1, 1, 1), ClagAggregationProtocol()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clagAggProtocolType.setStatus('current')
clagAggPortTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 225, 1, 3, 1), )
if mibBuilder.loadTexts: clagAggPortTable.setStatus('current')
clagAggPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 225, 1, 3, 1, 1), )
dot3adAggPortEntry.registerAugmentions(("CISCO-LAG-MIB", "clagAggPortEntry"))
clagAggPortEntry.setIndexNames(*dot3adAggPortEntry.getIndexNames())
if mibBuilder.loadTexts: clagAggPortEntry.setStatus('current')
clagAggPortAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 225, 1, 3, 1, 1, 1), ClagPortAdminStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clagAggPortAdminStatus.setStatus('current')
clagAggPortRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 225, 1, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("fast", 1), ("normal", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clagAggPortRate.setStatus('current')
clagAggPortListTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 225, 1, 4, 1), )
if mibBuilder.loadTexts: clagAggPortListTable.setStatus('current')
clagAggPortListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 225, 1, 4, 1, 1), )
dot3adAggPortListEntry.registerAugmentions(("CISCO-LAG-MIB", "clagAggPortListEntry"))
clagAggPortListEntry.setIndexNames(*dot3adAggPortListEntry.getIndexNames())
if mibBuilder.loadTexts: clagAggPortListEntry.setStatus('current')
clagAggPortListPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 225, 1, 4, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: clagAggPortListPorts.setStatus('current')
clagAggPortListInterfaceIndexList = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 225, 1, 4, 1, 1, 2), CiscoInterfaceIndexList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clagAggPortListInterfaceIndexList.setStatus('current')
clagAggChannelIfTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 225, 1, 5, 1), )
if mibBuilder.loadTexts: clagAggChannelIfTable.setStatus('current')
clagAggChannelIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 225, 1, 5, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: clagAggChannelIfEntry.setStatus('current')
clagAggChannelIfFastSwitchOver = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 225, 1, 5, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clagAggChannelIfFastSwitchOver.setStatus('current')
clagAggChannelIfMaxBundle = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 225, 1, 5, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clagAggChannelIfMaxBundle.setStatus('current')
clagAggChannelIfMinLink = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 225, 1, 5, 1, 1, 3), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clagAggChannelIfMinLink.setStatus('current')
clagAggChannelIfHashDistAdminMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 225, 1, 5, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("adaptive", 2), ("fixed", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clagAggChannelIfHashDistAdminMethod.setStatus('current')
clagAggChannelIfHashDistOperMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 225, 1, 5, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("adaptive", 2), ("fixed", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: clagAggChannelIfHashDistOperMethod.setStatus('current')
clagMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 225, 2))
clagMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 225, 3))
clagMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 225, 3, 1))
clagMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 225, 3, 2))
clagMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 225, 3, 1, 1)).setObjects(("CISCO-LAG-MIB", "clagAggProtocolGroup"), ("CISCO-LAG-MIB", "clagAggPortGroup"), ("CISCO-LAG-MIB", "clagAggDistributionGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clagMIBCompliance = clagMIBCompliance.setStatus('deprecated')
clagMIBCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 225, 3, 1, 2)).setObjects(("CISCO-LAG-MIB", "clagAggProtocolGroup"), ("CISCO-LAG-MIB", "clagAggPortGroup"), ("CISCO-LAG-MIB", "clagAggDistributionGroup"), ("CISCO-LAG-MIB", "clagAggDistributionMplsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clagMIBCompliance2 = clagMIBCompliance2.setStatus('deprecated')
clagMIBCompliance3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 225, 3, 1, 3)).setObjects(("CISCO-LAG-MIB", "clagAggProtocolGroup"), ("CISCO-LAG-MIB", "clagAggPortGroup"), ("CISCO-LAG-MIB", "clagAggDistributionGroup"), ("CISCO-LAG-MIB", "clagAggDistributionMplsGroup"), ("CISCO-LAG-MIB", "clagAggPortListGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clagMIBCompliance3 = clagMIBCompliance3.setStatus('deprecated')
clagMIBCompliance4 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 225, 3, 1, 4)).setObjects(("CISCO-LAG-MIB", "clagAggProtocolGroup"), ("CISCO-LAG-MIB", "clagAggPortGroup"), ("CISCO-LAG-MIB", "clagAggDistributionGroup"), ("CISCO-LAG-MIB", "clagAggDistributionMplsGroup"), ("CISCO-LAG-MIB", "clagAggPortListGroup"), ("CISCO-LAG-MIB", "clagAggMaxAggregatorsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clagMIBCompliance4 = clagMIBCompliance4.setStatus('deprecated')
clagMIBCompliance5 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 225, 3, 1, 5)).setObjects(("CISCO-LAG-MIB", "clagAggProtocolGroup"), ("CISCO-LAG-MIB", "clagAggPortGroup"), ("CISCO-LAG-MIB", "clagAggDistributionGroup"), ("CISCO-LAG-MIB", "clagAggDistributionMplsGroup"), ("CISCO-LAG-MIB", "clagAggPortListGroup"), ("CISCO-LAG-MIB", "clagAggMaxAggregatorsGroup"), ("CISCO-LAG-MIB", "clagAggRateGroup"), ("CISCO-LAG-MIB", "clagAggChannelIfLacpGroup"), ("CISCO-LAG-MIB", "clagAggChannelIfHashDistMethodGroup"), ("CISCO-LAG-MIB", "clagAggHashDistGlobalGroup"), ("CISCO-LAG-MIB", "clagAggChannelIfMinLinkGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clagMIBCompliance5 = clagMIBCompliance5.setStatus('deprecated')
clagMIBCompliance6 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 225, 3, 1, 6)).setObjects(("CISCO-LAG-MIB", "clagAggProtocolGroup"), ("CISCO-LAG-MIB", "clagAggPortGroup"), ("CISCO-LAG-MIB", "clagAggDistributionGroup"), ("CISCO-LAG-MIB", "clagAggDistributionMplsGroup"), ("CISCO-LAG-MIB", "clagAggPortListGroup"), ("CISCO-LAG-MIB", "clagAggMaxAggregatorsGroup"), ("CISCO-LAG-MIB", "clagAggRateGroup"), ("CISCO-LAG-MIB", "clagAggChannelIfLacpGroup"), ("CISCO-LAG-MIB", "clagAggChannelIfHashDistMethodGroup"), ("CISCO-LAG-MIB", "clagAggHashDistGlobalGroup"), ("CISCO-LAG-MIB", "clagAggChannelIfMinLinkGroup"), ("CISCO-LAG-MIB", "clagAggPortListInterfaceIndexGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clagMIBCompliance6 = clagMIBCompliance6.setStatus('current')
clagAggProtocolGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 225, 3, 2, 1)).setObjects(("CISCO-LAG-MIB", "clagAggProtocolType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clagAggProtocolGroup = clagAggProtocolGroup.setStatus('current')
clagAggPortGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 225, 3, 2, 2)).setObjects(("CISCO-LAG-MIB", "clagAggPortAdminStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clagAggPortGroup = clagAggPortGroup.setStatus('current')
clagAggDistributionGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 225, 3, 2, 3)).setObjects(("CISCO-LAG-MIB", "clagAggDistributionProtocol"), ("CISCO-LAG-MIB", "clagAggDistributionAddressMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clagAggDistributionGroup = clagAggDistributionGroup.setStatus('current')
clagAggDistributionMplsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 225, 3, 2, 4)).setObjects(("CISCO-LAG-MIB", "clagAggDistributionMplsProtocol"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clagAggDistributionMplsGroup = clagAggDistributionMplsGroup.setStatus('current')
clagAggPortListGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 225, 3, 2, 5)).setObjects(("CISCO-LAG-MIB", "clagAggPortListPorts"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clagAggPortListGroup = clagAggPortListGroup.setStatus('current')
clagAggMaxAggregatorsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 225, 3, 2, 6)).setObjects(("CISCO-LAG-MIB", "clagAggMaxAggregators"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clagAggMaxAggregatorsGroup = clagAggMaxAggregatorsGroup.setStatus('current')
clagAggRateGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 225, 3, 2, 7)).setObjects(("CISCO-LAG-MIB", "clagAggPortRate"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clagAggRateGroup = clagAggRateGroup.setStatus('current')
clagAggChannelIfLacpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 225, 3, 2, 8)).setObjects(("CISCO-LAG-MIB", "clagAggChannelIfFastSwitchOver"), ("CISCO-LAG-MIB", "clagAggChannelIfMaxBundle"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clagAggChannelIfLacpGroup = clagAggChannelIfLacpGroup.setStatus('current')
clagAggChannelIfHashDistMethodGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 225, 3, 2, 9)).setObjects(("CISCO-LAG-MIB", "clagAggChannelIfHashDistAdminMethod"), ("CISCO-LAG-MIB", "clagAggChannelIfHashDistOperMethod"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clagAggChannelIfHashDistMethodGroup = clagAggChannelIfHashDistMethodGroup.setStatus('current')
clagAggHashDistGlobalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 225, 3, 2, 10)).setObjects(("CISCO-LAG-MIB", "clagAggHashDistMethodGlobalConfig"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clagAggHashDistGlobalGroup = clagAggHashDistGlobalGroup.setStatus('current')
clagAggChannelIfMinLinkGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 225, 3, 2, 11)).setObjects(("CISCO-LAG-MIB", "clagAggChannelIfMinLink"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clagAggChannelIfMinLinkGroup = clagAggChannelIfMinLinkGroup.setStatus('current')
clagAggPortListInterfaceIndexGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 225, 3, 2, 12)).setObjects(("CISCO-LAG-MIB", "clagAggPortListInterfaceIndexList"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clagAggPortListInterfaceIndexGroup = clagAggPortListInterfaceIndexGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-LAG-MIB", clagGlobalConfigObjects=clagGlobalConfigObjects, clagAggDistributionMplsProtocol=clagAggDistributionMplsProtocol, clagAggDistributionGroup=clagAggDistributionGroup, clagMIBConformance=clagMIBConformance, clagMIBCompliance5=clagMIBCompliance5, ciscoLagMIB=ciscoLagMIB, clagAggChannelIfLacpGroup=clagAggChannelIfLacpGroup, clagAggChannelIfHashDistOperMethod=clagAggChannelIfHashDistOperMethod, clagAgg=clagAgg, clagAggProtocolType=clagAggProtocolType, clagMIBCompliance4=clagMIBCompliance4, clagAggDistributionAddressMode=clagAggDistributionAddressMode, ClagAggregationProtocol=ClagAggregationProtocol, clagAggPortListInterfaceIndexList=clagAggPortListInterfaceIndexList, clagAggProtocolGroup=clagAggProtocolGroup, clagAggChannelIfMinLinkGroup=clagAggChannelIfMinLinkGroup, clagAggProtocolTable=clagAggProtocolTable, clagAggPortListPorts=clagAggPortListPorts, ClagDistributionMplsProtocol=ClagDistributionMplsProtocol, clagAggPort=clagAggPort, clagMIBCompliance=clagMIBCompliance, clagAggChannelIfHashDistMethodGroup=clagAggChannelIfHashDistMethodGroup, clagAggPortListTable=clagAggPortListTable, clagAggChannelIfMinLink=clagAggChannelIfMinLink, clagAggPortList=clagAggPortList, clagAggProtocolEntry=clagAggProtocolEntry, clagAggPortGroup=clagAggPortGroup, clagAggHashDistMethodGlobalConfig=clagAggHashDistMethodGlobalConfig, ClagPortAdminStatus=ClagPortAdminStatus, clagMIBObjects=clagMIBObjects, clagAggDistributionProtocol=clagAggDistributionProtocol, clagAggMaxAggregatorsGroup=clagAggMaxAggregatorsGroup, clagAggChannelIfEntry=clagAggChannelIfEntry, clagAggPortListEntry=clagAggPortListEntry, clagAggPortRate=clagAggPortRate, clagAggDistributionMplsGroup=clagAggDistributionMplsGroup, clagAggChannelIfMaxBundle=clagAggChannelIfMaxBundle, ClagDistributionAddressMode=ClagDistributionAddressMode, clagMIBNotifications=clagMIBNotifications, clagAggPortAdminStatus=clagAggPortAdminStatus, clagAggRateGroup=clagAggRateGroup, PYSNMP_MODULE_ID=ciscoLagMIB, clagAggPortEntry=clagAggPortEntry, clagAggChannelIfHashDistAdminMethod=clagAggChannelIfHashDistAdminMethod, clagAggPortTable=clagAggPortTable, clagAggChannelIntf=clagAggChannelIntf, clagAggChannelIfTable=clagAggChannelIfTable, clagAggChannelIfFastSwitchOver=clagAggChannelIfFastSwitchOver, clagMIBCompliances=clagMIBCompliances, clagMIBCompliance2=clagMIBCompliance2, clagAggPortListInterfaceIndexGroup=clagAggPortListInterfaceIndexGroup, clagMIBCompliance6=clagMIBCompliance6, clagAggHashDistGlobalGroup=clagAggHashDistGlobalGroup, clagMIBCompliance3=clagMIBCompliance3, clagAggPortListGroup=clagAggPortListGroup, clagAggMaxAggregators=clagAggMaxAggregators, clagMIBGroups=clagMIBGroups, ClagDistributionProtocol=ClagDistributionProtocol)
