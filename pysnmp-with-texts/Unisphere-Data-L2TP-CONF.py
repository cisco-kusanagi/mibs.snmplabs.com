#
# PySNMP MIB module Unisphere-Data-L2TP-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-L2TP-CONF
# Produced by pysmi-0.3.4 at Wed May  1 15:31:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
TimeTicks, ModuleIdentity, IpAddress, iso, Integer32, Gauge32, Bits, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, Counter32, NotificationType, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ModuleIdentity", "IpAddress", "iso", "Integer32", "Gauge32", "Bits", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "Counter32", "NotificationType", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdL2tpUdpIpGroup, usdL2tpStatusGroup, usdL2tpConfigGroup2, usdL2tpMapGroup, usdL2tpStatGroup2, usdL2tpConfigGroup3, usdL2tpStatGroup, usdL2tpConfigGroup, usdL2tpStatusGroup2 = mibBuilder.importSymbols("Unisphere-Data-L2TP-MIB", "usdL2tpUdpIpGroup", "usdL2tpStatusGroup", "usdL2tpConfigGroup2", "usdL2tpMapGroup", "usdL2tpStatGroup2", "usdL2tpConfigGroup3", "usdL2tpStatGroup", "usdL2tpConfigGroup", "usdL2tpStatusGroup2")
usdL2tpAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 24))
usdL2tpAgent.setRevisions(('2001-10-17 16:03', '2001-10-17 14:21',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: usdL2tpAgent.setRevisionsDescriptions(('New objects were added to the configuration group.', 'The initial release of this management information module.',))
if mibBuilder.loadTexts: usdL2tpAgent.setLastUpdated('200110171603Z')
if mibBuilder.loadTexts: usdL2tpAgent.setOrganization('Unisphere Networks, Inc.')
if mibBuilder.loadTexts: usdL2tpAgent.setContactInfo(' Unisphere Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886 USA Tel: +1 978 589 5800 E-mail: mib@UnisphereNetworks.com')
if mibBuilder.loadTexts: usdL2tpAgent.setDescription('The agent capabilities definitions for the layer 2 tunneling protocol (L2TP) component of the SNMP agent in the Unisphere Routing Switch family of products.')
usdL2tpAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 24, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdL2tpAgentV1 = usdL2tpAgentV1.setProductRelease('Version 1 of the L2TP component of the Unisphere Routing Switch SNMP\n        agent.  This version of the L2TP component was supported in the\n        Unisphere RX 2.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdL2tpAgentV1 = usdL2tpAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: usdL2tpAgentV1.setDescription('The MIB supported by the SNMP agent for the L2TP application in the Unisphere Routing Switch. These capabilities became obsolete when rsL2tpTunnelStatusCumEstabTime, rsL2tpSessionStatusCumEstabTime and rsL2tpSessionStatPayLostPackets were added, and rsL2tpSessionStatusLacTunneledIfIndex replaced rsL2tpSessionStatusLacPppIfIndex.')
usdL2tpAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 24, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdL2tpAgentV2 = usdL2tpAgentV2.setProductRelease('Version 2 of the L2TP component of the Unisphere Routing Switch SNMP\n        agent.  This version of the L2TP component was supported in the\n        Unisphere RX 3.0 and 3.1 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdL2tpAgentV2 = usdL2tpAgentV2.setStatus('obsolete')
if mibBuilder.loadTexts: usdL2tpAgentV2.setDescription('The MIB supported by the SNMP agent for the L2TP application in the Unisphere Routing Switch. These capabilities became obsolete when usdL2tpSysConfigReceiveDataSequencingIgnore was added to the configuration group.')
usdL2tpAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 24, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdL2tpAgentV3 = usdL2tpAgentV3.setProductRelease('Version 3 of the L2TP component of the Unisphere Routing Switch SNMP\n        agent.  This version of the L2TP component was supported in the\n        Unisphere RX 3.2 system release.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdL2tpAgentV3 = usdL2tpAgentV3.setStatus('obsolete')
if mibBuilder.loadTexts: usdL2tpAgentV3.setDescription('The MIB supported by the SNMP agent for the L2TP application in the Unisphere Routing Switch. These capabilities became obsolete when new objects were added to the configuration group.')
usdL2tpAgentV4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 24, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdL2tpAgentV4 = usdL2tpAgentV4.setProductRelease('Version 4 of the L2TP component of the Unisphere Routing Switch SNMP\n        agent.  This version of the L2TP component is supported in the Unisphere\n        RX 3.3 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdL2tpAgentV4 = usdL2tpAgentV4.setStatus('current')
if mibBuilder.loadTexts: usdL2tpAgentV4.setDescription('The MIB supported by the SNMP agent for the L2TP application in the Unisphere Routing Switch.')
mibBuilder.exportSymbols("Unisphere-Data-L2TP-CONF", usdL2tpAgentV3=usdL2tpAgentV3, usdL2tpAgentV2=usdL2tpAgentV2, usdL2tpAgentV1=usdL2tpAgentV1, usdL2tpAgent=usdL2tpAgent, usdL2tpAgentV4=usdL2tpAgentV4, PYSNMP_MODULE_ID=usdL2tpAgent)
