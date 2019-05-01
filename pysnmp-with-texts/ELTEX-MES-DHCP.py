#
# PySNMP MIB module ELTEX-MES-DHCP (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ELTEX-MES-DHCP
# Produced by pysmi-0.3.4 at Wed May  1 13:01:12 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
eltMesDhcp, = mibBuilder.importSymbols("ELTEX-MES", "eltMesDhcp")
rlDhcpSrvConfParamsEntry, = mibBuilder.importSymbols("RADLAN-DHCP-MIB", "rlDhcpSrvConfParamsEntry")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, ObjectIdentity, IpAddress, Counter32, Gauge32, MibIdentifier, Unsigned32, ModuleIdentity, iso, TimeTicks, NotificationType, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "ObjectIdentity", "IpAddress", "Counter32", "Gauge32", "MibIdentifier", "Unsigned32", "ModuleIdentity", "iso", "TimeTicks", "NotificationType", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
class EltDhcpRelayOption82PolicyType(TextualConvention, Integer32):
    description = 'Specifies DHCP relay option 82 reforwarding policy'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("replace", 1), ("drop", 2), ("keep", 3))

class EltDhcpRelayOption82SuboptionType(TextualConvention, Integer32):
    description = 'Specifies global format of option 82 suboptions.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("tr101", 1), ("custom", 2))

class EltDhcpRelayOption82CombinationType(TextualConvention, Integer32):
    description = 'Specifies circuit id suboptions that will be inserted to a option 82.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(2, 3, 4, 5))
    namedValues = NamedValues(("sv", 2), ("pv", 3), ("spv", 4), ("bin", 5))

class EltDhcpRelayOption82DelimiterType(TextualConvention, Integer32):
    description = 'Specifies circuit id suboptions delimeter that will be inserted to a option 82.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("tr101", 1), ("dot", 2), ("comma", 3), ("semicolon", 4), ("hash", 5), ("slash", 6), ("space", 7))

