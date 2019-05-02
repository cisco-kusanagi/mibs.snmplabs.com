#
# PySNMP MIB module Unisphere-Data-Log-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-Log-CONF
# Produced by pysmi-0.3.4 at Wed May  1 15:31:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
ModuleIdentity, Counter32, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, MibIdentifier, TimeTicks, Integer32, Bits, iso, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter32", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "MibIdentifier", "TimeTicks", "Integer32", "Bits", "iso", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdLogGroup, usdLogGroup2, usdLogTrapGroup = mibBuilder.importSymbols("Unisphere-Data-LOG-MIB", "usdLogGroup", "usdLogGroup2", "usdLogTrapGroup")
usdLogAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 26))
usdLogAgent.setRevisions(('2001-03-28 22:07',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: usdLogAgent.setRevisionsDescriptions(('The initial release of this management information module.',))
if mibBuilder.loadTexts: usdLogAgent.setLastUpdated('200103282207Z')
if mibBuilder.loadTexts: usdLogAgent.setOrganization('Unisphere Networks, Inc.')
if mibBuilder.loadTexts: usdLogAgent.setContactInfo(' Unisphere Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886 USA Tel: +1 978 589 5800 E-mail: mib@UnisphereNetworks.com')
if mibBuilder.loadTexts: usdLogAgent.setDescription('The agent capabilities definitions for the logging managment component of the SNMP agent in the Unisphere Routing Switch family of products.')
usdLogAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 26, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdLogAgentV1 = usdLogAgentV1.setProductRelease('Version 1 of the logging managment component of the Unisphere Routing\n        Switch SNMP agent.  This version of the Log component was supported in\n        the Unisphere RX 1.3 system release.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdLogAgentV1 = usdLogAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: usdLogAgentV1.setDescription('The MIB supported by the SNMP agent for the logging managment application in the Unisphere Routing Switch. These capabilities became obsolete when the single syslog destination was replaced with a table of syslog destinations and the syslog facility was added.')
usdLogAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 26, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdLogAgentV2 = usdLogAgentV2.setProductRelease('Version 2 of the logging managment component of the Unisphere Routing\n        Switch SNMP agent.  This version of the Log component is supported in\n        the Unisphere RX 2.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdLogAgentV2 = usdLogAgentV2.setStatus('current')
if mibBuilder.loadTexts: usdLogAgentV2.setDescription('The MIB supported by the SNMP agent for the logging managment application in the Unisphere Routing Switch.')
mibBuilder.exportSymbols("Unisphere-Data-Log-CONF", PYSNMP_MODULE_ID=usdLogAgent, usdLogAgentV2=usdLogAgentV2, usdLogAgent=usdLogAgent, usdLogAgentV1=usdLogAgentV1)
