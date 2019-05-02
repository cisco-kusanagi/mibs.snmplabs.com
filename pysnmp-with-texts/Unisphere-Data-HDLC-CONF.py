#
# PySNMP MIB module Unisphere-Data-HDLC-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-HDLC-CONF
# Produced by pysmi-0.3.4 at Wed May  1 15:31:22 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
TimeTicks, Integer32, Unsigned32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Gauge32, ObjectIdentity, MibIdentifier, IpAddress, Counter32, Counter64, iso, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Integer32", "Unsigned32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Gauge32", "ObjectIdentity", "MibIdentifier", "IpAddress", "Counter32", "Counter64", "iso", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdHdlcGroup, usdHdlcGroup3, usdHdlcGroup2 = mibBuilder.importSymbols("Unisphere-Data-HDLC-MIB", "usdHdlcGroup", "usdHdlcGroup3", "usdHdlcGroup2")
usdHdlcAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 18))
usdHdlcAgent.setRevisions(('2001-03-28 14:17',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: usdHdlcAgent.setRevisionsDescriptions(('The initial release of this management information module.',))
if mibBuilder.loadTexts: usdHdlcAgent.setLastUpdated('200103281417Z')
if mibBuilder.loadTexts: usdHdlcAgent.setOrganization('Unisphere Networks, Inc.')
if mibBuilder.loadTexts: usdHdlcAgent.setContactInfo(' Unisphere Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886 USA Tel: +1 978 589 5800 E-mail: mib@UnisphereNetworks.com')
if mibBuilder.loadTexts: usdHdlcAgent.setDescription('The agent capabilities definitions for the HDLC component of the SNMP agent in the Unisphere Routing Switch family of products.')
usdHdlcAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 18, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdHdlcAgentV1 = usdHdlcAgentV1.setProductRelease('Version 1 of the HDLC component of the Unisphere Routing Switch SNMP\n        agent.  This version of the HDLC component was supported in the\n        Unisphere RX 1.0 system release.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdHdlcAgentV1 = usdHdlcAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: usdHdlcAgentV1.setDescription('The MIB supported by the SNMP agent for the HDLC application in the Unisphere Routing Switch. These capabilities became obsolete when rsHdlcIfDataPolarity was added.')
usdHdlcAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 18, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdHdlcAgentV2 = usdHdlcAgentV2.setProductRelease('Version 2 of the HDLC component of the Unisphere Routing Switch SNMP\n        agent.  This version of the HDLC component was supported in the\n        Unisphere RX 1.1 thru 3.0 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdHdlcAgentV2 = usdHdlcAgentV2.setStatus('current')
if mibBuilder.loadTexts: usdHdlcAgentV2.setDescription('The MIB supported by the SNMP agent for the HDLC application in the Unisphere Routing Switch. These capabilities became obsolete when more objects were added.')
usdHdlcAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 18, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdHdlcAgentV3 = usdHdlcAgentV3.setProductRelease('Version 3 of the HDLC component of the Unisphere Routing Switch SNMP\n        agent.  This version of the HDLC component is supported in the Unisphere\n        RX 3.1 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdHdlcAgentV3 = usdHdlcAgentV3.setStatus('current')
if mibBuilder.loadTexts: usdHdlcAgentV3.setDescription('The MIB supported by the SNMP agent for the HDLC application in the Unisphere Routing Switch.')
mibBuilder.exportSymbols("Unisphere-Data-HDLC-CONF", usdHdlcAgentV2=usdHdlcAgentV2, usdHdlcAgentV3=usdHdlcAgentV3, PYSNMP_MODULE_ID=usdHdlcAgent, usdHdlcAgentV1=usdHdlcAgentV1, usdHdlcAgent=usdHdlcAgent)