eltMesDhcpRelay = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 8, 1))
eltMesDhcpRelayOption82 = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 8, 1, 1))
eltDhcpRelayOption82Policy = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 23, 8, 1, 1, 1), EltDhcpRelayOption82PolicyType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltDhcpRelayOption82Policy.setStatus('current')
if mibBuilder.loadTexts: eltDhcpRelayOption82Policy.setDescription('Specifies global DHCP relay option 82 reforwarding policy')
eltDhcpRelayOption82IfPolicyTable = MibTable((1, 3, 6, 1, 4, 1, 35265, 1, 23, 8, 1, 1, 2), ).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltDhcpRelayOption82IfPolicyTable.setStatus('current')
if mibBuilder.loadTexts: eltDhcpRelayOption82IfPolicyTable.setDescription('A table of DHCP relay option 82 reforwarding policy for each port in the system. Policy stated in an entry of this table has a higher priority than global option.')
eltDhcpRelayOption82IfPolicyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35265, 1, 23, 8, 1, 1, 2, 1), ).setMaxAccess("readwrite").setIndexNames((0, "ELTEX-MES-DHCP", "eltDhcpRelayOption82IfIndex"))
if mibBuilder.loadTexts: eltDhcpRelayOption82IfPolicyEntry.setStatus('current')
if mibBuilder.loadTexts: eltDhcpRelayOption82IfPolicyEntry.setDescription('Specifies DHCP relay option 82 policy for port.')
eltDhcpRelayOption82IfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 8, 1, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltDhcpRelayOption82IfIndex.setStatus('current')
if mibBuilder.loadTexts: eltDhcpRelayOption82IfIndex.setDescription('Port number.')
eltDhcpRelayOption82IfPolicy = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 8, 1, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("replace", 1), ("drop", 2), ("keep", 3), ("global", 4))).clone(4)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltDhcpRelayOption82IfPolicy.setStatus('current')
if mibBuilder.loadTexts: eltDhcpRelayOption82IfPolicy.setDescription('DHCP relay option 82 reforwarding policy.')
eltDhcpRelayOption82AccessNodeIdentifier = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 23, 8, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 48))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltDhcpRelayOption82AccessNodeIdentifier.setStatus('current')
if mibBuilder.loadTexts: eltDhcpRelayOption82AccessNodeIdentifier.setDescription('Specifies an access node identifier')
eltDhcpRelayOption82CircuitIdSuboptionsCombination = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 23, 8, 1, 1, 4), EltDhcpRelayOption82CombinationType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltDhcpRelayOption82CircuitIdSuboptionsCombination.setStatus('current')
if mibBuilder.loadTexts: eltDhcpRelayOption82CircuitIdSuboptionsCombination.setDescription('Specifies circuit id suboptions that will be inserted to packet.')
eltDhcpRelayOption82CircuitIdSuboptionsDelimeter = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 23, 8, 1, 1, 5), EltDhcpRelayOption82DelimiterType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltDhcpRelayOption82CircuitIdSuboptionsDelimeter.setStatus('current')
if mibBuilder.loadTexts: eltDhcpRelayOption82CircuitIdSuboptionsDelimeter.setDescription('Specifies a char symbol that will delimit circuit id suboptions.')
eltDhcpRelayOption82SuboptionType = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 23, 8, 1, 1, 6), EltDhcpRelayOption82SuboptionType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltDhcpRelayOption82SuboptionType.setStatus('current')
if mibBuilder.loadTexts: eltDhcpRelayOption82SuboptionType.setDescription('Specifies global format of option 82 suboptions.')
eltDhcpRelayOption82RemoteIdentifier = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 23, 8, 1, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 63))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltDhcpRelayOption82RemoteIdentifier.setStatus('current')
if mibBuilder.loadTexts: eltDhcpRelayOption82RemoteIdentifier.setDescription('Specifies global remote Identifier suboption for Option 82.')
eltDhcpRelayBroadcastEnable = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 23, 8, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltDhcpRelayBroadcastEnable.setStatus('current')
if mibBuilder.loadTexts: eltDhcpRelayBroadcastEnable.setDescription('Enable or disable the of the DHCP relay broadcast subnet forwarding.')
eltMesDhcpSrv = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 8, 2))
eltDhcpSrvConfParamsTable = MibTable((1, 3, 6, 1, 4, 1, 35265, 1, 23, 8, 2, 1), ).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltDhcpSrvConfParamsTable.setStatus('current')
if mibBuilder.loadTexts: eltDhcpSrvConfParamsTable.setDescription('The DHCP Configuration Parameters Table.')
eltDhcpSrvConfParamsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35265, 1, 23, 8, 2, 1, 1), ).setMaxAccess("readwrite")
rlDhcpSrvConfParamsEntry.registerAugmentions(("ELTEX-MES-DHCP", "eltDhcpSrvConfParamsEntry"))
eltDhcpSrvConfParamsEntry.setIndexNames(*rlDhcpSrvConfParamsEntry.getIndexNames())
if mibBuilder.loadTexts: eltDhcpSrvConfParamsEntry.setStatus('current')
if mibBuilder.loadTexts: eltDhcpSrvConfParamsEntry.setDescription('The row definition for this table. Each entry corresponds to one specific parameters set.')
eltDhcpSrvConfParamsTftpSrvList = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 8, 2, 1, 1, 1), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltDhcpSrvConfParamsTftpSrvList.setStatus('current')
if mibBuilder.loadTexts: eltDhcpSrvConfParamsTftpSrvList.setDescription("The value of option code 150, which defines list of TFTP servers addresses. Each IP address is represented in dotted decimal notation format with ';' between them.")
mibBuilder.exportSymbols("ELTEX-MES-DHCP", eltDhcpRelayOption82SuboptionType=eltDhcpRelayOption82SuboptionType, EltDhcpRelayOption82PolicyType=EltDhcpRelayOption82PolicyType, eltDhcpRelayOption82Policy=eltDhcpRelayOption82Policy, eltDhcpRelayOption82AccessNodeIdentifier=eltDhcpRelayOption82AccessNodeIdentifier, eltDhcpSrvConfParamsEntry=eltDhcpSrvConfParamsEntry, EltDhcpRelayOption82SuboptionType=EltDhcpRelayOption82SuboptionType, eltDhcpRelayOption82IfPolicyEntry=eltDhcpRelayOption82IfPolicyEntry, eltDhcpRelayOption82CircuitIdSuboptionsDelimeter=eltDhcpRelayOption82CircuitIdSuboptionsDelimeter, eltDhcpRelayOption82RemoteIdentifier=eltDhcpRelayOption82RemoteIdentifier, eltDhcpRelayOption82IfIndex=eltDhcpRelayOption82IfIndex, eltDhcpRelayOption82IfPolicy=eltDhcpRelayOption82IfPolicy, eltMesDhcpRelay=eltMesDhcpRelay, eltDhcpSrvConfParamsTftpSrvList=eltDhcpSrvConfParamsTftpSrvList, eltDhcpSrvConfParamsTable=eltDhcpSrvConfParamsTable, eltDhcpRelayOption82CircuitIdSuboptionsCombination=eltDhcpRelayOption82CircuitIdSuboptionsCombination, EltDhcpRelayOption82DelimiterType=EltDhcpRelayOption82DelimiterType, eltDhcpRelayOption82IfPolicyTable=eltDhcpRelayOption82IfPolicyTable, eltMesDhcpSrv=eltMesDhcpSrv, eltDhcpRelayBroadcastEnable=eltDhcpRelayBroadcastEnable, eltMesDhcpRelayOption82=eltMesDhcpRelayOption82, EltDhcpRelayOption82CombinationType=EltDhcpRelayOption82CombinationType)
