#
# PySNMP MIB module ELTEX-MES-DHCP (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ELTEX-MES-DHCP
# Produced by pysmi-0.3.4 at Mon Apr 29 18:46:41 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
eltMesDhcp, = mibBuilder.importSymbols("ELTEX-MES", "eltMesDhcp")
rlDhcpSrvConfParamsEntry, = mibBuilder.importSymbols("RADLAN-DHCP-MIB", "rlDhcpSrvConfParamsEntry")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter32, Unsigned32, MibIdentifier, IpAddress, ObjectIdentity, Bits, ModuleIdentity, Counter64, NotificationType, iso, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter32", "Unsigned32", "MibIdentifier", "IpAddress", "ObjectIdentity", "Bits", "ModuleIdentity", "Counter64", "NotificationType", "iso", "Gauge32")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
class EltDhcpRelayOption82PolicyType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("replace", 1), ("drop", 2), ("keep", 3))

class EltDhcpRelayOption82SuboptionType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("tr101", 1), ("custom", 2))

class EltDhcpRelayOption82CombinationType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(2, 3, 4, 5))
    namedValues = NamedValues(("sv", 2), ("pv", 3), ("spv", 4), ("bin", 5))

class EltDhcpRelayOption82DelimiterType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("tr101", 1), ("dot", 2), ("comma", 3), ("semicolon", 4), ("hash", 5), ("slash", 6), ("space", 7))

eltMesDhcpRelay = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 8, 1))
eltMesDhcpRelayOption82 = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 8, 1, 1))
eltDhcpRelayOption82Policy = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 23, 8, 1, 1, 1), EltDhcpRelayOption82PolicyType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltDhcpRelayOption82Policy.setStatus('current')
eltDhcpRelayOption82IfPolicyTable = MibTable((1, 3, 6, 1, 4, 1, 35265, 1, 23, 8, 1, 1, 2), ).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltDhcpRelayOption82IfPolicyTable.setStatus('current')
eltDhcpRelayOption82IfPolicyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35265, 1, 23, 8, 1, 1, 2, 1), ).setMaxAccess("readwrite").setIndexNames((0, "ELTEX-MES-DHCP", "eltDhcpRelayOption82IfIndex"))
if mibBuilder.loadTexts: eltDhcpRelayOption82IfPolicyEntry.setStatus('current')
eltDhcpRelayOption82IfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 8, 1, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltDhcpRelayOption82IfIndex.setStatus('current')
eltDhcpRelayOption82IfPolicy = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 8, 1, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("replace", 1), ("drop", 2), ("keep", 3), ("global", 4))).clone(4)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltDhcpRelayOption82IfPolicy.setStatus('current')
eltDhcpRelayOption82AccessNodeIdentifier = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 23, 8, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 48))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltDhcpRelayOption82AccessNodeIdentifier.setStatus('current')
eltDhcpRelayOption82CircuitIdSuboptionsCombination = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 23, 8, 1, 1, 4), EltDhcpRelayOption82CombinationType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltDhcpRelayOption82CircuitIdSuboptionsCombination.setStatus('current')
eltDhcpRelayOption82CircuitIdSuboptionsDelimeter = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 23, 8, 1, 1, 5), EltDhcpRelayOption82DelimiterType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltDhcpRelayOption82CircuitIdSuboptionsDelimeter.setStatus('current')
eltDhcpRelayOption82SuboptionType = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 23, 8, 1, 1, 6), EltDhcpRelayOption82SuboptionType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltDhcpRelayOption82SuboptionType.setStatus('current')
eltDhcpRelayOption82RemoteIdentifier = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 23, 8, 1, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 63))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltDhcpRelayOption82RemoteIdentifier.setStatus('current')
eltDhcpRelayBroadcastEnable = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 23, 8, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltDhcpRelayBroadcastEnable.setStatus('current')
eltMesDhcpSrv = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 8, 2))
eltDhcpSrvConfParamsTable = MibTable((1, 3, 6, 1, 4, 1, 35265, 1, 23, 8, 2, 1), ).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltDhcpSrvConfParamsTable.setStatus('current')
eltDhcpSrvConfParamsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35265, 1, 23, 8, 2, 1, 1), ).setMaxAccess("readwrite")
rlDhcpSrvConfParamsEntry.registerAugmentions(("ELTEX-MES-DHCP", "eltDhcpSrvConfParamsEntry"))
eltDhcpSrvConfParamsEntry.setIndexNames(*rlDhcpSrvConfParamsEntry.getIndexNames())
if mibBuilder.loadTexts: eltDhcpSrvConfParamsEntry.setStatus('current')
eltDhcpSrvConfParamsTftpSrvList = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 8, 2, 1, 1, 1), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltDhcpSrvConfParamsTftpSrvList.setStatus('current')
mibBuilder.exportSymbols("ELTEX-MES-DHCP", eltMesDhcpRelayOption82=eltMesDhcpRelayOption82, eltMesDhcpRelay=eltMesDhcpRelay, eltDhcpSrvConfParamsTable=eltDhcpSrvConfParamsTable, eltDhcpSrvConfParamsEntry=eltDhcpSrvConfParamsEntry, eltDhcpRelayOption82IfPolicy=eltDhcpRelayOption82IfPolicy, eltMesDhcpSrv=eltMesDhcpSrv, eltDhcpSrvConfParamsTftpSrvList=eltDhcpSrvConfParamsTftpSrvList, eltDhcpRelayOption82CircuitIdSuboptionsDelimeter=eltDhcpRelayOption82CircuitIdSuboptionsDelimeter, eltDhcpRelayOption82Policy=eltDhcpRelayOption82Policy, eltDhcpRelayOption82IfPolicyTable=eltDhcpRelayOption82IfPolicyTable, EltDhcpRelayOption82PolicyType=EltDhcpRelayOption82PolicyType, EltDhcpRelayOption82SuboptionType=EltDhcpRelayOption82SuboptionType, EltDhcpRelayOption82DelimiterType=EltDhcpRelayOption82DelimiterType, eltDhcpRelayOption82IfPolicyEntry=eltDhcpRelayOption82IfPolicyEntry, eltDhcpRelayOption82RemoteIdentifier=eltDhcpRelayOption82RemoteIdentifier, EltDhcpRelayOption82CombinationType=EltDhcpRelayOption82CombinationType, eltDhcpRelayBroadcastEnable=eltDhcpRelayBroadcastEnable, eltDhcpRelayOption82SuboptionType=eltDhcpRelayOption82SuboptionType, eltDhcpRelayOption82CircuitIdSuboptionsCombination=eltDhcpRelayOption82CircuitIdSuboptionsCombination, eltDhcpRelayOption82AccessNodeIdentifier=eltDhcpRelayOption82AccessNodeIdentifier, eltDhcpRelayOption82IfIndex=eltDhcpRelayOption82IfIndex)
